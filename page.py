from tkinter import *
from tkinter.ttk import *
from dbQueryFuncs import getAllFineInfo, postFine, studentFineHistory, getStudentInfo, finePaidUpdate, getFineAmount
from msgFunc import sendTextMsg
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import filedialog
import csv


x_date = datetime.now()
ddmmyy = x_date.strftime("%d-%m-%y")

#! create root window
root = Tk()
root.title("-     FINE MANAGEMENT SYSTEM")
root.state("zoomed")
root.iconbitmap('images/FINEPAGEICON.ico')
root.configure(bg='white')

#? different pages of the app
notebook = ttk.Notebook()
homePage = ttk.Frame(root, style="Tab.TFrame")
profilePage = ttk.Frame(root, style="Tab.TFrame")
notebook.add(homePage, text="Fine")
notebook.add(profilePage, text="Search")
notebook.place(x=0, y=0, width=1290, height=670)

#style for the frame
sky_color = "sky blue"
gold_color = "gold"
color_tab = "#ccdee0"
#style
style = ttk.Style()
style.theme_create( "beautiful", parent = "alt", settings ={
        "TNotebook": {
            "configure": {"tabmargins": [600, 5, 0, 0], "background": '#121212' }},
        "TNotebook.Tab": {
            "configure": {"padding": [15, 1], "background": 'white', "font":('consolas italic', 14), "borderwidth":[1]},
            "map":       {"background": [("selected", 'white'), ('!active', 'grey'), ('active', '#ccdee0')],
                          "expand": [("selected", [1, 1, 1, 0])]}}})
style.theme_use("beautiful")
style.layout("Tab",
                    [('Notebook.tab', {'sticky': 'nswe', 'children':
                        [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                            #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                                [('Notebook.label', {'side': 'top', 'sticky': ''})],
                            #})],
                        })],
                    })]
                 )
style.configure('TLabel', background = 'white' , foreground = 'white')
style.configure('TFrame', background = 'white')


#icons 
photo1 = PhotoImage(file="images//STUDENTUSN.png")
label1 = Label(homePage, image=photo1, background="#FCFFE7")
label1.place(x=448, y=28)

photo2 = PhotoImage(file="images//FACULTYID.png")
label2 = Label(homePage, image=photo2, background="#FCFFE7")
label2.place(x=448, y=68)

photo3 = PhotoImage(file="images/FINEID.png")
label3 = Label(homePage, image=photo3, background="#FCFFE7")
label3.place(x=448, y=108)

photo4 = PhotoImage(file="images/FINEDISC.png")
label4 = Label(homePage, image=photo4, background="#FCFFE7")
label4.place(x=448, y=148)

#! send text message through twilio gather data
def sendTextMessage(usn, fineId):
    studentData = getStudentInfo(usn)
    name = studentData[1]
    phoneNo = studentData[2]
    fineAmount = getFineAmount(fineId)
    fineId = fineIdVar.get()
    if phoneNo != None:
        sendTextMsg(name, fineAmount, phoneNo)
    else:
        print("no number to send the text mesage")

#*! action function for the widgets
def imposeFine():
    postFine(usnVar.get().upper(), int(facultyIdVar.get()),
             int(fineIdVar.get()), fineReasonVar.get())
    sendTextMessage(usnVar.get(), int(fineIdVar.get())) # send text message logic
    usnVar.set("")
    facultyIdVar.set("")
    fineIdVar.set("")
    fineReasonVar.set("")


def searchStudent():
    # clear the table
    for row in fineDetailsTable.get_children():
        fineDetailsTable.delete(row)

    # get the student data and update in UI
    studentData = getStudentInfo(searchStudentVar.get())
    nameOfStudentVar.set(f"Name: {studentData[1]}")
    branchOfStudentVar.set(f"Branch: {studentData[3]}")
    phoneNoStudentVar.set(f"Phone No: {studentData[2]}")

    finesRecords = studentFineHistory(searchStudentVar.get())
    for indx, fineRecord in enumerate(finesRecords):
        paid_status = ''
        if fineRecord["paid_status"] == 0:
            paid_status = "Not Paid"
        else:
            paid_status = "Paid"

        fineDetailsTable.insert(parent="",
                                index="end",
                                iid=fineRecord["fine_id"],
                                values=(indx + 1, fineRecord["date"],
                                        fineRecord["description"],
                                        fineRecord["amount"], paid_status))
    totalFineToPay = 0
    for fineAmount in finesRecords:
        if fineAmount["paid_status"] != 1:
            totalFineToPay += fineAmount["amount"]

    outstandingFineVar.set(f"Pending Fine: ₹{str(totalFineToPay)}")


def finePayment():
    finePaidUpdate(fineDetailsTable.selection()[0])
    searchStudent()


#? Home page widgets
# usn input
usnLabel = Label(homePage, text="STUDENT USN", width=15, background="#FCFFE7", foreground="black" ).place(x=480, y=35)
usnVar = StringVar()
usnInput = Entry(homePage, textvariable=usnVar).place(x=600,
                                                      y=30,
                                                      width=200,
                                                      height=30)

# fined by => faculty info
facultyIdLabel = Label(homePage, text="FACULTY ID", width=15, background="#FCFFE7", foreground="black").place(x=480,
                                                                    y=75)
facultyIdVar = StringVar()
facultyIdInput = Entry(homePage, textvariable=facultyIdVar).place(x=600,
                                                                  y=70,
                                                                  width=200,
                                                                  height=30)
# fine amount input
fineIdLabel = Label(homePage, text="FINE ID", width=15, background="#FCFFE7", foreground="black").place(x=480, y=115)
fineIdVar = StringVar()
fineIdInput = Entry(homePage, textvariable=fineIdVar).place(x=600,
                                                            y=110,
                                                            width=200,
                                                            height=30)
# fine reason input
fineReasonLabel = Label(homePage, text="FINE DESCRIPTION",
                        width=18, background="#FCFFE7", foreground="black").place(x=480, y=155)
fineReasonVar = StringVar()
fineReasonInput = Entry(homePage, textvariable=fineReasonVar).place(x=600,
                                                                    y=150,
                                                                    width=200,
                                                                    height=60)
fineButton = tk.Button(homePage, text="FINE", command=imposeFine, width=25, bd=3,
                            bg='#EB455F', cursor='hand2', activebackground='#BAD7E9', fg='black').place(x=550,
                                                                     y=230)

# table for information about the available fines
usnLabel = Label(homePage,
                 text=">>>  GET FINE ID FROM BELOW INDEX  <<<",
                 width=150, background="#FCFFE7", foreground="black", font="Sans  13" ).place(x=470, y=310)
fineInfoTable = Treeview(homePage, height=11)
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

fineInfoTable.place(x=380, y=330)

#? Search Student Page Widgets
outstandingFineVar = StringVar()
outstandingFineLabel = Label(profilePage,
                             textvariable=outstandingFineVar,
                             width=20, background="#FCFFE7", foreground="black").place(x=760, y=50)

# usn input
searchStudentLabel = Label(profilePage, text="USN:",
                           width=10, background="#FCFFE7", foreground="black").place(x=500, y=15)
searchStudentVar = StringVar()
searchStudentInput = Entry(profilePage,
                           textvariable=searchStudentVar).place(x=540,
                                                                y=10,
                                                                width=200,
                                                                height=30)
# after search show info about the student
nameOfStudentVar = StringVar()
nameOfStudentVar.set("Name: ")
nameOfStudent = Label(profilePage, textvariable=nameOfStudentVar,
                      width=40, background="#FCFFE7", foreground="black").place(x=350, y=75)
branchOfStudentVar = StringVar()
branchOfStudentVar.set("Branch: ")
branchOfStudent = Label(profilePage, textvariable=branchOfStudentVar,
                        width=15, background="#FCFFE7", foreground="black").place(x=350, y=100)
phoneNoStudentVar = StringVar()
phoneNoStudentVar.set("Phone No: ")
phoneNoStudent = Label(profilePage, textvariable=phoneNoStudentVar,
                       width=25, background="#FCFFE7", foreground="black").place(x=350, y=125)

# table for showing the fines
fineDetailsTable = Treeview(profilePage, height=18)
fineDetailsTable['columns'] = ("Fine Id", "Date", "Description", "Amount",
                               "Paid")

# formate columns
fineDetailsTable.column("#0", width=15)
fineDetailsTable.column("Fine Id", anchor=CENTER, width=80)
fineDetailsTable.column("Date", anchor=CENTER, width=100)
fineDetailsTable.column("Description", anchor=W, width=320)
fineDetailsTable.column("Amount", anchor=CENTER, width=70)
fineDetailsTable.column("Paid", anchor=CENTER, width=80)

# create headings
fineDetailsTable.heading("#0", text="", anchor=W)
fineDetailsTable.heading("Fine Id", text="Fine Id", anchor=W)
fineDetailsTable.heading("Date", text="Date", anchor=W)
fineDetailsTable.heading("Description", text="Description", anchor=W)
fineDetailsTable.heading("Amount", text="Amount", anchor=CENTER)
fineDetailsTable.heading("Paid", text="Paid", anchor=W)
fineDetailsTable.place(x=300, y=160)

searchbuttonimg=PhotoImage(file='images/sbutton (1).png')
searchButton = tk.Button(profilePage, text="Search",image=searchbuttonimg,
                      command=searchStudent,bd=0,
                             cursor='hand2' , background="#FCFFE7").place(x=750, y=5)

finePaymentBtn = tk.Button(profilePage,
                        text="Fine Paid",
                        command=finePayment,bd=4,
                            bg='#EB455F', cursor='hand2', activebackground='#BAD7E9', fg='black', padx=35, pady=4).place(x=570, y=560)


root.mainloop()
