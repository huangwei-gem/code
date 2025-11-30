@echo off
echo 正在初始化Git仓库...
git init
echo.
echo 正在添加所有文件...
git add .
echo.
echo 正在提交代码...
git commit -m "初始提交：添加爬虫项目代码"
echo.
echo 提交完成！
echo.
echo 如果需要推送到远程仓库，请手动添加远程仓库并推送
echo 例如: git remote add origin <你的远程仓库URL>
echo      git push -u origin master
pause