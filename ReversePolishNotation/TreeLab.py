from sys import argv
import sys

#command line check
if len(sys.argv)==1:
    exit("ERROR : You forgot the input file. ")
else:
    F = open(argv[1],"r")
    lines = F.readlines()
 
    for i in range(len(lines)):
        stack = []
        A = lines[i].rstrip().split( )
        for i in A:
            #times operation
            if i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(float(b) * float(a))
            # subtract operation
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(float(b) - float(a))
            #division operation
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(float(b)/float(a))
            #plus operation
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(float(b)+float(a))
            #number 
            else:
                stack.append(float(i))
        print("intput: " + ' '.join(A))
        print("result: " + str (stack[0]) + "\n" )
        
