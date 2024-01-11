# import turtle as trtl

# tr = trtl.Turtle()


# def straight(pointer):
#     pointer.forward(50)

# straight(tr)



# wn = trtl.Screen()
# wn.mainloop() # This keeps the screen on



# def team(name, tank, attack, defence):
#     print(f'team name: {name}\n{tank} is my tank.\n{attack} is my attack.\n{defence} is my defensive player')

# team("firebluds","Bigboy","Fast","protective")
# team("water","massive","quick","overarching")


class champion():
    def __init__(self):
        self.name = ''
        self.strength = 0
        self.agility = 0
        self.magic = 0
        self.accuracy = 0
        self.hp = 100
    
    def stats (self):
        print (f' {self.name} \n agility lvl is {self.agility} \n has a stregth lvl of {self.strength} \n has a magic lvl of {self.magic}')

def fight(champ1,champ2):
    selection = input('Type 1 to use fist and type 2 to use magic')

    match selection:
        case '1':
            use_fist(champ1,champ2)
        case '2':
            use_magic(champ1,champ2)

def use_fist(champ1,champ2):
    if champ1.strength > champ2.strength:
        print (f' {champ1.name} hits {champ2.name}')
    else:
        print (f' {champ2.name} hits {champ1.name}')

def use_magic(champ1, champ2):
    if champ1.magic > champ2.magic:
        print (f' {champ1.name} uses fireball')
        if champ2.agility > champ1.agility:
            print (f'{champ2.name} uses dodge')
        else:
            print (" fireball is effective...")
    else:
        print (f' {champ2.name} uses fireball  ')
        if (champ1.agility > champ2.agility) :
            print (f'{champ1.name} uses dodge')
        else:
            print (" fireball is effective...")




manuel = champion()
manuel.name = "manuel"
manuel.agility = 14
manuel.strength = 8
manuel.magic = 6


myles = champion()
myles.name = "myles"
myles.agility = 12
myles.strength = 10
myles.magic = 7

while True:
    fight(manuel,myles)





