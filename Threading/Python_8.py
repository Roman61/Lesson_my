import random
import time
import threading
from threading import current_thread


def test(barrier):
    slp = random.randint(1, 17)
    print(f"Поток [{current_thread().name}] запущен в ({time.ctime()}), sleep({slp})")
    time.sleep(slp)

    barrier.wait()
    print(f'Поток [{current_thread().name}] преодолел барьер в({time.ctime()})\n')


bar = threading.Barrier(5)
for i in range(5):
    threading.Thread(target=test, args=(bar, ), name=f'thr-{i}').start()

