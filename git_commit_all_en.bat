@echo off
chcp 65001 >nul
:: Git Auto Commit Script
:: Author: huangwei-gem
:: Function: Automatically add all files and commit to GitHub repository

echo =========================================
echo Git Auto Commit All Files Script
echo =========================================
echo.

:: Check if we are in a Git repository
if not exist ".git" (
    echo Error: Current directory is not a Git repository!
    pause
    exit /b 1
)

:: Get current date and time as default commit message
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a:%%b)
set "default_msg=%mydate% %mytime% Auto commit all files"

:: Ask for commit message
set /p "commit_msg=Enter commit message (default: %default_msg%): "
if "%commit_msg%"=="" set "commit_msg=%default_msg%"

:: Show current status
echo.
echo Current Git Status:
git status --short
echo.

:: Add all files
echo Adding all files...
git add .

:: Check if there are files to commit
git status --porcelain > temp_git_status.txt
for %%i in (temp_git_status.txt) do set size=%%~zi
if %size% equ 0 (
    echo.
    echo No files to commit!
    del temp_git_status.txt
    pause
    exit /b 0
)

echo.
echo Files to be committed:
type temp_git_status.txt
del temp_git_status.txt
echo.

:: Commit files
echo Committing files...
git commit -m "%commit_msg%"

if %errorlevel% neq 0 (
    echo.
    echo Commit failed!
    pause
    exit /b 1
)

echo.
echo Commit successful!
echo Commit message: %commit_msg%
echo.

:: Push to remote repository
set /p "push_confirm=Push to remote repository? (y/n, default: y): "
if /i "%push_confirm%"=="n" (
    echo.
    echo Skipping push operation.
) else (
    echo.
    echo Pushing to remote repository...
    git push origin master
    
    if %errorlevel% neq 0 (
        echo.
        echo Push failed! Please check network connection or remote repository configuration
        pause
        exit /b 1
    )
    
    echo.
    echo Push successful!
)

echo.
echo =========================================
echo All operations completed!
echo =========================================
pause