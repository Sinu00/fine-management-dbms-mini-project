import tkinter as tk
import sqlite3
import subprocess
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def hide():
    closeeye.config(file='images/PassNotVis.png')
    password_entry.config(show='.')
    eyebutton.config(command=show)

def show():
    closeeye.config(file='images/PassVis.png')
    password_entry.config(show='')
    eyebutton.config(command=hide)

def usertemptext(e):
        username_entry.delete(0,END)
def passtemptext(e):
        password_entry.delete(0,END)

def check_credentials():
    conn = sqlite3.connect('./database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username_var.get(), password_var.get()))
    result = c.fetchone()
    if result:
        login_status_var.set("Login successful!")
        root.destroy()
        # open a main window
        subprocess.Popen(["python","main.py"])
        
    else:
        messagebox.showinfo("","Invalid username or password.")
    conn.close()

root = tk.Tk()
root.title("-     Login Page")
root.state("zoomed")
root.iconbitmap('images/LOGIN (1).ico')
root.configure(bg='#393E46')

root.whitebg = Image.open('images/orgbg.png')
photo = ImageTk.PhotoImage(root.whitebg)
root.whitebg_label = Label(root, image=photo, bg='#393E46')
root.whitebg_label.image = photo
root.whitebg_label.place(x=800, y=70)


root.side_image = Image.open('images//LOGINPAGE.png')
photo = ImageTk.PhotoImage(root.side_image)
root.side_image_label = Label(root, image=photo, bg='#393E46')
root.side_image_label.image = photo
root.side_image_label.place(x=280, y=200)

root.txtbg_image = Image.open('images/txtbng2.png')
photo = ImageTk.PhotoImage(root.txtbg_image)
root.side_image_label = Label(root, image=photo, bg='#393E46',bd='0')
root.side_image_label.image = photo
root.side_image_label.place(x=140, y=72)

root.cfms_image = Image.open('images/CFMS (1).png')
photo = ImageTk.PhotoImage(root.cfms_image)
root.side_image_label = Label(root, image=photo, bg='#FD7014')
root.side_image_label.image = photo
root.side_image_label.place(x=180, y=77)


logintextlabel=Label(root,text="🇸‌🇮‌🇬‌🇳‌ 🇮‌🇳‌​", bg="#FD7014", fg="white",
                                    font=("Rockwell", 20, "bold")).place(x=910,y=180)

username_var = tk.StringVar()
password_var = tk.StringVar()
login_status_var = tk.StringVar()

username_entry = tk.Entry(root, textvariable=username_var,  highlightthickness=0, relief=FLAT,bd=0, bg="#FD7014", fg="white",
                                    font=("Helvetica", 12))
username_entry.place(x=855,y=260)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", usertemptext)
username_frame=Frame(root,width=200,height=2,background='white').place(x=855,y=282)

password_entry = tk.Entry(root, textvariable=password_var, highlightthickness=0, relief=FLAT,bd=0, bg="#FD7014", fg="white",
                                    font=("Helvetica", 12))
password_entry.place(x=855,y=320)
password_entry.insert(0,"Password")
password_entry.bind("<FocusIn>", passtemptext)
password_frame=Frame(root,width=200,height=2,background='white').place(x=855,y=342)

closeeye=PhotoImage(file='images/PassVis.png')
eyebutton=Button(root,image=closeeye,bd=0,bg='#FD7014',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(x=1030,y=315)

loginbuttonimg=PhotoImage(file='images/loginbutton (1).png')
login_button = tk.Button(root, image=loginbuttonimg,text="Login", command=check_credentials, bd=0,
                            bg='#FD7014', cursor='hand2', activebackground='#FD7014', fg='white').place(x=905,y=360)
login_status_label = tk.Label(root, textvariable=login_status_var).place(x=800,y=10060)

root.mainloop()