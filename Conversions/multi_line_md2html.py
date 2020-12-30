#!/usr/bin/env python3

def codeToHtml(lines):
	positions = []
	for index in range(0, len(lines)):
		if lines[index].find("```",0,3) != -1:
			positions.append(index)
			
	for index in range(0, len(positions)):
		decimal = (index / 2) - (index // 2)
		if decimal == 0:
			language = lines[positions[index]].lstrip("```")
			prefix = "<pre><code class=\""+ language.rstrip("<br>") + "\">"
			suffix = "</code></pre>"
			sourcelines = ""
			for indice in range(positions[index] + 1, positions[index + 1]):
				sourcelines = sourcelines + prefix + lines[indice].rstrip("<br>") + suffix
				lines[indice] = "¡"
			sourcelines = "<div style = \"border: 2px solid black; margin: 10px; padding: 0px 20px 0px 20px\">" + sourcelines + "</div>"
			lines[positions[index]] = sourcelines
			lines[positions[index + 1]] = "¡"
	count = 0
	for line in lines:
		if line == "¡":
			count = count + 1
			
	for i in range(0, count):
		lines.remove("¡")
		
	return lines