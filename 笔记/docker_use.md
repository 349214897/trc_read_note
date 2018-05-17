1. install docker
sudo apt-get install docker.io
2. 加载docker
sudo docker load<docker_autopilot.img
3. cd autopilot_user/
4. sh build.sh
5. 返回到上一级目录-cd ..
6. sudo cp nvidia-docker/* /usr/sbin/
7. 修改run.sh
8. 运行(bash run.sh)
9. 启动docker中的镜像
sudo docker exec -it autopilot bash
10. 退出docker 镜像实例 exit

# 两个有用的命令
11. 显示docker中load的镜像 sudo docker images
12. 显示docker实例 sudo docker ps

# 删除运行的实例
1. 先stop
sudo docker stop sutopilot
2. 再删除
sudo docker rm autopilot1
