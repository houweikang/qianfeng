# 线程
'''
创建线程
t = threading.Thread(target=download,name='aa',args=(1,))
t.start()
t.join()

状态：
新建  就绪  运行 阻塞  结束


线程共享全局变量
python底层线程默认加锁 GIL 全局解释器锁 ’伪线程‘
耗时操作 用线程
高次运算 用进程

线程共享数据
锁：
    lock = threading.Lock()
    lock.acquire() 请求得到锁
    lock.release() 释放锁
    只要不释放，其他线程无法进入运行状态

避免死锁：
1.重构代码
2.lock.acquire(timeout=5)

生产者与消费者：两个线程之间的通信

q = queue.Queue()
q.put()
q.get()
'''
import threading
import time

money = 1000


def run1():
    global money
    for i in range(100):
        money -= 1


def run2():
    global money
    for i in range(100):
        money -= 1


# if __name__ == '__main__':
#     # 创建线程
#     t1 = threading.Thread(target=run1, name='t1')
#     t2 = threading.Thread(target=run2, name='t2')
#
#     # 启动
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print(money)

# 锁
lock = threading.Lock()

l1 = [0] * 10


def task1():
    # 获取线程锁，若已经上锁，则等待锁的释放
    lock.acquire()  # 阻塞
    for i in range(len(l1)):
        l1[i] = 1
        time.sleep(0.5)
    lock.release()  # 释放锁


def task2():
    lock.acquire()  # 阻塞
    for i in range(len(l1)):
        print('--------', l1[i])
        time.sleep(0.5)
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t2.start()
    t1.start()
