text = "X-DSPAM-Confidence:    0.8475"

startPos = text.find(":")
strNum = text[startPos+1:]
num = float(strNum)
print num