### 基本api
1. tf.gfile 类似于python的os模块
2. tf.summary   tf.summary()的各类方法，能够保存训练过程以及参数分布图并在tensorboard显示。
3. tf.contrib.slim
  > tensorflow官方对它的描述是：此目录中的任何代码未经官方支持，可能会随时更改或删除。每个目录下都有指定的所有者。它旨在包含额外功能和贡献，最终会合并到核心TensorFlow中，但其接口可能仍然会发生变化，或者需要进行一些测试，看是否可以获得更广泛的接受。所以slim依然不属于原生tensorflow。

  >那么什么是slim？slim到底有什么用？

  >slim是一个使构建，训练，评估神经网络变得简单的库。它可以消除原生tensorflow里面很多重复的模板性的代码，让代码更紧凑，更具备可读性。
4.
>tf.add_to_collection–向当前计算图中添加张量集合
>tf.get_collection–返回当前计算图中手动添加的张量集合

### [Tensorflow一些常用基本概念与函数（4）](https://blog.csdn.net/lenbow/article/details/52218551)

### [tensorflow scope命名方法（variable_scope()与name_scope()解析）](https://blog.csdn.net/xwd18280820053/article/details/70808583)
### [TensorFlow数据读取方法](https://blog.csdn.net/u010329292/article/details/68484485)
