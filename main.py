#naeemah davis
#a program to allow user to type values in an entry and convert them to a sorted list
from tkinter import *
window = Tk()
window.geometry("300x300")
window.config(bg="pink")
window.title("Enter Values")
window.resizable(width="False", height="False")


lbl_value = Label(window, text= "Enter a value", font="Arial 25", fg="white", bg="pink")
lbl_value.place(x=50, y=50)
e_value = Entry(window)
e_value.place(x=70, y=100)
# lbl_display = Label(window, text=" rxtcyvubhn ", bg="pink", fg="white", font="Arial 15")
# lbl_display.place(x=50, y=200, width=200, height=70)


def add():
    with open('a-list.txt', 'r') as List:
        numbers = []
        for num in List:
            x = num.split()
            numbers = numbers + x
            numbers.sort()
    # with open("a-list.txt", "a") as add_to_List:
    #     value_list = []
    #     # for num in aList:
    #     #     x = num.split(", ")
    #     add_to_List.write(value_list)
    #     for value in add_to_List:
    #         value = (e_value.get())
    #         add_to_List.write((value))
    #
    #     numbers = []
    #     for value in add_to_List:
    #         x = value.split()
    #         numbers = numbers + x
    #         numbers.sort()

    # with open("a-list.txt", "r") as List:
    #     numbers = []
    #     for value in List:
    #         x = value.split()
    #         numbers = numbers + x
    #         numbers.sort()
            # numbers.append(value[1:-1].split(","))
            # numbers.sort(key=lambda x: int(x[4]))

btn_enter = Button(window, text="Enter", font="Arial 20", fg="pink", bg= "white", command=add)
btn_enter.place(x=100, y=150)





window.mainloop()

