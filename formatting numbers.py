pi = 3.44444
print("the value of pi is {}".format(pi))
#O/P - the value of pi is 3.44444
print("the value of pi is {:.2f}".format(pi))
#O/P - the value of pi is 3.44 {:.2f} = it will take 2 numbers in floating values
num = 10000000
print("The num is {:,}".format(num))
#O/P - The num is 10,000,000
num = 101
print("The binary num is {:b}".format(num)) #{:b} = binary
#O/P - The binary num is 1100101
# o for octal, x (or X) for hexa, E for scientific notation
num = 101
print("The octal num is {:o}".format(num)) 
#O/P - The octal num is 145
num = 101
print("The hexal num is {:x}".format(num)) 
#O/P - The hexal num is 65
num = 101
print("The scientific notation num is {:E}".format(num)) 
#O/P - The scientific notation num is 1.010000E+02