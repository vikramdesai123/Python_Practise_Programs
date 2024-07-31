# Given an array of size n, write a program to check if it is sorted in ascending order or not. 
# Equal values are allowed in an array and two consecutive equal values are considered sorted.

def sortedOrNot(arr):
    if len(arr) == 0 or len(arr) ==1:
        return True
    else:
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True 
    

arr = [12,34,65,24]

if(sortedOrNot(arr)):
    print("Yes")
else:
    print("No")

