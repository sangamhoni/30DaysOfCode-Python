import tkinter

window = tkinter.Tk()
# adds a title to the GUI program
window.title("Learning Tkinter")

# adds a min size to the program window
window.minsize(width=500, height=300)

# LABEL
my_label=tkinter.Label(text="I am a Label", font=("Arial", 24, "normal"))       # we can use bold or italics instead of normal

# easiest way to print the label
# my_label.pack()
# or
# my_label.place()
# my_label.place(x=100, y=200)
# or
# my_label.grid(colum=0, row=0)

my_label.pack(side="bottom") # or left/right/top







window.mainloop()
# this main loop keeps running the program so it doesnt exit by itself (Similar to exitonclick())
