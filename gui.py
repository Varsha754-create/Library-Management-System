from tkinter import *
from tkinter import messagebox
from library import *
window = Tk()

window.title("Library Book Management System")
window.geometry("800x600")
window.configure(bg="misty rose")

heading = Label(
    window,
    text="Library Book Management System",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)
heading.grid(row=0, column=0, columnspan=2, pady=20)

book_id_label = Label(window, text="Book ID", font=("Arial", 14), bg="lightblue")
book_id_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

book_id_entry = Entry(window, font=("Arial", 14), width=30)
book_id_entry.grid(row=1, column=1, padx=20, pady=10)

book_name_label = Label(window, text="Book Name", font=("Arial", 14), bg="lightblue")
book_name_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

book_name_entry = Entry(window, font=("Arial", 14), width=30)
book_name_entry.grid(row=2, column=1, padx=20, pady=10)

author_label = Label(window, text="Author", font=("Arial", 14), bg="lightblue")
author_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

author_entry = Entry(window, font=("Arial", 14), width=30)
author_entry.grid(row=3, column=1, padx=20, pady=10)

quantity_label = Label(window, text="Quantity", font=("Arial", 14), bg="lightblue")
quantity_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

quantity_entry = Entry(window, font=("Arial", 14), width=30)
quantity_entry.grid(row=4, column=1, padx=20, pady=10)

def add():
    if book_id_entry.get() == "" or book_name_entry.get() == "" or author_entry.get() == "" or quantity_entry.get() == "":
        messagebox.showwarning("Warning", "Please Fill All Fields")
    elif not quantity_entry.get().isdigit():
        messagebox.showwarning("Warning", "Quantity Should Be Number")
    elif check_book_id(book_id_entry.get()):
        messagebox.showwarning("Warning", "Book ID Already Exists")
    else:
        book = Book(
            book_id_entry.get(),
            book_name_entry.get(),
            author_entry.get(),
            quantity_entry.get()
        )
        add_book(book)
        messagebox.showinfo("Success", "Book Added Successfully")

def show():
    result.delete(1.0, END)
    data = show_books()
    result.insert(END, data)

def search():
    result.delete(1.0, END)
    data = search_book(book_id_entry.get())
    result.insert(END, data)

def delete():
    delete_book(book_id_entry.get())
    result.delete(1.0, END)
    messagebox.showinfo("Success", "Book Deleted Successfully") 

def update():
    book = Book(
        book_id_entry.get(),
        book_name_entry.get(),
        author_entry.get(),
        quantity_entry.get()
    )
    update_book(book)
    result.delete(1.0, END)
    messagebox.showinfo("Success", "Book Updated Successfully")

def clear():
    book_id_entry.delete(0, END)
    book_name_entry.delete(0, END)
    author_entry.delete(0, END)
    quantity_entry.delete(0, END)
    result.delete(1.0, END)    

add_button = Button(
    window,
    text="Add Book",
    font=("Arial", 14),
    width=15,
    command=add
)
add_button.grid(row=5, column=1, pady=20)

show_button = Button(
    window,
    text="Show Books",
    font=("Arial", 14),
    width=15,
    command=show
)
show_button.grid(row=6, column=1, pady=10)

search_button = Button(
    window,
    text="Search Book",
    font=("Arial", 14),
    width=15,
    command=search
)
search_button.grid(row=6, column=0, pady=10)

delete_button = Button(
    window,
    text="Delete Book",
    font=("Arial", 14),
    width=15,
    command=delete
)
delete_button.grid(row=5, column=0, pady=20)

update_button = Button(
    window,
    text="Update Book",
    font=("Arial", 14),
    width=15,
    command=update
)
update_button.grid(row=6, column=2, padx=10)

clear_button = Button(
    window,
    text="Clear",
    font=("Arial", 14),
    width=15,
    command=clear
)
clear_button.grid(row=5, column=2, padx=10)
button_frame = Frame(window, bg="lightblue")
button_frame.grid(row=5, column=0, columnspan=3, pady=20)
result = Text(window, width=50, height=10, font=("Arial", 12))
result.grid(row=7, column=0, columnspan=3, pady=20)
window.mainloop()