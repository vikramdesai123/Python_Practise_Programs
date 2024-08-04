def factors(num):
    fact = []
    for i in range(1,(num+1)):
        if num%i == 0:
            fact.append(i)
    return fact

num = int(input("Enter number to find its factors:"))
print(factors(num))