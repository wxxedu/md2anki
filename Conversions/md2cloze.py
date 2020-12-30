#!/usr/bin/env python3

#changes bold to cloze. 

import definitions
import obsidianURLGenerator

def md2cloze(line, whetherDifferent):
	
	line = bold2cloze(line)
	
	line = ztklink2cloze(line)
	
	line = highlight2cloze(line)
	
	# 将cloze的序号替换，如果whetherDifferent为True，那么就需要替换成不同的cloze，反之则不用。
	if whetherDifferent:
		count = 0
		for index in range(0, len(line) - 6):
			idString = line[index] + line[index + 1] + line[index + 2]+line[index + 3] + line[index + 4] + line[index + 5]
			if idString == "{{c*::":
				count = count + 1
				print(count)
				line = line.replace("{{c*::", "{{c%d::"%(count), 1)
	else:
		line = line.replace("{{c*::", "{{c1::")
	
	return line

def bold2cloze(line):
	# 判断bold是前面还是后面
	isOpen = True
	
	# 把加粗中的**替换成统一的cloze
	for index in range(0, len(line) - 1):
		if line[index] + line[index+1] == "**":
			if isOpen:
				line = definitions.subString(line, index + 1, "¡") 
				line = definitions.subString(line, index, "¶")
				isOpen = False
			else:
				line = definitions.subString(line, index, "™")
				line = definitions.subString(line, index + 1, "¶")
				isOpen = True
	line = line.replace("¡", "{{c*::")
	line = line.replace("™", "}}")
	line = line.replace("¶", "")
	return line

def highlight2cloze(line):
	# 判断bold是前面还是后面
	isOpen = True
	
	# 把加粗中的**替换成统一的cloze
	for index in range(0, len(line) - 1):
		if line[index] + line[index+1] == "==":
			if isOpen:
				line = definitions.subString(line, index + 1, "¡") 
				line = definitions.subString(line, index, "¶")
				isOpen = False
			else:
				line = definitions.subString(line, index, "™")
				line = definitions.subString(line, index + 1, "¶")
				isOpen = True
	line = line.replace("¡", "{{c*::")
	line = line.replace("™", "}}")
	line = line.replace("¶", "")
	return line
	
def ztklink2cloze(line):
	line = line.replace("[[", "ª¡")
	line = line.replace("]]", "ª")
	segments = line.split("ª")
	for index in range(0, len(segments)):
		if segments[index].find("¡") != -1:
			print(index)
			segments[index] = processLine(segments[index])
	return "".join(segments)
	

def processLine(line):
	line = line.replace("¡", "")
	segments = line.split("|")
	url = obsidianURLGenerator.generate(segments[0])
	if len(segments) == 1:
		content = "{{c*::" + segments[0] + "}}"
		completeURL = "<a href = \"" + url + "\">" + content + "</a>"
	elif len(segments) == 2:
		content = "{{c*::" + segments[1] + "}}"
		completeURL = "<a href = \"" + url + "\">" + content + "</a>"
	return completeURL