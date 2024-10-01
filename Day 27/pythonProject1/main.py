from tkinter import *

FONT = ("Arial", 24, "bold")
window = Tk()
window.title("Joes Program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="i am a label", font=FONT)
my_label.pack()

my_label["text"] = "new Text"
my_label.config(text= "New text")

#Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("Clicky click")

button = Button(text = "Click Me!", command=button_clicked)
button.pack()

#entry
input = Entry()
input.pack()

window.mainloop()