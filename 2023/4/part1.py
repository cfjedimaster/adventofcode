import re 

input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

#lines = input.strip().split('\n')
lines = [line.rstrip() for line in open('input.txt','r')]

totalPoints = 0

for line in lines:
	# first, we dont care about card #
	(card, nums) = line.split(': ')
	(winningStr, myStr) = nums.split(' | ')
	#print('-'+winningStr+'-')
	#print('-'+myStr+'-')
	winningNumbers = re.findall(r'\d+', winningStr)
	# in theory i should convert to numbers, but we only care about matching
	#print(winningNumbers)
	myNumbers = re.findall(r'\d+', myStr)

	thisCard = 0
	for num in myNumbers:
		if num in winningNumbers:
			if thisCard == 0:
				thisCard = 1
			else:
				thisCard = thisCard * 2

	totalPoints += thisCard

print("Total", totalPoints)