#!/usr/bin/env python3

# Warings: used this BEFORE using bold2cloze.

import definitions


# 依次调用这个部分的其他三个函数
def mathjax2Anki(line):
	line = dollarSignChanger(line)
	line = largeBracketsSpacer(line)
	line = greaterOrLessThanExchanger(line)
	return line


# 这个部分的功能在于把Markdown文件中的美元符号转换Anki MathJax中相对应的\(\)和\[\]
# 具体来说：把行内公式$\dfrac{1}{2}$改成\(\dfrac{1}{2}\)，把display style的行间公式$$\dfrac{1}{2}$$改成\[\dfrac{1}{2}\]
def dollarSignChanger(line):
	
	# 判断是否是行间公式。行间公式最开始的时候必然是在这一行开头的两个美元符号，结尾也必然是这一行结尾的两个美元符号
	if line.count("$", 0, 2) == 2 and line.count("$", len(line) -2, len(line)):
		line = line.lstrip("$")
		line = line.rstrip("$")
		line = "\[" + line + "\]"
		
	# 判断美元符号在公式的前面还是在后面。目前问题：不支持有真正美元符号作为美元符号的Markdown
	isOpen = True
	for index in range(0, len(line)):
		if line[index] == "$":
			if isOpen:
				line = definitions.subString(line, index, "¡") 
				# 用¡是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = False
			else:
				line = definitions.subString(line, index, "™")
				# 用™是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = True
	line = line.replace("¡", "\(")
	line = line.replace("™", "\)")
	
	return line

# MathJax中如果出现两个连续“{”或者两个连续的“}”，会和Anki的Cloze卡片发生冲突，所以需要替换掉。

def largeBracketsSpacer(line):
	for index in range (0, len(line) - 1):
		if line[index] + line[index + 1] == "{{":
			line = definitions.subString(line, index, "¡")
		if line[index] + line[index + 1] == "}}":
			line =definitions.subString(line, index, "™")
	line = line.replace("¡", "{ ")
	line = line.replace("™", "} ")
	return line

# 替换掉文本中的大于号、小于号，因为这个会和Anki中的HTML代码的开始和结尾有冲突。

def greaterOrLessThanExchanger(line):
	for index in range (0, len(line)):
		if line[index] == ">":
			line = definitions.subString(line, index, "¡")
		if line[index] == "<":
			line = definitions.subString(line, index, "™")
	line = line.replace("¡", "&gt;")
	line = line.replace("™", "&lt;")
	return line