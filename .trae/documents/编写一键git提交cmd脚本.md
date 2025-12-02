# 一键Git提交脚本实现计划

## 项目分析
- 项目结构：Python爬虫项目集合，包含多个子项目
- 现有文件：.gitignore已配置，排除了不必要的文件
- GitHub仓库：https://github.com/huangwei-gem/code

## 实现目标
创建一个cmd脚本，实现一键提交整个代码到指定GitHub仓库的功能。

## 脚本功能设计
1. **初始化检查**：检查当前目录是否为git仓库
2. **添加文件**：git add . 添加所有变更文件（排除.gitignore中指定的文件）
3. **提交信息**：自动生成带时间戳的提交信息，或允许用户自定义
4. **推送代码**：git push origin main 推送到指定仓库
5. **错误处理**：处理常见的git错误情况
6. **用户反馈**：清晰的操作提示和结果反馈

## 脚本实现步骤
1. 在项目根目录创建 `git_commit.cmd` 文件
2. 编写cmd脚本内容，包含以下核心命令：
   - 检查git环境
   - 执行git add .
   - 生成或获取提交信息
   - 执行git commit
   - 执行git push
3. 添加适当的错误处理和用户提示
4. 确保脚本在Windows环境下正常运行

## 脚本内容设计
```cmd
@echo off
REM 一键Git提交脚本
REM 提交到 https://github.com/huangwei-gem/code

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

REM 生成带时间戳的提交信息
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YYYY=%dt:~0,4%"
set "MM=%dt:~4,2%"
set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%"
set "Min=%dt:~10,2%"
set "Sec=%dt:~12,2%"
set "default_commit_msg=自动提交 %YYYY%-%MM%-%DD% %HH%:%MM%:%Sec%"

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
git push origin main
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
```

## 预期效果
1. 双击运行脚本，自动执行git提交流程
2. 显示清晰的操作步骤和结果
3. 处理常见错误情况
4. 允许用户自定义提交信息
5. 自动推送到指定GitHub仓库

## 后续优化建议
1. 添加分支选择功能
2. 支持强制推送选项
3. 添加代码状态检查（如是否有未跟踪文件）
4. 支持批量提交多个仓库
5. 添加日志记录功能