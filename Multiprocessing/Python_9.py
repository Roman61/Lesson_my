import multiprocessing
import time


def test():
    while True:
        print(f"{multiprocessing.current_process().name} - {time.time()}")
        time.sleep(1)


prcs_list = []

if __name__ == '__main__':
    for i in range(5):
        prc = multiprocessing.Process(target=test, name=f"prc-{i}")
        prcs_list.append(prc)
        prc.start()
    print(" Процесс запущен ")

    for i in prcs_list:
        print(f'{i.pid} - {i.is_alive()}')
        time.sleep(10)
        i.terminate()
