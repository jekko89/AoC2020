#get input
file=open("input_day2.txt", "r")
passwords = []
valid = 0
for a in file:
    passwords.append(a)

#parse through input
for a in passwords:
    #parse first 4 characters for rules
    line = a.split()
    low_high = line[0].split('-')
    low = int(low_high[0])
    high = int(low_high[1])
    letter = line[1][0]
    
    #validate password
    letter_count = 0
    for b in line[2]:
        if(letter == b):
            letter_count += 1
    if(letter_count >= low and letter_count <= high):
        valid += 1

#output number of valid passwords
print(valid)
