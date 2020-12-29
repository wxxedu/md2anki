#!/usr/bin/env python3

## 这个文件我想要用来处理Markdown中间的Headings，把它们转换成对应的卡片信息。但是这个好像不是特别好做。

headings = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}


# 初始化，找到文件中的标题，并根据标题类型将index分别放入对应的词典之中。
def initialize():
	for index in range(0, len(lines)):
		headingLevel = lines[index].count("#", 0, 6)
		if headingLevel != 0:
			headings[headingLevel].append(index)

# 给出一个指定的index，找出它上面的headings
def getTitles(position):
	lastTitleIndex = 0
	while titles[index] < position and index < len(titles):
		lastTitleIndex = titles[index]
		index = index + 1