# 案例
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def dowload(url):
    response = urllib.request.urlopen(url)
    content = response.read()
    print('下载了{}的数据，长度为{}'.format(url, len(content)))


if __name__ == '__main__':
    urls = ['http://www.163.com', 'http://www.qq.com']
    g1 = gevent.spawn(dowload, urls[0])
    g2 = gevent.spawn(dowload, urls[1])

    # gevent.joinall(g1, g2)  # 类似 g1.join（）
    g1.join()
    g2.join()