from jsonParser import JsonParser

if __name__ == "__main__":
	jsonParser = JsonParser("test.json")
	test_data = {
    "name": "George MacNight",
    "age": 24,
    "rich": True,
    "job": "Masterchef",
    "family": {
        "mother": "Joanna Nimbers",
        "father": "Cooper MacNight",
        "brother": "Nick MacNight",
        "sister": "Layla MacNight",
        "wife": "Kate Gateberg",
        "son": "John MacNight",
        "daughter": "Candy MacNight",
        "pet": "Max"
    }
}
	jsonParser.write_file(test_data, 4)