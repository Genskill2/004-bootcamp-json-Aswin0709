# Add the functions in this file
import json

def load_journal():
	ret=[]
	f = open('journal.json',)
	data = json.load(f)
	for i in data:
		ret.append(i)
	f.close()
	print (ret) 
