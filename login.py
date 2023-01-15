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
root.configure(bg='#BAD7E9')

root.whitebg = Image.open('images/whitebg.png')
photo = ImageTk.PhotoImage(root.whitebg)
root.whitebg_label = Label(root, image=photo, bg='#BAD7E9')
root.whitebg_label.image = photo
root.whitebg_label.place(x=800, y=87)

root.whitebg = Image.open('images/login2.png')
photo = ImageTk.PhotoImage(root.whitebg)
root.whitebg_label = Label(root, image=photo, bg='white')
root.whitebg_label.image = photo
root.whitebg_label.place(x=900, y=90)

root.side_image = Image.open('images//LOGINPAGE.png')
photo = ImageTk.PhotoImage(root.side_image)
root.side_image_label = Label(root, image=photo, bg='#BAD7E9')
root.side_image_label.image = photo
root.side_image_label.place(x=100, y=200)

headinglabel=Label(root,text="🇫​🇮​🇳​🇪​ 🇲​🇦​🇳​🇦​🇬​🇪​🇲​🇪​🇳​🇹​ 🇸​🇾​🇸​🇹​🇪​🇲​", bg="#BAD7E9", fg="#ffffff",
                                    font=("Rockwell", 40, "bold")).place(x=430,y=2)

logintextlabel=Label(root,text="𝐋𝐎𝐆𝐈𝐍​", bg="white", fg="black",
                                    font=("Rockwell", 20, "bold")).place(x=910,y=180)

username_var = tk.StringVar()
password_var = tk.StringVar()
login_status_var = tk.StringVar()

username_entry = tk.Entry(root, textvariable=username_var,  highlightthickness=0, relief=FLAT,bd=0, bg="white", fg="#101010",
                                    font=("sans", 12, "bold"))
username_entry.place(x=855,y=260)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", usertemptext)
username_frame=Frame(root,width=200,height=2,background='black').place(x=855,y=282)

password_entry = tk.Entry(root, textvariable=password_var, highlightthickness=0, relief=FLAT,bd=0, bg="white", fg="#101010",
                                    font=("sans", 12, "bold"))
password_entry.place(x=855,y=320)
password_entry.insert(0,"Password")
password_entry.bind("<FocusIn>", passtemptext)
password_frame=Frame(root,width=200,height=2,background='black').place(x=855,y=342)
closeeye=PhotoImage(file='images/PassVis.png')
eyebutton=Button(root,image=closeeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(x=1030,y=315)

login_button = tk.Button(root, text="Login", command=check_credentials,width=25, bd=0,
                            bg='#2B3467', cursor='hand2', activebackground='#3047ff', fg='white').place(x=860,y=360)
login_status_label = tk.Label(root, textvariable=login_status_var).place(x=800,y=10060)

root.mainloop()
