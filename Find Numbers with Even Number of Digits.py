lst=[23,343,4342,23,2,34,4445,432]
even=[]
odd=[]
for i in lst:
    if len(str(i))%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)