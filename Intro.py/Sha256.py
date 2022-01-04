# Python 3 code to demonstrate
# SHA hash algorithms.
  
import hashlib

class cl:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# initializing string
str = "Satoshi Nakamoto"
  
result = hashlib.sha256(str.encode()) # encoding str into sha256
print (cl.HEADER + "\n\n______________________________________________________________________")
print (cl.HEADER + "______________________________________________________________________")
print (cl.HEADER + "______________________________________________________________________\n\n")
print(cl.BLUE + "The hexadecimal equivalent of ", str, " + SHA256 is : ") 

print(cl.WARNING + result.hexdigest() + cl.ENDC + "\n") # printing the equivalent hexadecimal value.
print (cl.HEADER + "______________________________________________________________________")
print (cl.HEADER + "______________________________________________________________________")
print (cl.HEADER + "______________________________________________________________________\n\n")
print ("\r")


""" 
Other hash functions:

result = hashlib.sha384(str.encode())
print(cl.ENDC + "The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())
  


result = hashlib.sha1(str.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())


"""