def setup():
    size(800, 800)
    global i
    global imagem1
    global imagem2
    global imagem3
    imagem1 = loadImage("pokebola.png")
    imagem2 = loadImage("masterbola.png")
    imagem3 = loadImage("pug.png")
    i = 0
    
def draw():
    global i
    background(100)
    image(imagem1, i, height/2, 100, 100)
    j = 50
    if i < width - 200:
        image(imagem3, width - 100, height/2, 100, 100)
    else: 
        image(imagem3, width - 200, height/2, 100 + j , 100 + j )
                
    i = i + 5
    j = j + 1
    if i > width:
        i = 0
        
    #for i in range (8):
    #    for j in range (8):
    #        if ((i + j) % 2 == 1):
    #            image(imagem1, i * 100, j * 100, 100, 100)
    #        elif ((i + j) % 3 == 2):
    #            image(imagem2, i * 100, j * 100, 100, 100)
    #        else:
    #            image(imagem3, i * 1000, j * 1000, 1000, 1000)
                
def move(i, j):
    image(imagem1, i, j, 100, 100)
            
