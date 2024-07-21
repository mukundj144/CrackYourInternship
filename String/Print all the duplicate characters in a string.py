def printDups(Str):

    count = {}
    for i in range(len(Str)):
        if(Str[i] in count):
            count[Str[i]] += 1
        else:
            count[Str[i]] = 1
        #increase the count of characters by 1 
 
    for it,val in count.items():  #iterating through the unordered map 
        if (val > 1):   #if the count of characters is greater than 1 then duplicate found
            print(str(it) + ", count = "+str(val))