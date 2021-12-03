#input = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

file = open(r"input.txt","r")

input = []
for line in file:
	input.append(line.strip())

file.close()

# we can assume every item has the same length, so figure out the column length first
colLen = len(input[0])

gamma = ""
epsilon = ""

# loop over columns

for col in range(0, colLen):
	#print("\nColumn", col+1)
	mcb_1 = 0
	mcb_0 = 0
	for i in range(0,len(input)):
		#print("Array item", i)
		thisInput = input[i][col]
		if thisInput == "1":
			mcb_1 += 1
		else:
			mcb_0 += 1
	
	if mcb_1 > mcb_0:
		gamma += "1"
		epsilon += "0"
	else:
		gamma += "0"
		epsilon += "1"


print("BINARY GAMMA: ", gamma)
print("BINARY EPSILON: ", epsilon)

intGamma = int(gamma, 2)
intEpsilon = int(epsilon, 2)

print("INT GAMMA: ", intGamma)
print("INT EPSILON: ", intEpsilon)

consumption = intGamma * intEpsilon
print("POWER CONSUMPTION: ", consumption)

	