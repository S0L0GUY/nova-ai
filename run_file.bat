@echo off
:loop
python f:\USB\vr-ai-chatbot-main\main.py
IF %ERRORLEVEL% NEQ 0 (
    echo "Program crashed. Restarting..."
    timeout /t 5
    goto loop
)
