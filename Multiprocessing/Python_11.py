import multiprocessing
import time

lock = multiprocessing.Lock()


def get_vqalue(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f' Процесс [{pr_name}] запущен')


if __name__ == '__main__':
    multiprocessing.Process(target=get_vqalue, args=(lock,)).start()
    multiprocessing.Process(target=get_vqalue, args=(lock,)).start()
    time.sleep(2)
    lock.release()
