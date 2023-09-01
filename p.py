lst=[23,34,1,23,12,34,56,88,7,56]
squreList=[]
for i in range(0,(len(lst)-1)):
    for j in range(1,(len(lst)-i)):
        if lst[j]<lst[j-1]:
            lst[j],lst[j-1]=lst[j-1],lst[j]
for i in lst:
    squreList.append(i**2)
print(squreList)