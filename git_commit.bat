@echo off

:: Git One-Click Commit Script (Batch Version)
:: For Windows Command Prompt

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

:: Ask to continue
echo Continue with commit? (y/n)
set /p "continue="
if /i not "%continue%"=="y" (
    echo Operation cancelled
    pause
    exit /b 0
)

:: Add all files
echo 2. Adding all modified files...
git add .
if %ERRORLEVEL% neq 0 (
    echo Git add failed
    pause
    exit /b 1
)
echo.

:: Ask for commit message
echo 3. Enter commit message:
set /p "commit_msg="
if "%commit_msg%"=="" (
    echo Commit message is empty, using default message.
    set "commit_msg=Auto commit - %date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%:%time:~6,2%"
)

:: Execute commit
echo 4. Executing commit...
git commit -m "%commit_msg%"
if %ERRORLEVEL% neq 0 (
    echo Git commit failed
    pause
    exit /b 1
)
echo.

:: Ask to push
echo 5. Push to remote repository? (y/n)
set /p "push="
if /i "%push%"=="y" (
    echo Pushing...
    git push origin master
    echo.
    if %ERRORLEVEL% equ 0 (
        echo Push successful!
    ) else (
        echo Push failed. Check network or permissions.
    )
) else (
    echo Skipping push.
)

echo.
echo === Operation completed ===
pause
