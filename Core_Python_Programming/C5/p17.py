# to display command line args
import sys

n = len(sys.argv)  # n is the number of args
args = sys.argv  # args list contains arguments
print("Number of command line args: ", n)
print("The args are: ", args)
print("Args one by one:")
for i in args:
    print(i)
