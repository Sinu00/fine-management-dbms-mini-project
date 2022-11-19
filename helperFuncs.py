"""
    script consist of many helper function which can be used to bulk load data into database from a csv file
"""
import sqlite3
import csv


#? insert row in to STUDENT table. schema==> (usn, name, phone, branch)
def insertStudentTable(usn, name, phNo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO students(usn, name,branch) VALUES (?,?,?)"""
    dataTuple = (usn, name, phNo)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#? insert a row into FACULTY table. schema==> (id, name)
def insertFacultyTable(id, name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO faculties(id, name) VALUES (?,?)"""
    dataTuple = (id, name)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#? insert a row into DEPARTMENT level fines table. schema==>(id, description, amount)
def insertDepartmentFineTable(id, description, amount):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO department_fines(id, description,amount) VALUES (?,?,?)"""
    dataTuple = (id, description, amount)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#? insert a row into COLLEGE level fines table. schema==> (id, description, amount)
def insertCollegeFineTable(id, description, amount):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO college_fines(id, description,amount) VALUES (?,?,?)"""
    dataTuple = (id, description, amount)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#? insert a row into FINES level fines table. schema==> (id, description, amount)

#! opening the CSV file
with open('studentData.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for usn, name in csvFile:
        print(usn, name.upper(), usn[5:7])
