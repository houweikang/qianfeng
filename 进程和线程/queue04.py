# 进程间通信
from multiprocessing import Queue

q = Queue(5)

lst = [1, 2, 3, 4, 5, 6]
for _ in lst:
    q.put(_)
    print(_, q.qsize())
    if q.full():
        print('队列已满')

