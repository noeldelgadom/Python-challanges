"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hint: 
search isdigit & isalpha


"""

a = input('Enter a sentence:    ')
a = [character for character in a]

letters, digits = 0, 0

for character in a:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1
    
print('     LETTERS        ', letters)
print('     DIGITS         ', digits)