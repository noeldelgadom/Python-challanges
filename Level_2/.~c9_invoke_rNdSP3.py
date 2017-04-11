"""
Given an array of equal-length strings, check if it is possible to rearrange 
the strings in such a way that after the rearrangement the strings at consecutive 
positions would differ by exactly one character.

Hint
For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false;
For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

"""
import math
import itertools

def isadjacent(word1, word2):
    count = 1
    list1, list2 = list(word1), list(word2)
    zipped = zip(list1, list2)
    for pair in zipped:
        if pair[0] is pair[1]:
            count += 1
    return True if count is len(word1) else False

def stringsRearrangement(inputArray):
    combinations = list(itertools.permutations(inputArray, len(inputArray)))
    isValid = []
    for i, combination in enumerate(combinations):
        isValid.append([True])                          # Set the value of column 1 as True
        for j in range(len(inputArray)-1):
            word1, word2 = combination[j], combination[j+1]
            isValid[i].append(isadjacent(word1, word2))
        
    for i in isValid:
        if False not in i:
            return True
    return False

print(stringsRearrangement(["aba", "bbb", "bab"]))
print(stringsRearrangement(["ab", "bb", "aa"]))