import os, shutil
import json
import socket

def unify_txt(files, OUTPUT_PATH):
    f = open(OUTPUT_PATH, 'w')   

    for file in files:  
        lines = open(file,"r").readlines()

        for line in lines:
            if line.find("##") != -1:
                pass
            elif line.find("Confirm as Staff") != -1:
                pass
            elif line == '\n':
                pass
            else:
                f.write(line)      
    f.close()


def separate_variables(file_path):
    ID_MACHINE = socket.gethostname()

    with open(file_path, 'r') as data:
        lines = data.readlines()
        list_var = []

        for line in lines:
            variables = line.strip('\n').split(';')
            variables[3] = variables[3][0:3].strip(' ')
            var = {"id_machine":ID_MACHINE, "date":variables[0], "error":variables[3]}
            list_var.append(var)
    return list_var


def create_json(variables, JSON_PATH):
    with open(JSON_PATH, 'w') as f:
        json.dump(variables, f, indent=3)


def remove_folder(FOLDER_PATH):
    for filename in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))