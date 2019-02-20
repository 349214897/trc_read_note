[python基础教程链接网址](http://www.runoob.com/python/python-operators.html)
### 1.is和==的区别
对象有三重属性,id,type,value
其中is是同一性操作
==是值相等操作
**另外对象和None执行上面判断操作时,注意到None的特殊性,及None和各种类型空值的差异**
- None是一个特殊的常量。
- None和False不同。
- None不是0。
- None不是空字符串。
- None和任何其他的数据类型比较永远返回False。
- None有自己的数据类型NoneType。
- 你可以将None赋值给任何变量，但是你不能创建其他NoneType对象。

### 2. int(a),bin(a),0b1000几种表示的联系和区别,以及print函数打印格式控制
bin(a)返回的是整形a的二进制字符串形式,返回的type是str
0b1000是二进制表示,type是int

### 3.print使用
- 字符串
- 拼接字符串
- 计算表达式
- 打印定义变量
[Python print函数用法，print 格式化输出](https://blog.csdn.net/zanfeng/article/details/52164124)
