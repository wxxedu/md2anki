#!/usr/bin/env python3

# swap strings

def subString(string,position,changeTo):
	new = []
	for s in string:
		new.append(s)
	new[position] = changeTo
	return "".join(new)