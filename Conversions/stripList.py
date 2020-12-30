#!/usr/bin/env python3

def strip(lines):
	for index in range(1, len(lines)):
		lines[index] = largeBracketsSpacer(lines[index])
		lines[index] = greaterOrLessThanExchanger(lines[index])
	lines = removeEmptyLines(lines)
	lines = removeRight(lines)
	lines = removeMetadata(lines)
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
		lines[index] = lines[index] + "<br>"
	return lines

def removeMetadata(lines):
	del lines[0:4]
	return lines

# for the subsititution of strings at a position. 

def subString(string,position,changeTo):
	new = []
	for s in string:
		new.append(s)
	new[position] = changeTo
	return "".join(new)

# this changes out the ">" and the "<" so that no conflicts with the html code will happen. 
# 替换掉文本中的大于号、小于号，因为这个会和Anki中的HTML代码的开始和结尾有冲突。

def greaterOrLessThanExchanger(line):
	for index in range (1, len(line)): # 这边修改成1，这样Markdown的引用可以被正常渲染。
		if line[index] == ">":
			line = subString(line, index, "¡")
		if line[index] == "<":
			line = subString(line, index, "™")
	line = line.replace("¡", "&gt;")
	line = line.replace("™", "&lt;")
	return line

# this changes the connecting brackets so that no conflicts would occur
# MathJax中如果出现两个连续“{”或者两个连续的“}”，会和Anki的Cloze卡片发生冲突，所以需要替换掉。

def largeBracketsSpacer(line):
	for index in range (1, len(line) - 1):
		if line[index] + line[index + 1] == "{{":
			line = subString(line, index, "¡")
		if line[index] + line[index + 1] == "}}":
			line = subString(line, index, "™")
	line = line.replace("¡", "{ ")
	line = line.replace("™", "} ")
	return line