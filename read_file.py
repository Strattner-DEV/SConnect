"""read_file.py

    Author: Bruno Cayres Messias <bruno.messias@strattner.com.br>
    Date: 07/13/2021

Description:
Library contains all the functions to read and manage the files
"""

import os, shutil
import json
import socket
import uuid


def unify_txt(files, OUTPUT_PATH):
    """unify_txt Unify every txt file into one txt file

    :param files: List of files that are txt
    :type files: List
    :param OUTPUT_PATH: The output path where the unify is gonna be saved
    :type OUTPUT_PATH: String
    """
    f = open(OUTPUT_PATH, "w")

    for file in files:
        lines = open(file, "r").readlines()

        for line in lines:
            if line.find("##") != -1:
                pass
            elif line.find("Confirm as Staff") != -1:
                pass
            elif line == "\n":
                pass
            else:
                f.write(line)
    f.close()


def separate_variables(version, file_path):
    """separate_variables: Separate only the necessary information

    :param file_path: File path where the logs txt is saved
    :type file_path: String
    :return: List of the necessary parameters in dict format
    :rtype: List
    """
    ID_MACHINE = socket.gethostname()

    with open(file_path, "r") as data:
        lines = data.readlines()
        list_var = []

        hash_id = uuid.uuid4().hex

        for line in lines:
            variables = line.strip("\n").split(";")

            try:
                variables[3] = variables[3][0:3].strip(" ")

                var = {
                    "id_machine": ID_MACHINE,
                    "firmware": version,
                    "date": variables[0],
                    "error": variables[3],
                    "id": hash_id,
                }

                list_var.append(var)
            except:
                pass

    return list_var


def create_json(variables, JSON_PATH):
    """create_json: Crete an Json file from an list

    :param variables: List of variables in dict format
    :type variables: List
    :param JSON_PATH: Path where the Jason is gonna be saved
    :type JSON_PATH: String
    """
    with open(JSON_PATH, "w") as f:
        json.dump(variables, f, indent=3)


def remove_folder(FOLDER_PATH):
    """remove_folder: Remove all the files in the folder path

    :param FOLDER_PATH: Path to the folder that's gonna be removed
    :type FOLDER_PATH: String
    """
    for filename in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))


def get_firmware(CONFIG_PATH):
    """get_firmware Get the value of specific firmware version

    :param CONFIG_PATH: Path to the config txt file
    :type CONFIG_PATH: String
    :return: Value of firmware version
    :rtype: String
    """
    lines = open(CONFIG_PATH, "r").readlines()

    for line in lines:
        if line.find("Project number:") != -1:
            var = line.strip("\n").split(" ")
        else:
            pass

    return var[2]


def sort_files(sorted_path, file_path):
    """sort_files: Sort the files in the sorted_path

    :param sorted_path: Path where the sorted files are gonna be saved
    :type sorted_path: String
    :param file_path: Path where the files are gonna be sorted
    :type file_path: String
    """
    lines_seen = set()  # holds lines already seen
    outfile = open(sorted_path, "w")
    for line in open(file_path, "r"):
        if line not in lines_seen:  # not a duplicate
            lines_seen.add(line)

    outfile.writelines(sorted(lines_seen))
    outfile.close()
