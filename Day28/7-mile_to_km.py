# wap a program to convert miles to kilometer

def miles_to_km():
    miles=float(miles_input.get())
    km=round(miles*1.609, 2)
    km_result_label.config(text=f"{km}")

from tkinter import *
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input=Entry(width=10)
miles_input.grid(row= 0,column= 1)
# Entry.config(padx=5, pady=5)


miles_label=Label(text="Miles")
miles_label.grid(row= 0,column= 2)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(row= 1,column= 0)

km_result_label=Label(text="0")
km_result_label.grid(row= 1,column=1)

km_label=Label(text="Km")
km_label.grid(row= 1,column= 2)

calc_button=Button(text="Calculate", command=miles_to_km)
calc_button.grid(row= 2,column= 1)


window.mainloop()