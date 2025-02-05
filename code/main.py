from tkinter import *
from tkinter import ttk

#These will help make the window to pop up when the user starts the program
window = Tk()
window.title("What will I do today!")
window.geometry("300x300")

#This is the choices, the "choices" being the radio button, while "choices2" being the checkedboxes
choices = ["Anime", "sleep", "game"]
choices2 = ["Eat", "draw", "Music"]

#This is to make sure each item in the list have their own variable. 
x = IntVar()
y = [IntVar() for _ in choices2]

#This function will show the selected buttons in the terminal once the user clicks the submit button
def show_selected():
    selected_radio = choices[x.get()]
    selected_checks = [choices2[i] for i, var in enumerate(y) if var.get() == 1]

    print("Selected Radio Button:", selected_radio)
    print("Selected Checkboxes:", selected_checks)


#buttons for radio button
for index in range(len(choices)):
    radiobutton = Radiobutton(window,text=choices[index],variable=x,value=index)
    radiobutton.pack()

#adds a line that seperates the check box and radio button
ttk.Separator(window, orient="horizontal").pack(fill="x", padx=5, pady=5)

#buttons for check boxes
for index, choice in enumerate(choices2):
    checkbutton = Checkbutton(window, text=choice, variable=y[index])
    checkbutton.pack()

#adds a line bellow the check boxes.
ttk.Separator(window, orient="horizontal").pack(fill="x", padx=5, pady=5)

#this is to show the submit button
btn = Button(window, text="Submit", command=show_selected)
btn.pack()

window.mainloop()