from tkinter import *


def miles_to_km():
    miles = float(m.get())
    km = round(miles * 1.609, 2)
    km_value.config(text=f"{km}")


tk = Tk()
tk.title("miles to km converter")
tk.config(padx=20, pady=20)

m = Entry(width=7)
m.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_value = Label(text="0")
km_value.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

w = Button(text="Calculate", command=miles_to_km)
w.grid(column=1, row=2)

tk.mainloop()

