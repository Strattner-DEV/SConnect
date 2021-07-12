import os
import config

from os import listdir
from os.path import isfile, join
from automation import open_vnc_viewer, open_matachana_tool
from read_file import unify_txt, separate_variables, create_json, remove_folder
from post_request import search_data, send_data

IP_MACHINE = config.IP_MACHINE

FOLDER_PATH = config.FOLDER_PATH
OUTPUT_PATH = config.OUTPUT_PATH
JSON_PATH = config.JSON_PATH
API_URL = config.API_URL

# open_vnc_viewer(IP_MACHINE)
# open_matachana_tool()

dir = os.listdir(FOLDER_PATH)
FOLDER = dir[0]
ALARM_PATH = f'{FOLDER_PATH}\\{FOLDER}\\DATA\\ALARM'

# get the full names of all the txt files in your folder 
FILES = [join(ALARM_PATH, f) for f in listdir(ALARM_PATH) if isfile(join(ALARM_PATH, f)) and f.endswith(".txt")]

unify_txt(FILES, OUTPUT_PATH)
variables = separate_variables(OUTPUT_PATH)
create_json(variables, JSON_PATH)

# remove_folder(FOLDER_PATH)

send_data(API_URL, JSON_PATH)
search_data(API_URL)