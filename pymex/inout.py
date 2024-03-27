import os
import yaml

def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print(f"{dir} created successfully.")
    else:
        print(f"{dir} already exists.")


def readInput(path):
    with open(path,'r') as f: 
        data = yaml.safe_load(f)
    return data


class W90inputfile(object):
    def __init__(self, **args):
        pass
       

# data = readInput('my_input.txt')
# for key in data['w90']:
#     print(key, '\t\t', data['w90'][key])

# print(type(data['system']['positions']))
# #print(type(data['system']['positions'][1]))