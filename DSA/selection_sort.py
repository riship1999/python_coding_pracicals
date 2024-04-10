"""
At end of each pass we have the smallest item in the array at its location.

For array of size = 5 we have 4 passes. so for n size array (n-1) passes (pass means i wala loop)

For array of szie = 5, we have total_comp = 4+3+2+1 ... so for n we have 1+2+3+3+....+(n-1) --> n(n-1)/2 --> O(n^2)

For swap same as passes --> (n-1) --> O(n)

Therefore worst case time complexity is O(n^2)
Adv --> swapping less

Dis adv 
Adaptive ? not adaptive
Stable ? Not stable

"""

def selection_sort(arr):
    #for array of size=5 we need 4 passes, so i=0,1,2,3
    for i in range(len(arr) - 1): 
        mini = i
        #for i=0 , j=1,2,3,4 ,comparison between (i=0,j=1) (i=0,j=2), (i=0,j=3) , (i=0,j=4) total_comp = 4
        #for i=1 , j=2,3,4, comparison between (i=1,j=2) (i=1,j=3), (i=1,j=4),  total_comp = 3
        #for i=2 , j=3,4, comparison between (i=2,j=3) (i=2,j=4),  total_comp = 2
        #for i=3 , j=4, comparison between (i=3,j=4) , total_comp = 1
        for j in range(i+1,len(arr)):
            if arr[mini] > arr[j]:
                #change min
                mini = j
        arr[i],arr[mini] = arr[mini] , arr[i]
    return arr
    
arr = [101,1,3,50,46,6,23]

print(selection_sort(arr))