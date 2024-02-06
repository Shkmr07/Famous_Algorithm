# Find Minimumm number in sorted and rotated Array

arr = [4,5,6,7,8,1]   # here array is Sorted and Rotated 
n = len(arr) # find the lenght

low,high = 0,n-1

# the approch is to find min in SRA is compare mid element with there neighboures if suppose the mid < mid -1 so the mid 
# itself is minimum element because after mid all element is small to mid - 1 then consider the mid itself is minimum element because the array is sorted and rotated
# on other side if mid > mid+1 then the answer is mid+1 why beacause mid is greater after all element is small to mid that why i assume my output is mid+1 

while low <= high:

    mid = low+(high-low)//2

    if mid-1 >= 0 and arr[mid-1] > arr[mid]: 
        print(arr[mid])
        break

    elif mid+1 < n and arr[mid] > arr[mid+1]:
        print(arr[mid+1])
        break

# if  the two if is True means mid + adjecent is not a minimum element then where i move my pointer that time compare the mid 
# pointer to high and low if my mid < high it means after mid all are greater element and the minumum is present at left side
# so move the high pointer to mid - 1 and same for another vice-versa. 

    elif arr[mid] < arr[high]: high = mid - 1

    else: low = mid + 1


