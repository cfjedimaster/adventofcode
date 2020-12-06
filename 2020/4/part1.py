sampleInput = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
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

#you must have every required field but cid
def validPassort(p):
	requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
	for req in requiredFields:
		#print(req,req in p)
		if (req in p) is False:
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
