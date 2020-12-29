#!/usr/bin/env python3

#changes bold to cloze. 

import definitions

def bold2Cloze(line, whetherDifferent):
	
	line = str(line)
		
	# 判断bold是前面还是后面
	isOpen = True
	
	# 替换成统一的cloze
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