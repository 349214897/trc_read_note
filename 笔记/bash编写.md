# BASH 用法小结
[BASH 数组用法小结 及　循环用法](http://blog.csdn.net/samxx8/article/details/8025548)  
[10 分钟学会Linux常用 bash命令](https://www.cnblogs.com/savorboard/p/bash-guide.html)  
[Bash shell中的位置参数$#,$*,$@,$0,$1,$2...及特殊参数$?,$-等的含义](http://blog.csdn.net/adaptiver/article/details/7240364)  
[bash find命令使用](https://jingyan.baidu.com/article/636f38bb6e0bdad6b846103e.html)  
[linux shell中'',""和``的区别](https://www.cnblogs.com/Skyar/p/5914942.html)  
[bash：如何给function传参数](http://blog.csdn.net/tsingyee/article/details/6136931)  
[Bash Shell字符串操作小结](https://www.cnblogs.com/frydsh/p/3261012.html)  
[Linux基础之-正则表达式（grep，sed，awk）](https://www.cnblogs.com/OldJack/p/6607155.html)

if [ -f $home/$1]    
1. if 条件判断关键字  
2. ``[ ]`` 语法要求  
3. -f 文件比较运算符,如果 filename为常规文件，则为真   
4. $home 取变量的值,如果.sh文件里面没有该就是则会取用户系统变量!你可以在终端中执行一下 echo $home 看看是什么路径  
5. $1 取输入的第一个参数.例: sh xxx.sh 111 那么此时 $1的值就是 111  
