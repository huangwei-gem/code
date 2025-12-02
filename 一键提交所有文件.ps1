# 一键提交所有文件到GitHub仓库
Write-Host "开始一键提交所有文件到GitHub仓库..."
Write-Host "目标仓库: https://github.com/huangwei-gem/code"

# 检查是否在Git仓库中
$gitStatus = git rev-parse --is-inside-work-tree 2>$null
if ($gitStatus -ne "true") {
    Write-Host "错误: 当前目录不是Git仓库!"
    exit 1
}

# 获取当前分支
$currentBranch = git rev-parse --abbrev-ref HEAD
Write-Host "当前分支: $currentBranch"

# 检查远程仓库
$remoteUrl = git config --get remote.origin.url
Write-Host "远程仓库: $remoteUrl"

Write-Host "检查文件状态..."

# 显示当前状态
$statusOutput = git status --porcelain
if ([string]::IsNullOrEmpty($statusOutput)) {
    Write-Host "工作目录已清理，没有需要提交的文件"
    exit 0
}

Write-Host "发现以下文件更改:"
$statusOutput | ForEach-Object {
    Write-Host "  $_"
}

# 生成提交信息
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMessage = "一键提交: $timestamp"

Write-Host ""
Write-Host "正在添加所有文件..."

# 添加所有文件（包括新文件、修改、删除）
git add -A

# 检查添加是否成功
if ($LASTEXITCODE -ne 0) {
    Write-Host "错误: 添加文件失败!"
    exit 1
}

Write-Host "所有文件已添加"

Write-Host "提交文件..."
Write-Host "提交信息: $commitMessage"

# 提交文件
git commit -m "$commitMessage"

# 检查提交是否成功
if ($LASTEXITCODE -ne 0) {
    Write-Host "错误: 提交失败!"
    exit 1
}

Write-Host "文件提交成功"

Write-Host "推送到远程仓库..."

# 推送到远程仓库
git push origin $currentBranch

# 检查推送是否成功
if ($LASTEXITCODE -ne 0) {
    Write-Host "错误: 推送失败!"
    exit 1
}

Write-Host "推送成功!"

# 显示最终的提交信息
Write-Host ""
Write-Host "一键提交完成!"
Write-Host "提交统计:"

# 显示提交统计
$commitCount = git rev-list --count HEAD
$author = git log -1 --pretty=format:"%an"
$date = git log -1 --pretty=format:"%ad" --date=format:"%Y-%m-%d %H:%M:%S"

Write-Host "  - 提交哈希: $(git rev-parse --short HEAD)"
Write-Host "  - 提交作者: $author"
Write-Host "  - 提交时间: $date"
Write-Host "  - 总提交数: $commitCount"

Write-Host ""
Write-Host "仓库地址: https://github.com/huangwei-gem/code"
Write-Host "所有文件已成功提交到GitHub!"