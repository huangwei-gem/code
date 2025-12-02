# 简化版Git一键提交所有文件脚本
# 作者: huangwei-gem
# 功能: 自动添加所有文件并提交到GitHub仓库

param(
    [string]$commitMessage = "$(Get-Date -Format 'MM-yyyy-dd HH:mm') Auto commit all files"
)

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "简化版Git一键提交所有文件脚本" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# 检查是否在Git仓库中
if (-not (Test-Path ".git")) {
    Write-Host "错误: 当前目录不是Git仓库!" -ForegroundColor Red
    Write-Host "请按任意键继续..." -ForegroundColor Yellow
    $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

# 显示当前状态
Write-Host "当前Git状态:" -ForegroundColor Yellow
git status --short
Write-Host ""

# 添加所有文件
Write-Host "正在添加所有文件..." -ForegroundColor Green
git add .

# 检查是否有文件需要提交
$status = git status --porcelain
if (-not $status) {
    Write-Host "没有文件需要提交!" -ForegroundColor Yellow
    Write-Host "请按任意键继续..." -ForegroundColor Yellow
    $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 0
}

Write-Host "发现需要提交的文件:" -ForegroundColor Yellow
Write-Host $status -ForegroundColor Gray
Write-Host ""

# 提交文件
Write-Host "正在提交文件..." -ForegroundColor Green
git commit -m $commitMessage

if ($LASTEXITCODE -ne 0) {
    Write-Host "提交失败!" -ForegroundColor Red
    Write-Host "请按任意键继续..." -ForegroundColor Yellow
    $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

Write-Host "提交成功!" -ForegroundColor Green
Write-Host "提交信息: $commitMessage" -ForegroundColor Gray
Write-Host ""

# 推送到远程仓库
Write-Host "正在推送到远程仓库..." -ForegroundColor Green
git push origin master

if ($LASTEXITCODE -ne 0) {
    Write-Host "推送失败! 请检查网络连接或远程仓库配置" -ForegroundColor Red
    Write-Host "请按任意键继续..." -ForegroundColor Yellow
    $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

Write-Host "推送成功!" -ForegroundColor Green
Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "所有操作完成!" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "请按任意键继续..." -ForegroundColor Yellow
$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")