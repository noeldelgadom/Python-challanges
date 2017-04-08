"""
Make a two-player Rock-Paper-Scissors game. 

Hint:
Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game


"""

rematch = 'y'
tie = 'Its a tie'
aWins = 'Player A wins!'
bWins = 'Player B wins!'

while rematch is 'y':
    a = input('Player A - chose r,p,s: ')
    b = input('Player B - chose r,p,s: ')
    if a is 'r':
        if b is 'r':
            print(tie)
        elif b is 'p':
            print(bWins)
        elif b is 's':
            print(aWins)
    elif a is 'p':
        if b is 'r':
            print(aWins)
        elif b is 'p':
            print(tie)
        elif b is 's':
            print(bWins)
    elif a is 's':
        if b is 'r':
            print(bWins)
        elif b is 'p':
            print(aWins)
        elif b is 's':
            print(tie)
    
    rematch = input('Want to play again?(y/n):')