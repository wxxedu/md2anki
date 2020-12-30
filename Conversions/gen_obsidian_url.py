#!/usr/bin/env python3

# This file turns the file name that we read into obsidian URL by combining it with the url scheme provided by obsidian

vaultURL = "obsidian://open?vault=Knowledge%20Base&file=52%20-%20Memory%20Base%2F"

def generate(title):
	title = encode(title)
	title = vaultURL + title
	return title

def encode(string):
	string = str(string.encode("utf-8"))
	string = string.replace("\\x", "%")
	string = string.replace(" ", "%20")
	string = string.replace("/", "%2F")
	string = string.lstrip("\'b")
	string = string.rstrip("\'")
	string = capitalize_unicode(string)
	return string

def capitalize_unicode(string):
	new = []
	position = -5
	for index in range(0, len(string)):
		if string[index] == "%":
			position = index
			new.append(string[index])
		elif index == position + 1 or index == position + 2:
			new.append(string[index].capitalize())
		else:
			new.append(string[index])
	return "".join(new)