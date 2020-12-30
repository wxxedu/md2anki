#!/usr/bin/env python3

# Put all your files into a single folder to make this URL work.

vaultURL = "obsidian://open?vault=Knowledge%20Base&file=2%20-%20ZTK%20Knowledge%20Base%2F"

def generate(title):
	title = title.replace(" ", "%20")
	title = vaultURL + title
	return title