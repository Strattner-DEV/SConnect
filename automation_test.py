import pyautogui
import time

pyautogui.PAUSE = 1

IP_MACHINE = "192.168.8.247"
PASSWORD = "d559044db3932bc4"

FOLDER_PATH = "C:\\Users\\STRATTNER\\Desktop\\BACKUP"
SCRIPT_PATH = "C:\\Users\\STRATTNER\\Desktop\\SCRIPTS"
VNC_PATH = "C:\\Program Files (x86)\\uvnc bvba\\UltraVNC"
BACKUP_CONF_PATH = "C:\\Users\\STRATTNER\\Desktop\\Backup_v1.6.6\\Backup_v1.6.6\\Backup_v1.6.6\\dist"


def open_vnc_viewer(IP_MACHINE, VNC_PATH, PASSWORD):
    """open_vnc_viewer Routine to open the UltraVNC and preparate to get the logs
    :param IP_MACHINE: IP of machine to connect
    :type IP_MACHINE: String
    """
    pyautogui.hotkey("winleft", "r")
    pyautogui.write("cmd")
    pyautogui.press("enter")
    pyautogui.write(f"cd {VNC_PATH}")
    pyautogui.press("enter")
    pyautogui.write(
        f"vncviewer.exe -connect {IP_MACHINE} -password 93486 -scale 150/100"
    )
    pyautogui.press("enter")
    pyautogui.click(297, 240) # Click on the password field
    pyautogui.write(PASSWORD)
    pyautogui.press("enter")

    pyautogui.click(325, 279) #Servide Data
    pyautogui.click(525, 405) # Pass
    pyautogui.click(525, 405) # Pass
    pyautogui.click(431, 337) # Machine Backup to CF
    pyautogui.click(547, 407) # X
    pyautogui.click(332, 99) # Configuration
    pyautogui.click(435, 288) # Alarm
    pyautogui.click(525, 405) # Pass
    time.sleep(3)
    pyautogui.click(312, 301) # Export history Alarms
    pyautogui.click(530, 18) # Exit
    pyautogui.click(571, 181) # Click on terminal
    pyautogui.write("exit")
    pyautogui.press("enter")


def open_matachana_tool(IP_MACHINE, BACKUP_CONF_PATH):
    """open_matachana_tool Automation of tool that create the folder with the logs from machine"""
    pyautogui.hotkey("winleft", "r")
    pyautogui.write("cmd")
    pyautogui.press("enter")
    pyautogui.write(f"cd {BACKUP_CONF_PATH}")
    pyautogui.press("enter")
    pyautogui.write("start Backup_Configuration.exe")
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.click(309, 142) # Click on IP field
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(IP_MACHINE)
    pyautogui.press("enter")
    time.sleep(2000)  # Delay of 30 min
    pyautogui.press("esc")
    pyautogui.click(556, 234) #CLick on terminal
    pyautogui.write("exit")
    pyautogui.press("enter")

pyautogui.click(636, 458)
time.sleep(3)

# open_vnc_viewer(IP_MACHINE, VNC_PATH, PASSWORD)
open_matachana_tool(IP_MACHINE, BACKUP_CONF_PATH)