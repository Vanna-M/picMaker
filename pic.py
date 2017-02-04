import random

picFile = open('pic.ppm', 'w')

xRes = 500
yRes = 500

header = "P3\n" + str(xRes) + "\n" + str(yRes) + "\n" + "255\n\n"
picFile.write(header)

def oneColor(r,g,b):
    for i in range(xRes):
        for j in range(yRes):
            picFile.write(str(r) + ' ' + str(g) + ' ' + str(b) + ' ')
        picFile.write('\n')

def gradient():
    row = 0
    numRows = 5
    numCols = 5
    rowLen = xRes/numRows
    colLen = yRes/numCols
    r = 100
    g = 100
    b = 100
    for i in range(xRes):
        row += 1
        col = 0
        if (row > rowLen):
            row = 0
            r += 200
            r %= 255
            g += 200
            g %= 255
            b += 200
            b %= 255
        for j in range(yRes):
            if (col > colLen):
                col = 0
                r += 200
                r %= 255
                g += 200
                g %= 255
                b += 200
                b %= 255
            picFile.write(str(r) + ' ' + str(g) + ' ' + str(b) + ' ')
            col += 1
        picFile.write('\n')

def whoKnows():

    numRows = 2
    numCols = 2
    rowLen = xRes/numRows
    colLen = yRes/numCols

    colors = []
    for i in range(numRows + numCols):
        r = random.randrange(255)
        g = random.randrange(255)
        b = random.randrange(255)
        colors.append([r,g,b])

    for i in range(xRes):

        if (i % rowLen == 0):
            rowNum = i/rowLen

        color = colors[rowNum]

        for j in range(yRes):
            r = color[0]
            g = color[1]
            b = color[2]

            if (j%colLen == 0 and j > 0):
                color = colors[rowNum + numRows]
                picFile.write('0 0 0 ')
            elif (i % rowLen == 0 or i == 0 or j == 0 or i == xRes-1 or j == yRes-1):
                picFile.write('0 0 0 ')
            else:
                picFile.write(str(r) + ' ' + str(g) + ' ' + str(b) + ' ')

        picFile.write('\n')

whoKnows()
picFile.close()