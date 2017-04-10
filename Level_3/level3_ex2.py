"""
Each cell in a 2D grid contains either a wall ('W') or an enemy ('E'), 
or is empty ('0'). Bombs can destroy enemies, but walls are too strong to be destroyed. 
A bomb placed in an empty cell destroys all enemies in the same row and column, but the destruction stops once it hits a wall.

field = [["0", "0", "E", "0"],
         ["W", "0", "W", "E"],
         ["0", "E", "0", "W"],
         ["0", "W", "0", "E"]]

the output should be
bomber(field) = 2.

Placing a bomb at (0, 1) or at (0, 3) destroys 2 enemies.


"""
def foundBomb(sequence):
    for w in sequence:
        if w == 'E':
            return True
        elif w == 'W':
            return False
    return False
            
def individual(field, row, col):
    print('     Testing :', field[row][col], '   row', row, 'col', col)
    
    # Initialize the string in the four directions. Initialize t
    toDown, toRight, toUp, toLeft = '', '', '', ''
    
    for i in range(row+1, len(field)):
        toDown += field[i][col]         # toDown will contain the characters in down direction
    for i in range(col+1, len(field)):
        toRight += field[row][i]        # toRight will contain the characters in right direction
    for i in range(row-1,-1,-1):
        toUp += field[i][col]           # toUp will contain the characters in up direction
    for i in range(col-1,-1,-1):
        toLeft += field[row][i]         # toLeft will contain the characters in left direction

    # Initialize total with 1 if col, row lands on an enemy
    total = 1 if field[row][col] == 'E' else 0        
    total += foundBomb(toDown) + foundBomb(toRight) + foundBomb(toUp) + foundBomb(toLeft)
        
    return total
    
def bomber(field):
    print('------ Here is your field -------')
    for rowField in field:
        print(rowField)
    print('----------------------------------')
    row = int(input('What row do you want to check?:    '))
    col = int(input('What column do you want to check?: '))
    print('--- That would kill %s enemies ---' % individual(field, row, col))
        
field = [['0','0','E','0'],['W','0','W','E'],['0','E','0','W'],['0','W','0','E']]
bomber(field)