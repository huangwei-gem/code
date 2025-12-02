# Git One-Click Commit Script (PowerShell Version)
# For Windows PowerShell 5.1 and above

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

# Ask to continue
$continue = Read-Host "Continue with commit? (y/n)"
if ($continue -notmatch "^[yY]$") {
    Write-Host "Operation cancelled"
    Read-Host "Press Enter to exit"
    exit 0
}

# Add all files
Write-Host "2. Adding all modified files..."
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "Git add failed"
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Ask for commit message
$commit_msg = Read-Host "3. Enter commit message"
if ([string]::IsNullOrEmpty($commit_msg)) {
    $commit_msg = "Auto commit - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    Write-Host "Using default commit message: $commit_msg"
}

# Execute commit
Write-Host "4. Executing commit..."
git commit -m "$commit_msg"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Git commit failed"
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Ask to push
$push = Read-Host "5. Push to remote repository? (y/n)"
if ($push -match "^[yY]$") {
    Write-Host "Pushing..."
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
} else {
    Write-Host "Skipping push" -ForegroundColor Gray
}

Write-Host ""
Write-Host "=== Operation completed ==="
Read-Host "Press Enter to exit"
