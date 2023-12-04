
#input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green","Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue","Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

input = [line.rstrip() for line in open('input.txt','r')]

# Our requirement
minRed = 12
minGreen = 13
minBlue = 14

goodGames = 0

for gameStr in input:
	parts = gameStr.split(":")
	game = parts[0]
	#print("Game:",game)
	draws = parts[1].strip().split(";")
	# We loop over the draws, and if we see one that invalidates our min reqs, we flip this
	toAdd = True
	for draw in draws:
		colors = draw.split(',')
		for colorStr in colors:
			num,color = colorStr.strip().split(' ')
			num = int(num)
			if color == "red" and num > minRed:
				toAdd = False
			if color == "green" and num > minGreen:
				toAdd = False
			if color == "blue" and num > minBlue:
				toAdd = False

	if toAdd == True:
		id = game.split(' ')[1]
		goodGames += int(id)

print(goodGames)
