"""
Binary search takes place only in sorted array.

Time Complexity of binary search -- > O(NlogN + logN)

"""

arr = [1,2,3,4,5,6,7,8]


def binary_search(arr,low, high, item):

    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            #jab mid bada hai item se toh high ko chota krdo
            return binary_search(arr,low,mid-1,item)
        else:
            #jab mid chota hai item se toh low ko bada kardo
            return binary_search(arr,mid+1,high,item)
    else:
        return -1
    

arr = [1,2,3,4,5,6,7,8]

print(binary_search(arr,0,len(arr)-1,5))

        