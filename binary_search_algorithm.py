import random
import time

def naive_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    else:
        return -1
    

# Binary search algorithm uses divide and conquor method.
def binary_serach(lst,target,high = None,low = None): #[1,3,4,5,6,10]
    if low is None:
        low = 0
    if high is None:
        high = len(lst) -1
    else:
        -1


    midpoint = len(lst) // 2

    if lst[midpoint] == target:
        return midpoint
    
    if lst[midpoint] >  target:
        return binary_serach(lst,target,midpoint+1,high)
    else:
        return binary_serach(lst,target,low,midpoint-1)
    

if __name__ == '__main__':
    lst = [1,2,3,34,44,55]    
    print(naive_search(lst,44))
    print(binary_serach(lst,44))
