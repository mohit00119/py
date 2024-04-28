#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     28/04/2024
# Copyright:   (c) ASUS 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#PROGRAM FOR BASIC CALCULATOR
a=int(input("enter the first value :"))
b=int(input("enter the second value :"))
print("""enter the wanted operation
+ for addition
- for subtraction
* for multiplication
/ for float division
// for int division""")
c=input("enter the operation to perform :")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='//':
    print(a//b)
else:
    print("Invalid Operation ")