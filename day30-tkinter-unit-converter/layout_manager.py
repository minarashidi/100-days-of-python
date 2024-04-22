from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="My first label")
my_label.config(text="This is my new label")
my_label.grid(row=0, column=0)

# Button
my_button = Button(text="Button1 - Click Me!", command=button_clicked)
my_button.grid(row=1, column=1)

# New Button
my_button = Button(text="Button2 - Click Me!", command=button_clicked)
my_button.grid(row=0, column=2)

# Entry
input = Entry(width=20)
print(input.get())
input.grid(row=2, column=3)
# entry.pack()
# entry.place(x=100, y=100) (Place layout management: precise positioning,  downside: so specific and we need to figure out the exact coordinates)
# entry.grid(row=0, column=0)

window.mainloop()
