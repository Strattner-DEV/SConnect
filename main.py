"""main.py

    Author: Bruno Cayres Messias <bruno.messias@strattner.com.br>
    Date: 07/13/2021

Description:
First script to get information from tool Backup_Configuration
"""
import os
import config

from os import listdir
from os.path import isfile, join
from automation import open_vnc_viewer, open_matachana_tool
from read_file import (
    get_firmware,
    unify_txt,
    separate_variables,
    create_json,
    remove_folder,
)
from post_request import search_data, send_data

# * Defining Constants
IP_MACHINE = config.IP_MACHINE
FOLDER_PATH = config.FOLDER_PATH
OUTPUT_PATH = config.OUTPUT_PATH
JSON_PATH = config.JSON_PATH
API_URL = config.API_URL

# * Automation Part
open_vnc_viewer(IP_MACHINE)
# open_matachana_tool()

# * Read Files and managed folder part
dir = os.listdir(FOLDER_PATH)
FOLDER = dir[0]
ALARM_PATH = f"{FOLDER_PATH}\\{FOLDER}\\DATA\\ALARM"
CONFIG_PATH = f"{FOLDER_PATH}\\{FOLDER}\\CONFIG\\Import.txt"

# Get the full names of all the txt files in your folder
FILES = [
    join(ALARM_PATH, f)
    for f in listdir(ALARM_PATH)
    if isfile(join(ALARM_PATH, f)) and f.endswith(".txt")
]

unify_txt(FILES, OUTPUT_PATH)
version = get_firmware(CONFIG_PATH)
variables = separate_variables(version, OUTPUT_PATH)
create_json(variables, JSON_PATH)

# remove_folder(FOLDER_PATH)

# * Send data part
# result = send_data(API_URL, JSON_PATH)

# if isinstance(result, str):
#     print(result)
# else:
#     # print(result.status_code)
#     if result.ok:
#         print("Successful Request!")
#         result.close()
#     else:
#         print("Bad Request!")
#         result.close()
