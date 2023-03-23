print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! lets play :)")
score = 0

answer = input("What does CPU stands For??")
if answer.lower() == "central processing unit":
    print("Your answer is correct !")
    score = score + 1
else:
    print("Incorrect")


answer = input("What is my Name??")
if answer.lower() == "jack":
    print("Your answer is correct !")
    score = score + 1
else:
    print("Incorrect")

answer = input("what is GPU")
if answer.lower() == "graphical processing unit":
    print("Your answer is correct !")
    score = score + 1
else:
    print("Incorrect")

answer = input("what is the world's population in billions? ")
if answer.lower() == "7.2":
    print("Your answer is correct !")
    score = score + 1
else:
    print("Incorrect")

print('\n')
print('You got ' + str(score) + ' questions correct !')
print('your mark is ' + str((score/4) * 100) + '%')
