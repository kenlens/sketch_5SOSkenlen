, , xCoordinate = 50
yCoordinate = 50
speed = 5
anotherSpeed = 6.7
ellipseSize=  50

def setup():
    size(400, 400)
    
def draw():
    background(99, 56, 155)
    global xCoordinate, speed, ellipseSize, yCoordinate, anotherSpeed
    leftTopBoundary = ellipseSize / 2
    rightBottomBoundary = 400 - ellipseSize / 2

    if xCoordinate >= rightBottomBoundary or xCoordinate <= leftTopBoundary:
        speed = -speed
        fill(
    if yCoordinate >= rightBottomBoundary or yCoordinate <= leftTopBoundary: 
        anotherSpeed = -anotherSpeed
    xCoordinate += speed
    yCoordinate += anotherSpeed
    fill(238, 203, 173)
    stroke(0, 191, 255)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    
