# Use the file name mbox-short.txt as the file name
sum = 0.0
count = 0

fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	num = float(line[19:].strip())
	sum += num
	count += 1
			
print "Average spam confidence:", sum/count