import tkinter
from tkinter import *

# FUNCTIONS
def convert_weight():
    insert_text(
        grams_field,
        convert_kg_to_grams(
            float(input_field_value.get())
        )
    )

    insert_text(
        pounds_field,
        convert_kg_to_pounds(
            float(input_field_value.get())
        )
    )

    insert_text(
        ounces_field,
        convert_kg_to_ounces(
            float(input_field_value.get())
        )
    )

def convert_kg_to_grams(kg):
    return float(kg) * 1000

def convert_kg_to_pounds(kg):
    return float(kg) * 2.20462

def convert_kg_to_ounces(kg):
    return float(kg) * 35.274

def insert_text(field, text):
    field.delete(1.0, END)
    field.insert(END, text)


window = Tk()

# LABEL
label = Label(window, text='Kg').grid(row=0, column=0)

# INPUT field
input_field_value = StringVar()
input_field = Entry(window, textvariable=input_field_value)
input_field.grid(row=0, column=1)

# BUTTON
button = Button(window, text='convert', command=convert_weight)
button.grid(row=0, column=2)

# COLUMNS LABELS ROW
Label(window, text='Grams').grid(row=1, column=0)
Label(window, text='Pounds').grid(row=1, column=1)
Label(window, text='Ounces').grid(row=1, column=2)

# VALUES FIELDS ROW
grams_field = Text(window, height=1, width=20)
grams_field.grid(row=2, column=0)

pounds_field = Text(window, height=1, width=20)
pounds_field.grid(row=2, column=1)

ounces_field = Text(window, height=1, width=20)
ounces_field.grid(row=2, column=2)

window.mainloop()
