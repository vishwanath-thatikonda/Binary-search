import random
import time

def other_algorithm(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    else:
        return -1
    
a = other_algorithm([1,2,3,4,6,7,8,22,456,72], 22)
print(a)