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
from read_file import (
    get_firmware,
    unify_txt,
    separate_variables,
    create_json,
    remove_folder,
    sort_files,
)
from post_request import send_data

# * Defining Constants
FOLDER_PATH = config.FOLDER_PATH
OUTPUT_PATH = config.OUTPUT_PATH
SORTED_PATH = config.SORTED_PATH
JSON_PATH = config.JSON_PATH
API_URL = config.API_URL
VNC_PATH = config.VNC_PATH
BACKUP_CONF_PATH = config.BACKUP_CONF_PATH
PASSWORD = config.PASSWORD
TRY = config.TRY

# -------------Put here all the IPs ----------------
IP_MACHINE_0 = "192.168.3.182"
IP_MACHINE_1 = "192.168.3.182"
# --------------------------------------------------

ip_list = []

for i in range(TRY):
    ip = locals()["IP_MACHINE_" + str(i)]
    ip_list.append(ip)

print(ip_list)

pyautogui.click(1019, 746)
time.sleep(3)

while True:
    index = 0
    for i in ip_list:

        pyautogui.alert(
            "Automation will Begin, please CLOSE ALL vnc windows, and do not use the computer in the next 30 mins",
            "Automation SmartConnect",
            timeout=10000,
        )

        # print(PASSWORD)

        # * Automation Part
        open_vnc_viewer(i, VNC_PATH, PASSWORD)
        open_matachana_tool(i, BACKUP_CONF_PATH)

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

            unify_txt(FILES, OUTPUT_PATH)

            # * Filter the variables
            sort_files(SORTED_PATH, OUTPUT_PATH)

            # * Read the file and separate variables
            version = get_firmware(CONFIG_PATH)
            variables = separate_variables(version, SORTED_PATH, index)

            create_json(variables, JSON_PATH)

            remove_folder(FOLDER_PATH)

            # * Send data part
            result = send_data(API_URL, JSON_PATH)

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
            print("Nothing to send")

        index = index + 1

    time.sleep(14400)
