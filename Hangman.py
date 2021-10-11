import time
print('Start guessing')
time.sleep(0.5)

word = 'secret'
guesses = ' '
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char , end = " ")
        else:
            print('-', end = " ")
            failed += 1
    if failed == 0:
        print('You won')
        break

    guess = input('Guess a character: ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('wrong')

    print('you have ' + str(turns) , ' left')

    if turns == 0:
        print('you loose')
