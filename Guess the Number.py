from random import randrange
num = randrange(20)
turns = 3

while turns > 0:
    guess = int(input("Enter your guess: (1-20)  "))
    if guess == num:
        print("You guessed the number!")
        break
    elif guess < num:
        turns -= 1
        if turns > 0:
            print("Too Low")
            print("You have " + str(turns) + " guesses left.")
            print("\n")
        else:
            print("You Loose.")
    else:
        turns -=1
        if turns > 0:
            print("Too High")
            print("You have " + str(turns) + " guesses left.")
            print("\n")
        else:
            print("You Loose.")
            print("The number you are guessing is " +str(num) + '.')
    

