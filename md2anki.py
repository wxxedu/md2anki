#! Python3
import genanki
import definitions
import md2mathjax
import bold2cloze
unconvertedFile = open("unconverted.md")

lines = unconvertedFile.readlines()

print (lines) # 打印文件用于检查

# 删除文件中的空行，仅保留不空的部分
for line in lines:
    if line == "\n":
        lines.remove(line)

# 找到文件中的标题，并根据标题类型将index分别放入对应的词典之中。
headings = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

for index in range(0, len(lines)):
    headingLevel = lines[index].count("#", 0, 6)
    if headingLevel != 0:
        headings[headingLevel].append(index)

print(headings)
        
# 给出一个指定的index，找出它上面的headings
def getTitles(position):
    lastTitleIndex = 0
    while titles[index] < position and index < len(titles):
        lastTitleIndex = titles[index]
        index = index + 1
        
for index in range(0, len(lines)):
    print(index)
    lines[index] = md2mathjax.mathjax2Anki(lines[index])
    lines[index] = bold2cloze.bold2Cloze(lines[index], True)

print (lines)
