import winreg
import os
import asyncio

system32_path = os.path.join(os.environ['SystemRoot'], 'System32')
file_path = os.path.join(system32_path, '1.cmd')
os.remove(file_path)

def modify_registry():
    key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
    value_name = "Shell"
    new_value_data = "explorer.exe"
    
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)

        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_value_data)

        winreg.CloseKey(key)
        os.system('shutdown -r -t 10')
        input("Ready! Your computer will restart after 10 seconds to apply the changes...")
    except Exception as e:
        print(f"Error: {e}")

async def async_sleep(seconds):
    await asyncio.sleep(seconds)

modify_registry()