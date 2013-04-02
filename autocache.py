#!/usr/bin/env python
#coding=utf-8

'''装饰器版的python自动缓存系统'''

import time
import hashlib
import pickle
from functools import wraps

_cache = {}

def _is_obsolete(entry, duration):
    '''是否过期'''
    if duration == -1: #永不过期
        return False
    return time.time() - entry['time'] > duration

def _compute_key(function, args,kw):
    '''序列化并求其哈希值'''
    key = pickle.dumps((function.func_name,args,kw))
    return hashlib.sha1(key).hexdigest() 

def memorize(duration = -1):
    '''自动缓存'''
    def _memoize(function):
        @wraps(function) # 自动复制函数信息
        def __memoize(*args, **kw):
            key = _compute_key(function, args, kw)
            #是否已缓存？
            if key in _cache:
                #是否过期？
                if _is_obsolete(_cache[key], duration) is False:
                    return _cache[key]['value']
            # 运行函数
            result = function(*args, **kw)
            #保存结果
            _cache[key] = {
                'value' : result,
                'time'  : time.time()
            }
            return result
        return __memoize
    return _memoize
