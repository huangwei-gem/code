# Git一键提交所有文件脚本
param(
    [string]$commitMessage = "",
    [switch]$push = $true
)

# 设置默认提交信息
if ($commitMessage -eq "") {
    $commitMessage = (Get-Date -Format "yyyy-MM-dd HH:mm:ss") + " 自动提交所有文件"
}

Write-Host "Git一键提交脚本" -ForegroundColor Green
Write-Host "================" -ForegroundColor Green

# 检查Git仓库
if (-not (Test-Path ".git")) {
    Write-Host "错误: 当前目录不是Git仓库!" -ForegroundColor Red
    exit 1
}

# 显示状态
git status --short

# 添加所有文件
git add .

# 检查是否有文件需要提交
$status = git status --porcelain
if (-not $status) {
    Write-Host "没有文件需要提交!" -ForegroundColor Yellow
    exit 0
}

# 提交文件
git commit -m "$commitMessage"

if ($push) {
    # 推送到远程仓库
    git push origin master
    Write-Host "推送完成!" -ForegroundColor Green
} else {
    Write-Host "提交完成!" -ForegroundColor Green
}