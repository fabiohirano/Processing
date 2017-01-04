import random

def value(plA, plB):
    if (plA == 1 and plB == 1):
        return (2, 2)
    if (plA == 1 and plB == -1):
        return (0, 3)
    if (plA == -1 and plB == 1):
        return (3, 0)
    if (plA == -1 and plB == -1):
        return (1, 1)

def randNum():
    if (random.randint(0,100) % 2 == 1):
        return 1
    else:
        return -1

def paint(x):
    if x == 1:
        return 255
    else:
        return 0

def setup():
    global nSquare, sizeSquare
    global m
    size(500, 500)
    nSquare = 100
    sizeSquare = width/nSquare
    m = [[0 for i in range(nSquare)] for j in range(nSquare)]
    for i in range (nSquare):
        for j in range(nSquare):
            m[i][j] = randNum()
            fill(paint(m[i][j]))
            rect(i * sizeSquare, j * sizeSquare, sizeSquare, sizeSquare)
            
def draw():    
#            fill(paint(m[i][j]))
#            rect(i * sizeSquare, j * sizeSquare, sizeSquare, sizeSquare)
    for i in range (nSquare):
        for j in range (nSquare):
            if j < nSquare-1:
                (vlA, vlB) = value (m[i][j], m[i][j+1])
                if vlA > vlB:
                    m[i][j+1] = m[i][j]
                elif vlB > vlA:
                    m[i][j] = m[i][j+1]
                else:
                    m[i][j] = m[i][j]
                fill(paint(m[i][j]))
                rect(i * sizeSquare, j * sizeSquare, sizeSquare, sizeSquare)
    delay(1000)