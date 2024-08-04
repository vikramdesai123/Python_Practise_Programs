from math import * 
    # 1st approach
        
# def factors(num):
#     fact = []
#     for i in range(1,(num+1)):
#         if num%i == 0:
#             fact.append(i)
#     return fact

# num = int(input("Enter number to find its factors:"))
# print(factors(num))


    # 2nd approach

def facts(num):
    i = 1
    while(i*i < num):
        if num%i == 0:
            print(i, end=" ")
        i = i+1
    
    for i in range(int(sqrt(num)), 0, -1):
        if num % i == 0:
            print(num//i , end=" ")
        

num = int(input("enter num to check its factors:"))
facts(num)