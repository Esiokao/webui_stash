@echo off
setlocal enabledelayedexpansion

:: Step 0: 解析參數
set OPEN_BROWSER=true
for %%a in (%*) do (
    if "%%a"=="--no-open" (
        set OPEN_BROWSER=false
    )
)

:: Step 1: Timestamp
for /f "tokens=1-4 delims=/ " %%a in ("%date%") do (
    set MM=%%a
    set DD=%%b
    set YYYY=%%c
)
for /f "tokens=1-2 delims=:." %%a in ("%time%") do (
    set HH=%%a
    set MIN=%%b
)
if "!HH:~0,1!"==" " set HH=0!HH:~1,1!
if "!MIN:~0,1!"==" " set MIN=0!MIN:~1,1!

:: Step 2: Git commit hash
set GIT_HASH=nogit
for /f %%i in ('git rev-parse --short HEAD 2^>nul') do set GIT_HASH=%%i

:: Step 3: Report file name
set TIMESTAMP=!YYYY!-!MM!-!DD!_!HH!!MIN!
set REPORT_NAME=report_!TIMESTAMP!_git-!GIT_HASH!.html
set REPORT_DIR=reports

:: Step 4: Ensure reports dir exists
if not exist "!REPORT_DIR!" mkdir "!REPORT_DIR!"

:: Step 5: Run tests
echo 🧪 Running tests...
poetry run pytest --alluredir=allure-results .

:: Step 6: Generate single-file HTML report
echo 📄 Generating single-file Allure report...
call allure generate --single-file allure-results -o tmp-report --clean

:: Step 7: Move report if it exists
if exist ".\tmp-report\index.html" (
    move /Y ".\tmp-report\index.html" "!REPORT_DIR!\!REPORT_NAME!"
    rmdir /s /q tmp-report
    echo ✅ Report saved to !REPORT_DIR!\!REPORT_NAME!

    :: Step 8: Open in browser (unless --no-browser)
    if /I "!OPEN_BROWSER!"=="true" (
        echo 🌐 Opening report in browser...
        start "" "!REPORT_DIR!\!REPORT_NAME!"
    ) else (
        echo 🚫 Skipping browser launch (via --no-browser)
    )
) else (
    echo ⚠️ Report not generated.
)

:: Step 9: Clean up allure-results
if exist "allure-results" (
    rmdir /s /q allure-results
    echo 🧹 Cleaned up allure-results
)

endlocal
