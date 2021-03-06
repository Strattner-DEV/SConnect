"""main.py
    Author: Bruno Cayres Messias <bruno.messias@strattner.com.br>
    Date: 07/13/2021
Description:
First script to get information from tool Backup_Configuration
"""
import os
import config
import time
import pyautogui

from os import listdir
from os.path import isfile, join
from automation import open_vnc_viewer, open_matachana_tool
from new_strip import REMOVE_PATH
from read_file import (
    get_firmware,
    unify_txt,
    separate_variables,
    create_json,
    remove_folder,
    sort_files,
    remove_last_part,
)
from post_request import send_data

# * Defining Constants
IP_MACHINE = config.IP_MACHINE
FOLDER_PATH = config.FOLDER_PATH
OUTPUT_PATH = config.OUTPUT_PATH
REMOVED_PATH = config.REMOVED_PATH
SORTED_PATH = config.SORTED_PATH
JSON_PATH = config.JSON_PATH
API_URL = config.API_URL
VNC_PATH = config.VNC_PATH
BACKUP_CONF_PATH = config.BACKUP_CONF_PATH
PASSWORD = config.PASSWORD

pyautogui.click(1019, 746)
time.sleep(3)

while True:

    pyautogui.alert(
        "Automation will Begin, please CLOSE ALL vnc windows, and do not use the computer in the next 30 mins",
        "Automation SmartConnect",
        timeout=10000,
    )

    # * Automation Part
    open_vnc_viewer(IP_MACHINE, VNC_PATH, PASSWORD)
    open_matachana_tool(IP_MACHINE, BACKUP_CONF_PATH)

    # * Read Files and managed folder part
    dir = os.listdir(FOLDER_PATH)
    FOLDER = dir[0]
    ALARM_PATH = f"{FOLDER_PATH}\\{FOLDER}\\DATA\\ALARM"
    CONFIG_PATH = f"{FOLDER_PATH}\\{FOLDER}\\CONFIG\\Import.txt"

    exists = os.path.exists(ALARM_PATH)

    if exists:
        # Get the full names of all the txt files in your folder
        FILES = [
            join(ALARM_PATH, f)
            for f in listdir(ALARM_PATH)
            if isfile(join(ALARM_PATH, f)) and f.endswith(".txt")
        ]

        # * Unify all files
        unify_txt(FILES, OUTPUT_PATH)

        # # Removed not sended data
        remove_last_part(OUTPUT_PATH, REMOVE_PATH)

        # * Filter the variables
        sort_files(SORTED_PATH, REMOVE_PATH)

        # * Read the file and separate variables
        version = get_firmware(CONFIG_PATH)
        variables = separate_variables(version, SORTED_PATH)
        create_json(variables, JSON_PATH)

        remove_folder(FOLDER_PATH)

        # * Send data part
        print("Sending Data...")
        result = send_data(API_URL, JSON_PATH)
        print(result)

        if isinstance(result, str):
            print(result)
        else:
            if result.ok:
                print("Successful Request!")
                result.close()
            else:
                print("Bad Request!")
                result.close()
    else:
        remove_folder(FOLDER_PATH)
        print("Nothing to send")

    time.sleep(14400)
