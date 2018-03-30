

## 执行评测
1. 跑完程序

>1 先进入路径build/bin/  

>2 ./test_perception -config /home/liuli/liuli/trc/autopilot/data/config.prototxt -image_dir=/home/liuli/liuli/trc/perception-eva/perception-eva/data/raw_images/ -list /home/liuli/liuli/trc/perception-eva/perception-eva/data/valid_image_list.txt -result_dir /home/liuli/liuli/trc/perception-eva/perception-eva/data/prototxt/


2. 把对应的结果存到prototxt
3. 执行val

## gdb调试相关
[gdb基本命令(非常详细)](http://blog.csdn.net/yinjiabin/article/details/7732931)
1. 进入子函数命令
[]()
2. 设置条件断点
(gdb) b 13 if i == 8
3. 删除断点  
**delete可删除单个断点，也可删除一个断点的集合，这个集合用连续的断点号来描述。**  
例如：
delete 5
delete 1-10  
**clear**  
用法:clear
    删除所在行的多有断点。
    clear location
## linux系统文件目录操作
[linux系统编程之文件与IO（四）：目录访问相关系统调用](https://www.cnblogs.com/mickole/p/3182205.html)  
linux下c调用shell命令
>#include "stdlib.h"  
>system(char* s)


## jsoncpp使用
1. [jsoncpp使用方法总结](http://www.cppblog.com/wanghaiguang/archive/2013/12/26/205020.html)
2. linux下jsoncpp配置
>sudo apt-get install scons(liuli电脑上该方法失效,用了源码安装)  
>scons platform=linux-gcc  
**!注意** 包含json.h时一定要包含到他的上一级目录,形式类似于json/json.h否则会爆出很多错误

## qt问题
QT编译，一直循环报错：file“xxxxx”has modification times xxxxx s in the future..
> find /your/dir -type f -exec touch {} +

## hash_map扩展
[C++笔记：STL扩展hash_map](http://blog.csdn.net/qdx411324962/article/details/42523163)

## cmake问题
[link_directories, LINK_LIBRARIES, target_link_libraries使用总结](http://blog.csdn.net/arackethis/article/details/43488177)
add_libraries,list,file,install,fuction,set_target_properties  
[gtest的构建使用](http://blog.csdn.net/clayandwind/article/details/48602431)

## configtool
生成json字符创文件在jsonutil/config_json_util.cpp的VVoid ConfigJsonUtil::GetProvinceJsonString( VInt nFormatIdx, VInt nProvinceId,const CVString &strDstBaiduNaviRoot, VWChar wcMapType, CVString &strJson )中
修改configtool
1.首先在navi_engine_request_manager_json_key_def.h中的_NE_DM_Data_Type_Enum添加ads和index类型
2.在config_json_util.cpp的static NE_DM_Data_Type_Enum GetFileType( CVString &strName )中添加对应获取type的代码
3.在config_json_util.cpp的VBool ConfigJsonUtil::GetFileDetails中的switch ( enFileType )的分支里面添加对应type的处理代码(这里有一个获取version的代码,可能需要自己加一些手动修改和加一些策略)
4.在config_json_util.cpp的VVoid ConfigJsonUtil::GetProvinceJsonString中的GenerateJsonForFile( strIL, nProvinceId, wcMapType,enFileType, szFileName, szVersion, szMD5, nFileSize );写入对应字符串

## build
./configure --prefix=absolutepath
make
make install

proto.pb.cc及protopb.h生成protoc --cpp_out=. file
[linux 给运行程序指定动态库路径](http://blog.csdn.net/hktkfly6/article/details/61922685)

error adding symbols: DSO missing from command line解决办法

## protobuf
protobuffer 编译时报错；
Please use 'syntax = "proto2";' or 'syntax = "proto3";' to specify a syntax
在.proto 文件开始加上
syntax = "proto2";  或 syntax = "proto3";  来指明 使用版本

## 解压及压缩
解压 tar zxvf 文件名.tar.gz
压缩 tar zcvf 文件名.tar.gz 目标名

## markdown  
ctral+shilft+p 显示快捷栏搜索

## git账户密码设置
git config --global user.name *
git config --global user.email *
git commit --amend --reset-author

[Git忽略规则.gitignore梳理](https://www.cnblogs.com/kevingrace/p/5690241.html)

[Git的一些常用命令，及.gitignore的配置](http://blog.csdn.net/zxyudia/article/details/67633321)

## dependent name is not a type [关于模板类中的迭代器](http://blog.csdn.net/guoxiaoqian8028/article/details/30240675)

## 设置terminal的shell环境默认为zsh，输入以下命令： chsh -s `which zsh`

### grep查询特定目录下内容并列出来
grep per_dt code/  -nr

### [解决因为本地代码和远程代码冲突，导致git pull无法拉取远程代码的问题](https://www.cnblogs.com/huanyou/p/6654813.html)

### 上车流程
1. 在约车群以特定格式约车
2. 在车上左边px2 ip 192.168.1.12 右边px2 ip 192.168.1.13 用户为nvidia
3. 在右边px2的vehicle/下面autopilot就是将要执行的代码,上自己的代码前一定要备份别人的用cp拷贝或者mv重命名,上完车后再恢复
4. 用roslaunch perception_ros/src/sky_touch/launch/

### ssh端口号22,查询端口号netstat -tan | grep 22 修改端口,[修改 /etc/ssh/sshd_config 文件](https://zhidao.baidu.com/question/536014390.html)

### [Linux--Terminator 必备快捷键](https://www.jianshu.com/p/b7b811e7117d)

### ffmpeg解码方法
ffmpeg -i vedio_second.h264 -qscale:v 2 second/second_%04d.jpg
