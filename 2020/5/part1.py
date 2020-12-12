import math

def getRow(s):
	s = s[0:7]
	#size = 128
	min = 1
	max = 128

	for letter in s:
		# its not half of max, but the avg
		half = math.floor((max+min)/2)
		#print('Currently min is',min,'and max is',max,'and the letter is',letter)
		#print('Also half is',half)
		if(letter == 'F'):
			# lower half
			max = half
			#print('I set max to',max)
		else:
			# upper half
			min = half
			#print('I set min to',min)

	#print('Final values', min, max)
	return min

def getCol(s):
	s = s[7:10]

	min = 1
	max = 8

	for letter in s:
		# its not half of max, but the avg
		half = math.floor((max+min)/2)
		#print('Currently min is',min,'and max is',max,'and the letter is',letter)
		#print('Also half is',half)
		if(letter == 'L'):
			# lower half
			max = half
			#print('I set max to',max)
		else:
			# upper half
			min = half
			#print('I set min to',min)

	#print('Final values', min, max)
	return min

def seatId(bpass):
	row = getRow(bpass)
	col = getCol(bpass)
	return (row*8)+col

# 357
input = 'FBFBBFFRLR'
# 567
input = 'BFFFBBFRRR'
# 119
input = 'FFFBBBFRRR'
# 820
input = 'BBFFBBFRLL'

file = open(r"input.txt","r")

input = []
for line in file:
	input.append(line.rstrip())

file.close()

highestId = 0
for boardingPass in input:
	#print(boardingPass)
	thisSeatId = seatId(boardingPass)
	if(thisSeatId > highestId):
		highestId = thisSeatId

print(highestId)

#row = getRow(input)
#print(row)
#col = getCol(input)
#print(col)
#print('Seat ID', seatId(row,col))
