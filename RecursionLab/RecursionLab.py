from sys import argv
import sys

#error check
if len(sys.argv) ==1:
    exit("ERROR : You forgot the input file. ")

#readfile function
F = open(argv[1],"r")
line = F.readlines()
A = []

#put array A setting
for i in line:
    A.append(int(i.rstrip("\n")))


#change to python code 
def divide(p,r):
    x = A[r]
    i = p-1 
    
    for j in range(p, r):
        if A[j] <= x:
            i += 1 
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
            
def sort205(p,r):
    if p < r :
        q = divide(p,r)
        sort205(p,q-1)
        sort205(q+1, r)

sort205(0,len(A)-1)

#adding /n on the result
for i in A:
    print(i) 


