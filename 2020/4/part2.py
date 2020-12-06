import re

sampleInput = """
ecl:gry pid:860033327 eyr:2020 hcl:#ffffff
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


file = open(r"input.txt","r")
input = file.read()
file.close()

# Given a string like sample above, split by one line, then part into 
# objects of key value pairs, return a list
def parseToPassport(s):
	passportStrings = s.strip().split('\n\n')
	passports = []

	for p in passportStrings:
		passport = {}
		p = p.replace('\n',' ')
		parts = p.split(' ')
		for part in parts:
			halves = part.split(':')
			passport[halves[0]] = halves[1]
		passports.append(passport)
	return passports

def validHeight(s):
	#must be Xcm or Xin
	#print('validHeight input', s)
	parts = re.split('([0-9]+)(in|cm)',s)
	# we had empty items at the beginning and end, tip: https://stackoverflow.com/a/30933281/52160
	parts = list(filter(None, parts))
	if(len(parts) != 2):
		return False
	parts[0] = int(parts[0])
	# first, unit must be cm or in
	if(parts[1] != 'cm') and (parts[1] != 'in'):
		return False
	if(parts[1] == 'cm') and ((parts[0] < 150) or (parts[0] > 193)):
		return False
	if(parts[1] == 'in') and ((parts[0] < 59) or (parts[0] > 76)):
		return False

	return True

def validHair(c):
	if(len(c)) != 7:
		return False
	if(c[0] != '#'):
		return False
	c = c[1:7]
	# I had a lot of trouble with the regex, kinda gave up
#	print(c)
	result = re.match('[a-f0-9]+', c, re.IGNORECASE)
#	print(result.start(), result.end())
#	print('result', c[result.start():result.end()])
	if(c[result.start():result.end()] != c):
		return False
	return True

# amb blu brn gry grn hzl oth
def validEye(c):
	if(c == 'amb') or (c == 'blu') or(c == 'brn') or (c == 'gry') or (c == 'grn') or (c == 'hzl') or (c == 'oth'):
		return True
	return False

def validPid(p):
	if(len(p) != 9):
		return False

	result = re.match('[a-z]',p, re.IGNORECASE)
	if(result):
		return False
	return True

#you must have every required field but cid
def validPassort(p):
	requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
	for req in requiredFields:
		#print(req,req in p)
		if (req in p) is False:
			print('missing field', req)
			return False

	# new rules
	year = int(p['byr'])
	if(year < 1920) or (year > 2002):
		print('byr invalid', year)
		return False

	year = int(p['iyr'])
	if(year < 2010) or (year > 2020):
		print('iyr invalid', year)
		return False

	year = int(p['eyr'])
	if(year < 2020) or (year > 2030):
		print('eyr invalid', year)
		return False

	if validHeight(p['hgt']) is False:
		print('hgt invalid', p['hgt'])
		return False

	if validHair(p['hcl']) is False:
		print('hcl invalid', p['hcl'])
		return False

	if validEye(p['ecl']) is False:
		print('ecl invalid', p['ecl'])
		return False

	if validPid(p['pid']) is False:
		print('pid invalid', p['pid'])
		return False

	return True

passports = parseToPassport(input)
#print(result)
print('total passports',len(passports))

validPassports = 0
for passport in passports:
	#print('checking',passport)
	if(validPassort(passport)):
		validPassports = validPassports + 1

print('valid passport',validPassports)
