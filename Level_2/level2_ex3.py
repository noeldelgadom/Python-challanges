"""
Write a a generator in Python. Be creative with how you generate 
as - strong as have a mix of lowercase letters, uppercase letters, 
numbers, and symbols. The as should be random, generating a new a 
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
        pStrength = input("How strong do you want your password to be? (weak, medium, strong): ")
        if pStrength == 'weak':
            passwordLength = 6
        elif pStrength == 'medium':
            passwordLength = 8
        elif pStrength == 'strong':
            passwordLength = 10
            
        a = ''      # a will be a string that is randomly generated. 
        for i in range(passwordLength - 4):
            character = random.randrange(4)
            if character == 0:
                a += random.choice(string.ascii_letters).lower()
            elif character == 1:
                a += random.choice(string.ascii_letters).upper()
            elif character == 2:
                a += str(random.randrange(10))
            elif character == 3:
                a += random.choice(string.punctuation)
    
        b = ''      # b will be a string with at least one lowercase, uppercase, number and symbol
        b += random.choice(string.ascii_letters).lower()
        b += random.choice(string.ascii_letters).upper()
        b += str(random.randrange(10))
        b += random.choice(string.punctuation)
        
        # Join a + b and shuffle the sum
        password = list(a + b)
        random.shuffle(password)
        password = ''.join(password)
        print('Your randomly generated %s strength password has %s characters:   %s' % (pStrength, passwordLength, password))
        
        newPassword = input("Do you want to generate a new one? (y/n): ")
        newPassword = True if newPassword is 'y' else False
        
    
if __name__ == '__main__':
    main()
    