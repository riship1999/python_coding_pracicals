"""

linear search looks for each item in the array, until item is found

Since it checks each and every item in the arr --> worst case time complexity is --> O(N) 
Jitna jyada bada array utna jyada time.

Advantage -- Sorted array not required 

"""



def linear_search(arr,item):

    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

arr = [1,2,3,4,6,19,20]
print(linear_search(arr,20))


