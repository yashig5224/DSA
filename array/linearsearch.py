def linear_search(arr,target):
    for i in range(len(arr)):   #For loop to traverse the array
        if arr[i]==target:     
            #Found the element
            return i
    return -1    # if not found 

arr=[4,2,7,8,1,2,5]
result=linear_search(arr,80)
print("element is found at index: ",result)   