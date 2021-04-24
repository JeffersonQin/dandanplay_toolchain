- [Introduction](#introduction)
- [ToolChain](#toolchain)
	- [ddp_api_server](#ddp_api_server)
		- [配置方法](#配置方法)
		- [使用方法](#使用方法)
	- [ddp_restart_server](#ddp_restart_server)
		- [配置方法](#配置方法-1)
		- [使用方法](#使用方法-1)

# Introduction

这个repo中的代码是一些本人使用/写的，有关弹弹Play的Toolchain。

# ToolChain

## ddp_api_server

弹弹Play动漫花园API服务器的修改版本（此版本没有使用proxy），来自：https://pastebin.ubuntu.com/p/mGP7JRpBtd/

由于我的服务器在上海，所以我是配合`proxychains`一起使用的

### 配置方法

在脚本内需要配置好`host`和`port`
```
run_host = <配置host>
run_port = <配置port>
```
如果需要允许任意连接，`run_host`可以设置为`0.0.0.0`。推荐使用`apache`之类的服务器做一下代理。

### 使用方法

如果你的服务器在国内，建议使用`proxychains`。若服务器在国外，请忽略命令开始的`proxychains4`

```bash
proxychains4 python3 ddp_api_server.py
```

后台运行方法：

```bash
nohup python3 ddp_api_server.py &
```

## ddp_restart_server

弹弹Play远程重启服务器，用于远程控制时的重启（毕竟有的时候会碰到奇奇怪怪的bug，重启一下就好了）

由于弹弹Play的远程服务只有Windows版本有，所以是核心功能是使用批处理脚本写的。同时，为了方便后台运行，此脚本在WSL内运行。如果你不知道WSL是什么，请看这里：https://docs.microsoft.com/zh-cn/windows/wsl/install-win10

下面是每个文件的功能：
- `ddp_restart.bat`: 实现重启功能
- `ddp_restart_server.py`: 重启服务器
- `start_server_wsl.sh`: `wsl`内的重启脚本
- `start_server_wsl.bat`: `windows`内的重启脚本，调用上一个文件，可用于开机启动, etc.

### 配置方法

请将`ddp_restart.bat`, `ddp_restart_server.py`, `start_server_wsl.sh`, `start_server_wsl.bat`置于同一文件夹内。

端口及`token`配置：在`ddp_restart_server.py`中

```
run_host = <配置host>
run_port = <配置port>
api_token = <配置token>
```

### 使用方法

如果需要开机自动启动，直接将`start_server_wsl.bat`的**快捷方式**扔到`启动`文件夹即可。

其他使用方式，请参考代码。
