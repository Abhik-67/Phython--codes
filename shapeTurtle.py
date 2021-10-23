import turtle
t=turtle.Turtle()
list1 = ["yellow","red","blue","green","black","purple"]
for i in range(200):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
