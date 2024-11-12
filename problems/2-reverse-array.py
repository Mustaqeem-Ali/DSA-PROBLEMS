arr = [1,2,3,4,5,6]

#reversing the array 

n = len(arr)

right = n - 1
left = 0
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)