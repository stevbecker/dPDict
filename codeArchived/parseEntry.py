from bs4 import BeautifulSoup
import json

with open('declare.axb8472', 'r') as entry:
  hw_doc = entry.read()
#fentry = open('declare.axb8472', 'r')
#hw_doc = fentry.read()

#print hw_doc

fj = open('declare.axb8472.json1', 'w')
#print fj

#soup = BeautifulSoup("declare.axb8472")
soup = BeautifulSoup(hw_doc)

"""
for span in soup.find_all('span'):
  #fj.write(str(span))
  json.dump(str(span), fj)
  print span
"""

jsonBody = {}

#get headword
jsonBody['hw'] = soup.find('idx:orth')['value']

#get inflection
infl = {}
for it in soup.find_all('idx:iform'):
  infl[it['name'].replace('.', '')] = it['value']
  print infl
jsonBody['infl'] = infl

#get id
jsonBody['id'] = soup.find('a')['id']

#get part of speech
jsonBody['pos'] = soup.find('i').get_text()

sublist = []
i=0
examp = []
for it in soup.find_all('blockquote'):
  i += 1
  if(it.parent.name=='idx:entry' or it.parent.name=='div'):
    subentry = {}
    subentry['df'] = it.get_text()
    subentry['es'] = examp
    #print subentry
    sublist.append(subentry)
    print sublist
    examp = []
  if(it.parent.name=='blockquote'):
    examp.append(it.get_text())
	
jsonBody['sublist'] = sublist

json.dump(jsonBody, fj)
