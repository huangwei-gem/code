@echo off
REM 一键通过SSH提交代码到GitHub仓库
REM 仓库地址: git@github.com:huangwei-gem/code.git

chcp 65001 >nul

echo ============================================
echo 一键Git提交脚本 (SSH方式)
echo 目标仓库：git@github.com:huangwei-gem/code.git
echo ============================================

REM 检查是否在git仓库中
if not exist .git (
    echo 错误：当前目录不是git仓库！
    echo 请先初始化git仓库并添加远程仓库：
    echo git init
    echo git remote add origin git@github.com:huangwei-gem/code.git
    pause
    exit /b 1
)

REM 获取当前分支
for /f %%i in ('git rev-parse --abbrev-ref HEAD') do set branch=%%i
echo 当前分支: %branch%

REM 添加所有变更文件
echo 正在添加所有变更文件...
git add .
if %errorlevel% neq 0 (
    echo 错误：添加文件失败！
    pause
    exit /b 1
)

REM 检查是否有文件被暂存
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo 没有需要提交的文件。
    pause
    exit /b 0
)

REM 生成带时间戳的提交信息
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YYYY=%dt:~0,4%"
set "MM=%dt:~4,2%"
set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%"
set "Min=%dt:~10,2%"
set "Sec=%dt:~12,2%"
set "default_commit_msg=自动提交 %YYYY%-%MM%-%DD% %HH%:%Min%:%Sec%"

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

REM 推送到远程仓库（使用SSH）
echo.
echo 正在通过SSH推送代码到远程仓库...
git push origin %branch%
if %errorlevel% neq 0 (
    echo 错误：推送失败！
    echo 请检查网络连接、SSH配置和GitHub权限
    pause
    exit /b 1
)

echo.
echo ============================================
echo 提交成功！
echo 提交信息：%commit_msg%
echo 仓库地址：git@github.com:huangwei-gem/code.git
echo ============================================
pause