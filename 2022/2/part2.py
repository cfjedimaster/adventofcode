# A = rock, B = Paper, C = Scissors
# X = rock, Y = Paper, Z = Scissors
#

input = [line.rstrip() for line in open('input.txt','r')]

#input = ["A Y","B X","C Z"]

totalScore = 0

def checkGame(other, myself):
	#print('checkGame, opp is ', other, 'and I am ', myself)
	if other == 'A' and myself == 'Y':
		return 'W'
	if other == 'B' and myself == 'Z':
		return 'W'
	if other == 'C' and myself == 'X':
		return 'W'
	if (other == 'A' and myself == 'X') or (other == 'B' and myself == 'Y') or (other == 'C' and myself == 'Z'):
		return 'D'

	return 'L'

# I return score based on your play
def playScore(p):
	if p == 'X':
		return 1
	if p == 'Y':
		return 2
	if p == 'Z':
		return 3

def getDesiredOutcome(other, outcome):

	# I need to lose 
	if outcome == 'X':
		if other == 'A':
			return 'Z'
		if other == 'B':
			return 'X'
		if other == 'C':
			return 'Y'

	# I need to draw
	if outcome == 'Y':
		if other == 'A':
			return 'X'
		if other == 'B':
			return 'Y'
		if other == 'C':
			return 'Z'
	
	# I need to win
	if outcome == 'Z':
		if other == 'A':
			return 'Y'
		if other == 'B':
			return 'Z'
		if other == 'C':
			return 'X'

for i in input:
	plays = i.split(' ')
	opp = plays[0]
	outcome = plays[1]
	# x means lose, y means draw, z means win
	#print('opp played ',opp, ' outcome is ', outcome);
	# so now I can just set 'me' to the right value
	me = getDesiredOutcome(opp, outcome)
	#print('i play', me)
	didWin = checkGame(opp, me)
	#print('did i win?', didWin)

	#now do score
	if didWin == 'W':
		totalScore = totalScore + 6
	if didWin == 'D':
		totalScore = totalScore + 3
		
	totalScore = totalScore + playScore(me)

print("Final Score", totalScore)