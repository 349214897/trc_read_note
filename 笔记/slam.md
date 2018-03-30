### [状态估计ekf和非线性估计的区别](http://blog.csdn.net/shenxiaolu1984/article/details/73522056)
### [ORB-SLAM（五）优化](https://www.cnblogs.com/luyb/p/5447497.html)
### [orb-slam-gpu代码地址](https://github.com/yunchih/ORB-SLAM2-GPU2016-final)
### [BA算法](http://blog.csdn.net/myarrow/article/details/53373661)
### ORB-SLAM论文阅读
#### 1.introduction(一个实时的slam算法必须提供BA),须具有下列条件:
 - 子序列之间有一致的观测特征(重合的场景)
 - 复杂的关键帧的数量的增长，他们的选择应避免不必要的冗余。
 - 关键帧和点足够精确,一系列关键帧有足够的视差和大量的闭环匹配
 - 关键帧的姿态估计和关键点的位置的初始估计用来非线性优化
 - 一个优化的可扩展的局部地图
 - 一个实时的全局闭环优化  
**第一个实时的应用BA的视觉里程计方法是PTAM**
**PTAM缺点:1.缺乏闭环检测 2.重定位的低不变形3.需要人工干预**
##### ORBSLAM发展了PTAM算法,主要贡献如下:
- 在所有的任务中使用相同的特征
- 在大场景中能够实时计算.由于使用了covisibility rqt_graph,tracking和mapping都在local covisible area下完成,独立于全局地图大小
- 用pose graph(Essential Graph)实时闭环
- 实时根据光照和视点不变性相机重定位
- 一种实时的稳定的初始化方法-基于模型选择
- 关键帧和点大量产生但选择比较严格,这种策略提升了tracking的鲁棒性和有利于长期操作,应为会丢弃过期的关键帧和点.

#### 2.Related Work
- A. Place recongnition(ORB特征检索)
- B. Map Initialize
- C. Monocular SLAM概览(**提到了 odometry SVO可能和我们工作有关联**)

#### 3.system overview
- 特征提取
- 三个线程(tracking,local mapping,loop closure).The tracking is in charge of localizing the camera with every frame and deciding when to insert a new keyframe.一旦tracking失败,就用全局图里面的place初始化模型.初始化之后,就可以用local
- map points,key frames,and their selections
- Covisibility Graph and Essential Graph
- Bags of Words Place Recognition

#### 4.automatic map initialization
#### 5.tracking
#### 6.Local mapping
#### 7.loop closing

### [SVO算法详解](http://blog.csdn.net/heyijia0327/article/details/51083398)

### [ORB特征](https://www.cnblogs.com/zjiaxing/p/5616653.html)

### [pnp算法求解相机姿态](http://rosclub.cn/post-566.html)

### [大牛讲堂｜SLAM最终话：视觉里程计 ](https://www.leiphone.com/news/201609/Qj6uJhaywpBD8vdq.html)
