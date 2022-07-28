from distutils.log import error
from genericpath import exists
import json, sys

class JsonBuilder():
    def __init__(self, file):
        if not exists(file):
            sys.exit("This file doesn't exist yet!")
        self.file = file

    def read_file(self):
        with open(self.file, "r") as file:
            return json.load(file)

    def write_file(self, data):
        with open(self.file, "w") as file:
            return json.dump(data, file)

    def read_key(self, keypath, seperator="/"):
        keys = keypath.split(seperator)
        with open(self.file, "r") as file:
            key0 = keys[0]
            data = json.load(file)[key0]
            del keys[0]
            for key in keys:
                data = data[key]
            return data

    def write_key(self, key, value):
        with open(self.file, "r+") as file:
            data = json.load(file)
            data[key] = value
            file.seek(0)
            json.dump(data, file, indent = 4)