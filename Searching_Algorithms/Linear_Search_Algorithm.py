def Linear_Search_Algorithm(list,value):
    index=-1
    #Loop throw each element in the list
    for id in range(0,len(list)-1):
        #check if the element matches the value
        if(list[id]==value):
            index=id
            break
    return index