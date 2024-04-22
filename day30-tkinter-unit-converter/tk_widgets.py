from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="I'm a label", font=("Arial", 20, "bold"))
my_label.pack(side="top")

# How to change properties of a component(label) that we created
# my_label.config(font=("Arial", 54), text="I am a new big label")
my_label["text"] = "I am a new label"


# Button
def button_clicked():
    my_label.config(text=f"User {user_input.get()}")


my_button = Button(text="Click Me!", command=button_clicked)
my_button.pack()

# Entry
user_input = StringVar()
entry = Entry(width=20, textvariable=user_input)
entry.insert(END, string="Email Address:")
entry.pack()

# Text
text = Text(height=5, width=30)
# Put cursor in textbox.
text.focus()
# Add some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # get the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Get current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Stockholm", "Berlin", "Paris", "Vancouver"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
