from tkinter import *
from tkinter.ttk import *
from dbQueryFuncs import getAllFineInfo, postFine, studentFineHistory, getStudentInfo

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


#*! action function for the widgets
def fineSubmit():
    postFine(usnVar.get().upper(), int(facultyIdVar.get()),
             int(fineIdVar.get()), fineReasonVar.get())
    usnVar.set("")
    facultyIdVar.set("")
    fineIdVar.set("")
    fineReasonVar.set("")


def searchBtn():
    # get the student data and update in UI
    studentData = getStudentInfo(searchStudentVar.get())
    print(studentData)
    nameOfStudentVar.set(f"Name: {studentData[1]}")
    branchOfStudentVar.set(f"Branch: {studentData[3]}")
    phoneNoStudentVar.set(f"Phone No: {studentData[2]}")


#? Home page widgets
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
fineIdLabel = Label(homePage, text="Fine Id", width=15).place(x=150, y=95)
fineIdVar = StringVar()
fineIdInput = Entry(homePage, textvariable=fineIdVar).place(x=260,
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

# table for information about the available fines
usnLabel = Label(homePage,
                 text="->  Get the FINE ID from the bellow index",
                 width=150).place(x=55, y=240)
fineInfoTable = Treeview(homePage, height=20)
fineInfoTable['columns'] = ("Fine Id", "Description", "Amount")

# formate columns
fineInfoTable.column("#0", width=15)
fineInfoTable.column("Fine Id", anchor=CENTER, width=100)
fineInfoTable.column("Description", anchor=W, width=350)
fineInfoTable.column("Amount", anchor=CENTER, width=100)

# create headings
fineInfoTable.heading("#0", text="", anchor=W)
fineInfoTable.heading("Fine Id", text="Fine Id", anchor=W)
fineInfoTable.heading("Description", text="Description", anchor=W)
fineInfoTable.heading("Amount", text="Amount", anchor=CENTER)

for indx, fine in enumerate(getAllFineInfo()):
    fineInfoTable.insert(parent="", index="end", iid=indx, values=fine)

fineInfoTable.place(x=55, y=265)

#? Search Student Page Widgets
outstandingFineLabel = Label(profilePage, text="Pending Fine:",
                             width=15).place(x=530, y=15)
outstandingFineVar = StringVar()
# usn input
searchStudentLabel = Label(profilePage, text="Search Student USN",
                           width=15).place(x=20, y=15)
searchStudentVar = StringVar()
searchStudentInput = Entry(profilePage,
                           textvariable=searchStudentVar).place(x=160,
                                                                y=10,
                                                                width=200,
                                                                height=30)
# after search show info about the student
nameOfStudentVar = StringVar()
nameOfStudentVar.set("Name: ")
nameOfStudent = Label(profilePage, textvariable=nameOfStudentVar,
                      width=40).place(x=40, y=55)
branchOfStudentVar = StringVar()
branchOfStudentVar.set("Branch: ")
branchOfStudent = Label(profilePage, textvariable=branchOfStudentVar,
                        width=15).place(x=40, y=80)
phoneNoStudentVar = StringVar()
phoneNoStudentVar.set("Phone No: ")
phoneNoStudent = Label(profilePage, textvariable=phoneNoStudentVar,
                       width=25).place(x=40, y=105)

# table for showing the fines
fineDetailsTable = Treeview(profilePage, height=400)
fineDetailsTable['columns'] = ("Fine Id", "Description", "Amount", "Paid")

# formate columns
fineDetailsTable.column("#0", width=15)
fineDetailsTable.column("Fine Id", anchor=CENTER, width=100)
fineDetailsTable.column("Description", anchor=W, width=350)
fineDetailsTable.column("Amount", anchor=CENTER, width=100)
fineDetailsTable.column("Paid", anchor=CENTER, width=100)

# create headings
fineDetailsTable.heading("#0", text="", anchor=W)
fineDetailsTable.heading("Fine Id", text="Fine Id", anchor=W)
fineDetailsTable.heading("Description", text="Description", anchor=W)
fineDetailsTable.heading("Amount", text="Amount", anchor=CENTER)
fineDetailsTable.heading("Paid", text="Paid", anchor=W)

searchButton = Button(profilePage, text="Search",
                      command=searchBtn).place(x=370, y=10)
fineDetailsTable.place(x=10, y=140)

root.mainloop()
