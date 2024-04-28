#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ASUS
#
# Created:     28/04/2024
# Copyright:   (c) ASUS 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

i = int(input("Enter starting number: "))
j = int(input("Enter ending number: "))
k = int(input("Enter updation: "))
l = input("Choose to print in row or column: ")
choice = input("Enter 'forward' or 'backward': ")

if choice == "forward":
    for m in range(i, j + 1, k):
        if l == 'row':
            print(m, end=' ')
        elif l == 'column':
            print(m)
        else:
            print('Invalid ')

elif choice == "backward":
    for m in range(j, i - 1, -k):
        if l == 'row':
            print(m, end=' ')
        elif l == 'column':
            print(m)
        else:
            print('Invalid choice')

else:
    print('Invalid ')