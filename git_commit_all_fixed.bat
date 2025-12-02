@echo off
chcp 65001 >nul
REM Git一键提交所有文件脚本
REM 作者: huangwei-gem
REM 功能: 自动添加所有文件并提交到GitHub仓库

echo =========================================
echo Git一键提交所有文件脚本
echo =========================================
echo.

REM 检查是否在Git仓库中
if not exist ".git" (
    echo 错误: 当前目录不是Git仓库!
    pause
    exit /b 1
)

REM 获取当前日期时间作为默认提交信息
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a:%%b)
set "default_msg=%mydate% %mytime% 自动提交所有文件"

REM 询问提交信息
set /p commit_msg="请输入提交信息 (默认: %default_msg%): "
if "%commit_msg%"=="" set "commit_msg=%default_msg%"

REM 显示当前状态
echo.
echo 当前Git状态:
git status --short
echo.

REM 添加所有文件
echo 正在添加所有文件...
git add .

REM 检查是否有文件需要提交
git status --porcelain > temp_git_status.txt
for %%i in (temp_git_status.txt) do set size=%%~zi
if %size% equ 0 (
    echo.
    echo 没有文件需要提交!
    del temp_git_status.txt
    pause
    exit /b 0
)

echo.
echo 发现需要提交的文件:
type temp_git_status.txt
del temp_git_status.txt
echo.

REM 提交文件
echo 正在提交文件...
git commit -m "%commit_msg%"

if %errorlevel% neq 0 (
    echo.
    echo 提交失败!
    pause
    exit /b 1
)

echo.
echo 提交成功!
echo 提交信息: %commit_msg%
echo.

REM 推送到远程仓库
set /p push_confirm="是否推送到远程仓库? (y/n, 默认: y): "
if /i "%push_confirm%"=="n" (
    echo.
    echo 跳过推送操作。
) else (
    echo.
    echo 正在推送到远程仓库...
    git push origin master
    
    if %errorlevel% neq 0 (
        echo.
        echo 推送失败! 请检查网络连接或远程仓库配置
        pause
        exit /b 1
    )
    
    echo.
    echo 推送成功!
)

echo.
echo =========================================
echo 所有操作完成!
echo =========================================
pause