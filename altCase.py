def casify(phrase):
	ul = []
	for c in range(len(phrase)):
		if c % 2:
			ul.append(phrase[c].upper())
		else:
			ul.append(phrase[c].lower())
	return ''.join(ul)
