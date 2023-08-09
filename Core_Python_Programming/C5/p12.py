# accepting 3 integers separated by comma
var1, var2, var3 = [int(x) for x in input("Enter 3 numbers: ") .split(',')]
print("Sum of entered integers is {0}".format(var1 + var2 + var3))