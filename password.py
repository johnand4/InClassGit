import string
from random import *

def password (length):
	password = ""
	for x in range(length):
		password +=  "".join(choice(string.ascii_letters + string.punctuation  + string.digits))
	print (password)

password(10)
