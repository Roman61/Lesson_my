import multiprocessing
import random


def get_text(g):
    val = random.randint(0, 10)
    print(f"В процессе добавили: {val}")
    g.put(str(val))


queue = multiprocessing.Queue()
pr_list = []

if __name__ == '__main__':
    for _ in range(10):
        pr = multiprocessing.Process(target=get_text, args=(queue,))
        pr_list.append(pr)
        pr.start()

    for i in pr_list:
        i.join()

    for i in range(queue.qsize()):
        print(queue.get(i))


