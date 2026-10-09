import turtle
import random

turtles = list()                            # Наші черепашки будуть зберігатися у списку

def setup():
    """Функія для створення та позиціонування черепашок"""
    global turtles
    startline = -620                        # Змінна кординати X лінії старту
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')

    turtle_ycor = [-40, -20, 0, 20, 40]     # Кординати Y для старту черепашок
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green']

    # Створюємо цикл по всім черепашкам, де для конжної з них створюємо об'єкт, встановлюємо для нього форму 'turtle', задаємо позицію
    # на стартововму полі, назначаєм колір, та додаємо у глобальний список
    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)

setup()
turtle.mainloop()