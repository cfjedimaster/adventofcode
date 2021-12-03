#baseInput = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
file = open(r"input.txt","r")

baseInput = []
for line in file:
	baseInput.append(line.strip())

file.close()


oxgenRating = 0
co2Rating = 0

colLen = len(baseInput[0])

input = baseInput.copy()
currentCol = 0
while oxgenRating == 0:

	#print("Working with col ", currentCol)	

	mcb_1 = 0
	mcb_0 = 0

	for i in range(0, len(input)):
		thisInput = input[i][currentCol]
		if thisInput == "1":
			mcb_1 += 1
		else: 
			mcb_0 += 1

	# at this point, we've counted the col
	if mcb_1 >= mcb_0:
		input = list(filter(lambda i: i[currentCol] == "1", input))
	else:
		input = list(filter(lambda i: i[currentCol] == "0", input))
	
	#are we done?
	if len(input) == 1:
		oxgenRating = input[0]
	else:
		currentCol += 1

intOxygenRating = int(oxgenRating, 2)
print("OXYGEN RATING BIN", oxgenRating)
print("OXYGEN RATING", intOxygenRating)

currentCol = 0
input = baseInput.copy()

while co2Rating == 0:

	#print("Working with col ", currentCol)	

	mcb_1 = 0
	mcb_0 = 0

	for i in range(0, len(input)):
		thisInput = input[i][currentCol]
		if thisInput == "1":
			mcb_1 += 1
		else: 
			mcb_0 += 1

	# at this point, we've counted the col
	if mcb_1 < mcb_0:
		input = list(filter(lambda i: i[currentCol] == "1", input))
	else:
		input = list(filter(lambda i: i[currentCol] == "0", input))
	
	#are we done?
	if len(input) == 1:
		co2Rating = input[0]
	else:
		currentCol += 1

intCO2Rating = int(co2Rating, 2)
print("CO2 RATING BIN", co2Rating)
print("CO2 RATING", intCO2Rating)

lsRating = intOxygenRating * intCO2Rating
print("LIFE SUPPORT RATING", lsRating)