from sys import argv
import sys
from xmlrpc.client import boolean

#error check
if len(sys.argv) ==1:
    exit("ERROR : You forgot the input file. ")

#readfile function
F = open(argv[1],"r")
line = F.readlines()

A = line[0].rstrip("\n").split(" ")
B = line[1].rstrip("\n").split(" ")
# print(A)
# print(B)

resultA = "A = {"
for i in A:
    if(i == A[len(A)-1]):
        resultA += i+"}"
    else:
        resultA += i+", "

resultB = "B = {"
for j in B:
    if(j == B[len(B)-1]):
        resultB += j+"}"
    else:
        resultB += j+", "

print(resultA)
print(resultB)


intersection=[]
for i in A:
    for j in B:
        if i == j:
            intersection.append(i)
resultInt = "A intersect B = {"
for i in intersection:
    if(i == intersection[len(intersection)-1]) :
        resultInt += i 
    else:
        resultInt += i + ", "

print(resultInt + "}")


unions = []
for i in A+B:
    if i not in unions:
        unions.append(i)
resultUni = "A union B = {"
for i in unions:
    if(i==unions[len(unions)-1]):
        resultUni += i + "}"
    else:
        resultUni += i + ", "
print(resultUni)


AXB = "A X B = {"
BXA = "B X A = {"

for i in A:
    for j in B:

        if(i == A[len(A)-1] and j == B[len(B)-1]):
            AXB += "("+i+","+j+")}"
            BXA += "("+j+","+i+")}"
        else:
            AXB += "("+i+","+j+"),"
            BXA += "("+j+","+i+"),"

#A-B
Asub = A 
for i in intersection:
    Asub.remove(i)
resultAsub   = "A - B = {"
for i in Asub:
    if(i==Asub[len(Asub)-1]):
        resultAsub+= i + "}"
    else:
        resultAsub+= i + ", "
print(resultAsub)


#B-A
Bsub = B
for i in intersection:
    Bsub.remove(i)
resultBsub   = "B - A = {"
for i in Bsub:
    if(i==Bsub[len(Bsub)-1]):
        resultBsub+= i + "}"
    else:
        resultBsub+= i + ", "
print(resultBsub)



print(AXB)
print(BXA)

