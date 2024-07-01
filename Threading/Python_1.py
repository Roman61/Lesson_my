import threading
import time


def get_data(data, value):
    for _ in range(value):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


thr_list = []

for i in range(3):
    thr = threading.Thread(group=None, target=get_data,
                           name=f"thr-{i}", args=(str(time.time()), i,),
                           kwargs={}, daemon=None)
    thr_list.append(thr)
    # thr = threading.Thread(target=get_data, args=(str(time()),), name="thr-1")
    thr.start()

print(thr_list)

for i in thr_list:
    i.join()

print("finish")
# print("Name", threading.main_thread().name)
# threading.main_thread().setName("resault")
# print("resault", threading.main_thread().name)

# for i in range(100):
#     print(f"current: {i}")
#     time.sleep(1)
#
#     if i % 10 == 0:
#         print("active tread:", threading.active_count())
#         print("enumerate:", threading.enumerate())
#         print("thr-1 is alive:", thr.is_alive())
