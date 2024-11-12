# Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

# Each student gets exactly one packet.
# The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized.
# Examples:

# Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3 
# Output: 2 
# Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the minimum difference, that is 2. 


# Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 5 
# Output: 7
# Explanation: If we distribute chocolate packets {3, 2, 4, 9, 7}, we will get the minimum difference, that is 9 – 2 = 7. 

arr = [7, 3, 2, 4, 9, 12, 56]
m = 5

n = len(arr)
min_diff = float('inf')
for i in range(n - m + 1): #here last 4 elements cant iterated because fixed size of 5
    diff = arr[i+m-1] - arr[i]
    
    if diff < min_diff:
        min_diff = diff
print(min_diff)
    