@echo off

REM 解决中文乱码问题 - 设置为UTF-8编码
@chcp 65001 >nul

echo ============================================
echo 一键Git提交脚本
echo 目标仓库：https://github.com/huangwei-gem/code
echo ============================================

REM 检查是否在git仓库中
if not exist .git (
    echo 错误：当前目录不是git仓库！
    echo 请先初始化git仓库并添加远程仓库：
    echo git init
    echo git remote add origin https://github.com/huangwei-gem/code.git
    pause
    exit /b 1
)

REM 添加所有变更文件
echo 正在添加所有变更文件...
git add .
if %errorlevel% neq 0 (
    echo 错误：添加文件失败！
    pause
    exit /b 1
)

REM 生成带时间戳的提交信息 - 使用更可靠的方式
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do set "today=%%c-%%a-%%b"
for /f "tokens=1-2 delims=: " %%a in ('time /t') do set "now=%%a:%%b"
set "default_commit_msg=自动提交 %today% %now%"

REM 提示用户输入提交信息或使用默认值
echo.
echo 默认提交信息：%default_commit_msg%
echo 按Enter使用默认信息，或输入自定义提交信息：
set /p commit_msg=提交信息：
if "%commit_msg%"=="" set commit_msg=%default_commit_msg%

REM 提交代码
echo.
echo 正在提交代码...
git commit -m "%commit_msg%"
if %errorlevel% neq 0 (
    echo 错误：提交失败！
    pause
    exit /b 1
)

REM 推送到远程仓库
echo.
echo 正在推送代码到远程仓库...
git push origin master
if %errorlevel% neq 0 (
    echo 错误：推送失败！
    echo 请检查网络连接和GitHub权限
    pause
    exit /b 1
)

echo.
echo ============================================
echo 提交成功！
echo 提交信息：%commit_msg%
echo 仓库地址：https://github.com/huangwei-gem/code
echo ============================================
pause