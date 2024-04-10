"""
animation - https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/

At the end of each pass (i) the biggest item in the array mlves to its location.
                pass = 1
15,3,30,2,11    swap = 1 comparison = 1 (between 15,3)
3,15,30,2,11    swap = 0 comparison = 1 (betweeen 15,30)
3,15,30,2,11    swap = 1 comparison = 1 (between 30,2)
3,15,2,30,11    swap = 1 comparison = 1 (between 30,11) ,total_swap = 3 (Max=4), total_comp = 4
3,15,2,11,30    
AT THE END OF FIRST PASS IT PLACES THE BIGGEST ELEMENT IN THE ARRAY TO ITS LOCATION

                pass = 2
3,15,2,11,30   swap = 0 comp =1 (between 3,15)
3,2,15,11,30   swap = 1 comp = 1 (between 15,2)
3,2,11,15,30   swap = 1 comp = 1 (between 15,11), total_swap = 2 (Max=3) , total_comp = 3
AT THE END OF SECOND PASS IT PLACES THE SECOND HIGHEST ELEMENT IN THE ARRAY TO ITS LOCATION

                pass = 3
2,3,11,15,30   swap = 1 comp = 1 (between 3,2)
2,3,11,15,30   swap = 0 comp = 1 (between 3,11), total_swap = 1 (Max=2) , total_comp = 2

                pass=4
2,3,11,15,30 swap=0 comp =1 (between 2,3), total_swap = 0 (Max=1) , total_comp = 1


Total passes for array of 5 items = 4 , so for n it is (n-1)
Max Swap = 4+3+2+1, so for n ---> 1+2+3+4+.....+(n-1)
Max comp = 4+3+2+1, so for n ---> 1+2+3+4+.....+(n-1)

Hence worst case time complexity --> 4+3+2+1, so for n ---> 1+2+3+4+.....+(n-1) --> n(n-1)/2 --> O(n^2)
space complexity --> O(1)

Adaptive ?  --> Bubble sort is adaptive, can be modified with flag variable
sorting Algo is said to be adaptive agar woh khud se samaj raha ki a part of array is sorted and hence reduces 
time complexity.
so for sorted array (best case) it does not take O(n^2)
 
Stable ? -->  when we have same item it should not swap
Yes bubble sort is stable it will not swap same item in the array. 

"""

def bubble_sort(arr):
    #i wala loop passes wala loop hai, for n items passes = n-1
    
    for i in range(len(arr)-1): 
        #j wala loop har pass me bade item of apni jaga dalega toh we will need i comparison less
        
        for j in range(len(arr) - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]

              
    return arr

def adaptive_bubble_sort(arr):
    #i wala loop passes wala loop hai, for n items passes = n-1
    
    for i in range(len(arr)-1): 
        #j wala loop har pass me bade item of apni jaga dalega toh we will need i comparison less
        flag = 0
        for j in range(len(arr) - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break
    
    return arr

arr = [10,3,10,300,20,15,23]
print(adaptive_bubble_sort(arr))