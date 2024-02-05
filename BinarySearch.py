# Finding  Missing number in AP

arr = [2,4,8,10,12,14,16,18,20,22]
n = len(arr)

diff = (arr[n-1]-arr[0])//n   # Here i find d the commmon difference of formuala is tn = a+(n-1)*d
# here we find the d so the formula is tn = last element of array and a = first element of array and every time one element is missing
# so if n=11 and one element is missing means (n+1) so the n = 12 so we apply formula and get difference. 
low,high = 0,n-1
# Here we use binary search to find missing number in AP.
while low <= high:
    mid = low+(high-low)//2
# so we check mid adjecent element if any adjecent element is not match with diff so the answers is adjecent + diff  
# for example: 2 4 8 10 12 14 in this array the mid is 8 and the difference of (8-4) is 4 so it not match with my difference value.
# so my answer is  4 + difference value so the output is (4+2)=  6 is the missing number.
    if mid-1 > 0 and  arr[mid]-arr[mid-1] != diff:
        print(arr[mid-1]+diff)
        break

    elif mid+1 < n and  arr[mid+1] - arr[mid] != diff:
        print(arr[mid]+diff)
        break
# if both adjecent element have same difference so that time where we move our pointer.
# i show you a example: 2 4 8 10 12 14 18 20 22 and mid element is 14. if the number is not missing so that time
# array is look 2 4 6 8 10 12 14 18 20 22 in mid position 12 present but currently  14 is present which is not  correct
# so what if  can  do we simpel decrace my high pointer and vice-versa.
    elif arr[mid] != ((mid*diff)+arr[0]):
        high = mid - 1

    else: low = mid + 1


