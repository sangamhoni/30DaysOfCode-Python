import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label.pack(side="left")

# CHANGING THE TEXT
# 1st method
my_label["text"] = "New Text"
# 2nd method
my_label.config(text="New Text")


# creating button
def button_clicked():
    print("I got clicked")
    # to print the entered text from the Entry
    new_text=input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry (to get a input box)
input=tkinter.Entry(width=20)
input.pack()
print(input.get())











window.mainloop()
