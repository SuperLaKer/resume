虚拟环境不加sudo,否则会添加到系统环境里面

```
pip install virtualenv
pip install virtualenvwrapper

virtualenv envname -p D:\ENV\python27\python.exe
mkvirtualenv -p /usr/bin/python3.7 venv　
# -p参数指定Python解释器程序路径
这将会使用 /usr/bin/python2.7 中的Python解释器。

# 默认python

cd /usr/bin
sudo rm -rf python
sudo ln -s /usr/bin/python3  /usr/bin/python

sudo apt install python3-pip
```

```
# 进入虚拟环境文件
cd envname
# 进入相关的启动文件夹
cd Scripts

activate  # 启动虚拟环境
deactivate # 退出虚拟环境
```

```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
4）使用source .bashrc使其生效一下。
```

#### pip升级

```
python -m pip install --upgrade pip
```

