from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)


def mile_to_km():
    km = round(float(mile_input.get()) * 1.609)
    calculated_km.config(text=f"{km}")


mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(row=1, column=0)

calculated_km = Label(text="0")
calculated_km.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
