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
