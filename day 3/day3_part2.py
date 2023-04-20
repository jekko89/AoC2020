#get input map
file = open("input_day3.txt", "r")
lines = []
forest = {}
collisions = []

for a in file:
    lines.append(a)
posX = 0
posY = 0

for y in lines:
    #extend input map in x axis up to 3000
    while(posX < 3000):
        for x in y:
            if(x != "\n"):
                forest[posX,posY] = x
                posX += 1
    posX = 0
    posY += 1

#set vector 1
posX = 0
posY = 0
vectorX = 1
vectorY = 1

#calculate collisions
collision = 0
while(posY < 323):
    if(forest[posX,posY] == '#'):
        collision += 1
    posX += vectorX
    posY += vectorY
collisions.append(collision)


#set vector 2
posX = 0
posY = 0
vectorX = 3
vectorY = 1

#calculate collisions
collision = 0
while(posY < 323):
    if(forest[posX,posY] == '#'):
        collision += 1
    posX += vectorX
    posY += vectorY
collisions.append(collision)

#set vector 3
posX = 0
posY = 0
vectorX = 5
vectorY = 1

#calculate collisions
collision = 0
while(posY < 323):
    if(forest[posX,posY] == '#'):
        collision += 1
    posX += vectorX
    posY += vectorY
collisions.append(collision)

#set vector 4
posX = 0
posY = 0
vectorX = 7
vectorY = 1

#calculate collisions
collision = 0
while(posY < 323):
    if(forest[posX,posY] == '#'):
        collision += 1
    posX += vectorX
    posY += vectorY
collisions.append(collision)

#set vector 5
posX = 0
posY = 0
vectorX = 1
vectorY = 2

#calculate collisions
collision = 0
while(posY < 323):
    if(forest[posX,posY] == '#'):
        collision += 1
    posX += vectorX
    posY += vectorY
collisions.append(collision)

print(collisions)
print(collisions[0] * collisions[1] * collisions[2] * collisions[3] * collisions[4])
