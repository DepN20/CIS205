from sys import argv
import sys

#if statment = statment
#if not statment(ends w/ ?, start) = not statement

if len(sys.argv) ==1:
    exit("ERROR : You forgot the input file. ")

F = open(argv[1])
sentences = F.readlines()
for i in sentences:
    without = i.strip("\n") #excepting \n so output comes out as instruction said
    if "?" in i: #question mark
        i = without + " NOT A STATEMENT"
        print(i)
    elif (" " not in i ): #single word 
        i = without + " NOT A STATEMENT"
        print(i)
    elif ("What" in i ) or ("Where" in i ) or ("How" in i) or ("Why" in i)or ("Who" in i) or ("When" in i) or ("how" in i ) : #question word
        i = without + " NOT A STATEMENT"
        print(i)
    elif ("She" in i) or ("It" in i) or ("They"in i)or ("He" in i) or ("his" in i) or ("her" in i) or ("its" in i): #pronounce
        i = without + " NOT A STATEMENT"
        print (i)
    else : #when it is statment
        print(without + " STATEMENT")





