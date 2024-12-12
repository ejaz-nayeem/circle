import turtle as t5  # Correct alias

# Take input from the user
x = int(input("Enter any number (other than 1 to exit): "))

leo = t5.Turtle()
window = t5.Screen()

# The loop will stop if the user enters 1
while x != 1:
    leo.width(10)
    leo.color("black", "red")
    leo.begin_fill()
    leo.goto(0, 0)
    leo.left(180)
    leo.down() 
    leo.circle(-100)
    leo.end_fill()

    leo.width(10)
    leo.color("blue", "red")
    leo.begin_fill()
    leo.goto(0, 0)
    leo.left(180)
    leo.down() 
    leo.circle(95)
    leo.end_fill()

    # Ask again for input and break if x is 1
    x = int(input("Enter any number (other than 1 to exit): "))

window.mainloop()
