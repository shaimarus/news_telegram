# Web service for monitoring telegram channel <br/>
## This service help identify anomaly behavior of users. <br/>
This service allows you to observe the anomalous behavior of users, namely how they put emojis in relation to time <br/>

1.You should add next credentials for telegram: <br/>
api_id='' <br/>
api_hash='' <br/>
phone = '' <br/>
username='' <br/>

2.Data gathering:
a. you can put ab.py to cron, run it every 10 minutes,it will be block if you want do it often. <br/>
b. you can run ab3.py through subprocess.Popen(): <br/>

import subprocess <br/>
cmd = ['python3', '/path/to/file/ab2.py'] <br/>
process = subprocess.Popen(cmd) <br/>


3.streamlit run streamlit.py <br/>

And then service will be available at <br/>
http://localhost:8501/ <br/>

![Image alt](https://github.com/shaimarus/news_telegram/blob/main/picture1.jpeg)
![Image alt](https://github.com/shaimarus/news_telegram/blob/main/picture2.jpeg)

