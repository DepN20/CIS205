from sys import argv

#bring the file.
#open and read file. -> saved as array..
# modifying to get the right answers.

# Error check
if len(argv)<2:
    print ("ERROR: You forgot the file name")
else:
    F = open(argv[1],"r")
    lines = F.readlines()
    num=0
    for i in lines:
        counts = i.count("8")
        num += counts
    print( "result :" + str(num) )
