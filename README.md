# codeUpdateService
代码更新服务

## 环境
Python3 Centos

## 安装
yum install python3-tools
pip3 install bottle

## 启动服务
nohup python3 -u /data/app/python/webhook/index.py > out.log 2>&1 &
