Write-Host "正在初始化Git仓库..." -ForegroundColor Green
git init

Write-Host "正在添加所有文件..." -ForegroundColor Green
git add .

Write-Host "正在提交代码..." -ForegroundColor Green
git commit -m "初始提交：添加爬虫项目代码"

Write-Host "正在配置远程仓库..." -ForegroundColor Green
git remote add origin https://github.com/huangwei-gem/code

Write-Host "正在推送到远程仓库..." -ForegroundColor Green
git push -u origin master

Write-Host "代码提交和推送完成！" -ForegroundColor Green
Write-Host ""
Write-Host "你的代码已经推送到：https://github.com/huangwei-gem/code" -ForegroundColor Green