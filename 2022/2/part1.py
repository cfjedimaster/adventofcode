input = [line.rstrip() for line in open('input.txt','r')]

#input = ["A Y","B X","C Z"]

totalScore = 0

def checkGame(other, myself):
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

for i in input:
	plays = i.split(' ')
	opp = plays[0]
	me = plays[1]
	didWin = checkGame(opp, me)

	#now do score
	if didWin == 'W':
		totalScore = totalScore + 6
	if didWin == 'D':
		totalScore = totalScore + 3
		
	totalScore = totalScore + playScore(me)

print("Final Score", totalScore)