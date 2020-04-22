# pygame, this is modified number guessing game written in python

def Easy():
    # function for easy game
    max_trial = 6
    answer = 5
    guess_count = 0
    guess = None
    print('level 1 (easy mode)')
    while guess != answer and guess_count < max_trial:
        try:
            print(f'you have {max_trial - guess_count} guess left')
            guess = int(input('guess  a number between 1-10: '))
        except ValueError:
            print('please enter a valid number between 1-10 and try again!')
            break
        guess_count += 1
        if guess != answer:
            print('wrong answer')

            if guess_count == max_trial:
                print('Game Over')
        else:
            print('you got it right')


def Medium():
    # function for medium game
    max_trial = 4
    answer = 15
    guess_count = 0
    guess = None
    print('level 2 (Medium mode)')
    while guess != answer and guess_count < max_trial:
        try:
            print(f'you have {max_trial - guess_count} guess left')
            guess = int(input('guess  a number between 1-20: '))
        except ValueError:
            print('please enter a valid number between 1-20 and try again!')
            break
        guess_count += 1
        if guess != answer:
            print('wrong answer')
            if guess_count == max_trial:
                print('Game Over')
        else:
            print('you got it right')


def Hard():
    # function for hard game
    max_trial = 3
    answer = 48
    guess_count = 0
    guess = None
    print('level 3 (hard mode)')
    while guess != answer and guess_count < max_trial:
        try:
            print(f'you have {max_trial - guess_count} guess left')
            guess = int(input('guess  a number between 1-50: '))
        except ValueError:
            print('please enter a valid number between 1-50 and try again!')
            break
        guess_count += 1
        if guess != answer:
            print('wrong answer')
            if guess_count == max_trial:
                print('Game Over')
        else:
            print('you got it right')


levels = {1: Easy, 2: Medium, 3: Hard}  # dictionary containing key value pairs of game functions levels

#game_selector = ''
try:
    game_selector = input(
        'welcome to the number guessing game\n the '
        'levels are \n 1.Easy \n 2.Medium\n 3.Hard\n'
        'please choose a game level(1,2 or 3):- ')
    game_list = levels.get(int(game_selector))  #
    # instance of game level function from the dictionary selector

    game_list()  # galling the game function

except:
    print('please enter a valid selection 1,2 or 3 and try again')

