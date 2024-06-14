@echo off
:: Batch script to run a PowerShell script as an administrator

:: Get the current directory of the batch file
set "script_dir=%~dp0"
set "script_path=%script_dir%update_python_and_dependencies.ps1"
set "error_log_path=%script_dir%error_log.txt"

:: Check if the PowerShell script exists
if not exist "%script_path%" (
    echo PowerShell script not found: %script_path%
    echo Make sure the script is in the same directory as this batch file.
    pause
    exit /b 1
)

:: Check if running as administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    :: If not running as administrator, restart with elevated privileges
    echo Requesting administrative privileges...
    echo Please confirm the UAC prompt.
    PowerShell -Command "Start-Process -FilePath '%comspec%' -ArgumentList '/c %~dpnx0' -Verb RunAs"
    exit /b
)

:: If running as administrator, execute the PowerShell script
echo Running PowerShell script as administrator...
PowerShell -NoProfile -ExecutionPolicy Bypass -File "%script_path%" > "%error_log_path%" 2>&1

set "ps_errorlevel=%errorlevel%"

:: Check if the PowerShell script returned an error
if %ps_errorlevel% neq 0 (
    echo Error occurred while running PowerShell script. Check the error log for details.
    echo Error level: %ps_errorlevel%
    echo Error occurred at %date% %time% with error level %ps_errorlevel% >> "%error_log_path%"
    type "%error_log_path%"
) else (
    echo PowerShell script executed successfully.
)

pause
exit /b %ps_errorlevel%
