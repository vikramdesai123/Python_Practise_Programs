# problem statement-

# A parking lot in a mall has RxC number of parking spaces. Each parking space will either be  empty(0) or full(1). 
# The status (0/1) of a parking space is represented as the element of the matrix. 
# The task is to find index of the prpeinzta row(R) in the parking lot that has the most of the parking spaces full(1).

# Note :
# RxC- Size of the matrix
# Elements of the matrix M should be only 0 or 1.

# Example 1:
# Input :
# 3   -> Value of R(row)
# 3    -> value of C(column)
# [0 1 0 1 1 0 1 1 1] -> Elements of the array M[R][C] where each element is separated by new line.
# Output :
# 3  -> Row 3 has maximum number of 1’s


arr = [[0,1,0],
       [1,1,0],
       [1,1,1]]
m = 3
n = 3
highSum = 0
sum = 0      
for i in range(m):
    for j in range(n):
        sum = sum + arr[i][j]
    
    if sum > highSum:
        highSum = sum
        sum = 0
        id = i + 1  
print(id)
    