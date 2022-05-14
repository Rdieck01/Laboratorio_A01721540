#importación de librerías
import turtle
from turtle import *
import random
from random import randrange
# deifinición de variables
caught = 0
lives=5
#Creación de pantalla
screen= Screen()
screen.bgcolor('white')

# Se deifnen una tortuga como "score" y se colocan sus propiedades
score= Turtle()
score.color("light blue")
score.penup()
score.hideturtle()
score.goto(0,200)
score.pensize(5)

# Se deifnen una tortuga como "jugador" y se colocan sus propiedades
player= Turtle()
player.penup()
player.shape("circle")
player.hideturtle()
player.goto(0,-250)
player.showturtle()


# Movimiento horizontal(izquierda y derecha)
def lt():
    player.backward(20)
    
def rt():

    player.fd(20)

# Se asignan límites
def lbound():

    if (player.xcor() <= -250):

        player.setx(-250)


def rbound():

    if (player.xcor() >= 250):

        player.setx(250)

# Se asignan teclas para jugar
screen.listen()


screen.onkeypress(lt , "a")

screen.onkeypress(rt , "d")
#Ciclo de juego
#La condición de cuando se tiene vidas
while lives>0:

    lbound()

    rbound()
#Valores aleatorios de la basura y cangrejos
    posxt = (random.randint(-220,220))
    
    posxc = (random.randint(-220,220))
#Propiedades de la basura
    trash = Turtle()
    
    trash.speed(0)

    trash.rt(90)

    trash.penup()

    trash.color("green")

    trash.shape("square")

    trash.shapesize(1.5)

    trash.hideturtle()

    trash.goto(posxt , 250)

    trash.showturtle()
    
    trash.speed(1.2)

    trash.fd(500)
# Acumulación de puntos y Perdida de vidas con la basura
    if(trash.xcor() > player.xcor() - 20 and trash.xcor() < player.xcor() + 20 and trash.ycor() < player.ycor() + 20 and trash.ycor() > player.ycor() - 20):

        caught += 1

        trash.hideturtle()
        
        score.undo()

        score.write("SCORE: " + str(caught) + " " + " Lives: " + str(lives)  , align = "center" , font = ("Arial" , 24 , "bold"))

    else:
        
        lives= lives -1
        
        trash.hideturtle()
        
        score.undo()
        
        score.write("SCORE: " + str(caught) + " " + " Lives: " + str(lives)  , align = "center" , font = ("Arial" , 24 , "bold"))

#Propiedades de los cangrejos   
    crab= Turtle()
    
    crab.speed(0)

    crab.rt(90)

    crab.penup()

    crab.color("red")

    crab.shape("square")

    crab.shapesize(1.5)

    crab.hideturtle()

    crab.goto(posxc , 250)

    crab.showturtle()
    
    crab.speed(1.2)

    crab.fd(500)
    
        
# Perdida de vidas con los cangrejos 
    if(crab.xcor() > player.xcor() - 20 and crab.xcor() < player.xcor() + 20 and crab.ycor() < player.ycor() + 20 and crab.ycor() > player.ycor() - 20):

        lives= lives -1

        crab.hideturtle()
        
        score.undo()
        
        score.write("SCORE: " + str(caught) + " " + " Lives: " + str(lives)  , align = "center" , font = ("Arial" , 24 , "bold"))

        
    else:
        
        crab.hideturtle()
        
        score.undo()
        
        score.write("SCORE: " + str(caught) + " " + " Lives: " + str(lives)  , align = "center" , font = ("Arial" , 24 , "bold"))
    
#Fin del juego  
score.hideturtle
score.goto(0,0)
score.undo
score.write("Game Over ", align = "center" , font = ("Arial" , 48 , "bold"))