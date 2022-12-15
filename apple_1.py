#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

pear_image = "pear.gif"



wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()

xcor = apple.xcor()
ycor = apple.ycor()

letters = ["a", "s", "d", "f", "g", "h", "i", "j", "k", "l"]

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
  apple.goto(0, -160)
  letter.clear()
  apple.hideturtle()


#-----function calls-----
draw_apple(apple)
apple.penup()
letter = trtl.Turtle()
letter.hideturtle()
letter.penup()
letter.goto(-20, 100)
letter.color("white")
letter.write("a", font=("Unbounded", 50))

wn.onkeypress(drop_apple, "a")
wn.listen()



wn.mainloop()