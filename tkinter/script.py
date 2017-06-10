from tkinter import *

window = Tk()

# BUTTON callback
def km_to_miles():
    miles = float(input_field_value.get()) * 1.6
    text_field.insert(END, miles)

# BUTTON
execute_but = Button(
    window,
    text='Execute',
    command=km_to_miles
)

execute_but.grid(
    row=1,
    column=1,
    rowspan=2
)

# INPUT field
input_field_value = StringVar()

input_field = Entry(
    window,
    textvariable=input_field_value
)

input_field.grid(
    row=0,
    column=1
)

# TEXT field
text_field = Text(
    window,
    height=2,
    width=100
)

text_field.grid(
    row=0,
    column=2
)

window.mainloop()
