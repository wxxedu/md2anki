#!/usr/bin/env python3
import sys
sys.path.append("./Conversions/")
import os
import gen_obsidian_url
import multi_line_md2html
import single_line_md2html
import stripList
import gen_cloze

# add your path to your obsidian knowledge base here, as it will help you locate the folder of the files that you want to locate

path = "/Users/xiuxuan/Library/Mobile Documents/iCloud~org~zrey~metion/Documents/Knowledge Base/52 - Memory Base"
file_names = os.listdir(path)

# if you want to generate multiple clozes in a single card, leave this option open

whetherDifferent = True

# if in obsidian you use ztk time stamps, put the number of digits that you want to remove here. 

ztk_digit = 15

lines = {}

for file_name in file_names:
	full_path = path + "/" + file_name
	file = open(full_path)
	lines[file_name] = file.readlines()
	lines[file_name] = stripList.strip(lines[file_name])
	lines[file_name] = multi_line_md2html.codeToHtml(lines[file_name])
	for index in range(0, len(lines[file_name])):
		lines[file_name][index] = single_line_md2html.slmd2html(lines[file_name][index])
	note_content = "".join(lines[file_name])
	note_content = gen_cloze.generate(note_content, True)
	
	obsidian_url = gen_obsidian_url.generate(file_name)
	obsidian_url = obsidian_url.rstrip(".md")
	
	note_title = ""

	for index in range(ztk_digit, len(file_name)):
		note_title = note_title + file_name[index]
		
	note_title_with_link = "\nSource: <a href = \"" + obsidian_url + "\">" + note_title.rstrip(".md") + "</a><br>"
	lines[file_name] = note_title_with_link + note_content
	

export = open("./Files/converted.txt", "w")
for file_name in file_names:
	export.write(lines[file_name])
export.close()		