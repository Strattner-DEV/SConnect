import os
import config
import time
import pyautogui
import socket

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
from post_request import send_data

# * Defining Constants
FOLDER_PATH = config.FOLDER_PATH
OUTPUT_PATH = config.OUTPUT_PATH
JSON_PATH = config.JSON_PATH
API_URL = config.API_URL
VNC_PATH = config.VNC_PATH
BACKUP_CONF_PATH = config.BACKUP_CONF_PATH
PASSWORD = config.PASSWORD
TRY = config.TRY
IP_MACHINE_0 = "192.168.3.182"
IP_MACHINE_1 = "192.168.3.185"

ip_list =[]

for i in range(TRY):
    ip = locals()["IP_MACHINE_"+str(i)]
    ip_list.append(ip)

def do_something(IP):
    print(IP)

for i in ip_list:
    print(ip_list)
    do_something(i)

index = 0

ID_MACHINE = socket.gethostname() + "_" +str(index)
print(ID_MACHINE)
