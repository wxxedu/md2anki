#!/usr/bin/env python3

def generate(line, whetherDifferent):
	
	# 将cloze的序号替换，如果whetherDifferent为True，那么就需要替换成不同的cloze，反之则不用。
	if whetherDifferent:
		count = 0
		for index in range(0, len(line) - 6):
			idString = line[index] + line[index + 1] + line[index + 2]+line[index + 3] + line[index + 4] + line[index + 5]
			if idString == "{{c*::":
				count = count + 1
				line = line.replace("{{c*::", "{{c%d::"%(count), 1)
	else:
		line = line.replace("{{c*::", "{{c1::")
		
	return line
