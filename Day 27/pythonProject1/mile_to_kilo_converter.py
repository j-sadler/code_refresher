from tkinter import *

from bokeh.layouts import column
def miles_to_kilo():
    miles = float(miles_input.get())
    kilo = str(miles * 1.609)
    kilo_results_label.config(text = f"{kilo}")



window = Tk()

window.title("Miles to Kilometer Converter")
window.config(padx= 20, pady= 20)

miles_input = Entry(width = 6)
miles_input.grid(column =  1, row = 0)

miles_lable = Label(text = "Miles")
miles_lable.grid(column =  2, row = 0)

is_equal_to = Label(text = "is equal to")
is_equal_to.grid(column =  0, row = 1)

kilo_results_label = Label(text = "0")
kilo_results_label.grid(column =  1, row = 1)

kilo_label = Label(text = "km")
kilo_label.grid(column =  2, row = 1)

calculate_button = Button(text = "Calculate", command= miles_to_kilo)
calculate_button.grid(column =  1, row = 2)

window.mainloop()