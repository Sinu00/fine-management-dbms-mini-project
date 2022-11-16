from tkinter import *
from tkinter.ttk import *


#* action function for the widgets
def fineSubmit():
    print(usnVar.get())
    usnVar.set("")


def searchBtn():
    fineRecord = [
        ("11-02-22", "IA retest fine", "600", "Not Paid"),
        ("11-02-22", "Fine for using phone in class", "200", "Not Paid"),
        ("11-02-22", "IA retest fine", "600", "Not Paid"),
    ]
    for indx, data in enumerate(fineRecord):
        fineDetailsTable.insert(parent="", index="end", iid=indx, values=data)


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
notebook.place(x=10, y=5, width=730, height=600)

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
facultyIdInput = Entry(homePage, textvariable=facultyIdVar).place(x=260,
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
fineButton = Button(homePage, text="Fine", command=fineSubmit).place(x=280,
                                                                     y=200)

#? Search Student Page Widgets
outstandingFineLabel = Label(profilePage, text="Pending Fine:",
                             width=15).place(x=530, y=15)
outstandingFineVar = StringVar()
# usn input
searchStudentLabel = Label(profilePage, text="Search Student USN",
                           width=15).place(x=20, y=15)
searchStudentVar = StringVar()
searchStudentInput = Entry(profilePage, textvariable=usnVar).place(x=160,
                                                                   y=10,
                                                                   width=200,
                                                                   height=30)
# table creation
fineDetailsTable = Treeview(profilePage, height=400)
fineDetailsTable['columns'] = ("Date", "Description", "Amount", "Paid")

# formate columns
fineDetailsTable.column("#0", width=15)
fineDetailsTable.column("Date", anchor=CENTER, width=100)
fineDetailsTable.column("Description", anchor=W, width=350)
fineDetailsTable.column("Amount", anchor=CENTER, width=100)
fineDetailsTable.column("Paid", anchor=CENTER, width=100)

# create headings
fineDetailsTable.heading("#0", text="", anchor=W)
fineDetailsTable.heading("Date", text="Date", anchor=W)
fineDetailsTable.heading("Description", text="Description", anchor=W)
fineDetailsTable.heading("Amount", text="Amount", anchor=CENTER)
fineDetailsTable.heading("Paid", text="Paid", anchor=W)

searchButton = Button(profilePage, text="Search",
                      command=searchBtn).place(x=370, y=10)
fineDetailsTable.place(x=10, y=140)

root.mainloop()
