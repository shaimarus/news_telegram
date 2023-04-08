import streamlit as st
from datetime import date, datetime
import json
import pandas as pd




st.set_page_config(
    #page_title="Shift Systems - Tandau",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.shift-systems.kz/',
    #     'Report a bug': "https://www.shift-systems.kz/",
    #     'About': ""#"Сервис по расшифровке файлов  https://www.shift-systems.kz/"
    # }
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

tabs = ["Orda Kz", "Ztb", "Tengri","Nurkz"]
selected_tab = st.sidebar.selectbox("Выберите новости", tabs)

# Определение содержимого каждой вкладки
if selected_tab == "Orda Kz":
    
    # Ваш код для содержимого первой вкладки
    st.title('Orda Kz')

    with open('orda.json', 'r') as infile:
        data = json.load(infile)
    df3=pd.DataFrame(data,columns=['time_insert','id','public_date','text','emoji','cnt'])
    df3['time_insert']=pd.to_datetime(df3['time_insert'])+pd.Timedelta(hours=0)
    df3['public_date']=pd.to_datetime(df3['public_date'])+pd.Timedelta(hours=6)
    df3.sort_values('time_insert',ascending=False,inplace=True)


    for i in range(20):
        number=sorted(df3['id'].unique(),reverse=True)[i]
        b=[]
        for k in range(len(df3[df3['id']==number][['time_insert','emoji','cnt']])):
            a1=df3[df3['id']==number][['time_insert','emoji','cnt']].iloc[k]
            a=dict()
            for i in range(len(a1[1])):
                a[a1[1][i]]=a1[2][i]
            a['insert_time']=datetime.strptime(str(a1[0]), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S") 
            b.append(a)

        emojis = b[0].keys()
        emoji_counts = {emoji: [d.get(emoji, 0) for d in b] for emoji in emojis}

        l1=emoji_counts[list(emoji_counts.keys())[0]][::]

        def func1(l1):

            em1=[]
            for i in range(len(l1)):
                if i==0:
                    em1.append(l1[0])
                else:
                    em1.append(-l1[i-1]+l1[i])
            return em1        

        
        st.write(df3[df3['id']==number]['public_date'].iloc[0])
        #st.write(df3[df3['id']==number]['text'].iloc[0])
        st.title(df3[df3['id']==number]['text'].iloc[0].split('\n')[0])
        st.write(''.join(df3[df3['id']==number]['text'].iloc[0].split('\n')[1:]))
        dictionary = dict(zip(df3[df3['id']==number][['emoji','cnt']].iloc[0]['emoji'], df3[df3['id']==number][['emoji','cnt']].iloc[0]['cnt']))

        cols = st.columns(len(dictionary.keys()))

        for i, col in enumerate(cols):
            col.write(f"{list(dictionary.keys())[i]} {list(dictionary.values())[i]}")

        st.write("Анализ поставленных смайликов по времени:")
        import altair as alt
        charts = []
        for i in list(emoji_counts.keys())[:-1][:]:
            chart = alt.Chart(pd.DataFrame({'insert_time': emoji_counts['insert_time'][::-1],
                                            'count': func1(emoji_counts[i][::-1])})).mark_bar().encode(
                x=alt.X('insert_time:T', axis=alt.Axis(format='%H:%M %d.%m.%y', labels=True, labelAngle=270)),
                y='count',

            ).properties( title=alt.TitleParams(text=str(i), align='left'),height=200 ,width=alt.Step(40)).interactive()

            charts.append(chart)
        combined_chart = alt.hconcat(*charts)    
        st.altair_chart(combined_chart, use_container_width=True)

elif selected_tab == "Ztb":
    st.title('Ztb')
    with open('ztb.json', 'r') as infile:
        data = json.load(infile)
    df3=pd.DataFrame(data,columns=['time_insert','id','public_date','text','emoji','cnt'])
    df3['time_insert']=pd.to_datetime(df3['time_insert'])+pd.Timedelta(hours=0)
    df3['public_date']=pd.to_datetime(df3['public_date'])+pd.Timedelta(hours=6)
    df3.sort_values('time_insert',ascending=False,inplace=True)


    for i in range(10):
        number=sorted(df3['id'].unique(),reverse=True)[i]
        b=[]
        for k in range(len(df3[df3['id']==number][['time_insert','emoji','cnt']])):
            a1=df3[df3['id']==number][['time_insert','emoji','cnt']].iloc[k]
            a=dict()
            for i in range(len(a1[1])):
                a[a1[1][i]]=a1[2][i]
            a['insert_time']=datetime.strptime(str(a1[0]), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S") 
            b.append(a)

        emojis = b[0].keys()
        emoji_counts = {emoji: [d.get(emoji, 0) for d in b] for emoji in emojis}

        l1=emoji_counts[list(emoji_counts.keys())[0]][::]

        def func1(l1):

            em1=[]
            for i in range(len(l1)):
                if i==0:
                    em1.append(l1[0])
                else:
                    em1.append(-l1[i-1]+l1[i])
            return em1        

        
        st.write(df3[df3['id']==number]['public_date'].iloc[0])
        #st.write(df3[df3['id']==number]['text'].iloc[0])
        st.title(df3[df3['id']==number]['text'].iloc[0].split('\n')[0])
        st.write(''.join(df3[df3['id']==number]['text'].iloc[0].split('\n')[1:]))
        dictionary = dict(zip(df3[df3['id']==number][['emoji','cnt']].iloc[0]['emoji'], df3[df3['id']==number][['emoji','cnt']].iloc[0]['cnt']))

        cols = st.columns(len(dictionary.keys()))

        for i, col in enumerate(cols):
            col.write(f"{list(dictionary.keys())[i]} {list(dictionary.values())[i]}")

        st.write("Анализ поставленных смайликов по времени:")
        import altair as alt
        charts = []
        for i in list(emoji_counts.keys())[:-1][:]:
            chart = alt.Chart(pd.DataFrame({'insert_time': emoji_counts['insert_time'][::-1],
                                            'count': func1(emoji_counts[i][::-1])})).mark_bar().encode(
                x=alt.X('insert_time:T', axis=alt.Axis(format='%H:%M')),
                y='count',

            ).properties( title=alt.TitleParams(text=str(i), align='left'),height=200 ,width=alt.Step(40))

            charts.append(chart)
        combined_chart = alt.hconcat(*charts)    
        st.altair_chart(combined_chart, use_container_width=True)

elif selected_tab == "Tengri":
    st.title('Tengri')
    with open('tengri.json', 'r') as infile:
        data = json.load(infile)
    df3=pd.DataFrame(data,columns=['time_insert','id','public_date','text','emoji','cnt'])
    df3['time_insert']=pd.to_datetime(df3['time_insert'])+pd.Timedelta(hours=0)
    df3['public_date']=pd.to_datetime(df3['public_date'])+pd.Timedelta(hours=6)
    df3.sort_values('time_insert',ascending=False,inplace=True)


    for i in range(10):
        number=sorted(df3['id'].unique(),reverse=True)[i]
        b=[]
        for k in range(len(df3[df3['id']==number][['time_insert','emoji','cnt']])):
            a1=df3[df3['id']==number][['time_insert','emoji','cnt']].iloc[k]
            a=dict()
            for i in range(len(a1[1])):
                a[a1[1][i]]=a1[2][i]
            a['insert_time']=datetime.strptime(str(a1[0]), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S") 
            b.append(a)

        emojis = b[0].keys()
        emoji_counts = {emoji: [d.get(emoji, 0) for d in b] for emoji in emojis}

        l1=emoji_counts[list(emoji_counts.keys())[0]][::]

        def func1(l1):

            em1=[]
            for i in range(len(l1)):
                if i==0:
                    em1.append(l1[0])
                else:
                    em1.append(-l1[i-1]+l1[i])
            return em1        

        
        st.write(df3[df3['id']==number]['public_date'].iloc[0])
        #st.write(df3[df3['id']==number]['text'].iloc[0])
        st.title(df3[df3['id']==number]['text'].iloc[0].split('\n')[0])
        st.write(''.join(df3[df3['id']==number]['text'].iloc[0].split('\n')[1:]))
        dictionary = dict(zip(df3[df3['id']==number][['emoji','cnt']].iloc[0]['emoji'], df3[df3['id']==number][['emoji','cnt']].iloc[0]['cnt']))

        cols = st.columns(len(dictionary.keys()))

        for i, col in enumerate(cols):
            col.write(f"{list(dictionary.keys())[i]} {list(dictionary.values())[i]}")

        st.write("Анализ поставленных смайликов по времени:")
        import altair as alt
        charts = []
        for i in list(emoji_counts.keys())[:-1][:]:
            chart = alt.Chart(pd.DataFrame({'insert_time': emoji_counts['insert_time'][::-1],
                                            'count': func1(emoji_counts[i][::-1])})).mark_bar().encode(
                x=alt.X('insert_time:T', axis=alt.Axis(format='%H:%M')),
                y='count',

            ).properties( title=alt.TitleParams(text=str(i), align='left'),height=200 ,width=alt.Step(40))

            charts.append(chart)
        combined_chart = alt.hconcat(*charts)    
        st.altair_chart(combined_chart, use_container_width=True)

elif selected_tab == "Nurkz":
    st.title('Nurkz')
    with open('nurkz.json', 'r') as infile:
        data = json.load(infile)
    df3=pd.DataFrame(data,columns=['time_insert','id','public_date','text','emoji','cnt'])
    df3['time_insert']=pd.to_datetime(df3['time_insert'])+pd.Timedelta(hours=0)
    df3['public_date']=pd.to_datetime(df3['public_date'])+pd.Timedelta(hours=6)
    df3.sort_values('time_insert',ascending=False,inplace=True)


    for i in range(10):
        number=sorted(df3['id'].unique(),reverse=True)[i]
        b=[]
        for k in range(len(df3[df3['id']==number][['time_insert','emoji','cnt']])):
            a1=df3[df3['id']==number][['time_insert','emoji','cnt']].iloc[k]
            a=dict()
            for i in range(len(a1[1])):
                a[a1[1][i]]=a1[2][i]
            a['insert_time']=datetime.strptime(str(a1[0]), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S") 
            b.append(a)

        emojis = b[0].keys()
        emoji_counts = {emoji: [d.get(emoji, 0) for d in b] for emoji in emojis}

        l1=emoji_counts[list(emoji_counts.keys())[0]][::]

        def func1(l1):

            em1=[]
            for i in range(len(l1)):
                if i==0:
                    em1.append(l1[0])
                else:
                    em1.append(-l1[i-1]+l1[i])
            return em1        

        
        st.write(df3[df3['id']==number]['public_date'].iloc[0])
        #st.write(df3[df3['id']==number]['text'].iloc[0])
        st.title(df3[df3['id']==number]['text'].iloc[0].split('\n')[0])
        st.write(''.join(df3[df3['id']==number]['text'].iloc[0].split('\n')[1:]))
        dictionary = dict(zip(df3[df3['id']==number][['emoji','cnt']].iloc[0]['emoji'], df3[df3['id']==number][['emoji','cnt']].iloc[0]['cnt']))

        cols = st.columns(len(dictionary.keys()))

        for i, col in enumerate(cols):
            col.write(f"{list(dictionary.keys())[i]} {list(dictionary.values())[i]}")

        st.write("Анализ поставленных смайликов по времени:")
        import altair as alt
        charts = []
        for i in list(emoji_counts.keys())[:-1][:]:
            chart = alt.Chart(pd.DataFrame({'insert_time': emoji_counts['insert_time'][::-1],
                                            'count': func1(emoji_counts[i][::-1])})).mark_bar().encode(
                x=alt.X('insert_time:T', axis=alt.Axis(format='%H:%M %Y.%m.%d')),
                y='count',

            ).properties( title=alt.TitleParams(text=str(i), align='left'),height=200 ,width=alt.Step(40))

            charts.append(chart)
        combined_chart = alt.hconcat(*charts)    
        st.altair_chart(combined_chart, use_container_width=True)
    