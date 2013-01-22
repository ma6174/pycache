# python简单缓存系统

类似于memcached，通过set方法来将内容缓存起来，可以设置生存时间，通过get方法从缓存中获取数据，当然只有在生存时间内的内容才能被返回，超过了生存时间，直接返回None

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
