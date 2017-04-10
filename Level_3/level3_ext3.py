"""
check this ;) 
https://www.hackerrank.com/challenges/password-cracker

good look!!!

"""

# Read text file
text_file = open("level3_ext3_input.txt", "r")
lines = text_file.read().split('\n')
text_file.close()
T = int(lines[0]) 

for passwordCounter in range(T):
    
    # Cycle data
    N = lines[1+passwordCounter*3]
    password = lines[2+passwordCounter*3].split(' ')
    loginAttempt = lines[3+passwordCounter*3]
    
    # Cycle initialization
    original = loginAttempt
    output = ''
    sequence = []
    sequenceSize = 0

    while len(sequence) is sequenceSize:
        sequenceSize += 1
        for i in range(len(password)):
            if password[i] == loginAttempt[:len(password[i])]:
                sequence.append(i)
                loginAttempt = loginAttempt[len(password[i]):]
                output += password[i]
                break
    
    # Decide what to output based on if the original matches the output
    if original == output:
        outputPrint = [password[x] for x in sequence]
        print(' '.join(outputPrint))
    else:
        print('WRONG PASSWORD')