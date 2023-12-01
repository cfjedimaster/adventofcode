import re


def getCalibrationValue(s):
	matches = re.findall(r'\d', s)
	if(len(matches) >= 2):
		return int(matches[0] + matches[len(matches)-1])
	else:
		return int(matches[0] + matches[0])

#input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
input = [line.rstrip() for line in open('input.txt','r')]

total = 0
for i in input:
	calibration = getCalibrationValue(i)
	#print("calibration", calibration)
	total += calibration

print("Total", total)
