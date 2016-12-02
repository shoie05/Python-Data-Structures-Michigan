fname = raw_input("Enter File name: ")
if len(fname) < 1 : name = "mbox-short.txt"
fhandle = open(fname)

d = dict()
max = 0

for line in fhandle:
	line = line.rstrip()
	words = line.split()
	if not line.startswith("From "): continue
	d[words[1]] = d.get(words[1], 0) + 1		#returns 0 if words[1] is not in dictionary
												#else increments the value corresponding to that key by 1
		
for key in d:		#loops through keys of d
	if d[key] > max:
		max = d[key]
		reqdKey = key

print reqdKey, max