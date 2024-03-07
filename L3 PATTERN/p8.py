#wapp to read username and password
# if username is kamal and pass is abc123-->success else failure

import getpass
username = input("enter username ")  #input function will echo
password = getpass.getpass("enter password ")   #non-echo

if(username == 'rishi') and (password == 'abc123'):
	print("Success")
else:
	print("failure") 