"""
Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, uppercase letters, 
numbers, and symbols. The passwords should be random, generating a new password 
every time the user asks for a new a. 
Include your run-time code in a main method.


Extra:

Ask the user how strong they want their a to be. For weak as, 
pick a word or two from a list.


"""

import random
import string

def main():
    newPassword = True
    
    while newPassword:
        
        # Prompt user for password strength
        pStrength = input("What password strength do you want? (weak, strong): ")
        
        if pStrength == 'weak':
            worldList = ['bird', 'home', 'rock', 'fork', 'walk', 'eat', 'jump']
            password = random.choice(worldList)
            passwordLength = len(password)
        else:
            a = ''      # a will be a string with at least one lowercase, uppercase, number and symbol
            a += random.choice(string.ascii_letters).lower()
            a += random.choice(string.ascii_letters).upper()
            a += str(random.randrange(10))
            a += random.choice(string.punctuation)
            
            b = ''      # b will be a randomly generated string with 4 characters
            for i in range(4):
                character = random.randrange(4)
                if character is 0:
                    b += random.choice(string.ascii_letters).lower()
                elif character is 1:
                    b += random.choice(string.ascii_letters).upper()
                elif character is 2:
                    b += str(random.randrange(10))
                elif character is 3:
                    b += random.choice(string.punctuation)
                    
            # Join a + b and shuffle the sum
            password = list(a + b)
            random.shuffle(password)
            password = ''.join(password)
            
        print('Your randomly generated %s password has %s characters:   %s' % (pStrength, 8, password))
        newPassword = input("Do you want to generate a new one? (y/n): ")
        newPassword = True if newPassword is 'y' else False
    
if __name__ == '__main__':
    main()
    