@echo off
setlocal
cd /d "%~dp0"

echo ========================================
echo       LABORATORIO DE SHERLOCK
echo ========================================
echo.

where py >nul 2>&1
if errorlevel 1 (
    echo No se encontro Python.
    echo Instala Python 3.9 o superior y marca "Add Python to PATH".
    echo Descarga oficial: https://www.python.org/downloads/
    pause
    exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
    echo Creando un entorno aislado de Python...
    py -3 -m venv .venv
    if errorlevel 1 (
        echo No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

echo Comprobando Sherlock y sus dependencias...
".venv\Scripts\python.exe" -m pip install --disable-pip-version-check -r requirements.txt
if errorlevel 1 (
    echo No se pudo instalar Sherlock. Revisa tu conexion a Internet.
    pause
    exit /b 1
)

echo.
".venv\Scripts\python.exe" buscar_usuario.py
set "CODIGO=%ERRORLEVEL%"

echo.
pause
exit /b %CODIGO%
