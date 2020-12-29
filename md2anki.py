#! Python3
# 这是主文件，在这里运行。
import genanki
import definitions
import md2mathjax
import md2cloze
import apply_headings
import stripList

# 打开文件
unconvertedFile = open("unconverted.md")
lines = unconvertedFile.readlines()

print (lines) # 打印文件用于检查

lines = stripList.strip(lines)

        
for index in range(0, len(lines)):
    lines[index] = md2mathjax.mathjax2Anki(lines[index])
    lines[index] = md2cloze.md2cloze(lines[index], True)

convertedFile = open("converted.txt", "w")
for line in lines:
    convertedFile.write(line)
    
convertedFile.close()

