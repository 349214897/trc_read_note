# find及xargs配合使用
命令find test2/ -name '*.tes' |xargs rm -rf, 即将find产生的输出（test2目录下的所有tes文件），作为rm的参数，从而完全删除

# sed用法
[linux命令：批量将查找到的文件移动或者复制到其他目录并尽可能保持原文件的目录结构](https://www.cnblogs.com/FoChen/p/7645187.html)

# cp文件时，保留它的目录结构
find  ./test_copy -name *.txt -exec cp -rp --parents {}  dst_copy \;

# [bash for使用](https://blog.csdn.net/z_qifa/article/details/74202619)
  #!/bin/bash
  #方法一
  dir=$(ls -l /usr/ |awk '/^d/ {print $NF}')
  for i in $dir
  do
      echo $i
  done

# [sed在文件的每一行行首或行尾添加内容](https://blog.csdn.net/huangjin0507/article/details/50538206)

  1. 在每行的头添加字符，比如"HEAD"，命令如下：

  sed 's/^/HEAD&/g' test.file

  2. 在每行的行尾添加字符，比如“TAIL”，命令如下：

  sed 's/$/&TAIL/g' test.file

  3. 替换字符串
  sed -i 's/123/234/g' test.file
  有时用/不合适时可以用#替代:
  sed -i 's#^.#/media/liuli/DATA/gan_and_raw/raw#g' list.txt
  
# 删除增加行总结
  1、删除文档的第一行

  sed -i '1d' <file>

  2、删除文档的最后一行
  sed -i '$d' <file>

  3、在文档指定行中增加一行
  例如文档如下：
  echo "1";
  echo "2";
  echo "4";
  echo "5";
  想要在echo "2";后面加上一条echo "3";可以用如下命令
  sed -i '/echo "2";/aecho "3";' <file>
  之所以用分号，是因为文本中本来就有，也就是说分号不是必须的．
  抽象出来就是： sed -i '/* /a*' <file>

  4、删除文件中的第k行，例如k=3
  sed -i '3d' <file>

  5、删除文件中包含某个关键字开头的所有行
  sed -i '/^QWQ/d' <file>

  6、删除文件中包含某个关键字的所有行
  sed -i '/QWQ/d' <file>
