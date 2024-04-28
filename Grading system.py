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

#GRADING SYSTEM
s=int(input("enter no of subjects :"))
l=[]
for i in range(s):
    a=input("enter the subject :")
    l.append(a)
dic={}
for i in l:
    dic[i]=int(input(f"enter marks in {i} :"))
a=(sum(list(dic.values()))/len(list(dic.keys())))
print("Total Percentage :",a)
if a<50:
    print("GRADE-E")
if a>=50 and a<60:
    print("GRADE-D")
if a>=60 and a<70:
    print("GRADE-C")
if a>=70 and a<80:
    print("GRADE-B")
if a>=80 and a<90:
    print("GRADE-A")
if a>=90 and a<100:
    print("GRADE-A+")