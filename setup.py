import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['AyraIcon.ico']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="AyraIcon.ico",
    target_name="AYRA"
)

# SETUP CX FREEZE
setup(
    name = "AYRA",
    version = "1.0",
    description = "GUI for Analog/Digital Cards",
    author = "AYRA Electronics",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
