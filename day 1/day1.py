i=open("advent_day1_input.txt", "r")
nums = []
for x in i:
    nums.append(int(x))
for y in nums:
    for z in nums:
        if(y+z==2020):
            print("Y is " + str(y))
            print("Z is " + str(z))
            print("Answer is " + str((y*z)))
