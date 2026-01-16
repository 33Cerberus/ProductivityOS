@echo off
setlocal enabledelayedexpansion

set OUTPUT_FILE=extracted_code.txt

rem Clear output file if it exists
if exist %OUTPUT_FILE% del %OUTPUT_FILE%

echo Collecting Python files...
echo.

rem Loop through all .py files recursively
for /r %%f in (*.py) do (
    set "filepath=%%f"
    
    rem Check if path contains .venv
    echo !filepath! | findstr /i "\.venv" >nul
    if errorlevel 1 (
        rem Get relative path
        set "relpath=%%f"
        set "relpath=!relpath:%CD%\=!"
        
        rem Add header with file path
        echo ========== !relpath! ========== >> %OUTPUT_FILE%
        echo. >> %OUTPUT_FILE%
        
        rem Add file content
        type "%%f" >> %OUTPUT_FILE%
        
        rem Add separator
        echo. >> %OUTPUT_FILE%
        echo. >> %OUTPUT_FILE%
        
        echo Processed: !relpath!
    )
)

echo.
echo Done! Output saved to %OUTPUT_FILE%
pause