# python装饰器自动缓存系统(autocache.py)

### 说明

- 这是一个函数装饰器，用来给函数增加缓存。
- 程序根据函数名和参数自动缓存，可以设置缓存时间(秒)。
- 只要函数名和参数完全相同并且缓存时间没到，则直接返回缓存里面的值。否则执行函数，再将结果缓存。

### 使用方法

参考 [test_autocache.py](test_autocache.py)

### 优点

- 使用简单方便，直接在要缓存的函数前加装饰器即可
- 根据函数名和参数进行缓存，更加智能

### 存在问题

- 函数的缓存时间只能在函数定义的时候设置一次
- 缓存存在内存里，只能在程序结束时释放

### Todo

- 增加自定义缓存时间功能
- 数据持久化

# python键值缓存系统(cache.py)

### 说明

- 经典的键值缓存系统，类似于memcached，
- 通过set方法来将内容缓存起来， 可以设置生存时间。
- 通过get方法从缓存中获取数据，当然只有在生存时间内的内容才能被返回，超过了生存时间，直接返回None。
- 通过delete方法删除缓存，
- 通过clear方法清空缓存。

### 经典用法：

假设有一条`python`语句的执行时间很长，结果在一段时间内不会变化，我们可以对这条语句进行缓存。

例如：有一个sql查询要花费较长时间

`result = sql()`

然后我们可以用我的小缓存系统进行缓存处理，可以用下面的语句来替代

```python
cache = Cache()
result = cache.get("sql_result")
if result is None:
    result = sql()
    cache.set(key='sql_result', data=result, age=10)
```

解释一下：首先从缓存中读取元素，如果在缓存中，直接从缓存中获得，如果缓存中没有，则执行sql查询并将结果存入缓存，并设置生存时间为10秒

### 其他用法

参考 [test_cache.py](test_cache.py)

### 优点

- 直接对函数的返回值进行缓存，不依赖于具体函数
- 方法操作比较全面，能对具体的键值对进行操作

### 存在问题

- 用户自定义`key`，如果key相同则会覆盖原来的值
- 没有持久化，程序结束缓存删除

### Todo

- 增加自定义缓存时间功能
- 数据持久化
