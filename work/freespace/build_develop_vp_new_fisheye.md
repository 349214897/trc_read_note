### 1.把camodocalcopy到/home/liuli/2018trc/baidu/apollo-pilot/perception/src/common/ipm文件夹下
### 2.注释了,解决了 _cuDACC的问题,cuda和eigen版本不匹配
>//#define __CUDACC_VER__ "__CUDACC_VER__ is no longer supported.  Use __CUDACC_VER_MAJOR__, __CUDACC_VER_MINOR__, and __CUDACC_VER_BUILD__ instead."
### 3.修改l3-apollo下的hardware_configure.proto文件,路径如下
>/home/liuli/2018trc/baidu/vp/vps-apollo/modules/common/proto/config/
>添加了    enum CameraModelType {
        PINHOLE = 0;
        MEI     = 1;
    }
    及
    optional CameraModelType camera_model = 14;  /* 相机模型 */
    optional float xi = 15;                 /* MEI 模型参数 */

### 4.拉取对应commit-id vps-apollo代码,将thirdparty放到根目录,在CmakeList里注释一些代码,./build.sh -m eda编译就可以了
### **5.鱼眼ipm与广角有区别,使用的是左手坐标系,需要在reset函数里面置为相反的符号**

### 6.编译好vps-apollo和perception代码后,在perception_config.dongzhi.MKZ009里面改成对应的参数


### 待修改点
1.多相机的调度
2.perception.cpp将结果入adapter时
3.roi等区域的设置
4.参数调整
