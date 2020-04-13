import math
import random
import turtle
#import time
import os
win_length = 700
win_height = 700

turtle.screensize(win_length, win_height)


wel=turtle.Turtle()
wel.penup()
wel.resizemode("user")
wel.shapesize(0.00005,0.000005,0.000005)
wel.setpos(-135,280)
wel.color("purple")
wel.write("Welcome to the Hangman Game ",font=("Calibri", 17, "bold"))
wel.pendown()

hang=turtle.Turtle()
hang.resizemode("user")
hang.shapesize(0.00005,0.000005,0.000005)
hang.pensize(4)
hang.color("red")
hang.speed(500)
hang.penup()
hang.setpos(-100,-120)
hang.pendown()
hang.forward(20)
hang.left(180)
hang.forward(40)
hang.right(180)
hang.forward(20)
hang.left(90)
hang.forward(220)
hang.right(90)
hang.forward(100)
hang.right(90)
hang.forward(45)

text = turtle.Turtle()
text.penup()
text.setpos(-290, 200)
text.resizemode("user")
text.shapesize(0.00005,0.000005,0.000005)
text.fillcolor("white")
text.pendown()
text.write("The letters you already used: ", font=("Arial", 14, "normal"))
one=turtle.Turtle()
one.resizemode("user")
one.shapesize(0.04,0.04,0.04)
one.pensize(3)

one.color("black")
text2=turtle.Turtle()
text3=turtle.Turtle()
text4=turtle.Turtle()
text5=turtle.Turtle()

text3.penup()
text3.resizemode("user")
text3.shapesize(0.00005,0.000005,0.000005)
text3.setpos(-290,-200)
text3.pendown()

text5.penup()
text5.resizemode("user")
text5.shapesize(0.00005,0.000005,0.000005)
text5.setpos(130,-200)
text5.pendown()

text4.penup()
text4.resizemode("user")
text4.shapesize(0.00005,0.000005,0.000005)
text4.setpos(-290,-270)
text4.pendown()

text2.penup()
text2.resizemode("user")
text2.shapesize(0.00005,0.000005,0.000005)
text2.setpos(-20, 200)
text2.pendown()

f=random.choice(open('words.txt').read().split()).strip()

print(list(f))
count=0
listf=list(f)
for i in listf:
    count+=1
    
print("The word has " +str(count)+" letters. You have 6 tries total!")
cout=-1
letters=[]
length=len(letters)
count=0
j=0
hang=0

for i in listf:
    while j<6:
        word = str(input("guess a letter:"))

        if word in listf:
            letters.append(word)
            print("correct: "+word +" is one of our letters. You have:"+str(count)+" tries left.")
            # print("you guessed these letters: "+str(letters))
            text2.write(' , '.join(letters),font=("Arial", 14, "italic"))

        else:
            hang+=1
            letters.append(word)
            print("no, guess another letter. You have: "+str(count)+" tries left.")

            text2.write(' , '.join(letters),font=("Arial", 14, "italic"))
            # print(writt(word)+ str(letters))
            if hang==1:
                one.circle(30)
            if hang==2:
                one.right(90)
                one.forward(70)
            if hang==3:
                one.right(180)
                one.forward(50)
                one.left(90)
                one.forward(30)
            if hang==4:
                one.right(180)
                one.forward(60)
            if hang==5:
                one.left(180)
                one.forward(30)
                one.left(90)
                one.forward(50)
                one.left(20)
                one.forward(35)
                one.right(180)
            if hang==6:
                one.forward(35)
                one.left(140)
                one.forward(35)


        count-=1
        j+=1


text3.write("You are out of tries.Try to Guess the word: ",font=("Arial", 16, "italic"))
final=str(input("you are done. Guess the word:"))
text5.write(final,font=("Arial", 16, "italic"))

if final==f:
    text4.write("You Guessed it the right word!",font=("Arial", 14, "italic"))
    # print("you won")
else:
    text4.write("Sorry, You Lost. You guessed the wrong word!!",font=("Arial", 14, "bold"))










os.system("pause")
