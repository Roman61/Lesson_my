import multiprocessing
import random
import time


def add_value(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        vtime = time.ctime()
        array[index] = num
        print(f"array[{index}] = {num}, sleep = {vtime}")
        time.sleep(num)
    pass


if __name__ == '__main__':
    process = []
    lock = multiprocessing.Lock()
    arr = multiprocessing.Array("i", range(10))
    print(list(arr))

    for i in range(10):
        pr = (multiprocessing.Process(target=add_value, args=(lock, arr, i,)))
        process.append(pr)
        pr.start()

        for i in process:
            i.join()

    print(list(arr))
