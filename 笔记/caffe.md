## caffe中工厂模式初探
[梳理caffe代码layer_factory(六)](http://blog.csdn.net/langb2014/article/details/50991315)  
[caffe代码阅读7：LayerRegistry的实现细节-2016.3.18](http://blog.csdn.net/xizero00/article/details/50923722)  
[Caffe model里为啥有的layer top和bottom还能一样的？知乎](https://www.zhihu.com/question/46501015?sort=created)

register类功能是根据prototxt中的type在列表中找到对应的构造函数指针,调用构造函数生成对应的对象,构造网络(所以register是单例的)

## [Caffe框架详细梳理](https://www.cnblogs.com/fuleying/p/5893917.html)

## [Caffe net:init()函数代码详细注解](http://blog.csdn.net/mrhiuser/article/details/52345469)

## net::init()中下面代码不是很清楚其含义
    for (int top_id = 0; top_id < top_vecs_[layer_id].size(); ++top_id) {
      if (blob_loss_weights_.size() <= top_id_vecs_[layer_id][top_id]) {
        blob_loss_weights_.resize(top_id_vecs_[layer_id][top_id] + 1, Dtype(0));
      }
      blob_loss_weights_[top_id_vecs_[layer_id][top_id]] = layer->loss(top_id);

## 新网络进展
1. Inception
2. Xception
3. 面向移动端
    1. ShuffleNet
    2. MobileNet

4. ResNeXt

## deepmind关系推理网络
DeepMind’s Relational Reasoning Networks — Demystified  
[详细介绍](http://geek.csdn.net/news/detail/209580)

## [Face paper：Light-Head R-CNN介绍](http://blog.csdn.net/wfei101/article/details/78757151)
[如何评价论文 : Light-Head R-CNN ?知乎](https://www.zhihu.com/question/68483928)  
[如何评价 MSRA 最新的 Deformable Convolutional Networks？知乎](https://www.zhihu.com/question/57493889)  
[深度学习方法（十二）：卷积神经网络结构变化——Spatial Transformer Networks](http://blog.csdn.net/xbinworld/article/details/69049680)
[深度学习方法（十三）：卷积神经网络结构变化——可变形卷积网络deformable convolutional networks](http://blog.csdn.net/xbinworld/article/details/69367281)
