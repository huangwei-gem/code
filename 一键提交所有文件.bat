@echo off

:: 一键提交所有文件到GitHub仓库
:: 目标仓库: https://github.com/huangwei-gem/code

echo 开始一键提交所有文件到GitHub仓库...
echo 目标仓库: https://github.com/huangwei-gem/code
echo.

:: 检查是否在Git仓库中
git rev-parse --is-inside-work-tree >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 当前目录不是Git仓库!
    pause
    exit /b 1
)

:: 获取当前分支
for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD') do set currentBranch=%%i
echo 当前分支: %currentBranch%

:: 检查远程仓库
for /f "tokens=*" %%i in ('git config --get remote.origin.url') do set remoteUrl=%%i
echo 远程仓库: %remoteUrl%

echo.
echo 检查文件状态...

:: 显示当前状态
git status --porcelain > temp_status.txt
set /p statusOutput=<temp_status.txt
del temp_status.txt

if "%statusOutput%"=="" (
    echo 工作目录已清理，没有需要提交的文件
    pause
    exit /b 0
)

:: 显示文件更改
echo 发现以下文件更改:
git status --porcelain

echo.
echo 正在添加所有文件...

:: 添加所有文件（包括新文件、修改、删除）
git add -A
if %errorlevel% neq 0 (
    echo 错误: 添加文件失败!
    pause
    exit /b 1
)

echo 所有文件已添加

:: 生成提交信息
echo.
echo 提交文件...
for /f "tokens=*" %%i in ('powershell -command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"') do set timestamp=%%i
set commitMessage=一键提交: %timestamp%
echo 提交信息: %commitMessage%

:: 提交文件
git commit -m "%commitMessage%"
if %errorlevel% neq 0 (
    echo 错误: 提交失败!
    pause
    exit /b 1
)

echo 文件提交成功

echo.
echo 推送到远程仓库...

:: 推送到远程仓库
git push origin %currentBranch%
if %errorlevel% neq 0 (
    echo 错误: 推送失败!
    pause
    exit /b 1
)

echo 推送成功!

:: 显示最终的提交信息
echo.
echo 一键提交完成!
echo 提交统计:

:: 显示提交统计
for /f "tokens=*" %%i in ('git rev-list --count HEAD') do set commitCount=%%i
for /f "tokens=*" %%i in ('git log -1 --pretty=format:"%%an"') do set author=%%i
for /f "tokens=*" %%i in ('git log -1 --pretty=format:"%%ad" --date=format:"%%Y-%%m-%%d %%H:%%M:%%S"') do set date=%%i
for /f "tokens=*" %%i in ('git rev-parse --short HEAD') do set commitHash=%%i

echo   - 提交哈希: %commitHash%
echo   - 提交作者: %author%
echo   - 提交时间: %date%
echo   - 总提交数: %commitCount%

echo.
echo 仓库地址: https://github.com/huangwei-gem/code
echo 所有文件已成功提交到GitHub!
echo.
pause