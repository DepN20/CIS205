from sys import argv



def drawRow(numSpaces, numStars):
    space = " "
    star = "*"
    print((space * numSpaces),(star * numStars))


def drawPyramid(height):
    space = height-1
    star = 1
    for i in range(height):
        drawRow(space, star)
        space -= 1
        star +=2


def drawReversePyramid(height):
    space = 0
    star = height*2 -1
    for i in range(height):
        drawRow(space, star)
        space += 1
        star -=2





if len(argv)<2:
    print ("ERROR: Please supply command-line parameter")
elif int(argv[1])<0:
    print ("ERROR: Number must be non-negative")
else:
    drawPyramid(int(argv[1]))
    print(" ")
    drawReversePyramid(int(argv[1]))
