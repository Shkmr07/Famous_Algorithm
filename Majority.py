# Majority element question ( Boyer-Moore Voting Algorithm)

arr = [2,1,2,2,2,5]       #input array
n,mj,ct = len(arr),0,1   # I assume that the first index of an array is my majority element

for i in range(1,n):

    if arr[i] == arr[mj]: ct += 1 # count the majority element if both are equal
    else: ct -= 1  # else decrease the count 

    if ct == 0:  #  if my count become 0 then set to 1 and  i update my majority index
        mj = i
        ct = 1

ans =  arr.count(arr[mj]) # this algorithm provide more voting index if supose the  majority element not there time it provides any index.
print(arr[mj] if ans > (n//2) else "No Majority element") # that's why we check that majority element count is greater then (n//2) or not with help of .count() method

