Write-Host "正在初始化Git仓库..." -ForegroundColor Green
git init

Write-Host "正在添加所有文件..." -ForegroundColor Green
git add .

Write-Host "正在提交代码..." -ForegroundColor Green
git commit -m "初始提交：添加爬虫项目代码"

Write-Host "提交完成！" -ForegroundColor Green
Write-Host ""
Write-Host "如果需要推送到远程仓库，请手动添加远程仓库并推送" -ForegroundColor Yellow
Write-Host "例如: git remote add origin <你的远程仓库URL>" -ForegroundColor Yellow
Write-Host "     git push -u origin master" -ForegroundColor Yellow