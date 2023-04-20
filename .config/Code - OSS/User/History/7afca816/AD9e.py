import datetime
import time

last_login = datetime.datetime.now()

def cal():
    while True:
        time_el = datetime.datetime.now() - last_login

        print(time_el)
        time.sleep(5)

cal()