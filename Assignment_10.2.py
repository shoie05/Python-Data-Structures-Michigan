fname = raw_input("Enter file name: ")
if len(name) < 1 : name = "C:\Programming_for_Everybody-PythonProg\mbox-short.txt"

fhandle = open(fname)

hourDict = dict()
lst = list()

for line in fhandle:
	if line.startswith("From "):
		time = line.split()[-2]
		hour = str(time.split(":")[0])
		hourDict[hour] = hourDict.get(hour, 0) + 1
		
for hour, count in hourDict.items():
	lst.append((hour, count))
	
lst.sort()

for hour, count in lst:
	print hour, count