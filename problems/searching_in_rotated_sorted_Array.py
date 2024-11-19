# Searching in a rotated sorted array

arr = [4,5,6,0,1,2,3]
target = 0

# the element should be found in O(n logn) time complexity

l,r = 0,len(arr)-1

while l <= r:
    mid = (l+r)//2
    if arr[mid] == target:
        print("Element found at index",mid)
        break
    if arr[l] <= arr[mid]:
        if target > arr[mid] or target < nums[l]:
            l = mid+1
        else:
            r = mid-1
    else:
        if target < arr[mid] or target > arr[r]:
            r = mid-1
        else:
            l = mid+1
    
        