# Here in the question you are asked to find the maximum and minimum element in the given array 

#here there are three approaches in python

# ==> By sorting the array and returing the first and last element in the array

# ==> By using built-in functions max() and min() to find the maximum and minimum elements in the array

# ==> By setting up two pointers maxi and mini and tranversing through the array and finding the solution

arr = [1,8,2,5,3]

mini = arr[0]

maxi = arr[0]

for i in range(len(arr)):
    if arr[i] > maxi :
        maxi = arr[i]
    if arr[i] < mini:
        mini = arr[i]
print([mini,maxi])