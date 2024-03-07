"""In python we can declare variable in below given format and
if we print, we will get
print(i) = 1
print(j) = 2
print(k) = 3
"""
d,e,f = 1,2,3 

"""
In the same, for below declaration 
we will get 
 print(u) = a
 print(v) = 50
 print(w) = b

"""
u,v,w = ('a',50,'b')


"""
Now to understand enumerate -->
 it returns index, value for any given iterable (it can be list, string, dict)

the below loop will print tuple --> 
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, 50)

"""
lst = [10,20,30,40,50]
for i in enumerate(lst):
    print(i)

"""
As explained above to unpack tuple using loop 
"""
for index,value in enumerate(lst):
    print(f'index = {index}, value = {value}')