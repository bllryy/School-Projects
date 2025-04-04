list = [1,100]
target =  84

def linear_search(list, target):
    index = 0
    while index < len(list)
        if list[index] == target:
            return index
        else:
            index+=1

    if index == len(list) - 1:
        return  "no"
    
print("Linear Search")
print(linear_search(nums,84))

"""
How many checks in this algo
84... smh
"""

"""
why called linear function 

f(x) = x <= linear function

this algo is O(n)

def can do better than this
"""

"""
Binary search 
check the mid point and checks to see if the target is bigger and smaller than the mid
point

bigger or smaller part <= binary part

if its smaller look at the middle of the list starting from the befinning up until the og midpoint


having the size of the list after ever iteration
were only checking at most half of the amount of numbers from original

Base case:
    if the midpoint of the list is the actual target
        return 1
    
    if the value isnt in the list
        return not found

    recursive case
        take the midpoint of the list
            compare our num to see if it is bigger or smaller
                if big discard the left half of the list 
                if smaller discard right half of the list
            do binary search again on the smaller list
"""

def binary_search(list, target):
    print(list)
    #BASE CASE: not found
    if len(list) == 1 and list[0] != target:
        return "no"
    
    # if at midpoint
    if list[len(list)//2] == target:
        return "yes"
    
    # recursive 
    if list[len(list)//2] > target:
        return binary_search(list[0:len(list)//2],target)
    
    if list[len(list)//2] < target:
        return binary_search(list[0:len(list)//2],target)
    

print(binary_search(nums,84))

"""
sorting nums

unsorted nums or sorted
and want to sort them in the least amout of time

what if we took a list of nums and splitted it down the middle
and sorted each sublist then we get a recurisve type problem

Base case:
    list is of len 1 or 0
        already sorted
    
Recursive case
    split the list down the middle
    do the sname basecase for the two sublists

at the end
    zip the list back together

merge sort. called merge sort b/c were merging two smaller lists back into a larger list
"""

nums = [7,4,9,10,15,13,12,1,3,2]

def merge_sort(nums,start,end):
    # base case
    
    if len(nums) == 1 or len(nums) == 0:
        return nums
    
    mid = start + (end-start)//2

    left = merge_sort(nums[:len(nums)//2])

    right = merge_sort(nums[len(nums)//2:])

    # lists back toegther
    ileft = 0
    iright = 0

    sorted = []

    """
    compare each element at index 0 
    append the smaller one into the sorted list and increment that index by 1 until we run out of nums
    """

    while len(sorted) < len(nums):
        if left[ileft] < right{iright}:
            sorted.append(left[ileft])
            ileft +=1

        if left[left] > right[iright]:
            sorted.append(right[iright])
            iright += 1

        if ileft == len(left) -1:
            sorted.append(right[iright])
            print("Merge end")
            return sorted
        
        if iright == len(right) -1:
            sorted.append(left[ileft])
            print("Merge end")
            return sorted



