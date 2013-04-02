#!/usr/bin/env python
#coding=utf-8
from cache import Cache

def a_hard_function():
    '''一个需要缓存的函数'''
    print "getting result"
    from time import sleep
    import random
    sleep(2)
    print "done"
    return random.randint(1,100)

if __name__ == "__main__":
    cache = Cache()
    cache.set('a','aaaa',5)   #a的值是'aaaa',生存时间位5秒
    cache.set('b',[1,2])      #b的值是[1,2],生存时间无限长
    while True:
        result = cache.get("hard_func")
        if result is None:
            result = a_hard_function()
            cache.set("hard_func",result,2)
        print cache.get('a'),
        print cache.get('b'),
        print result
