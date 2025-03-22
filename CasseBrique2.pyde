from Paddle2 import Paddle #import de la classe Paddle
from Ball2 import Ball
from Brick2 import Brick

playingGame = False
L = []
bricks = [] #création de la liste
def setup():
    global paddle # on déclare la variable paddle comme globale
    size(605,600)
    paddle = Paddle() # on crée l'objet paddle
    global ball 
    ball = Ball()

def draw():
    global playingGame
    background(0,0,0)
    fill(0,200,0);
    textAlign(CENTER);
    textSize(20)
    text("Score :", 543, 20) 
    text(ball.c, 590, 20)
    text("Vies :", 550, 40)
    text(ball.v+1, 590, 40)
    #appel des méthodes pour le paddle
    paddle.display()
    if playingGame:
        paddle.checkEdges()
        paddle.update()
    #appel des méthodes pour la balle
    ball.display()
    if playingGame:
        ball.checkEdges()
        ball.update()
        if (ball.meets(paddle)):
            if (ball.dir.y >0):
                ball.dir.y *= -1
        for i in range(len(bricks)):
            bricks[i].display()
        for i in range(len(bricks)-1,-1,-1):
            if(ball.meets(bricks[i])):
                bricks.pop(i)
                ball.dir.y*=-1
                ball.c = ball.c +1
    #defaite
    if ball.v < 0:
        while bricks != []:
                bricks.pop()
        while L != []:
            L.pop()
        L.append(1)
        ball.c = 0
        ball.v = 2
        ball.vel = PVector(1, 1)*6
        ball.dir = PVector(1, 1)
        ball.pos = PVector(width/2, height/2)
        paddle.w = 120
        for x in range(5, width -80, 75):
            addBrick(x + 37.5, 50, 6)
            addBrick(x + 37.5, 70, 5)
            addBrick(x + 37.5, 90, 4)
    if bricks == []:
        playingGame = False
    #Victoire 1er niveau
    if len(bricks) == 0 and ball.c > 1 and len(L) == 1:
        fill(0,200,0)
        textAlign(CENTER);
        textSize(20);
        text("Bravo !! Tu as gagne avec ", 280, 280)
        text(ball.c, 397, 280)
        text("points :)", 445, 280)
        text("Il te reste", 280, 300)
        text(ball.v+1, 330, 300)
        text("vies", 360, 300)
        text("Tu passes au niveau 2 !!", 302.5, 320)
        playingGame = False
        fill(0, 0, 0)
        rect(500, 0, 105, 50)
    #Victoire 2eme niveau
    if len(bricks) == 0 and ball.c > 1 and len(L) == 2:
        fill(0, 200, 0)
        textAlign(CENTER);
        textSize(20)
        text("BRAVO !!! Tu as fini les 2 niveaux", 302.5, 280)
        text("Tu as", 280, 300)
        text(ball.c, 315, 300)
        text("points", 353, 300)
        text("Appuie pour relancer", 302, 320)
        playingGame = False
        fill(0, 0, 0)
        rect(500, 0, 105, 50)

# détection des mouvements touches q et d et s
def keyPressed():
    if key == "q" or key == "Q":
        paddle.isMovingLeft = True
    elif key == "d" or key == "D":
        paddle.isMovingRight = True

#annulation des mouvements quand on relâche la touche
def keyReleased():
    paddle.isMovingRight = False
    paddle.isMovingLeft = False

#met la variable PlayingGame a True lorsque la souris est pressée
def mousePressed():
    global playingGame
    playingGame = True
    ball.v = ball.v - 1
    #lancer le 1er niveau
    if bricks == [] and len(L) == 0:
        ball.c = 0
        for x in range(5, width -80, 75):
            addBrick(x + 37.5, 50, 6)
            addBrick(x + 37.5, 70, 5)
            addBrick(x + 37.5, 90, 4)
        ball.vel = PVector(1, 1)*1
        ball.dir = PVector(1, 1)
        ball.pos = PVector(width/2, height/2)
        L.append(1)
    #si on perd une vie
    if ball.v >= 0:
        ball.vel = PVector(1, 1)*6
        ball.dir = PVector(1, 1)
        ball.pos = PVector(width/2, height/2)
    #lancer le 2eme niveau
    if len(bricks) == 0 and ball.c > 0 and len(L) == 1:
        for x in range(5, width -80, 75):
            addBrick(x + 37.5, 50, 8)
            addBrick(x + 37.5, 70, 7)
            addBrick(x + 37.5, 90, 6)
            addBrick(x + 37.5, 110, 5)
            addBrick(x + 37.5, 130, 4)
            addBrick(x + 37.5, 150, 3)
            addBrick(x + 37.5, 170, 2)
            addBrick(x + 37.5, 190, 1)
        ball.vel = PVector(1, 1)*6
        ball.dir = PVector(1, 1)
        ball.pos = PVector(width/2, height/2)
        ball.v = ball.v +1
        paddle.w = 60
        L.append(1)

#fonction qui crée des briques
def addBrick(x,y,hits):
    brick = Brick(x,y,hits)
    bricks.append(brick)
