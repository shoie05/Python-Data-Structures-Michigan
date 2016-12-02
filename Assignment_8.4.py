fname = raw_input("Enter file name: ")
fhandler = open(fname)

wordList = list()

for line in fhandler:
	line = line.rstrip()
	words = line.split()
	for word in words:
		if word not in wordList:
			wordList.append(word)
			
wordList.sort()
print wordList