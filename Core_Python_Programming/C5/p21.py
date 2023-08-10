import argparse

parser = argparse.ArgumentParser(description="This program calculates the sum of two given numbers.")
parser.add_argument("n1", type=float, help="Input the first number")
parser.add_argument("n2", type=float, help="Input the second number")

args = parser.parse_args()

result = float(args.n1) + float(args.n2)
print("Sum of two=", result)