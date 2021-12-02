
pos = 0
depth = 0

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
	if type == "down":
		depth += amount
	if type == "up":
		depth -= amount

	#print(type,amount)
	#print("Currently at pos",pos, "and depth", depth)

result = pos * depth
print("Final result", result)