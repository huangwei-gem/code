# Git大文件上传脚本
# 提供多种解决方案处理大文件

$remoteUrl = "https://github.com/huangwei-gem/code"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Git大文件上传脚本" -ForegroundColor Cyan
Write-Host "时间: $timestamp" -ForegroundColor Cyan
Write-Host "远程仓库: $remoteUrl" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# 函数：检查Git LFS是否安装
function Test-GitLFS {
    try {
        $result = git lfs version 2>$null
        return $result -ne $null
    } catch {
        return $false
    }
}

# 函数：配置Git LFS
function Configure-GitLFS {
    Write-Host "正在配置Git LFS..." -ForegroundColor Green
    
    # 初始化LFS
    git lfs install
    
    # 追踪大文件类型
    git lfs track "*.zip"
    git lfs track "*.rar"
    git lfs track "*.7z"
    git lfs track "*.tar.gz"
    git lfs track "*.mp4"
    git lfs track "*.mp3"
    git lfs track "*.avi"
    git lfs track "*.mov"
    git lfs track "*.xlsx"
    git lfs track "*.docx"
    git lfs track "*.pptx"
    git lfs track "*.pdf"
    
    # 添加.gitattributes文件
    git add .gitattributes
    
    Write-Host "Git LFS配置完成！" -ForegroundColor Green
}

# 函数：查找大文件
function Find-LargeFiles {
    param([int]$maxSizeMB = 90)
    
    Write-Host "正在查找大文件..." -ForegroundColor Green
    $largeFiles = Get-ChildItem -Path "." -Recurse -File | Where-Object { $_.Length -gt ($maxSizeMB * 1MB) }
    
    if ($largeFiles.Count -gt 0) {
        Write-Host "发现 $($largeFiles.Count) 个大文件:" -ForegroundColor Yellow
        foreach ($file in $largeFiles) {
            Write-Host "  - $($file.FullName) ($([math]::Round($file.Length / 1MB, 2)) MB)" -ForegroundColor Gray
        }
        return $true
    }
    return $false
}

# 主流程
Write-Host "选择上传方案：" -ForegroundColor Cyan
Write-Host "1. Git LFS (推荐) - 官方大文件存储方案" -ForegroundColor Green
Write-Host "2. 智能过滤 - 只上传代码，排除大文件" -ForegroundColor Green
Write-Host "3. 强制上传 - 尝试直接上传所有文件" -ForegroundColor Yellow
Write-Host ""

$choice = Read-Host "请输入选项 (1-3)"

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

switch ($choice) {
    "1" {
        # Git LFS方案
        Write-Host "使用Git LFS方案..." -ForegroundColor Cyan
        
        if (!(Test-GitLFS)) {
            Write-Host "Git LFS未安装！" -ForegroundColor Red
            Write-Host "请访问 https://git-lfs.com/ 下载安装" -ForegroundColor Yellow
            Write-Host "或使用 Chocolatey: choco install git-lfs" -ForegroundColor Gray
            exit 1
        }
        
        # 配置Git LFS
        Configure-GitLFS
        
        Write-Host "正在添加所有文件..." -ForegroundColor Green
        git add .
        
        Write-Host "正在提交代码..." -ForegroundColor Green
        $commitMessage = "Git LFS提交：$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git commit -m $commitMessage
        
        Write-Host "正在推送到远程仓库..." -ForegroundColor Green
        git push -u origin master
        
        Write-Host "Git LFS上传完成！" -ForegroundColor Green
    }
    
    "2" {
        # 智能过滤方案
        Write-Host "使用智能过滤方案..." -ForegroundColor Cyan
        
        if (Find-LargeFiles) {
            Write-Host "大文件将被排除上传" -ForegroundColor Yellow
        }
        
        # 创建临时.gitignore
        $tempGitignore = @"
# 大文件排除规则
*.zip
*.rar
*.7z
*.tar.gz
*.mp4
*.mp3
*.avi
*.mov
*.exe
*.dll
*.pyd

# 数据文件
data/
datasets/
*.csv
*.json
*.xml
*.db
*.sqlite

# 临时文件
temp/
tmp/
*.tmp
*.temp

# 日志文件
*.log
logs/
"@
        
        $tempGitignore | Out-File -FilePath ".gitignore_temp" -Encoding UTF8 -Force
        Copy-Item ".gitignore_temp" ".gitignore" -Force
        
        Write-Host "已创建过滤规则，大文件将被排除" -ForegroundColor Yellow
        
        Write-Host "正在添加文件..." -ForegroundColor Green
        git add .
        
        Write-Host "正在提交代码..." -ForegroundColor Green
        $commitMessage = "智能过滤提交：$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git commit -m $commitMessage
        
        Write-Host "正在推送到远程仓库..." -ForegroundColor Green
        git push -u origin master
        
        Write-Host "智能过滤上传完成！" -ForegroundColor Green
    }
    
    "3" {
        # 强制上传方案
        Write-Host "使用强制上传方案..." -ForegroundColor Yellow
        Write-Host "警告：此方案可能因文件大小限制而失败！" -ForegroundColor Red
        
        if (Find-LargeFiles) {
            Write-Host "检测到有大文件，建议改用方案1或2" -ForegroundColor Red
            $confirm = Read-Host "仍要继续吗? (y/n)"
            if ($confirm -ne "y" -and $confirm -ne "Y") {
                Write-Host "取消操作" -ForegroundColor Yellow
                exit 0
            }
        }
        
        Write-Host "正在添加所有文件..." -ForegroundColor Green
        git add .
        
        Write-Host "正在提交代码..." -ForegroundColor Green
        $commitMessage = "强制提交：$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git commit -m $commitMessage
        
        Write-Host "正在推送到远程仓库..." -ForegroundColor Green
        try {
            git push -u origin master
            Write-Host "强制上传成功！" -ForegroundColor Green
        } catch {
            Write-Host "上传失败：$_" -ForegroundColor Red
            Write-Host "建议改用Git LFS方案" -ForegroundColor Yellow
        }
    }
    
    default {
        Write-Host "无效选项！" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "操作完成！仓库地址：$remoteUrl" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan