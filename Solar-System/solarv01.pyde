
def setup():
    size(400,400,P3D)
    
def draw():
    background(0, 0, 0)
    translate(width/2, height/2, 0)
#    rotateX (millis() * 0.001 * PI)
#    rotateZ (millis() * 0.0004 * PI)
    rotateY (millis() * 0.001 * PI)
    lights()
    noStroke()
    fill(255, 255,0)
    sphere(50)
    fill(0, 255, 0)
    translate(100, 0, 0)
    #sphere(10)
    rotateY (millis() * 0.003 * PI)
    sphere(15)
    translate(30 , 0, 0)
    fill(255)
    sphere(5)
    rotateY (millis() * 0.002 * PI)
    
