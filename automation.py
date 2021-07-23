"""automation.py

    Author: Bruno Cayres Messias <bruno.messias@strattner.com.br>
    Date: 07/13/2021

Description:
Prototype of an automation script to make the routine of get the data from machine
"""
import pyautogui
import time

pyautogui.PAUSE = 1


def open_vnc_viewer(IP_MACHINE):
    """open_vnc_viewer Routine to open the UltraVNC and preparate to get the logs

    :param IP_MACHINE: IP of machine to connect
    :type IP_MACHINE: String
    """
    pyautogui.press("winleft")
    pyautogui.write("cmd")
    pyautogui.press("enter")
    pyautogui.write("cd  C:\\Program Files (x86)\\uvnc bvba\\UltraVNC")
    pyautogui.press("enter")
    pyautogui.write("start vncviewer.exe")
    pyautogui.press("enter")
    pyautogui.write(IP_MACHINE)
    pyautogui.press("enter")
    # (Resolution 1024x768)
    pyautogui.click(572, 385)
    pyautogui.write("93486")
    pyautogui.press("enter")
    pyautogui.click(499, 423)
    pyautogui.write("bce4255e9100c612")
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
    pyautogui.click(884, 66)


def open_matachana_tool():
    """open_matachana_tool Automation of tool that create the folder with the logs from machine"""
    pyautogui.press("winleft")
    pyautogui.write("backup_")
    pyautogui.write("conf")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(600)  # Delay of 10 min
    pyautogui.press("esc")
