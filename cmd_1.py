#to accept multiple command line arguments 
import sys
import cowsay

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: #slicing of the list from first indexed (second) element to the last [start:end:step] , this is how we slice , the end is not counted 
    print("HEllo my name is",  arg)

# a package is a module written by people which we can use , found at pypi.org 
#we have something like pip to install paython packages like cowsay pip install cowsay 

cowsay.cow("HEllo, "+ sys.argv[1])

print(sys.argv[0],sys.argv[1])