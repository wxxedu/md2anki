#!/usr/bin/env python3
import definitions

def mathjaxAnki(line):
	lineString = str(line)
	if lineString.count("$", 0, 2) == 2 and lineString.count("$", len(lineString) -2, len(lineString)):
		lineString = lineString.lstrip("$")
		lineString = lineString.rstrip("$")
		lineString = "\[" + lineString + "\]"
	isOpen = True
	for index in range(0, len(lineString)):
		if lineString[index] == "$":
			if isOpen:
				lineString = definitions.subString(lineString, index, "¡")
				isOpen = False
			else:
				lineString = definitions.subString(lineString, index, "™")
				isOpen = True
	lineString = lineString.replace("¡", "\(")
	lineString = lineString.replace("™", "\)")
	return lineString