### 配置筛选脚本
1. 运行参数设置
> python test_lane_acc_fn_fp_16anchor.py --model='此处为模型的prototxt文件' --weights='caffemodel'
2. test_lane_acc_fn_fp_16anchor.py需要修改的地方
> - 找到caffe_root改成本机caffe对应的地址

            caffe_root = '/home/liuli/bollard/caffe-apollo/'
>- 找到fileobj=open('select_list.txt','w+')这一行,改成自己想要输出的名字
>- 找到下面代码段,把a<0.91改成任意自己需要筛选精度

            if(a<0.91):
                fileobj.write(image_path)
                fileobj.write('\n')

### 配置评测脚本
1. 运行参数示例(后面参数内容可以随意设置)
> python to_xinping.py --model='prototxt文件' --weights='caffemodel' --result='123' --list='123'
2. to_xinping.py需要修改的地方
> - 首先要把test_scrip文件中对应的protobuf文件夹放到与to_xinping.py同级目录
>- 下列代码把txt文件换成自己需要的文档(由上一步筛选脚本产生)

        with open('select_file_85.txt') as f:
            image_use_list = f.readlines()
            image_use_list = [e.split('/')[-1].rstrip('\n') for e in image_use_list]
>- 把下列代码中目录改为perception模块输出结果坐在路径

        pred_output=fromfile(image_path,'/home/liuli/2018trc/baidu/apollo-pilot/perception/src/result')

### 原始label转化为16像素间隔label
1. 下载perception_data_manager工具
2. 安装anaconda3
3. 安装opencv,protobuf
> conda install -c https://conda.binstar.org/menpo opencv
> conda install protobuf
4. 进入perception_data_manager的script目录,修改lane_test.sh中下列路径为对应本地路径

        export PYTHONPATH=/home/liuli/todocker/minor_work/perception_data_manager:$PYTHONPATH
        export PATH="/home/liuli/anaconda3/bin:$PATH"

        python ../modules/lane/lane_data_manager.py ../modules/conf/lane_config_test.prototxt --inputdir /media/liuli/Elements/mark_task_5411-20180530_jianghuai_sunny-LAYER4_LANE_2018/
