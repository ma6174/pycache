#!/usr/bin/env python
#coding=utf-8

'''装饰器版的python自动缓存系统，使用redis持久化数据库'''

import hashlib
import pickle
import redis
from functools import wraps

r = redis.Redis(host="localhost",port=6379,db=0)

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
            if r.exists(key):
                try: # 判断存在和返回之间还有一段时间，可能造成key不存在
                    return r[key]
                except:
                    pass
            # 运行函数
            result = function(*args, **kw)
            #保存结果
            r[key] = result
            r.expire(key,duration)
            return result
        return __memoize
    return _memoize
