#!/usr/bin/env python
#coding=utf-8
from time import time
class Cache:
    '''简单的缓存系统'''
    def __init__(self):
        '''初始化'''
        self.mem = {}
        self.time = {}

    def set(self, key, data, age=-1):
        '''保存键为key的值，时间位age'''
        self.mem[key] = data
        if age == -1:
            self.time[key] = -1
        else:
            self.time[key] = time() + age
        return True

    def get(self,key):
        '''获取键key对应的值'''
        if key in self.mem.keys():
            if self.time[key] == -1 or self.time[key] > time():
                return self.mem[key]
            else:
                self.delete(key)
                return None
        else:
            return None

    def delete(self,key):
        '''删除键为key的条目'''
        del self.mem[key]
        del self.time[key]
        return True

    def clear(self):
        '''清空所有缓存'''
        self.mem.clear()
        self.time.clear()

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
