# find the sum of even numbers
import sys

args = sys.argv[1:]
print(args)
sum = 0
for i in args:
    x = int(i)
    if x % 2 == 0:
        sum += x

print("Sum of entered even numbers is: ", sum)
