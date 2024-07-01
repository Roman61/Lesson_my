import time
import threading

value = 0
locker = threading.Lock()


def inc_value():
    global value
    while True:
        with locker:
            if value >= 100:
                break
            value += 1
            print(value)
            time.sleep(0.1)


thr_list = []

for _ in range(5):
    thr = threading.Thread(target=inc_value)
    thr_list.append(thr)
    thr.start()

for i in thr_list:
    i.join()

print("finish")
