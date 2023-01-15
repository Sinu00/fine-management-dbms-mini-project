'''
    functions to query the database and return the data 
'''
import sqlite3
import nanoid
from datetime import datetime

x_date = datetime.now()
ddmmyy = x_date.strftime("%d-%m-%y")


# function will return everything in the college, department lvl fines tables ==> data returned by the function in used to show the fines that can be pressed to a student in the home page table
def getAllFineInfo():
    allFines = []
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # query the data from 2 tables
    dataFromDb = cursor.execute("""SELECT * FROM department_fines""")
    for data in dataFromDb:
        allFines.append(data)
    dataFromDb = cursor.execute("""SELECT * FROM college_fines""")
    for data in dataFromDb:
        allFines.append(data)
    conn.commit()
    conn.close()
    #returning array of tuples with all the fines from both tables
    return allFines


# posts a fine in to the fines table the schema of the table is (id,usn,date, paid, fine_id,description, fined_by)
def postFine(usn, facultyId, fineId, description):
    # print(ddmmyy)
    # print(nanoid.generate(size=12), usn, ddmmyy, 0, fineId, description,
    #       facultyId)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO fines(id, usn,date, paid,fine_id,description,fined_by) VALUES (?,?,?,?,?,?,?)"""
    dataTuple = (nanoid.generate(size=12), usn, ddmmyy, 0, fineId, description,
                 facultyId)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()


# get all the fines of a student from the fines database
# return array of dictionaries {date,fine_id,description, amount, paid_status}
def studentFineHistory(usn):
    studentFineHistory = []
    allFinesInfo = getAllFineInfo()
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    studentFineQueryResult = cursor.execute(
        "SELECT * FROM fines WHERE usn LIKE ?;", (usn.upper(), ))
    for fine in studentFineQueryResult:
        fineDict = {
            "date": fine[2],
            "fine_id": fine[0],
            "description": fine[5],
            "paid_status": fine[3]
        }
        # get fine info from the college and department fines by fine id
        for fineInfo in allFinesInfo:
            if fineInfo[0] == fine[4]:
                fineDict["amount"] = fineInfo[2]

        studentFineHistory.append(fineDict)
    conn.commit()
    conn.close()
    return studentFineHistory


# get the data of the student from the students db returns (usn, name, no, branch)
def getStudentInfo(usn):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    studentInfo = cursor.execute("SELECT * FROM students WHERE usn LIKE ?;",
                                 (usn.upper(), ))
    studentInfo = tuple(studentInfo)
    conn.commit()
    conn.close()
    return studentInfo[0]

# paying the selected fine 
def finePaidUpdate(fine_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    studentInfo = cursor.execute("UPDATE fines SET paid = 1 WHERE id = ?",
                                 (fine_id, ))
    conn.commit()
    conn.close()

def getFineAmount(fineId):
    allFines = getAllFineInfo()
    for fine in allFines:
        if fineId == fine[0]:
            return fine[2]

