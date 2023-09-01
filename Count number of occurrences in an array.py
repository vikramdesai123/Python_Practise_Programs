def occurence(array):
    o={}
    for i in array:
        if i in o:
            o[i]+=1
        else:
            o[i]=1
    print(o)        

occurence(array=[12,23,34,23,34,45,56,56,56,34,23,12])