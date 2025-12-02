@echo off

REM Solve garbled code problem - Set to UTF-8 encoding
@chcp 65001 >nul

echo ============================================
echo One-click Git Commit Script
echo Target Repository: https://github.com/huangwei-gem/code
echo ============================================

REM Check if in git repository
if not exist .git (
    echo Error: Current directory is not a git repository!
    echo Please initialize git repository and add remote repository first:
    echo git init
    echo git remote add origin https://github.com/huangwei-gem/code.git
    pause
    exit /b 1
)

REM Check git remote configuration
echo Checking git remote configuration...
git remote -v > git_remote_temp.txt
set /p REMOTE_URL=<git_remote_temp.txt
del git_remote_temp.txt

REM Check if remote URL contains proxy (common issue)
echo %REMOTE_URL% | findstr /i "xget.xi-xu.me" >nul
if %errorlevel% equ 0 (
    echo Warning: Detected proxy URL in git remote configuration!
    echo This may cause connection issues. If push fails, check your git proxy settings.
    echo To remove proxy settings: git config --global --unset url.https://xget.xi-xu.me/gh/.insteadof
    echo.
)

REM Add all changed files
echo Adding all changed files...
git add .
if %errorlevel% neq 0 (
    echo Error: Failed to add files!
    pause
    exit /b 1
)

REM Generate commit message with timestamp - Using more reliable method
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do set "today=%%c-%%a-%%b"
for /f "tokens=1-2 delims=: " %%a in ('time /t') do set "now=%%a:%%b"
set "default_commit_msg=Auto-commit %today% %now%"

REM Prompt user to enter commit message or use default
echo.
echo Default commit message: %default_commit_msg%
echo Press Enter to use default message, or enter custom commit message:
set /p commit_msg=Commit message: 
if "%commit_msg%"=="" set commit_msg=%default_commit_msg%

REM Check if there are changes to commit
git status --porcelain > git_status_temp.txt
for %%i in (git_status_temp.txt) do set "size=%%~zi"

if %size% equ 0 (
    echo Info: Working tree is clean, nothing to commit.
    del git_status_temp.txt
    
    echo.
    echo ============================================
    echo Operation completed!
    echo Repository URL: https://github.com/huangwei-gem/code
    echo ============================================
    pause
    exit /b 0
) else (
    del git_status_temp.txt
    
    REM Commit code
    echo.
    echo Committing code...
    git commit -m "%commit_msg%"
    if %errorlevel% neq 0 (
        echo Error: Commit failed!
        pause
        exit /b 1
    )
    
    REM Push to remote repository
    echo.
    echo Pushing code to remote repository...
    git push origin master
    if %errorlevel% neq 0 (
        echo Error: Push failed!
        echo Please check network connection and GitHub permissions
        pause
        exit /b 1
    )
    
    echo.
    echo ============================================
    echo Commit successful!
    echo Commit message: %commit_msg%
    echo Repository URL: https://github.com/huangwei-gem/code
    echo ============================================
    pause
)