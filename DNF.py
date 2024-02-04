# Detch National Flag Algorithm
#problem:- sort the array which contain only (0,1,2)
arr = [0,1,2,0,1,2]
n = len(arr) # length of the array

low,mid,high = 0,0,n-1 # take three pointer

while mid <= high: # why <= to why not only < , because why my mid and high at same index and that element is 0
                   # then if i use only < opearter the 0 swap is not happen and the answer is not correct.

    if arr[mid] == 0: # if arr[mid] == 0 then swap  with low and  move both pointer.
        arr[low],arr[mid] = arr[mid],arr[low]
        low += 1
        mid += 1

    elif arr[mid] == 1: # if arr[mid]==1 move mid pointer because we check any 0 is there not with help of mid.
        mid += 1

    else: # if arr[mid]==2 then  we swap the mid to high because we found a greater element at middle or first so we put into a last point.
        arr[mid],arr[high] = arr[high],arr[mid]
        high -=  1 # move the high pointer to  left because we sucuessfully place higher value so we don't disturb the element

print(arr)

