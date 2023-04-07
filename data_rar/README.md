
# Data_rar
本文件夹主要是生成训练所用的txt
# train and test
1. 解压pytorch_radarGesture_10classification/pic中的压缩包得到图片
2. 运行(pytorch_radarGesture_10classification/)merge_RGB_*.py其中一个文件对pic中图片进行处理得到train和test
# 得到train.py所需的txt(里面是图片路径和标签)
将所用数据放在此文件夹，运行process.py便可以生成（注意要在cfg文件更改路径）
* train.txt
* val.txt
* test.txt
# 下载
本项目所用到的一些手势文件：

* 从雷达得到的bin文件(项目不需要)(https://www.aliyundrive.com/s/uhdjRysv3Tn 提取码: 71bp)
* 最终的训练数据以及测试数据(https://www.aliyundrive.com/s/JWMBoemJtq2 提取码: 6q8l)
* 本项目所训练得到的weights(不需要下载，可自己训练)(https://www.aliyundrive.com/s/ynQDJmJWu74 提取码: ns30)
