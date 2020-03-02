#  Игра "Царство драконов"

import random
import time

def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одно из них - дружелюбный дракон,
    который готов поделиься с вами своими сокровищами. Во второй - 
    жадный и голодный дракон, который мигом вас съест.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (Нажмите клавишу 1 или 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('Вы приближаетесь к пещеру...')
    time.sleep(2)
    print('Её темнота заставляет вас дрожать....')
    time.sleep(2)
    print('Большоой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('... Делиться с вами сокровищами!')
    else:
        print('... моментально вас съедает!')

playAgain = 'Да'
while playAgain == 'Да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()
