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
	#print('col',s)

	columns = [0,1,2,3,4,5,6,7]

	for letter in s:
		if(letter == 'L'):
			columns = columns[0:int(len(columns)/2)]
		else:
			columns = columns[int(len(columns)/2):int(len(columns))]

	return columns[0]


def seatId(bpass):
	row = getRow(bpass)
	col = getCol(bpass)
	return (row*8)+col


file = open(r"input.txt","r")

input = []
for line in file:
	input.append(line.rstrip())

file.close()

# bug with dupes, test:
# BFBFFBBLLL
# BFBFFBBLLR
#print(seatId('BFBFFBBLLL'))
#print('------------------------')
#print(seatId('BFBFFBBLLR'))

# Record every pass so we can find the 'gap'
seats = []
for boardingPass in input:
	#print(boardingPass)
	thisSeatId = seatId(boardingPass)
	#thisRow = getRow(boardingPass)
	# dont bother saving row 1 or 128
	#if(thisRow != 1) and (thisRow != 128):
	#print('row',thisRow,'pass',boardingPass,'seatid',thisRow)
	if(thisSeatId in seats):
		print('wtf dupe of ',thisSeatId)	
	#if(thisSeatId == 665):
		#print('dupe test', boardingPass)
	seats.append(thisSeatId)

print('ok done getting seats, total is',len(seats))

seats = sorted(seats)
#print(seats)

# ok, so seats is sorted, if next index is NOT this+1, we found our missing seat
for x,val in enumerate(seats):
	#print(x,val)
	if((x < len(seats)-1) and val+1 != seats[x+1]):
		print('MISSING!', x, seats[x],seats[x+1])
	

# 576 is too low