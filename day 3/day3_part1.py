#get input map
file = open("input_day3.txt", "r")
lines = []
forest = {}
for a in file:
    lines.append(a)
posX = 0
posY = 0

for y in lines:
    #extend input map in x axis up to 1000
    while(posX < 1000):
        for x in y:
            if(x != "\n"):
                forest[posX,posY] = x
                posX += 1
    posX = 0
    posY += 1

#set vector
posX = 0
posY = 0

vectorX = 3
vectorY = 1

collision = 0

#calculate collisions
while(posY < 323):
    if(forest[posX,posY] == '#'):
        collision += 1
    posX += vectorX
    posY += vectorY

print(collision)
