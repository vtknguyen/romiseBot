import urllib2, json
import altCase #alternates case in strings

#Takes in a string(phrase) and a boolean(casify) 
def anagram(phrase,casify):

	phrase = phrase.split()
	newPhrase = ''
	for word in phrase:
		try:
    			urlHead = "http://www.anagramica.com/best/:"
    			apiRsp = urllib2.urlopen(urlHead+word)
    			data = json.loads(apiRsp.read().decode(apiRsp.info().getparam('charset') or 'utf-8'))
    			newPhrase += data['best'][0] + ' '
		except:
			newPhrase += word + ' '	
	#print (newPhrase)
	if casify:
		return altCase.casify(newPhrase)
	else:
		return newPhrase
