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
                return None
        else:
            return None

if __name__ == "__main__":
    cache = Cache()
    t = time()
    cache.set('a',100,3) #a的值是100,生存时间位3秒
    cache.set('b',999)   #b的值是999,生存时间无限长
    while True:
        print cache.get('a'),
        print cache.get('b')
