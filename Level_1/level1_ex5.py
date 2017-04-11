"""
Write a program that asks the user how many Fibonacci numbers to generate and 
then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.

Hint 
The Fibonacci sequence is a sequence of numbers where the next number 
in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, 

"""

def builder(number):
    if number is 1:
        return ['1']
    else:
        counter = 2
        sequence = [1,1]
        
        while counter<number:
            sequence.append(sequence[-1]+sequence[-2])
            counter += 1
        sequence = [str(x) for x in sequence]
        return sequence

number = int(input('How many Fibonacci numbers? '))
print(', '.join(builder(number)))