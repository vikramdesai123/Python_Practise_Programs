class First:
    def duplicate(self,arr):
        arr2=[]
        
        for i in arr:
            if i in arr2:
                print(i) 
                break   
            else:
                arr2.append(i)
            
    
if __name__=="__main__":
    arr=[2,34,5,65,34,44,5,6,44]
    f=First()
    f.duplicate(arr)
    
    