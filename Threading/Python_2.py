import threading
import time


def get_data(data):
    for _ in range(5):
        time.sleep(1)
        print(f'[{threading.current_thread().name}] - {data}' + "\n")


thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True)
thr.start()
time.sleep(1)
print("finish")
