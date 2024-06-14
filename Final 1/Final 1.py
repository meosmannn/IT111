import random

class Die:
    def __init__(self):
        self.held = False
        self.showing = random.randint(1, 7)

    def roll(self):
        if not self.held:
            self.showing = random.randint(1, 7)

    def hold(self):
        self.held = True

def make_dice(number):
    dice = []
    count = 0
    while count < number:
        dice.append(Die())
        count += 1
    return dice

def roll_dice():
    count = 0
    while count < 5:
        if not Player_dice[count].held:
            Player_dice[count].roll()
        print("Die " + str(count+1) + ": " + str(Player_dice[count].showing))
        count += 1
    print()

def hold_dice():
    count = 0
    while count < 5:
        hold = input("Hold Die " + str(count+1) + "?  y/n ")
        if hold == 'y':
            Player_dice[count].hold()
        count += 1

Player_dice = make_dice(5)
roll_number = 1
while roll_number < 4:
    print("Roll " + str(roll_number))
    roll_dice()
    if (roll_number < 3):
        hold_dice()
    roll_number = roll_number + 1
    print()
