import random

top_of_range = input('type a number')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please enter a number larger than 0 ')
        quit()
else:
    print("enter a number")
    quit()

random_num = random.randrange(0, top_of_range)
guesses = 0

while True:
    guesses = guesses + 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("enter a number")
        continue

    if user_guess == random_num:
        print('You Got it !!')
        break

    else:
        print('you got it wrong')

print('you got it in', guesses, 'guesses')









