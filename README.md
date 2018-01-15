# PythonDemo

### 第一个问题

项目转移遇见的编译问题

> No Python interpreter selected

字面上的意思就是‘没有选择Python解释器’

然后直接去按照以下操作添加就可以了

> Python–>Preferences–>Project Interpreter–>Python Interpreter 
> 点击“+”号选择系统安装的Python。

### 第二个问题,TypeError: 'str' object does not support item assignment

运行代码

```python
def reverse(li):
    for i in range(0, len(li)/ 2):
        temp = li[i]
        li[i] = li[-i - 1]
        li[-i - 1] = temp


l = [1, 2, 3, 4, 5]
str = '1234567'
print '翻转之前:', (str)
reverse(l)
print '翻转之后:', (str)
```

字符串是不可变对象，不要试图用下标的方法去改变字符串的值。

转换成列表或者数组即可，修改方案如下：
```python
def reverse(li):
    for i in range(0, len(li)/ 2):
        temp = li[i]
        li[i] = li[-i - 1]
        li[-i - 1] = temp


str = '1234567'
str2l = [int(x) for x in str[::-1]]
print 'str翻转之前:', (str2l)
reverse(str2l)
print 'str翻转之后:', (str2l)
```
