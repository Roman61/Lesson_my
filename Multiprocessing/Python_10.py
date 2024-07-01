import multiprocessing


class Process(multiprocessing.Process):
    @staticmethod
    def run():
        print("work")


if __name__ == '__main__':
    pr = Process()
    pr.start()
