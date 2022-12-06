sampleInput = [
	["2-4","6-8"],
	["2-3","4-5"],
	["5-7","7-9"],
	["2-8","3-7"],
	["6-6","4-6"],
	["2-6","4-8"]
]

input = [line.rstrip() for line in open('input.txt','r')]

def fullyContains(a,b):
	minA,maxA = a.split('-')
	minB,maxB = b.split('-')
	
	minA = int(minA)
	minB = int(minB)
	maxA = int(maxA)
	maxB = int(maxB)

	# check if B is inside A first
	if(minB >= minA and maxB <= maxA):
		return True

	# now check if A in B
	if(minA >= minB and maxA <= maxB):
		return True

	return False

totalContained = 0

for pair in input:
	pairA,pairB = pair.split(',')
	
	if(fullyContains(pairA, pairB)):
		totalContained = totalContained + 1

print("Total Contained", totalContained)