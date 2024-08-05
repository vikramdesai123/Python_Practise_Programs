# Problem Statement – 

# An automobile company manufactures both a two wheeler (TW) and a four wheeler (FW). A company manager wants to make the production of both types of vehicle according to the given data below:

#   -1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
#   -2nd data, Total number of wheels = W
# The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data




def calculate_Vehical(v,w):
    if v>=w or w<2 or w%2!=0:
        print("invalid inputs")
    else:
        fw = (w-(2*v))//2 
        tw = v - fw 
    
        print("TW: {0} anf FW: {1}".format(tw, fw))
    
v=80
w=220

calculate_Vehical(v,w)