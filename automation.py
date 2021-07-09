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
#TODO Adicionar a rotina de exportar dados através da ultravnc

def open_matachana_tool():
    pyautogui.press("winleft")
    pyautogui.write("backup_")
    pyautogui.write("conf")
    pyautogui.press("enter")
    pyautogui.click(4219, 768) #TODO Atualizar posição
