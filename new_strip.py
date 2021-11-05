import os, shutil
import json
import socket
import uuid

FOLDER_PATH = "C:\\Users\\bruno.messias\\OneDrive - Strattner\\Documentos\\GitHub\\SConnect\\backup"
SCRIPT_PATH = (
    "C:\\Users\\bruno.messias\\OneDrive - Strattner\\Documentos\\GitHub\\SConnect"
)
VNC_PATH = "C:\\Program Files\\uvnc bvba\\UltraVNC"
BACKUP_CONF_PATH = (
    "C:\\Users\\Hospital\\Desktop\\Backup_v1.6.6\\Backup_v1.6.6\\Backup_v1.6.6\\dist"
)

# ------------- Não Atualizar ----------------------------------
OUTPUT_PATH = f"{SCRIPT_PATH}\\output.txt"
SORTED_PATH = f"{SCRIPT_PATH}\\sorted.txt"
REMOVE_PATH = f"{SCRIPT_PATH}\\remove.txt"
JSON_PATH = f"{SCRIPT_PATH}\\data.json"

def remove_last_part(file_path, output_path):

    f = open(output_path, "w")

    with open(file_path, "r") as data:
        lines = data.readlines()
 
        for line in lines:
            variables = line.strip("\n").split(" ")
            line = (variables[0] + " " + variables[1] + "\n")
            f.write(line)

    f.close()

remove_last_part(SORTED_PATH, REMOVE_PATH)