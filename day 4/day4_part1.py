#open input file
file=open("input_day4.txt", "r")

#declare variables
passports = {}
passportNum = 0
lines = []
validCount = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


#get input
for a in file:
    lines.append(a)
    line = a.split()
    
    for b in line:
        b = b.split(':')
        field = b[0]
        data = b[1]
        passports[passportNum,field] = data

    #figure out end/start of a new passport
    if not line:
        passportNum += 1

#validate passport information
for c in range(passportNum+1):
    valid = 1
    for d in fields:
        #check for all required values - if field is missing, set valid to 0
        #Note: cid can be ignored
        if not passports.get((c,d)):
            valid = 0
    validCount += valid
    

#return valid passports
print(validCount)
