import pprint

pp = pprint.PrettyPrinter(indent=4)

testNumbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
numbers = [1,76,38,96,62,41,27,33,4,2,94,15,89,25,66,14,30,0,71,21,48,44,87,73,60,50,77,45,29,18,5,99,65,16,93,95,37,3,52,32,46,80,98,63,92,24,35,55,12,81,51,17,70,78,61,91,54,8,72,40,74,68,75,67,39,64,10,53,9,31,6,7,47,42,90,20,19,36,22,43,58,28,79,86,57,49,83,84,97,11,85,26,69,23,59,82,88,34,56,13]

testBoardStr = """
22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

file = open(r"input.txt","r")
boardStr = file.read()
file.close()

#boardStr = testBoardStr
#numbers = testNumbers

# Given a string input of N boards of rows and cols, I create an array of board objects, 
# where each board has a rows and cols prop. These are both arrays of objects that look like:
# { num: X, picked: false } So we can track when a number is picked. 
def getBoards(str):
	#first, split by newline
	boards  = str.split("\n\n")
	result = []
	for board in boards:
		newBoard = {
			"rows":[], "cols":[]
		}

		#do rows
		rows = board.split("\n")
		for x,row in enumerate(rows):
			row = row.split()
			rows[x] = row
			objectRow = []
			for cell in row:
				objectRow.append({"num": int(cell), "picked": False})
			newBoard["rows"].append(objectRow)
		#print(rows)

		#do cols
		# safe to assume 5 x 5 here, reuse rows to make cols
		for x in range(0,5):
			objectCol = []
			for y in range(0,5):
				cell = rows[y][x]
				#print("col test", y, x, cell)
				objectCol.append({"num":int(cell), "picked":False})
			newBoard["cols"].append(objectCol)

		result.append(newBoard)

	return result

def updateBoards(boards, num):
	for board in boards:
		# loop through rows
		for row in board["rows"]:
			for cell in row:
				if cell["num"] == num:
					cell["picked"] = True
		for col in board["cols"]:
			for cell in col:
				if cell["num"] == num:
					cell["picked"] = True

	return boards

def isWinner(board):
	
	for row in board["rows"]:
		allGood = True
		for cell in row:
			if cell["picked"] == False:
				allGood = False
		if allGood:
			return True

	for col in board["cols"]:
		allGood = True
		for cell in col:
			if cell["picked"] == False:
				allGood = False
		if allGood:
			return True

	return False

def getScore(board,num):
	print("get score for num",num)
	sum = 0
	for row in board["rows"]:
		for cell in row:
			if cell["picked"] == False:
				sum += cell["num"]
	return sum * num

boards = getBoards(boardStr.strip())

winningBoards = []

for number in numbers:
	print("Picked ",number)

	# i believe that since im working with complex obs
	# im passing by ref so the return isn't really necessary, but...
	boards = updateBoards(boards, number)
	
	for (b,board) in enumerate(boards):
		if isWinner(board):
			winningBoards.append({"board":boards.pop(b), "number":number})
			print("Added a winner...")
			#score = getScore(board, number)
			#pp.pprint(board["rows"])
			#print("Final Score", score)
			#winner = board
			#winningScore = score

winner = winningBoards.pop(-1)
print(getScore(winner["board"], winner["number"]))


