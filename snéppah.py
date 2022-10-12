import os,time,random
mobs = ['Bunses','Tahw','Pryn',]
# Name,Health
player = []
def clear():
    os.system('clear')
def player__init__():
    name = input('choose/name>')
    player.append(name)
    player.append(random.randrange(50,100))
clear()
print('Snéppah by, Easton')
player__init__()
def btMsg(name):
    msg = random.randrange(0,2)
    if msg == 0:
        return f'A wild {name} appeared'
    elif msg == 1:
        return f'You\'ve encountered a {name}'
def drawScreen():
    clear()
    print(f'{player[0]} HP:{player[1]}')
def isAttack():
    attackBack = random.randrange(0,2)
    if(attackBack == 0):
        player[1] -= random.randrange(0,15)
def isHeal():
    player[1] += random.randrange(5,20) 
def update():
    drawScreen()
    M = btMsg(mobs[random.randrange(0,3)])
    MHP = random.randrange(50,100)
    print(f'MHP:{MHP}')
    print(M)
    for x in range(0,player[1]):
        option = input('attack(a)/heal(h)>')
        if option == 'h':
            isHeal()
        if option == 'a':
            MHP -= random.randrange(5,20)
        if(MHP <= 0):
            M = btMsg(mobs[random.randrange(0,3)])
            MHP = random.randrange(50,100)
            clear()
            time.sleep(1)
        clear()
        print(f'{player[0]} HP:{player[1]}')
        print(f'MHP:{MHP}')
        print(M)
        isAttack()
update()


