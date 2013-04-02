#!/usr/bin/env python
#coding=utf-8
from autocache import memorize

@memorize(3)
def a_hard_function(a):
    '''一个需要缓存的函数'''
    print "getting result"
    from time import sleep
    import random
    sleep(2)
    return a,random.randint(1,100)

if __name__=='__main__':
    while True:
        print a_hard_function(1)
        print a_hard_function(2)
        print a_hard_function.__doc__ #函数文档保持不变
