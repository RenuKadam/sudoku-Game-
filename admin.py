from tkinter import *
from tkinter import messagebox
import subprocess

def admin_mode():
    global admin_log
    admin_log.destroy()
    subprocess.Popen(['python','admin_mode.py'])
    
def login():
    username = user.get()
    password = passw.get()
    
    if username == 'admin' and password == 'admin123':
        var = messagebox.showinfo('Admin login', 'Login Successfully')
        if var:
            admin_mode()
    elif username == '' and password == '':
        messagebox.showerror('Admin login', 'Blank username and password not allowed')
    else:
        messagebox.showerror('Admin login', 'Incorrect Username and Password')

admin_log = Tk()
admin_log.title("Admin Login")
admin_log.geometry("1366x768")
admin_log.configure(bg="#F9B474")

# Create a new frame
frame = Frame(admin_log, bg="white")  # Set the background color as needed
frame.place(relx=0.2, rely=0.2, relwidth=0.57, relheight=0.6)

header_label = Label(frame, text="ADMIN LOGIN PAGE", font=("times new roman", 20, "bold"),bg="white")
header_label.place(x=260,y=40)
user_label = Label(frame, text="USERNAME :", font=("times new roman", 18, "bold"),bg="white")
user_label.place(x=160,y=150)
pass_label = Label(frame, text="PASSWORD :", font=("times new roman", 18, "bold"),bg="white")
pass_label.place(x=160,y=250)

# Create entry fields
user = Entry(frame, font=("times new roman", 15, "bold"),bg="#b8b6b6" )
user.place(x=400,y=152)
passw = Entry(frame, font=("times new roman", 15, "bold"), show='*', bg='#b8b6b6')
passw.place(x=400,y=252)

# Create login button
log_but = Button(frame, text="LOGIN", font=("times new roman", 14, "bold"), bg='#b8b6b6', bd=3, command=login)
log_but.place(x=310,y=340)

admin_log.mainloop()
