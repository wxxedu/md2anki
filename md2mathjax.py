#!/usr/bin/env python3
# 这个部分的功能在于把Markdown文件中的美元符号转换Anki MathJax中相对应的\(\)和\[\]
# 具体来说：把行内公式$\dfrac{1}{2}$改成\(\dfrac{1}{2}\)，把display style的行间公式$$\dfrac{1}{2}$$改成\[\dfrac{1}{2}\]

import definitions

def mathjaxAnki(line):
	lineString = str(line)
	
	# 判断是否是行间公式。行间公式最开始的时候必然是在这一行开头的两个美元符号，结尾也必然是这一行结尾的两个美元符号
	if lineString.count("$", 0, 2) == 2 and lineString.count("$", len(lineString) -2, len(lineString)):
		lineString = lineString.lstrip("$")
		lineString = lineString.rstrip("$")
		lineString = "\[" + lineString + "\]"
		
	# 判断美元符号在公式的前面还是在后面。目前问题：不支持有真正美元符号作为美元符号的Markdown
	isOpen = True
	for index in range(0, len(lineString)):
		if lineString[index] == "$":
			if isOpen:
				lineString = definitions.subString(lineString, index, "¡") 
				# 用¡是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = False
			else:
				lineString = definitions.subString(lineString, index, "™")
				# 用™是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = True
	lineString = lineString.replace("¡", "\(")
	lineString = lineString.replace("™", "\)")
	
	return lineString