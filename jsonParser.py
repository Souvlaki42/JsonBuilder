import json

def readDataFromJsonFile(filename, indents = 4, sortKeys = False):
	with open(filename) as file:
		return json.load(file, indent = indents, sort_keys = sortKeys)

def writeDataToJsonFile(filename, data, indents = 4, sortKeys = False):
	with open(filename, "w") as file:
		return json.dump(data, file, indent = indents, sort_keys = sortKeys)

def readKeyFromJsonFile(filename, keypath, seperator = "/"):
	keys = keypath.split(seperator)
	with open(filename) as file:
		data = json.load(file)
		for key in keys:
			data = data[key]
		return data

def writeKeyToJsonFile(filename, keypath, value, seperator = "/", indents = 4, sortKeys = False, createMissing = True):
	keys = keypath.split(seperator)
	with open(filename) as file:
		data = json.load(file)
		d = data
		for key in keys[:-1]:
			if key in d:
				d = d[key]
			elif createMissing:
				d = d.setdefault(key, {})
			else:
				return data
		if keys[-1] in d or createMissing:
			d[keys[-1]] = value
		writeDataToJsonFile(filename, data, indents, sortKeys)
		return data