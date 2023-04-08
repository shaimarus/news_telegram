import subprocess
import time
log_file = '/home/user/news_telegram/ab3.log' 
while True:
    # Вызываем скрипт с помощью subprocess
    subprocess.Popen(['/usr/bin/python3', '/home/user/news_telegram/ab.py'], stdout=open(log_file, 'a'), stderr=subprocess.STDOUT)
    # Задержка в 60 секунд
    time.sleep(600)