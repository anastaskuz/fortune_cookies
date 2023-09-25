@echo off

call venv\Scripts\activate

set TOKEN=
set NAME_DB=
set PATH_FOR_DB=
set PATH_FOR_IMG=

python main.py
pause