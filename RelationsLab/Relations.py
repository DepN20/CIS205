import sys
from sys import argv

#reflexive method
def reflexive(set,x,y):
    reflexive = True
    for s in set:
        n = len(x)
        found = False
        for i in range(n):
            if s == x[i] and s==y[i]:
                found = True
        if found ==False:
            reflexive = False
            break
    if reflexive == True:
        reflexive = str("Yes")
    else:
        reflexive = str("No")
    print("Reflexive: " + str(reflexive))

#symmetric method
def symmetric(set,x,y):
    symmetric = True
    n = len(x)
    for i in range(n):
        found = False
        for j in range(n):
            if x[i] == y[j] and y[i] == x[j]:
                found = True
        if found == False:
            symmetric = False
            break
    if symmetric == True:
        symmetric = str("Yes")
    else:
        symmetric = str("No")
    print("Symmetric: " + str(symmetric))

#error check
if len(sys.argv)==1:
    exit("ERROR : You forgot the input file. ")
else:
    
    set =[]
    x = []
    y = []
    
    F = open(argv[1],"r")
    lines = F.readlines()
    
    for i in range(len(lines)):
        A = lines[i].rstrip()
        if i==0:
            set = A.split(" ")
        else:
            split1 = A.split(" ")
            x.append(split1[0])
            y.append(split1[1])
    resultset = "Set: {"
    for i in set:
        if(i == set[len(set)-1]):
            resultset += i+"}"
        else:
            resultset += i+", "
    relation = "Relation: {"
    for i in range(len(x)):
        if i == len(x)-1 :
            relation += "(" + x[i]+ ", " + y[i] + ") }"
        else:
            relation += "(" + x[i]+ ", " + y[i] + "), "
            
    print(resultset)
    print(relation)
    print("")
    reflexive(set,x,y)
    symmetric(set,x,y)

    
