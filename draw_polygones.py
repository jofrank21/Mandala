import turtle
import tkinter as tk
import random

""" This app allows the user to draw a mandala by creating multiple polygons based on his input. Alternatively, the user
can also draw randomly generated mandalas.
    """

# Defining the parameters for the labels and entry fields.
text_font = 'Verdana'

label_conf = {'pady': 10, 'font': (text_font, 12)}
entry_conf = {'borderwidth': 4, 'width': 20}
button_conf = {'pady': 10, 'width': 15, 'font': (text_font, 10, 'bold'), 'fg': 'white', 'highlightbackground': 'blue'}

window = tk.Tk()
window.title('Mandala Creator v. 0.1')

# Greeting the user and telling him what the app is about.
welcome_label = tk.Label(text='Welcome to the Mandala Creator!', pady=20, font=(text_font, 25, 'bold'))
welcome_label.pack()

desc_label = tk.Label(text='This nifty little tool will allow you to create manifold'
                              ' mandalas, by drawing colorful polygons of your choice. \n Just give it a try!',
                      cnf=label_conf)
desc_label.pack()


# Allows the user to specify the number of sides, the polygon will have.
side_label = tk.Label(text='Number of sides', cnf=label_conf)
sides_entry = tk.Entry(cnf=entry_conf)
side_label.pack()
sides_entry.pack()

# Determining how many polygons will be drawn.
poly_count_label = tk.Label(text='Number of polygons', cnf=label_conf)
poly_count = tk.Entry(cnf=entry_conf)
poly_count_label.pack()
poly_count.pack()

# Determines the length of each side of the polygon.
side_length_label = tk.Label(text='Length of each side', cnf=label_conf)
side_length = tk.Entry(cnf=entry_conf)
side_length_label.pack()
side_length.pack()

# Offset between each of the polygons.
offset_label = tk.Label(text='Offset in degrees', cnf=label_conf)
offset_entry = tk.Entry(cnf=entry_conf)
offset_label.pack()
offset_entry.pack()

# Line color for the polygons.
color_label = tk.Label(text='Line color', cnf=label_conf)
line_color = tk.Entry(cnf=entry_conf)
color_label.pack()
line_color.pack()

# Width of the polygon lines.
pen_size_label = tk.Label(text='Line width', cnf=label_conf)
pen_size = tk.Entry(cnf=entry_conf)
pen_size_label.pack()
pen_size.pack()

def from_rgb(rgb):
    """Translating an RGB tuple into a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def draw_polygons(no_recs=1, offset=3, sides=4, deg=12, rec_length=24):
    """
    Draws a number of polygons.
    :return: polygon
    """
    for i in range(0, no_recs):
        for j in range(0, sides):
            turtle.forward(rec_length)
            turtle.left(deg)

        turtle.left(offset)

def draw_poly():
    """
    Gets user input and draws a number of polygons, based on the users input.
    :return: polygon
    """

    number_recs = int(poly_count.get())
    offset_deg = int(offset_entry.get())
    poly_sides = int(sides_entry.get())
    deg = round(360 / poly_sides)
    rec_length = int(side_length.get())

    # Pen color defaults to black, if not stated otherwise.
    if line_color.get() == '':
        turtle.pencolor('Black')
    else:
        turtle.pencolor(line_color.get())

    # Pen size defaults to 1, if not stated otherwise.
    if pen_size.get() == '':
        turtle.pensize(1)
    else:
        turtle.pensize(pen_size.get())

    draw_polygons(number_recs, offset_deg, poly_sides, deg, rec_length)

    turtle.hideturtle()


def draw_poly_rand():
    """
    Draws a polygon, based on random arguments.
    :return:
    """

    no_poly = random.randint(20, 40)
    offset_deg = random.randint(4, 90)
    poly_sides = random.randint(3, 18)
    deg = round(360 / poly_sides)
    rec_length = random.randint(10, 30)

    turtle.pensize(random.randint(1, 5))

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    pen_color = from_rgb((r, g, b))

    turtle.pencolor(pen_color)

    draw_polygons(no_poly, offset_deg, poly_sides, deg, rec_length)

    turtle.hideturtle()


# Divider
divider_label = tk.Label(text='')
divider_label.pack()

# Drawing a user defined mandala.
draw_poly_button = tk.Button(text="Let's draw!",
                             cnf=button_conf,
                             command=draw_poly)

draw_poly_button.pack()

# Divider
divider_label_2 = tk.Label(text='')
divider_label_2.pack()

# Drawing a mandala with random input.
draw_random = tk.Button(text="Surprise me!",
                             cnf=button_conf,
                             command=draw_poly_rand)

draw_random.pack()

window.mainloop()