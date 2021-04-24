@echo off
:: 改编码为UTF-8
chcp 65001
:: 杀进程
taskkill /F /IM dandanplay.exe
:: 重新启动
start %APPDATA%\弹弹play\dandanplay.exe