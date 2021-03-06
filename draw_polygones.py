import turtle
import tkinter as tk

""" This app allows the user to draw a mandala by creating multiple polygons based on his input.
    """

# Parameters for the labels and entry fields.
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


def draw_polygons(no_recs=1, offset=3, sides=4):
    for i in range(0, no_recs):
        for j in range(0, sides):
            turtle.forward(rec_length)
            turtle.left(deg)

        turtle.left(offset)


def test():
    global deg
    global rec_length

    number_recs = int(poly_count.get())
    offset_deg = int(offset_entry.get())
    poly_sides = int(sides_entry.get())
    deg = 360 / poly_sides
    rec_length = int(side_length.get())

    if line_color.get() == '':
        turtle.pencolor('Black')
    else:
        turtle.pencolor(line_color.get())

    if pen_size.get() == '':
        turtle.pensize(1)
    else:
        turtle.pensize(pen_size.get())

    draw_polygons(number_recs, offset_deg, poly_sides)

    turtle.hideturtle()


# Divider
divider_label = tk.Label(text='')
divider_label.pack()

# Drawing a user defined mandala.
draw_poly_button = tk.Button(text="Let's draw!",
                             cnf=button_conf,
                             command=test)

draw_poly_button.pack()

# Divider
divider_label_2 = tk.Label(text='')
divider_label_2.pack()

# Draw a mandala with random input.
draw_random = tk.Button(text="Surprise me!",
                             cnf=button_conf,
                             command=test)

draw_random.pack()

# Clearing the canvas.


# Exiting the app.




'''
print('Please enter the length of the square:')
rec_length = int(input())
print()
print('How many rectangles do you want to draw?')
no_recs = int(input())
print()
print('Even or custom offset between the polygons?')
offset_choice = input()
if offset_choice == 'Even':
    offset = 360/no_recs
else:
    print('Enter the offset you want to use:')
    offset = int(input())
print()
print('How many sides should the polygon have')
sides = int(input())

deg = 360/sides

draw_polygons(no_recs, offset, sides)

turtle.mainloop()
'''

window.mainloop()