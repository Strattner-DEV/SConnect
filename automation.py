import pyautogui  #TODO pip install pyautogui
import time

pyautogui.PAUSE = 1

def open_vnc_viewer(IP_MACHINE):
    pyautogui.press("winleft")
    pyautogui.write("ultravnc ")
    pyautogui.write("viewer")
    pyautogui.press("enter")
    pyautogui.write(IP_MACHINE)
    pyautogui.press("enter")
    # (Resolução 1024x768)
    pyautogui.click(572,385)
    pyautogui.write("93486")
    pyautogui.press("enter")
    pyautogui.click(499,423)
    pyautogui.write("bce4255e9100c612")
    pyautogui.press("enter")
    pyautogui.click(507,476)
    pyautogui.click(853,680)
    pyautogui.click(853,680)
    pyautogui.click(686,571)
    pyautogui.click(895,680)
    pyautogui.click(503,175)
    pyautogui.click(691,487)
    pyautogui.click(853,680)
    pyautogui.click(499,507)
    pyautogui.click(884,66)

def open_matachana_tool():
    pyautogui.press("winleft")
    pyautogui.write("backup_")
    pyautogui.write("conf")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(600) # Delay de 10 Minutos
    pyautogui.press("esc")
