"""Reusable utilities across the project"""
import os
import json


def clear_screen() -> None:
	"""Clears the console"""
	# for windows
	if os.name == 'nt':
		os.system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		os.system('clear')


def strike_through(text: str) -> str:
	"""Returns a strike-through version of the input text"""
	result = ''
	for c in text:
		result = result + c + '\u0336'
	return result


def save_json(data, filename: str) -> None:
	"""Saves the input dict to a file"""
	with open(filename, 'w') as file:
		json.dump(data, file)


def load_json(filename: str):
	"""Loads and returns the json data from a file as json. If the file is missing, returns None"""
	try:
		with open(filename) as file:
			return json.load(file)
	except FileNotFoundError:
		return None
