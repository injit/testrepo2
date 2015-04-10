from tkinter import Tk, Button, Label, Entry


container = Tk()

first_number_label = Label(container, text = "First Number:")
first_number_label.grid(row= 1, column= 0)
first_entry = Entry(container)
first_entry.grid(row = 1, column = 1)

second_number_label = Label(container, text = "Second Number:")
second_number_label.grid(row = 2, column = 0)
second_entry = Entry(container)
second_entry.grid(row = 2, column = 1)

ans_label = Label(container, text = "Ans")
ans_label.grid(row= 3, columnspan = 2)


def do_addition():
	ans_label['text'] = str(int(first_entry.get()) + int(second_entry.get()))
def do_subtraction():
	ans_label['text'] = str(int(first_entry.get()) - int(second_entry.get()))
def do_division():
	ans_label['text'] = str(int(first_entry.get()) / int(second_entry.get()))
def do_multiplication():
	ans_label['text'] = str(int(first_entry.get()) * int(second_entry.get()))


button1 = Button(container, text= "+", command = do_addition)
button1.grid(row = 0, column = 3)
button2 = Button(container, text= "-", command = do_subtraction)
button2.grid(row = 1, column = 3)
button3 = Button(container, text= "/", command = do_division)
button3.grid(row = 2, column = 3)
button4 = Button(container, text= "*", command = do_multiplication)
button4.grid(row = 3, column = 3)

container.mainloop()
