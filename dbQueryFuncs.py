'''
    functions to query the database and return the data 
'''
import sqlite3


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
