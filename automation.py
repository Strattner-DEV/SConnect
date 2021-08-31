"""automation.py
    Author: Bruno Cayres Messias <bruno.messias@strattner.com.br>
    Date: 07/13/2021
Description:
Prototype of an automation script to make the routine of get the data from machine
"""
import pyautogui
import time

pyautogui.PAUSE = 1


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
        f"vncviewer.exe -connect {IP_MACHINE} -password 93486 -scale 250/100"
    )
    pyautogui.press("enter")
    # (Resolution 1024x768)
    pyautogui.click(499, 423)
    pyautogui.write(PASSWORD)
    pyautogui.press("enter")
    pyautogui.click(507, 476)
    pyautogui.click(853, 680)
    pyautogui.click(853, 680)
    pyautogui.click(686, 571)
    pyautogui.click(895, 680)
    pyautogui.click(503, 175)
    pyautogui.click(691, 487)
    pyautogui.click(853, 680)
    pyautogui.click(499, 507)
    pyautogui.click(888, 46)
    pyautogui.click(574, 262)
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
    pyautogui.click(536, 257)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(IP_MACHINE)
    pyautogui.press("enter")
    time.sleep(600)  # Delay of 10 min
    pyautogui.press("esc")
    pyautogui.click(574, 262)
    pyautogui.write("exit")
    pyautogui.press("enter")
