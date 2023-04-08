import configparser
import json
from datetime import date, datetime
import time
import logging
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)

# some functions to parse json date
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)


# Reading Configs
#config = configparser.ConfigParser()
#config.read("config.ini")

api_id=''
api_hash=''

api_hash = str(api_hash)

#phone = config['Telegram']['phone']
phone = ''
username=''
# Create the client and connect
client = TelegramClient(username, api_id, api_hash)


async def channel2(input_channel):

    if input_channel=='orda':
        user_input_channel='https://t.me/orda_kz'
    elif input_channel=='ztb':
        user_input_channel='https://t.me/ztb_qaz'    
    elif input_channel=='tengri':
        user_input_channel='https://t.me/tengrinews'  
    elif input_channel=='nurkz':
        user_input_channel='https://t.me/newsnurkz'  




    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel


    limit = 150
    my_channel = await client.get_entity(entity)
    messages5 = await client.get_messages(my_channel, limit=limit+1)
    max_id = messages5[-1].id
    print('max_id:',max_id,'input_channel:',input_channel)


    offset_id = 0
    
    all_messages = []
    #all_messages2 = []
    total_messages = 0
    total_count_limit = 0
    
    from os.path import exists
    file_exists = exists(input_channel+'.json')
    if not file_exists:
        all_messages2=[]

    else:    
        with open(input_channel+'.json', 'r') as infile:
            all_messages2 = json.load(infile)


    while True:
        #print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
        history = await client(GetHistoryRequest(
            peer=my_channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=max_id,
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        import pytz
        for message in messages:
            
            try:
                all_messages2.append([datetime.now().strftime('%d.%m.%Y %H:%M:%S'),message.to_dict()['id'],datetime.strptime(str(message.to_dict()['date']), '%Y-%m-%d %H:%M:%S%z').strftime('%d.%m.%Y %H:%M:%S'),message.to_dict()['message'],[i['reaction']['emoticon'] for i in message.to_dict()['reactions']['results']],[i['count'] for i in message.to_dict()['reactions']['results']]])

            except:
                pass    
            message.to_dict()
            all_messages.append(message.to_dict())

        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            print(len(all_messages))
            break
    with open(input_channel+'.json', 'w') as outfile:
        json.dump(all_messages2, outfile, cls=DateTimeEncoder)




async def main(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    await channel2('orda')
    await channel2('ztb')
    await channel2('tengri')
    await channel2('nurkz')

    
with client:
    client.loop.run_until_complete(main(phone))

with open('test.log', 'w') as outfile:
    json.dump(datetime.now().strftime('%d.%m.%Y %H:%M:%S') , outfile, cls=DateTimeEncoder)