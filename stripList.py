#!/usr/bin/env python3

def strip(lines):
	lines = removeEmptyLines(lines)
	lines = removeHeadings(lines)
	return lines


def removeEmptyLines(lines):
	index = 0
	while index < len(lines):
		if lines[index] == "\n":
			lines.remove(lines[index])
			index = index - 1
		index = index + 1
	return lines


def removeHeadings(lines):
	index = 0
	while index < len(lines):
		if lines[index][0] == "#":
			lines.remove(lines[index])
			index = index - 1
		index = index  + 1
	return lines
		