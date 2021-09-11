import json

def load_json():
	with open(r"complete_list.json", "r") as read_file:
		data = json.load(read_file)
	return data