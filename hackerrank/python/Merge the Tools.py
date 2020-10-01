def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    nn=int(n/k)
    #print(nn) #debugging text
    list1=list()
    list2=[]
    for i in range(0,n,k):
        list1.append(string[i:i+k])
    #print(list1) #debugging text
    
    for i in range(nn):
        #print("kk") #debugging text
       list2.append(usort(list1[i]))
    for i in range(nn):
        print(list2[i])

def usort(arr):
    arr=list(arr)
    string=str()
    n=len(arr)
    for i in range(n):
        if(string.count(arr[i])==0):
            string+= str(arr[i])
    return string

