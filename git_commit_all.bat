@echo off

echo Starting one-click commit all files to GitHub repository...
echo Target repository: https://github.com/huangwei-gem/code

:: Check if in Git repository
git rev-parse --is-inside-work-tree >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Current directory is not a Git repository!
    pause
    exit /b 1
)

:: Get current branch
for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD') do set currentBranch=%%i
echo Current branch: %currentBranch%

:: Check remote repository
for /f "tokens=*" %%i in ('git config --get remote.origin.url') do set remoteUrl=%%i
echo Remote repository: %remoteUrl%

echo.
echo Checking file status...

:: Check if there are any changes
git diff --quiet && git diff --staged --quiet
if %errorlevel% equ 0 (
    echo Working directory is clean, no files to commit
    pause
    exit /b 0
)

:: Show file changes
echo Found file changes:
git status --short

echo.
echo Adding all files...
git add -A
if %errorlevel% neq 0 (
    echo Error: Failed to add files!
    pause
    exit /b 1
)
echo All files added

:: Generate commit message
echo.
echo Committing files...
set timestamp=%date% %time%
set commitMessage=One-click commit: %timestamp%
echo Commit message: %commitMessage%

:: Commit files
git commit -m "%commitMessage%"
if %errorlevel% neq 0 (
    echo Error: Commit failed!
    pause
    exit /b 1
)
echo Files committed successfully

echo.
echo Pushing to remote repository...

:: Try to push with SSL verification disabled if regular push fails
git push origin %currentBranch%
if %errorlevel% neq 0 (
    echo Regular push failed, trying with SSL verification disabled...
    git -c http.sslVerify=false push origin %currentBranch%
    if %errorlevel% neq 0 (
        echo Error: Push failed!
        echo You may need to configure Git SSL settings or check your network connection.
        pause
        exit /b 1
    )
)

echo Push successful!

echo.
echo One-click commit completed!
echo All files successfully committed to GitHub!
pause