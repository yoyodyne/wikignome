#!/usr/bin/env python

import wikipedia as wiki

grammar_mistake = "on accident"

def search_wiki(phrase):
	return wiki.search(phrase, results=1)

if __name__ == "__main__":
	print wiki.page("New York")
	#print search_wiki(grammar_mistake)
