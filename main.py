from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kil_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Kilometers Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column= 1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kil_result_label = Label(text="0")
kil_result_label.grid(column=1, row=1)

kil_label = Label(text="Km")
kil_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()