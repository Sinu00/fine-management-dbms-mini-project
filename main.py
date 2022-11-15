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
homePage = Frame(root, border=180)
profilePage = Frame(root)
notebook.add(homePage, text="Fine")
notebook.add(profilePage, text="Search")
notebook.grid(row=0, column=1)

#? Fine page widgets
# usn input
usnLabel = Label(homePage, text="Student USN", width=15).grid(row=1, column=0)
usnVar = StringVar()
usnInput = Entry(homePage, textvariable=usnVar).grid(row=1, column=1)

# fined by => faculty info
facultyIdLabel = Label(homePage, text="Faculty Id", width=15).grid(row=2,
                                                                   column=0)
facultyIdVar = StringVar()
facultyIdInput = Entry(homePage, textvariable=usnVar).grid(row=2, column=1)
# fine amount input
fineAmountLabel = Label(homePage, text="Fine Id", width=15).grid(row=3,
                                                                 column=0)
fineAmountVar = StringVar()
fineAmountInput = Entry(homePage, textvariable=fineAmountVar).grid(row=3,
                                                                   column=1)
# fine reason input
fineReasonLabel = Label(homePage, text="Fine Description",
                        width=15).grid(row=4, column=0)
fineReasonVar = StringVar()
fineReasonInput = Entry(homePage, textvariable=fineReasonVar).grid(row=4,
                                                                   column=1)
submitButton = Button(homePage, text="Fine Confirm",
                      command=submit).grid(row=5, column=1)

#? Search Student Page Widgets

root.mainloop()
