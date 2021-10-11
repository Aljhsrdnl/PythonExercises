from random import choice
p = ['rock', 'scissor', 'paper']

cScore = 0
pScore = 0

while cScore < 5 or pScore < 5:
    print('\n')
    pChoice = str(input('Enter your bet (rock, paper, scissor):  '))
    cChoice = choice(p)
    print('player: ' + pChoice + ' VS ' + 'computer: ' + cChoice)
    print('\n')

    if pChoice == 'rock' and cChoice == 'paper':
        cScore += 1
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))
        if cScore == 5:
            print('the computer wins!')
            break

    elif pChoice == 'paper' and cChoice == 'rock':
        pScore += 1
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))
        if pScore == 5:
            print('You won!')
            break

    elif pChoice == 'rock' and cChoice == 'scissor':
        pScore += 1
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))
        if pScore == 5:
            print('You won!')
            break

    elif pChoice == 'scissor' and cChoice == 'rock':
        cScore += 1
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))
        if cScore == 5:
            print('the computer wins!')
            break

    elif pChoice == 'paper' and cChoice == 'scissor':
        cScore += 1
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))
        if cScore == 5:
            print('the computer wins!')
            break

    elif pChoice == 'scissor' and cChoice == 'paper':
        pScore += 1
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))
        if pScore == 5:
            print('You won!')
            break
    elif pChoice == 'paper' and cChoice == 'paper':
        print('Draw')
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))

    elif pChoice == 'scissor' and cChoice == 'scissor':
        print('Draw')
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))

    elif pChoice == 'rock' and cChoice == 'rock':
        print('Draw')
        print('player: ' + str(pScore) + ' computer: ' + str(cScore))
