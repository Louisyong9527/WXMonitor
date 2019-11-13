WXMonitor
 
本项目依赖于网页版微信进行开发，如登录不了，则无法使用此项目；且无任何解决办法。    
网页版微信地址：<https://wx.qq.com/>。 

## 功能说明

实时监控微信所有聊天，包括好友发来的消息，微信群聊的消息。

## 安装
首先，把 Python3 安装好，并配置好环境，个人建议新手安装 Anaconda，具体安装教程，可自行谷歌搜索~  


直接下载此项目或 clone 项目到本地。  

使用 pip 安装依赖:

```
pip3 install -r requirements.txt
# 或者是使用 pip
# pip install -r requirements.txt
```

## 运行

在本地 cmd 中跳转项目目录下，运行:  

```
wxdemo.py
```

第一次运行会跳出二维码，扫码登录。如输出日志中打印成：『登录成功』，则表示运行成功。  
登录成功后一段时间内再运行，微信会保持登录状态，不需要再扫码。 


## LICENSE
[MIT License](https://github.com/sfyc23/EverydayWechat/blob/master/LICENSE)
