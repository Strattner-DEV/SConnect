"""test.py

    Author: Bruno Cayres Messias <bruno.messias@strattner.com.br>
    Date: 07/13/2021

Description:
First script to get information from tool Backup_Configuration
"""
import os
import config

from os import listdir
from os.path import isfile, join
from read_file import (
    get_firmware,
    unify_txt,
    separate_variables,
    create_json,
)

# * Defining Constants
IP_MACHINE = config.IP_MACHINE
FOLDER_PATH = config.FOLDER_PATH
OUTPUT_PATH = config.OUTPUT_PATH
JSON_PATH = config.JSON_PATH
API_URL = config.API_URL

# * Read Files and managed folder part
dir = os.listdir(FOLDER_PATH)
FOLDER = dir[0]
ALARM_PATH = f"{FOLDER_PATH}\\{FOLDER}\\DATA\\ALARM"
CONFIG_PATH = f"{FOLDER_PATH}\\{FOLDER}\\CONFIG\\Import.txt"

# Get the full names of all the txt files in your folder

exists = os.path.exists(ALARM_PATH)

if exists:

    FILES = [
        join(ALARM_PATH, f)
        for f in listdir(ALARM_PATH)
        if isfile(join(ALARM_PATH, f)) and f.endswith(".txt")
    ]

    unify_txt(FILES, OUTPUT_PATH)
    version = get_firmware(CONFIG_PATH)
    variables = separate_variables(version, OUTPUT_PATH)
    create_json(variables, JSON_PATH)
else:
    print("Nothing to send")
