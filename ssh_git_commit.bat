@echo off
REM One-click SSH commit script for GitHub repository
REM Repository URL: git@github.com:huangwei-gem/code.git

chcp 65001 >nul

echo ============================================
echo One-click Git Commit Script (SSH)
echo Target Repository: git@github.com:huangwei-gem/code.git
echo ============================================

REM Check if we are in a git repository
if not exist .git (
    echo Error: Current directory is not a git repository!
    echo Please initialize a git repository and add remote first:
    echo git init
    echo git remote add origin git@github.com:huangwei-gem/code.git
    pause
    exit /b 1
)

REM Get current branch
for /f %%i in ('git rev-parse --abbrev-ref HEAD') do set branch=%%i
echo Current Branch: %branch%

REM Add all changed files
echo Adding all changed files...
git add .
if %errorlevel% neq 0 (
    echo Error: Failed to add files!
    pause
    exit /b 1
)

REM Check if there are files staged for commit
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo No files to commit.
    pause
    exit /b 0
)

REM Generate timestamp for commit message
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YYYY=%dt:~0,4%"
set "MM=%dt:~4,2%"
set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%"
set "Min=%dt:~10,2%"
set "Sec=%dt:~12,2%"
set "default_commit_msg=Auto commit %YYYY%-%MM%-%DD% %HH%:%Min%:%Sec%"

REM Prompt user for commit message or use default
echo.
echo Default commit message: %default_commit_msg%
echo Press Enter to use default, or enter custom commit message:
set /p commit_msg=Commit Message: 
if "%commit_msg%"=="" set commit_msg=%default_commit_msg%

REM Commit changes
echo.
echo Committing changes...
git commit -m "%commit_msg%"
if %errorlevel% neq 0 (
    echo Error: Commit failed!
    pause
    exit /b 1
)

REM Push to remote repository (using SSH)
echo.
echo Pushing changes to remote repository via SSH...
git push origin %branch%
if %errorlevel% neq 0 (
    echo Error: Push failed!
    echo Please check network connection, SSH configuration and GitHub permissions
    pause
    exit /b 1
)

echo.
echo ============================================
echo Commit Successful!
echo Commit Message: %commit_msg%
echo Repository URL: git@github.com:huangwei-gem/code.git
echo ============================================
pause