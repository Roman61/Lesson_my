import time
import threading

value = 0
locker = threading.RLock()


def loker_man():
    print(" Блокируем поток ")
    locker.acquire()
    print(" Поток разблокирован ")


t1 = threading.Thread(target=loker_man())
t2 = threading.Thread(target=loker_man())
t1.start()
t2.start()

locker.release()
time.sleep(0.2)
locker.release()
print("finish")
