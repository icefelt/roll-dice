# use random.shuffle to create die rolls
# roll 3 6-sided die
# roll 1 20-sided dice


# from random import shuffle
# dice = [1,2,3,4,5,6]
# shuffle(dice)
# print(dice)



########## one way to roll 3 X 6 sided dice
# using random.shuffle(x)
# from random import shuffle
# dice = [1,2,3,4,5,6]
# shuffle(dice)
# # print(dice)

# roll = dice[1]
# print(roll)

# shuffle(dice)
# roll = dice[1]
# print(roll)

# shuffle(dice)
# roll = dice[1]
# print(roll)


########## second way to roll 3 X 6 sided dice
# using random.randit(a, b)
# from random import randint
# die1 = randint(1,6)
# die2 = randint(1,6)
# die3 = randint(1,6)
# print(die1)
# print(die2)
# print(die3)



########## third way to roll 3 X 6 sided dice using text input form user
# import random

# question = input('Would you like to roll the dice [y/n]?\n')

# while question != 'n':
#     if question == 'y':
#         die1 = random.randint(1, 6)
#         die2 = random.randint(1, 6)
#         die3 = random.randint(1, 6)
#         print(die1, die2, die3)
#         question = input('\nWould you like to roll the dice again[y/n]?\n')
#     else:
#         print('Invalid response. Please type "y" or "n".')
#         question = input('Would you like to roll the dice [y/n]?\n')        

# print('Good Bye!')


########## fourth way to roll 3 X 6 sided dice using text input form user
# from random import randint
# ques = input('Do you want to dice [y/n]?\n')

# while ques.lower() == 'y':
#     print(f'your number is {randint(1,6)}')
#     ques = input('Do you want to roll again?')
# else:
#     print('Good Bye!')



########## fourth way to roll 3 X 6 sided dice using text input form user
# WIP
# Next, do this using a function

