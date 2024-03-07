#wapp to read and integer from CLA and find the sqrt of the number
# command line arguments CLA


import sys
import math

try:
	num = int(sys.argv[1])
	if num < 0:
		raise Exception("-ve number not supported")
	res = math.sqrt(num)
except IndexError:
	print("u need to pass 1 integer argument from command line")
except ValueError:
	print("u need to pass integer only")
except Exception as e:
	print("issue ",e)
else:
	print("res = ",res)


#At sys.argv[0]--> file name is present (python p2.py)
#therefore we write sys.argv[1]-->to give number at index 1
#sys is the module that comsist of argv[] list ,SYS IS USED TO ACCESS CLA
