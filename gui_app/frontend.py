from tkinter import *
import backend

window = Tk()
window.wm_title('Book Store')

def insert_in_list(records):
    list_element.delete(0, END)

    for row in records:
        list_element.insert(END, row)

def get_selected_row():
    index = list_element.curselection()

    if index:
        selected_row = list_element.get(index)

        if selected_row:
            return selected_row

    return ('', '', '', '', '')

def select_list_row_event_handler(event):
    selected_row = get_selected_row()

    if selected_row:
        input_title.delete(0, END)
        input_title.insert(END, selected_row[1])

        input_author.delete(0, END)
        input_author.insert(END, selected_row[2])

        input_year.delete(0, END)
        input_year.insert(END, selected_row[3])

        input_isbn.delete(0, END)
        input_isbn.insert(END, selected_row[4])

def view_all():
    insert_in_list(backend.view_all_books())

def search_books():
    insert_in_list(
        backend.search_books(
            input_title_value.get(),
            input_author_value.get(),
            input_year_value.get(),
            input_isbn_value.get()
        )
    )

def add_book():
    backend.add_book(
        input_title_value.get(),
        input_author_value.get(),
        input_year_value.get(),
        input_isbn_value.get()
    )
    view_all()

def delete_book():
    selected_row = get_selected_row()

    if selected_row:
        backend.delete_book(selected_item[0])
        view_all()

def update_book():
    selected_row = get_selected_row()
    print(selected_row)

    if selected_row:
        backend.update_book(
            selected_row[0],
            selected_row[1],
            selected_row[2],
            selected_row[3],
            selected_row[4],
        )
        view_all()


def dummy():
    print(1)

# LABLES
Label(window, text='Title').grid(row=0, column=0)
Label(window, text='Author').grid(row=0, column=2)
Label(window, text='Year').grid(row=1, column=0)
Label(window, text='ISBN').grid(row=1, column=2)

# INPUT FIELDS

# TITLE field
input_title_value = StringVar()
input_title = Entry(window, textvariable=input_title_value)
input_title.grid(row=0, column=1)

# AUTHOR field
input_author_value = StringVar()
input_author = Entry(window, textvariable=input_author_value)
input_author.grid(row=0, column=3)

# YEAR field
input_year_value = StringVar()
input_year = Entry(window, textvariable=input_year_value)
input_year.grid(row=1, column=1)

# AUTHOR field
input_isbn_value = StringVar()
input_isbn = Entry(window, textvariable=input_isbn_value)
input_isbn.grid(row=1, column=3)

# LIST element
list_element = Listbox(window, height=6, width=35)
list_element.grid(row=2, column=0, rowspan=6, columnspan=2)

list_scrollbar = Scrollbar(window)
list_scrollbar.grid(row=2, column=2, rowspan=6)

list_element.configure(yscrollcommand=list_scrollbar.set)
list_scrollbar.configure(command=list_element.yview)

list_element.bind('<<ListboxSelect>>', select_list_row_event_handler)

# BUTTONS
Button(window, text='View all', command=view_all, width=12).grid(row=2, column=3)
Button(window, text='Search entry', command=search_books, width=12).grid(row=3, column=3)
Button(window, text='Add entry', command=add_book, width=12).grid(row=4, column=3)
Button(window, text='Update', command=update_book, width=12).grid(row=5, column=3)
Button(window, text='Delete', command=delete_book, width=12).grid(row=6, column=3)
Button(window, text='Close', command=window.destroy, width=12).grid(row=7, column=3)

window.mainloop()
