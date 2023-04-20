#open input file
file=open("input_day4.txt", "r")

#declare variables
passports = {}
passportNum = 0
lines = []
validCount = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validEye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


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

loop = 0
#validate passport information
for c in range(passportNum+1):
    valid = 1
    loop += 1
    for d in fields:
        #check for all required values - if field is missing, set valid to 0
        #Note: cid can be ignored
        if not passports.get((c,d)):
            valid = 0
    for d in fields:
        if valid == 1:
            if d == 'byr':
                #(Birth Year) - four digits; at least 1920 and at most 2002.
                if int(passports.get((c,d))) < 1920 or int(passports.get((c,d))) > 2002:
                    valid = 0
            if d == 'iyr':
                #(Issue Year) - four digits; at least 2010 and at most 2020.
                if len(passports.get((c,d))) != 4 or int(passports.get((c,d))) < 2010 or int(passports.get((c,d))) > 2020:
                    valid = 0
            if d == 'eyr':
                #(Expiration Year) - four digits; at least 2020 and at most 2030.
                if len(passports.get((c,d))) != 4 or int(passports.get((c,d))) < 2020 or int(passports.get((c,d))) > 2030:
                    valid = 0
            if d == 'hgt':
                #(Height) - a number followed by either cm or in:
                    #If cm, the number must be at least 150 and at most 193.
                    #If in, the number must be at least 59 and at most 76.
                try:
                    #verify if value is a number
                    int(passports.get((c,d))[:-2])
                except ValueError:
                    #error if not a number, makes passport invalid
                    valid = 0
                except TypeError:
                    valid = 0
                try:
                    passports.get((c,d))[-2:]
                except TypeError:
                    valid = 0
                if passports.get((c,d))[-2:] == 'cm':

                    #If cm, the number must be at least 150 and at most 193.
                    if int(passports.get((c,d))[:-2]) < 150 or int(passports.get((c,d))[:-2]) > 193:
                        valid = 0
                if passports.get((c,d))[-2:] == 'in':
                    #If in, the number must be at least 59 and at most 76.
                    if int(passports.get((c,d))[:-2]) < 59 or int(passports.get((c,d))[:-2]) > 76:
                        valid = 0
            if d == 'hcl':
                #(Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                for e in passports.get((c,d))[1:]:
                    if e.isnumeric() == False:
                        if e.isalpha() == False:
                            valid = 0
                
                if passports.get((c,d))[0:1] != '#' or len(passports.get((c,d))[1:]) != 6:
                    valid = 0
                                                           
            if d == 'ecl':
                #(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                valid = 0
                for e in validEye:
                    if passports.get((c,d)) == e:
                        valid = 1
            if d == 'pid':
                #(Passport ID) - a nine-digit number, including leading zeroes.
                if len(passports.get((c,d))) != 9 or passports.get((c,d)).isnumeric() == False:
                    valid = 0
    validCount += valid

#return valid passports
print(validCount)
