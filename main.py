from tkinter import *
from tkinter.ttk import *
import sqlite3


#* action function for the widgets
def submit():
    print(usnVar.get())
    usnVar.set("")


#! create root window
root = Tk()
root.title("Home")
root.geometry('750x600')

#? different pages of the app
notebook = Notebook()
homePage = Frame(root)
profilePage = Frame(root)
notebook.add(homePage, text="Fine")
notebook.add(profilePage, text="Search")
notebook.place(x=10, y=5, width=750, height=600)

#? Fine page widgets
# usn input
usnLabel = Label(homePage, text="Student USN", width=15).place(x=150, y=15)
usnVar = StringVar()
usnInput = Entry(homePage, textvariable=usnVar).place(x=260,
                                                      y=10,
                                                      width=200,
                                                      height=30)

# fined by => faculty info
facultyIdLabel = Label(homePage, text="Faculty Id", width=15).place(x=150,
                                                                    y=55)
facultyIdVar = StringVar()
facultyIdInput = Entry(homePage, textvariable=usnVar).place(x=260,
                                                            y=50,
                                                            width=200,
                                                            height=30)
# fine amount input
fineAmountLabel = Label(homePage, text="Fine Id", width=15).place(x=150, y=95)
fineAmountVar = StringVar()
fineAmountInput = Entry(homePage, textvariable=fineAmountVar).place(x=260,
                                                                    y=90,
                                                                    width=200,
                                                                    height=30)
# fine reason input
fineReasonLabel = Label(homePage, text="Fine Description",
                        width=15).place(x=150, y=135)
fineReasonVar = StringVar()
fineReasonInput = Entry(homePage, textvariable=fineReasonVar).place(x=260,
                                                                    y=130,
                                                                    width=200,
                                                                    height=60)
submitButton = Button(homePage, text="Fine Confirm",
                      command=submit).place(x=280, y=200)

#? Search Student Page Widgets

root.mainloop()
