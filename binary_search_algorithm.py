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
        return -1


    midpoint = len(lst) // 2

    if lst[midpoint] == target:
        return midpoint
    
    if lst[midpoint] >  target:
        return binary_serach(lst,target,midpoint+1,high)
    else:
        return binary_serach(lst,target,low,midpoint-1)
    

if __name__ == '__main__':
    # lst = [1,2,3,34,44,55]    
    # print(naive_search(lst,44))
    # print(binary_serach(lst,44))
    
    length = 10000
    number_lst = set()
    while len(number_lst) < length:
        number_lst.add(random.randint(-3*length,3*length))

    number_lst = sorted(list(number_lst))

    
    start = time.time()
    for target in number_lst:
        naive_search(number_lst,target)
    end = time.time()
    print("The navie search time is", end - start, "seconds")

    start = time.time()
    for target in number_lst:
        binary_serach(number_lst,target)
    end = time.time()
    print("The binary search time is", end - start, "seconds")


