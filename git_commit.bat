@echo off

:: Git One-Click Commit Script (Batch Version)
:: For Windows Command Prompt
:: 一键提交，自动使用日期作为提交信息

:: Set code page to UTF-8
chcp 65001 > nul

:: Check if Git is installed
git --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Git is not installed or not in PATH
    pause
    exit /b 1
)

:: Show current status
echo === Git One-Click Commit Script ===
echo Current directory: %cd%
echo.
echo 1. Checking current status...
git status
echo.

:: Add all files
echo 2. Adding all modified files...
git add .
if %ERRORLEVEL% neq 0 (
    echo Git add failed
    pause
    exit /b 1
)
echo.

:: Use date as commit message
set "commit_msg=Auto commit - %date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%:%time:~6,2%"
echo 3. Using commit message: %commit_msg%

:: Execute commit
echo 4. Executing commit...
git commit -m "%commit_msg%"
if %ERRORLEVEL% neq 0 (
    echo Git commit failed
    pause
    exit /b 1
)
echo.

:: Push to remote repository automatically
echo 5. Pushing to remote repository...
git push origin master
echo.
if %ERRORLEVEL% equ 0 (
    echo Push successful!
) else (
    echo Push failed! Error: SSL certificate problem or network issue.
    echo Please check:
    echo 1. Your network connection
    echo 2. Git SSL configuration
    echo 3. Your GitHub credentials
    echo.
    echo Solution 1: Disable SSL verification temporarily:
    echo git config --global http.sslVerify false
    echo.
    echo Solution 2: Use SSH instead of HTTPS:
    echo git remote set-url origin git@github.com:huangwei-gem/code.git
)

echo.
echo === Operation completed ===
pause
