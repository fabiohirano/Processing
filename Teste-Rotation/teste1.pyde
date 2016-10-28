def setup():
    size(500, 500, P3D)
    global img
    img = loadImage("a.png")
    global img2
    img2 = loadImage("bulba.png")
    
def draw():
    background(100)
    translate(width/2, height/2, 0)
    rotateY(millis() * PI * 0.001)
    imageMode(CENTER)
    image(img, 0, 0, 200, 200)
   
      ############ OUTRO PLANETA
    
    translate(150, 0, 0)
    rotateY(millis() * PI * 0.001)
    imageMode(CENTER)
    image(img2, 0, 0, 100, 100) 
