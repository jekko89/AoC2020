i=open("advent_day1_input.txt", "r")
nums = []
for x in i:
    nums.append(int(x))
for y in nums:
    for z in nums:
        for a in nums:
            if(y+z+a==2020):
                print("Y is " + str(y))
                print("Z is " + str(z))
                print("A is " + str(a))
                print("Answer is " + str((y*z*a)))

