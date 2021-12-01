
#input = [199, 200, 208,210,200,207,240,269,260,263]
file = open(r"input.txt","r")

input = []
for line in file:
	input.append(int(line))

file.close()

last = input[0]
numTimesDecreased = 0

# New logic is to get 2 3-reading windows. So if we loop, we can wait until iteration 4
# and then get 1+2+3 and 2+3+4

for index,x in enumerate(input):
	if index >= 3:
		# get first range
		firstRange = input[index-3] + input[index-2] + input[index-1]
		secondRange = input[index-2] + input[index-1] + input[index]
		print("Index:",index)
		print("firstRange total", firstRange)
		print("secondRange total", secondRange)
		print("")
		if secondRange > firstRange:
			numTimesDecreased += 1
	
print("Number of times decreased", numTimesDecreased)
