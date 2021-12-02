
pos = 0
depth = 0
aim = 0

#input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

file = open(r"input.txt","r")

input = []
for line in file:
	input.append(line)

file.close()


for command in input:
	# split into type/amt
	type,amount = command.split(" ")
	amount = int(amount)

	if type == "forward":
		pos += amount
		depth += aim * amount
	if type == "down":
		aim += amount
	if type == "up":
		aim -= amount

	#print(type,amount)
	#print("Currently at pos",pos, "and depth", depth)

result = pos * depth
print("Final result", result)