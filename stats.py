# stats

def get_book_text(path):
    text = None
    with open(path) as f:
        text = f.read()
    return(text)

# word counter
# accepts text 
# returns number of words formed by split()

def word_count(text):
	num_words = 0
	for i in text.split():
		num_words += 1
	return num_words

# char counter
# accepts text
# returns dictionary of characters : number of occurrences in text

def char_count(text):
	lowered = sorted(text.lower())
	chars = {}

	for i in lowered:
		if i not in chars:
			chars[i] = 1
		else:
			chars[i] += 1

	return(chars)

# char count list
# accepts dictionary of characters : number of occurrences in text

def lister(chars):
    dictlist = []
    for i in chars:
        if i.isalpha():
            chardict = {"letter": i, "num": chars[i]}
            dictlist.append(chardict)
        
    def sorter(dicts):
        return dicts["num"]
    
    dictlist.sort(reverse=True, key=sorter)
    
    return dictlist

def printer(printlist):
    for i in range(len(printlist)):
        print(f"{printlist[i]["letter"]}: {printlist[i]["num"]}")
