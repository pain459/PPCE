# Enter 2 numbers using same line
a, b, c = [int(x) for x in input("Enter 2 numbers: ").split()]  # Enter 2 numbers with space.
print("Entered numbers are {0}, {1} and {2}".format(a, b, c))
