import psycopg2
from tkinter import *
import tkinter as tk
import psycopg2


def save_data(conn, skill, description):
    cur = conn.cursor()
    query = '''INSERT INTO skills (name, description) VALUES (%s,%s);'''
    cur.execute(query, (skill, description))
    print('Insert Successfully')
    conn.commit()
    getAll(conn)


def getAll(conn):
    cur = conn.cursor()
    query = '''SELECT * FROM skills  ;'''
    cur.execute(query)
    row = cur.fetchall()
    for i in range(5, len(row) + 5):
        frameSkill = Frame(root)
        frameSkill.grid(row=i, column=2)
        labelSkill = Label(frameSkill, text=row[5 - i][1])
        labelSkill.pack(padx=5, pady=5)


def create_tables(conn):
    command = ''' CREATE TABLE student (
            name VARCHAR(10) PRIMARY KEY,
            age VARCHAR(3) ,
            phone VARCHAR(11) 
            );'''
    try:
        # create table
        cur = conn.cursor()
        cur.execute(command)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


conn = psycopg2.connect(dbname="overtimedb",
                        user="overtimeuser",
                        password="overtime",
                        host="overtimedb.catn9kdwbteq.us-east-1.rds.amazonaws.com",
                        port="5432")
# a cursor is an object that allows you to interact with a database by executing SQL queries and fetching results.
connCursor = conn.cursor()
print("connect successfully")

root = Tk()
label_name = Label(root, text="Skill")
label_name.grid(row=1, column=0)

entry_name = Entry(root)
entry_name.grid(row=1, column=1)

label_desc = Label(root, text="Description")
label_desc.grid(row=2, column=0)

entry_desc = Entry(root)
entry_desc.grid(row=2, column=1)

button = Button(
    root, text="Add Data",
    command=lambda: save_data(
        conn,
        entry_name.get(),
        entry_desc.get(),
    )
)
button.grid(row=3, column=1)

getAll(conn)
root.mainloop()
print("data fetched successfully")
conn.close()
