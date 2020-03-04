from multiprocessing import Process
from time import sleep
import os


def task1(s):
    while True:
        sleep(s)
        print('1111111111','  子进程：',os.getpid(),'  父进程:',os.getppid())


def task2(s):
    while True:
        sleep(s)
        print('2222',' 子进程：',os.getpid(),'  父进程:',os.getppid())

number = 1
if __name__ == '__main__':
    print(os.getpid())
    p1 = Process(target=task1, name='任务1',args=(1,))
    p1.start()
    p2 = Process(target=task2, name='任务2',args=(1.5,))
    p2.start()

    while True:
        number += 1
        if number == 10:
            sleep(5)
            p1.terminate()
            p2.terminate()
            break