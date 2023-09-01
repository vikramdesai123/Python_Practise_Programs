def rev(array):
    rev_arr=[]
    
    for i in range(len(array)):
        x=array.pop()
        rev_arr.append(x)
    print(rev_arr)

rev(array=[23,34,12,23,35,665,65,4])