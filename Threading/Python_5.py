import time
import threading


def test():
    while True:
        print("test")
        time.sleep(1)


thr = threading.Timer(5, test)
thr.setDaemon(True)
thr.start()

for _ in range(6):
    print("111")
    time.sleep(1)

thr.cancel()
print('finish')
