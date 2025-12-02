# Git One-Click Commit Script (PowerShell Version)
# For Windows PowerShell 5.1 and above
# 一键提交，自动使用日期作为提交信息，自动推送到远程仓库

# Check if Git is installed
try {
    git --version | Out-Null
} catch {
    Write-Host "Git is not installed or not in PATH"
    Read-Host "Press Enter to exit"
    exit 1
}

# Show current status
Write-Host "=== Git One-Click Commit Script ==="
Write-Host "Current directory: $(Get-Location)"
Write-Host ""
Write-Host "1. Checking current status..."
git status
Write-Host ""

# Add all files
Write-Host "2. Adding all modified files..."
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "Git add failed"
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Use date as commit message
$commit_msg = "Auto commit - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host "3. Using commit message: $commit_msg"

# Execute commit
Write-Host "4. Executing commit..."
git commit -m "$commit_msg"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Git commit failed"
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Push to remote repository automatically
Write-Host "5. Pushing to remote repository..."
git push origin master
if ($LASTEXITCODE -eq 0) {
    Write-Host "Push successful!"
} else {
    Write-Host "Push failed! Error: SSL certificate problem or network issue." -ForegroundColor Red
    Write-Host "Please check:" -ForegroundColor Yellow
    Write-Host "1. Your network connection" -ForegroundColor Yellow
    Write-Host "2. Git SSL configuration" -ForegroundColor Yellow
    Write-Host "3. Your GitHub credentials" -ForegroundColor Yellow
    Write-Host "" -ForegroundColor White
    Write-Host "Solution 1: Disable SSL verification temporarily:" -ForegroundColor Cyan
    Write-Host "git config --global http.sslVerify false" -ForegroundColor Green
    Write-Host "" -ForegroundColor White
    Write-Host "Solution 2: Use SSH instead of HTTPS:" -ForegroundColor Cyan
    Write-Host "git remote set-url origin git@github.com:huangwei-gem/code.git" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== Operation completed ==="
Read-Host "Press Enter to exit"
