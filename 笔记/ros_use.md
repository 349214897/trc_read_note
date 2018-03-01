### 1.单独编译perception_ros下的package
  1. cd perception_ros
  2. 把utils下面的package.xml改成package.bak.xml
  3. catkin_make --pkg bag_msgs_sync
  4. 编译完后,可执行的程序在perception_ros/devel/lib/bag_msgs_sync下面

### 2.自己写package
  1. 按照bag_msgs_sync下的组织方式,把CMakeLists.txt改成自己对应的内容,拷贝代码sync.cpp或者新建cpp文件,然后利用catkin_make编译

### 3.查看运行节点关系
  rosrun rqt_graph rqt_graph   
  rostopic查看主题相关消息   
  rostopic echo [rostopic]显示在一个主题上的数据  
  rostopic list显示当前订阅和被发布的主题列表  
  rostopic hz返回数据发布的速率  
  rqt_plot是rqt软件包的一部分,可以动态绘制发布到某一主题上的数据的图形  
  > rosrun rqt_plot rqt_plot

### 4.message和topic的区别
  两个ros nodes欲实现通信,其中一个节点向rostopics发布rosmessages,另一个节点向rostopics订阅此topic来接收messages
