import os
os.system('clear')
text = open('level.txt','r')
textRead = text.read()
lines = textRead.split('\n')
# Set up arrays
ll = []
player = []
toPrintArray = []
def level():
    # Pull letters from file
    commentAmount = 0
    for line in lines:
        if(';' in line):
            commentAmount += 1
        else:
            ll.append(list(line))
    # Get players line position
    update = 0
    for i in ll:
        if('@' in ll[update]):
            player.append(update)
        update += 1
    # Get players x position
    update = 0
    for i in ll[player[0]]:
        if((ll[player[0]])[update]== '@'):
            player.append(update)
        update += 1
    # Parse and print the final test
    update = 0
    toPrint = ''
    for i in ll:
        update2 = 0
        for i in ll[update]:
            toPrint += (ll[update])[update2]
            update2 += 1
        update += 1
        toPrintArray.append(toPrint)
        toPrint = ''
def draw():
    # Draws the canvas using the print array
    print(f'x:{player[0]} y:{player[1]}')
    update = 0
    for i in toPrintArray:
        print(toPrintArray[update])
        update += 1
level()
draw()