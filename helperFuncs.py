"""
    script consist of many helper function which can be used to bulk load data into database from a csv file
"""
import sqlite3
import csv


#? insert a row into student table
def insertStudentTable(usn, name, phNo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO students(usn, name,branch) VALUES (?,?,?)"""
    dataTuple = (usn, name, phNo)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#? insert a row into student table
def insertFacultyTable(id, name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO faculties(id, name) VALUES (?,?)"""
    dataTuple = (id, name)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#? insert a row into department level fines table
def insertDepartmentFineTable(id, description, amount):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO department_fines(id, description,amount) VALUES (?,?,?)"""
    dataTuple = (id, description, amount)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#? insert a row into college level fines table
def insertCollegeFineTable(id, description, amount):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO college_fines(id, description,amount) VALUES (?,?,?)"""
    dataTuple = (id, description, amount)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#! opening the CSV file
with open('college-fines.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for usn, name, amount in csvFile:
        insertCollegeFineTable(usn, name.upper(), amount)
