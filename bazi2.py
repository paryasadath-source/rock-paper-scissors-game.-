import random

bazi=['sang' , 'kaqaz' , 'qeychi']

you_point=0
computer_point=0
shart_bazi=True 

while(shart_bazi):
    you = input("entekhab kon (sang,kaqaz,qeychi): ")
    you = you.lower()
    
    rand=random.randint(0,2)
    computer=bazi[rand]

    if you=='sang' and computer=='kaqaz':
        computer_point=computer_point+1

    if you=='qeychi' and computer=='kaqaz':
        you_point=you_point+1

    if you=='sang' and computer=='qeychi':
        you_point=you_point+1

    if you=='kaqaz' and computer=='qeychi':
        computer_point=computer_point+1

    if you=='qeychi' and computer=='sang':
        computer_point=computer_point+1

    if you=='kaqaz' and computer=='sang':
        you_point=you_point+1

    print("YOU:", you_point, "-", you)
    print("COM:", computer_point, "-", computer)

    if you_point>=3 or computer_point>=3:
        shart_bazi=False

        if you_point>computer_point:
            print("YOU WIN!")
        else:
            print("YOU LOSE :(")