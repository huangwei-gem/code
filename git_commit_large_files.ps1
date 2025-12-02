# Git增强版一键提交脚本 - 支持大文件和LFS
# 作者: huangwei-gem
# 功能: 自动添加所有文件，处理大文件，支持Git LFS

param(
    [string]$commitMessage = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') 自动提交所有文件",
    [switch]$push = $true,
    [switch]$force = $false,
    [switch]$useLFS = $true,
    [int]$largeFileSizeMB = 50  # 大于50MB的文件使用LFS
)

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Git增强版一键提交脚本 (支持LFS)" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# 检查是否在Git仓库中
if (-not (Test-Path ".git")) {
    Write-Host "错误: 当前目录不是Git仓库!" -ForegroundColor Red
    exit 1
}

# 检查Git LFS是否安装
if ($useLFS) {
    try {
        $lfsCheck = git lfs version
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Git LFS已安装: $lfsCheck" -ForegroundColor Green
        } else {
            Write-Host "警告: Git LFS未安装，大文件处理功能将不可用" -ForegroundColor Yellow
            $useLFS = $false
        }
    } catch {
        Write-Host "警告: Git LFS未安装，大文件处理功能将不可用" -ForegroundColor Yellow
        $useLFS = $false
    }
}

# 显示当前状态
Write-Host "当前Git状态:" -ForegroundColor Yellow
git status --short
Write-Host ""

# 查找大文件并配置LFS
if ($useLFS) {
    Write-Host "正在扫描大文件 (>$largeFileSizeMB MB)..." -ForegroundColor Green
    
    # 获取所有文件
    $allFiles = git ls-files --cached --others --exclude-standard
    $largeFiles = @()
    
    foreach ($file in $allFiles) {
        if (Test-Path $file) {
            $fileSize = (Get-Item $file).Length / 1MB
            if ($fileSize -gt $largeFileSizeMB) {
                $largeFiles += $file
                Write-Host "发现大文件: $file ($([math]::Round($fileSize, 2)) MB)" -ForegroundColor Yellow
            }
        }
    }
    
    # 为大文件配置LFS
    if ($largeFiles.Count -gt 0) {
        Write-Host "正在为大文件配置Git LFS..." -ForegroundColor Green
        foreach ($largeFile in $largeFiles) {
            # 获取文件扩展名
            $extension = [System.IO.Path]::GetExtension($largeFile)
            if ($extension) {
                $pattern = "*$extension"
                git lfs track $pattern
                Write-Host "已配置LFS跟踪: $pattern" -ForegroundColor Gray
            }
        }
        git add .gitattributes
    }
}

# 添加所有文件
Write-Host "正在添加所有文件..." -ForegroundColor Green
if ($force) {
    git add -A
} else {
    git add .
}

# 检查是否有文件需要提交
$status = git status --porcelain
if (-not $status) {
    Write-Host "没有文件需要提交!" -ForegroundColor Yellow
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
    exit 1
}

Write-Host "提交成功!" -ForegroundColor Green
Write-Host "提交信息: $commitMessage" -ForegroundColor Gray
Write-Host ""

# 推送到远程仓库
if ($push) {
    Write-Host "正在推送到远程仓库..." -ForegroundColor Green
    if ($force) {
        git push -f origin master
    } else {
        git push origin master
    }
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "推送失败! 请检查网络连接或远程仓库配置" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "推送成功!" -ForegroundColor Green
    
    # 如果使用了LFS，推送LFS对象
    if ($useLFS) {
        Write-Host "正在推送LFS对象..." -ForegroundColor Green
        git lfs push origin master --all
        if ($LASTEXITCODE -eq 0) {
            Write-Host "LFS对象推送成功!" -ForegroundColor Green
        } else {
            Write-Host "LFS对象推送失败!" -ForegroundColor Red
        }
    }
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "所有操作完成!" -ForegroundColor Green
if ($useLFS) {
    Write-Host "已处理大文件并配置Git LFS" -ForegroundColor Gray
}
Write-Host "=========================================" -ForegroundColor Cyan