"""
    script consist of many helper function which can be used to bulk load data into database from a csv file
"""
import sqlite3
import csv


#? insert a row into student table
def insertToDb(usn, name, phNo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    queryStr = """INSERT INTO students(usn, name,branch) VALUES (?,?,?)"""
    dataTuple = (usn, name, phNo)
    cursor.execute(queryStr, dataTuple)
    conn.commit()
    conn.close()
    print("insert success")


#! opening the CSV file
with open('aSecData.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for usn, name in csvFile:
        insertToDb(usn, name.upper(), usn[5:7])
