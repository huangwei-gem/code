# One-click commit all files to GitHub repository
Write-Host "Starting one-click commit all files to GitHub repository..."
Write-Host "Target repository: https://github.com/huangwei-gem/code"

# Check if in Git repository
$gitCheck = git rev-parse --is-inside-work-tree 2>$null
if ($gitCheck -ne "true") {
    Write-Host "Error: Current directory is not a Git repository!"
    exit 1
}

# Get current branch
$branch = git rev-parse --abbrev-ref HEAD
Write-Host "Current branch: $branch"

# Get remote URL
$remote = git config --get remote.origin.url
Write-Host "Remote repository: $remote"

Write-Host ""
Write-Host "Checking file status..."

# Check for changes
$changes = git status --porcelain
if ([string]::IsNullOrEmpty($changes)) {
    Write-Host "Working directory is clean, no files to commit"
    exit 0
}

Write-Host "Found file changes:"
Write-Host $changes

Write-Host ""
Write-Host "Adding all files..."
git add -A
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to add files!"
    exit 1
}
Write-Host "All files added"

Write-Host ""
Write-Host "Committing files..."
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$message = "One-click commit: $timestamp"
Write-Host "Commit message: $message"

git commit -m $message
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Commit failed!"
    exit 1
}
Write-Host "Files committed successfully"

Write-Host ""
Write-Host "Pushing to remote repository..."
git push origin $branch
if ($LASTEXITCODE -ne 0) {
    Write-Host "Regular push failed, trying with SSL verification disabled..."
    git -c http.sslVerify=false push origin $branch
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Push failed!"
        Write-Host "You may need to configure Git SSL settings or check your network connection."
        exit 1
    }
}
Write-Host "Push successful!"

Write-Host ""
Write-Host "One-click commit completed!"
Write-Host "All files successfully committed to GitHub!"