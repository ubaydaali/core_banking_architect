@echo off
echo [HYDRA] Compiling Core-Banking Engine...
cobc -x -free -o cobol_engine/hydra_core.exe src/hydra_core.cbl
if %errorlevel% neq 0 (
    echo [!] Compilation failed.
    exit /b %errorlevel%
)
echo [HYDRA] Compilation successful!
