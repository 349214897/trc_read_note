###1. 上传必须为文件,目录会出错
###2. jobs.sh中挂载目录改成适配的,且afs_path必须手动适配
###3. 用到euclidean_loss时,caffekm中loss_layer会校验bottom是否为2,这时回引起错误,应该注释
    //virtual inline int ExactNumBottomBlobs() const { return 2; }

### submit.sh说明
    71 if [ -n "$HDFS_PATH" ]; then
    72     ~/.hgcp/software-install/HGCP_client/tools/hadoop-v2/hadoop/bin/hadoop \
    73     fs -D fs.default.name=afs://xingtian.afs.baidu.com:9902 -D hadoop.job.ugi=IVBU_KM_Data,IVBU_km_2018 \
    74     -D dfs.replication=1 -D fs.afs.impl=org.apache.hadoop.fs.DFileSystem \
    75     -mkdir /user/IVBU_KM_Data/l3Team/$HDFS_PATH
    76 fi


 ./submit.sh --job_name=auto_hpp4 --submitter_name=tanricheng --job_dir=. --hdfs_path=hpp_hdfs8 --training_data_file=training/training_data/data.tar.gz --afs_path=hpp_afs8 --job_script=jobs.sh
