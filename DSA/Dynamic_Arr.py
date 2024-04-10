import sys

L =[]
for i in range(100):
    print(i, "size = " ,sys.getsizeof(L))
    L.append(i)

#concept of dynamic array in which the size of array gets doubled ( in python increases by 8 )