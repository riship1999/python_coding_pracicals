movie_list = ["stree", "mic" ,"dilwale", "kkkg", "suryayansham"]

import random
r = random.randrange(len(movie_list))
print(movie_list[r])


import random
r = random.randrange(0, len(movie_list))   #a <= N < b
print(movie_list[r])


from random import *
r = randrange(len(movie_list))
print(movie_list[r])

from random import *
r = randint(0 , len(movie_list)-1)        #a <= N <= b
print(movie_list[r])