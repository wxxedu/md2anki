#!/usr/bin/env python3
import definitions

def md2html(line):
	line = quote2html(line)
	line = inlineCode2html(line)
	return line

def quote2html(line):
	if line[0] == ">":
		line = line.lstrip("> ")
		line = line.rstrip("\n")
		line = "<div style = \"border-left: 3px solid black; margin: 10px; padding: 10px; font-style: italic;\">" + line + "</div>"
	return line

def inlineCode2html(line):
	isOpen = True
	for index in range(0, len(line)):
		if line[index] == "`":
			if isOpen:
				line = definitions.subString(line, index, "¡") 
				# 用¡是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = False
			else:
				line = definitions.subString(line, index, "™")
				# 用™是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = True
	line = line.replace("¡", "<label style = \"border: 2px solid gray; margin: 5px; padding: 5px; border-radius: 5px; text-color: #DDDDDD;\">")
	line = line.replace("™", "</label>")
	
	return line