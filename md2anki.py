#! Python3
# 这是主文件，在这里运行。
import genanki
import definitions
import md2mathjax
import md2cloze
import md2html
import apply_headings
import stripList
import codeToHtml
# 打开文件
unconvertedFile = open("unconverted.md")
lines = unconvertedFile.readlines()

lines = stripList.strip(lines)


        
for index in range(0, len(lines)):
    lines[index] = md2mathjax.mathjax2Anki(lines[index])
    
lines = codeToHtml.codeToHtml(lines)
    
for index in range(0, len(lines)):
    lines[index] = md2html.md2html(lines[index])
    lines[index] = md2cloze.md2cloze(lines[index], True)

for index in range(0, len(lines)):
    lines[index] = lines[index] + "\n"
    
print(lines)

convertedFile = open("converted.txt", "w")
for line in lines:
    convertedFile.write(line)
    
convertedFile.close()

