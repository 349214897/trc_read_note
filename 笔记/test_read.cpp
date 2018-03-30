#include"caffe/caffe.hpp"
#include<string>
using namespace caffe;
using namespace std;

int main()
{
    string model_file="/home/liuli/2018trc/autopilot/data/model/lane/lane_det_5a_2c_0213/deploy.prototxt";
    string trained_file="/home/liuli/2018trc/autopilot/data/model/lane/lane_det_5a_2c_0213/lane_det_2c_bollard_iter_60000.caffemodel";
    caffe::Caffe::set_mode(caffe::Caffe::GPU);
    //caffe::Caffe::SetDevice(gpu_id);
    Net<float> net(model_file,TEST);
    net.CopyTrainedLayersFrom(trained_file);
    //caffe::Caffe::DeviceQuery();

    return 0;
}

