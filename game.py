level = open('level.txt','r')
level_text = level.read()
lines = level_text.split('\n')
player = [0,0]
ogPlayer = [0,0]
walls = ['#']
levelLines = []
def getLevel():
    for line in lines:
        if(';' in line):
            this_line = 'useless'
        else:
            for i in walls:
                levelLines.append(line)
def isPlayer():
    update = 0
    for i in levelLines:
        if('@' in levelLines[update]):
            player[1] = update
        update+=1
def getPlayerPosition():
    pos = 0
    for i in list(levelLines[player[1]]):
        if('@' in list(levelLines[player[1]])):
            player[0] = pos-1
        pos += 1
def move():
    line2[ogPlayer[0]] = '-'
    line2[player[0]] = '@'
def newMove():
    move = input('./move>')
    if move == "w":
        ogPlayer[1] = player[1]
        player[1] -= 1 
    elif move == "pos":
        print(player)
    elif move == "s":
        ogPlayer[1] = player[1]
        player[1] += 1
    elif move == "a":
        ogPlayer[0] = player[0]
        player[0] -= 1
    elif move == "d":
        ogPlayer[0] = player[0]
        player[0] += 1
    lineParse()
    print(levelLines[0])
    print(levelLines[1])
    print(levelLines[2])
def setUp():
    getLevel()
    isPlayer()
    getPlayerPosition()  
setUp()
line1 = list(levelLines[0])
line2 = list(levelLines[1])
line3 = list(levelLines[2])
def lineParse():
    levelLines[0] = ""
    levelLines[1] = ""
    levelLines[2] = ""
    for i in line1:
        levelLines[0] += i
    for i in line2:
        levelLines[1] += i
    for i in line3:
        levelLines[2] += i
move()
while True:
    newMove()
    move()
