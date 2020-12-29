#!/usr/bin/env python3

def strip(lines):
	lines = removeEmptyLines(lines)
	lines = removeRight(lines)
	return lines


def removeEmptyLines(lines):
	index = 0
	while index < len(lines):
		if lines[index] == "\n":
			lines.remove(lines[index])
			index = index - 1
		index = index + 1
	return lines


def removeRight(lines):
	index = 0
	for index in range(0, len(lines)):
		lines[index] = lines[index].rstrip("\n")
	print(lines)
	return lines
		