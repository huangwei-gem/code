# 一键通过SSH提交代码到GitHub仓库
# 仓库地址: git@github.com:huangwei-gem/code.git

# 设置UTF-8编码以正确显示中文
$OutputEncoding = New-Object -typename System.Text.UTF8Encoding
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "============================================" -ForegroundColor Green
Write-Host "一键Git提交脚本 (SSH方式)" -ForegroundColor Green
Write-Host "目标仓库：git@github.com:huangwei-gem/code.git" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green

try {
    # 检查是否在git仓库中
    $gitDir = Get-ChildItem -Path . -Filter ".git" -Directory -ErrorAction SilentlyContinue
    if (-not $gitDir) {
        Write-Host "错误：当前目录不是git仓库！" -ForegroundColor Red
        Write-Host "请先初始化git仓库并添加远程仓库：" -ForegroundColor Yellow
        Write-Host "git init" -ForegroundColor Yellow
        Write-Host "git remote add origin git@github.com:huangwei-gem/code.git" -ForegroundColor Yellow
        Pause
        exit 1
    }

    # 获取当前分支
    $branch = git rev-parse --abbrev-ref HEAD
    Write-Host "当前分支: $branch" -ForegroundColor Cyan

    # 添加所有变更文件
    Write-Host "正在添加所有变更文件..." -ForegroundColor Cyan
    git add .

    # 检查是否有文件被暂存
    $stagedChanges = git diff --cached --name-only
    if ([string]::IsNullOrEmpty($stagedChanges)) {
        Write-Host "没有需要提交的文件。" -ForegroundColor Yellow
        exit 0
    }

    # 生成带时间戳的提交信息
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $defaultCommitMsg = "自动提交 $timestamp"

    # 提示用户输入提交信息或使用默认值
    Write-Host "`n默认提交信息：$defaultCommitMsg" -ForegroundColor Cyan
    Write-Host "按Enter使用默认信息，或输入自定义提交信息：" -ForegroundColor Cyan
    $commitMsg = Read-Host "提交信息"

    if ([string]::IsNullOrWhiteSpace($commitMsg)) {
        $commitMsg = $defaultCommitMsg
    }

    # 提交代码
    Write-Host "`n正在提交代码..." -ForegroundColor Cyan
    git commit -m "$commitMsg"

    # 推送到远程仓库（使用SSH）
    Write-Host "`n正在通过SSH推送代码到远程仓库..." -ForegroundColor Cyan
    git push origin $branch

    Write-Host "`n============================================" -ForegroundColor Green
    Write-Host "提交成功！" -ForegroundColor Green
    Write-Host "提交信息：$commitMsg" -ForegroundColor Green
    Write-Host "仓库地址：git@github.com:huangwei-gem/code.git" -ForegroundColor Green
    Write-Host "============================================" -ForegroundColor Green
}
catch {
    Write-Host "`n错误：$($_.Exception.Message)" -ForegroundColor Red
    Write-Host "请检查网络连接、SSH配置和GitHub权限" -ForegroundColor Yellow
    Pause
    exit 1
}

Pause