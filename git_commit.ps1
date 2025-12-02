# Git自动提交和推送脚本
# 适用于爬虫项目

$remoteUrl = "https://github.com/huangwei-gem/code"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Git自动提交和推送脚本" -ForegroundColor Cyan
Write-Host "时间: $timestamp" -ForegroundColor Cyan
Write-Host "远程仓库: $remoteUrl" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# 检查是否已初始化Git仓库
if (!(Test-Path .git)) {
    Write-Host "正在初始化Git仓库..." -ForegroundColor Green
    git init
}

# 检查远程仓库是否已配置
$remoteExists = git remote get-url origin 2>$null
if (!$remoteExists) {
    Write-Host "正在配置远程仓库..." -ForegroundColor Green
    git remote add origin $remoteUrl
} else {
    Write-Host "远程仓库已配置: $remoteExists" -ForegroundColor Yellow
}

Write-Host "正在检查文件更改..." -ForegroundColor Green
$status = git status --porcelain

if (!$status) {
    Write-Host "没有文件更改需要提交" -ForegroundColor Yellow
} else {
    Write-Host "发现文件更改:" -ForegroundColor Green
    Write-Host $status -ForegroundColor Gray
    
    Write-Host "正在添加更改的文件..." -ForegroundColor Green
    git add .
    
    Write-Host "正在提交代码..." -ForegroundColor Green
    $commitMessage = "自动提交：$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    git commit -m $commitMessage
    
    Write-Host "正在推送到远程仓库..." -ForegroundColor Green
    git push -u origin master
    
    Write-Host "代码提交和推送完成！" -ForegroundColor Green
}

Write-Host ""
Write-Host "操作完成！你的代码仓库地址：" -ForegroundColor Cyan
Write-Host $remoteUrl -ForegroundColor Blue
Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan