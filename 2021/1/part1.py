
#input = [199, 200, 208,210,200,207,240,269,260,263]
file = open(r"input.txt","r")

input = []
for line in file:
	input.append(int(line))

file.close()

last = input[0]
numTimesDecreased = 0

for x in input:
	if x > last:
		numTimesDecreased += 1
	
	last = x

print("Number of times decreased", numTimesDecreased)
