global telaDoJogo
global bolaX, bolaY
global velocidadeBolaVertical
telaDoJogo = 0
bolaX, bolaY = 0, 0
tamanhoBola = 20
corBola = color(255)
gravidade = 1
velocidadeBolaVertical = 0

def setup():
    global bolaX, bolaY
    size(500, 500)
    bolaX, bolaY = width/2, height/5
    
def draw():
    #print(telaDoJogo)
    if telaDoJogo == 0:
        telaInicial()
    elif telaDoJogo == 1:
        joga()
    elif telaDoJogo == 2:
        perdeuSaiDaquiSeuRuim()
    else:
        deuRuim()
        
def telaInicial():
    background(0)
    textAlign(CENTER)
    textSize(30)
    text("Clique para iniciar! =)", width/2, height/2)

def joga():
    background(224, 112, 0)
    aplicaGravidade()
    desenhaBola()
    naoFoge()
    
def desenhaBola():
    fill(corBola)
    ellipse(bolaX, bolaY, tamanhoBola, tamanhoBola)
  
def aplicaGravidade():
    global velocidadeBolaVertical
    global bolaX, bolaY
    
    velocidadeBolaVertical += gravidade
    bolaY += velocidadeBolaVertical

def quicaChao(superficie):
    global velocidadeBolaVertical
    global bolaX, bolaY
    bolaY = superficie - (tamanhoBola/2)
    velocidadeBolaVertical *= -1
    
def quicaTeto(superficie):
    global velocidadeBolaVertical    
    global bolaX, bolaY
    bolaY = superficie + (tamanhoBola/2)
    velocidadeBolaVertical *= -1
    
def naoFoge():
    if (bolaY + (tamanhoBola/2) > height):
        quicaChao(height)
    if (bolaY - (tamanhoBola/2) < 0):
        quicaTeto(0)    
    
def perdeuSaiDaquiSeuRuim():
    pass

def deuRuim():
    pass
    
def mousePressed():
    if telaDoJogo == 0:
        iniciaJogo()

def iniciaJogo():
    global telaDoJogo
    telaDoJogo = 1
