# 启动
sudo nvidia-docker run --net host --hostname trc_graph --name graph  --user root:root -p 8880:60 -v /home/liuli/todocker:/my-devel -it imburbank/graph_nets:latest-gpu
# 浏览器 127.0.0.1:port
