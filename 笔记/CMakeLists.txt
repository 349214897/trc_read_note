cmake_minimum_required(VERSION 2.8)
project(test_read)
include_directories(/home/liuli/2018trc/autopilot-thirdparty/thirdparty/caffe/install/include  /usr/local/cuda/targets/x86_64-linux/include/)
link_libraries("/home/liuli/2018trc/autopilot-thirdparty/thirdparty/caffe/build/lib/libcaffe.so")
link_libraries("/usr/lib/x86_64-linux-gnu/libboost_system.so")
include_directories(/usr/local/cuda-7.5/targets/x86_64-linux/lib/)
add_executable(test_read test_read.cpp)


