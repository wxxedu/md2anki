#!/usr/bin/env python3
import gen_obsidian_url

inlinecode_to_cloze = True
ztk_to_cloze = False


# the main function that contains the sequence that needs to be runned for every line.

def slmd2html(line):
	line = quote2html(line)
	line = inlineCode2html(line)
	line = mdmathjax2ankimathjax(line)
	line = image_to_html(line)
	line = headings_to_html(line)
	line = bold2cloze(line)
	line = highlight2cloze(line)
	line = ztklink2cloze(line)
	line = line.replace("¶", "")
	return line

# for the subsititution of strings at a position. 

def subString(string,position,changeTo):
	new = []
	for s in string:
		new.append(s)
	new[position] = changeTo
	return "".join(new)

# for capitalizing all the characters in a string (currently not used)

def capitalize(string):
	new = []
	for s in string:
		new.append(s.capitalize())
	return "".join(new)



# this swaps the ">" and change it into html format of quotations



def quote2html(line):
	if line[0] == ">":
		line = line.lstrip("> ")
		line = "<div style = \"border-left: 3px solid black; margin: 10px; padding: 10px; font-style: italic;\">" + line + "</div>"
	return line

# this changes the inline "`code`" code to html

def inlineCode2html(line):
	isOpen = True
	for index in range(0, len(line)):
		if line[index] == "`":
			if isOpen:
				line = subString(line, index, "¡") 
				# 用¡是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = False
			else:
				line = subString(line, index, "™")
				# 用™是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = True
	if inlinecode_to_cloze:
		line = line.replace("¡", "<code style = \"border: 2px solid gray; margin: 2px; padding: 2px; border-radius: 5px;\">{{c*::")
		line = line.replace("™", "}}</code>")
	else:
		line = line.replace("¡", "<code style = \"border: 2px solid gray; margin: 2px; padding: 2px; border-radius: 5px;\">")
		line = line.replace("™", "</code>")
	return line

# this changes the dollar signs into mathjax. 

def mdmathjax2ankimathjax(line):
	
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
				line = subString(line, index, "¡") 
				# 用¡是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = False
			else:
				line = subString(line, index, "™")
				# 用™是因为，如果直接替换为“\(”，for循环中的index的数值就会有问题，因为lineString变长了，但是for循环中的len(lineString)不会变大，导致最后一个符号如果是美元符号没有办法被判断出来。
				isOpen = True
	line = line.replace("¡", "\(")
	line = line.replace("™", "\)")
	
	return line



## turns bold into cloze, while adding the formating bold

def bold2cloze(line):
	# 判断bold是前面还是后面
	isOpen = True
	
	# 把加粗中的**替换成统一的cloze
	for index in range(0, len(line) - 1):
		if line[index] + line[index+1] == "**":
			if isOpen:
				line = subString(line, index + 1, "¡") 
				line = subString(line, index, "¶")
				isOpen = False
			else:
				line = subString(line, index, "™")
				line = subString(line, index + 1, "¶")
				isOpen = True
	line = line.replace("¡", "<label style = \"font-style: bold;\">{{c*::")
	line = line.replace("™", "}}</label>")
	return line

# turns the highlight syntax: "==highlight==" into cloze, while adding highlight to the code

def highlight2cloze(line):
	# 判断bold是前面还是后面
	isOpen = True
	
	# 把加粗中的**替换成统一的cloze
	for index in range(0, len(line) - 1):
		if line[index] + line[index+1] == "==":
			if isOpen:
				line = subString(line, index + 1, "¡") 
				line = subString(line, index, "¶")
				isOpen = False
			else:
				line = subString(line, index, "™")
				line = subString(line, index + 1, "¶")
				isOpen = True
	line = line.replace("¡", "<label style = \"background-color: yellow;\">{{c*::")
	line = line.replace("™", "}}</label>")
	return line

# turns the wiki-link syntax: "[[wikilink|name]]" into cloze, while adding the link back to the original Obsidian file

def ztklink2cloze(line):
	line = line.replace("[[", "ª¡")
	line = line.replace("]]", "¶ª")
	segments = line.split("ª")
	for index in range(0, len(segments)):
		if segments[index].find("¡") != -1:
			segments[index] = process_ztk_line(segments[index])
	return "".join(segments)

	
def process_ztk_line(line):
	line = line.replace("¡", "")
	segments = line.split("|")
	url = gen_obsidian_url.generate(segments[0])
	content = segments[0]
	if len(segments) == 1:
		if ztk_to_cloze:
			content = "{{c*::" + segments[0] + "}}"
		completeURL = "<a href = \"" + url + "\">" + content + "</a>"
	elif len(segments) == 2:
		if ztk_to_cloze:
			content = "{{c*::" + segments[1] + "}}"
		completeURL = "<a href = \"" + url + "\">" + content + "</a>"
	return completeURL

# changes the images from markdown format into anki HTML format

def image_to_html(line):
	if line[0] == "!" and line[1] == "[":
		position = -1
		premise = False
		for index in range(0, len(line) - 1):
			if line[index] == "]" and line[index + 1] == "(":
				position = index
				premise = True
		if premise and position > 0:
			name_string = ""
			url_string = ""
			for index in range(2, position):
				name_string = name_string + line[index]
			for index in range(position + 2, len(line) -1):
				url_string = url_string + line[index]
			return_string = "<image src = \"" + url_string + "\">" + name_string + "</image>"
			return return_string
		else:
			return line
	else:
		return line
	
# convert headings from markdown format to anki HTML format

def headings_to_html(line):
	if line[0] == "#":
		count = 0
		premise = True
		while premise:
			if line[count + 1] == "#":
				count = count + 1
			else:
				premise = False
		if line[count + 1] == " ":
			line = line.lstrip("#")
			line = line.lstrip(" ")
			line = "<h%d>"%(count + 1) + line + "</h%d>"%(count + 1)
			return line
		else:
			return line
	else:
		return line