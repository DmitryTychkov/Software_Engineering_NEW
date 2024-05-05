import datetime
import time

def one_second():
    for x in range(5):
        print("Текущее время: ", datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)


one_second()
