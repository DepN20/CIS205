from sys import argv
import math
import sys

    #error check
if len(sys.argv) == 1 :
    exit("ERROR : You forgot the number ")
elif int(argv[1])<2:
    print("check you number again")
elif(int(argv[2])<1):
    print("check your second number again")
else:
    n = int(argv[1])
    r= int(argv[2])

    def CombGenerator(n, r):
        d=[] #make array d

        d.append(42)

        for k in range(1, r+1):
            d.append(k)
        print(d[1:])

        combi= math.comb(n,r)

        for k in range(2, combi+1):
            max = n
            i = r
            while d[i] == max:
                i= i-1
                max = max - 1
            d[i] = d[i]+1
            for j in range(i+1, r+1):
                d[j] = d[j-1]+1
            print(d[1:])
    CombGenerator(n, r)