# gevent

import time

import gevent
from gevent import monkey

monkey.patch_all() #检测到time.sleep(0.4) 耗时的操作，自动切换


def a():
    for i in range(5):
        print('a', i)
        time.sleep(0.4)


def b():
    for i in range(5):
        print('b', i)
        time.sleep(0.4)


def c():
    for i in range(5):
        print('c', i)
        time.sleep(0.4)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    # 阻塞主进程
    g1.join()
    g2.join()
    g3.join()
