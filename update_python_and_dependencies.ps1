# PowerShell script to check for Python installation, update it, and install required dependencies

# Paths for error logging
$errorLogPath = "$PSScriptRoot\error_log.txt"

function Log-Error {
    param (
        [string]$message
    )

    # Attempt to log the error message, retrying if the file is in use
    for ($i = 0; $i -lt 5; $i++) {
        try {
            Add-content -Path $errorLogPath -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss'): $message"
            return
        } catch {
            Start-Sleep -Seconds 1
        }
    }
}

# Check if Python is installed
Write-Host "Checking for Python installation and updates..."
$pythonInstalled = Get-Command python -ErrorAction SilentlyContinue

if (-not $pythonInstalled) {
    Log-Error "Python is not installed. Please install Python first."
    Write-Host "Python is not installed. Please install Python first."
    exit 1
}

# Check for the latest Python version and install it
Write-Host "Updating Python to the latest version..."
try {
    Start-Process "powershell" -ArgumentList "winget install --id Python.Python.3 --source winget" -Wait -NoNewWindow
} catch {
    Log-Error "Failed to update Python: $_"
    Write-Host "Failed to update Python. Check the error log for details."
    exit 1
}

# Install required Python packages
Write-Host "Installing required Python packages..."
try {
    python -m pip install --upgrade pip
    python -m pip install Pillow ffmpeg PyAV
} catch {
    Log-Error "Failed to install Python packages: $_"
    Write-Host "Failed to install Python packages. Check the error log for details."
    exit 1
}

Write-Host "Python and required packages are successfully installed and updated."
