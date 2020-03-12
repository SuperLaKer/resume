#### 安装环境包

```
1、解压：libfastcommon-master.zip
2、进入目录：cd libfastcommon-master
3、执行：./make.sh  ================ok
4、执行：sudo ./make.sh install===============ok
```

#### 安装fastdfs

```
1、解压：fastdfs-master.zip
2、进入目录：cd fastdfs-master
3、执行：./make.sh===============ok
4、执行：sudo ./make.sh install===============ok
```

#### 配置跟踪服务器tracker

```
 cd /etc/fdfs/
 tracker.conf.smple重命名,注意备份
 修改：base_path=/home/lla/fastdfs/tracker
 
 cd ~ mkdir -p fastdfs/tracker
 cd ~ cd fastdfs
 mkdir storage
```

配置storage

```
重命名：sudo cp /etc/fdfs/storage.conf.sample
配置工作目录：base_path=/home/lla/fastdfs/storage
配置：store_path0=/home/python/fastdfs/storage
ip：tracker_server= 虚拟机ip+22122
```

启动tracker和storage

```
sudo service fdfs_trackerd start
sudo service fdfs_storaged start
sudo /usr/local/nginx/sbin/nginx
```

测试是否安装成功

```
client.conf.sample
base_path=/home/lla/fastdfs/tracker
tracker_server=虚拟机ip+22122

上传文件
fdfs_upload_file /etc/fdfs/client.conf +要上传的文件
返回：group1/M00/00/00/rBIK6VcaP0aARXXvAAHrUgHEviQ394.jpg 说名成功
fdfs_upload_file /etc/fdfs/client.conf /mnt/h/colorsplash/1542.jpg
group1/M00/00/00/fwAAAVySU5uAS_7SAAt7qrAOeVQ447.jpg
```

