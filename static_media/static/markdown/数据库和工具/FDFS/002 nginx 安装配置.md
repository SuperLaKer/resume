```
解压：nginx.tar.gz、fastdfs-ngnix-module-master.zip
cd ngnix

sudo ./configure --prefix=/usr/local/nginx/ --add-module=路径fastdfs-nginx-module-master/src

sudo make
sudo ./make install

fastdfs
```

```
安装nginx及fastdfs-nginx-module
1. 解压缩 nginx-1.8.1.tar.gz
2. 解压缩 fastdfs-nginx-module-master.zip
3. 进入nginx-1.8.1目录中
4. 执行
sudo ./configure --prefix=/usr/local/nginx/ --add-module=fastdfs-nginx-module-master解压后的目录的绝对路径/src
sudo ./configure --prefix=/usr/local/nginx/ --add-module=/mnt/d/linux_data/fastdfs-nginx-module-master/src

sudo ./make============================makefile 删除 werror
sudo ./make install
5. sudo cp fastdfs-nginx-module-master解压后的目录中src下的mod_fastdfs.conf  /etc/fdfs/mod_fastdfs.conf
6. sudo vim /etc/fdfs/mod_fastdfs.conf
修改内容：
connect_timeout=10
tracker_server=自己ubuntu虚拟机的ip地址:22122
url_have_group_name=true
store_path0=/home/python/fastdfs/storage
7. sudo cp 解压缩的fastdfs-master目录中的http.conf  /etc/fdfs/http.conf
8. sudo cp 解压缩的fastdfs-master目录中的mime.types /etc/fdfs/mime.types
9.sudo vim /usr/local/nginx/conf/nginx.conf
在http部分中添加配置信息如下：
server {
            listen       8888; //监听端口
            server_name  localhost;  //本地
            location ~/group[0-9]/ {  //正则表达式
                ngx_fastdfs_module;
            }
            error_page   500 502 503 504  /50x.html;
            location = /50x.html {
            root   html;
            }
        }
10. 启动nginx
sudo /usr/local/nginx/sbin/nginx  //nginx启动程序
ps aux | grep nginx
sudo /usr/local/nginx/sbin/nginx -s stop
```

