sampleInput = [
	["2-4","6-8"],
	["2-3","4-5"],
	["5-7","7-9"],
	["2-8","3-7"],
	["6-6","4-6"],
	["2-6","4-8"]
]

input = [line.rstrip() for line in open('input.txt','r')]

def overlap(a,b):
	minA,maxA = a.split('-')
	minB,maxB = b.split('-')
	
	minA = int(minA)
	minB = int(minB)
	maxA = int(maxA)
	maxB = int(maxB)

	if(minB >= minA and minB <= maxA):
		return True

	if(maxB >= minA and maxB <= maxA):
		return True

	if(minA >= minB and minA <= maxB):
		return True

	if(maxA >= minB and maxA <= maxB):
		return True

	return False

totalOverlap = 0

for pair in input:
	pairA,pairB = pair.split(',')
	
	if(overlap(pairA, pairB)):
		totalOverlap = totalOverlap + 1

print("Total Overlap", totalOverlap)