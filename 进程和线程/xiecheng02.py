# greenlet 完成协程任务
import time
from greenlet import greenlet


def a():
    for i in range(5):
        print('a', i)
        gb.switch()
        time.sleep(0.4)


def b():
    for i in range(5):
        print('b', i)
        gc.switch()
        time.sleep(0.4)


def c():
    for i in range(5):
        print('c', i)
        ga.switch()
        time.sleep(0.4)


if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)

    ga.switch()
