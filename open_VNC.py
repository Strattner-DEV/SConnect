import pyautogui
import config

pyautogui.PAUSE = 1

IP_MACHINE = config.IP_MACHINE
VNC_PATH = config.VNC_PATH
PASSWORD = config.PASSWORD

def open_vnc(IP_MACHINE, VNC_PATH, PASSWORD):
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

open_vnc(IP_MACHINE, VNC_PATH, PASSWORD)