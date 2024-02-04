# kadane's Algorithm
# Problem find Longest subarray sum

arr = [-2,-3,4,-1,-2,1,5,-3]

mx,sm = float("-inf"),0 # finding maximum in subarray sum

for i in range(len(arr)):

    sm += arr[i]  # Adding elements in sm variable

    if sm > 0:  mx = max(mx,sm) # if  my sm variable contain positive interger then compare mx variable.

    if  sm < 0: sm = 0 #  if sum goes nagative that set it  to 0. 

print(mx)
