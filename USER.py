from tkinter import *
from tkinter import messagebox
import subprocess
import sqlite3

userroot = Tk()
userroot.title("User Login")
userroot.geometry("1366x768")
userroot.configure(bg="#F9B474")

# Create a new frame
frame = Frame(userroot, bg="white")  
frame.place(relx=0.25, rely=0.15, relwidth=0.57, relheight=0.6)


def login():
    username = user.get()
    password = passw.get()
    
    #database access 
    # create a db or connect to one 
    connection = sqlite3.connect('register_1.db')

    # cursor made
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT name FROM user WHERE userid=?",(user.get(),))
    res = mycursor.fetchone()
    if res is None:
        messagebox.showerror("login","Invalid USER ID")
    else:
      result = res[0]

      if password == result:
        var = messagebox.showinfo('login', 'Login Successfully')
        if var:
           user_mode()
        elif username == '' and password == '':
          messagebox.showerror('login', 'Blank user ID and name not allowed')
        else:
          messagebox.showerror('login', 'Incorrect User ID and name')
       
    # commit changes
    connection.commit()

     # close connection
    connection.close()

def register():
    subprocess.Popen(['python','register.py'])
    userroot.destroy()

def user_mode():
    subprocess.Popen(['python','user_mode.py',user.get()])
    userroot.destroy()
    
# number validation
def validate_numeric(value):
    if not value:
        return True 
    if not value.isdigit():
        messagebox.showerror('Error', 'Please enter a valid numeric value.')
        return False
    return True

numeric = frame.register(validate_numeric)

# Password 
def validate_password(value):
    if not value:
        return True 

    if len(value) < 6:
        messagebox.showerror('Error', 'Password too short. Must be at least 6 characters.')
        return False

    has_digit = False
    for char in value:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        messagebox.showerror('Error', 'Password must include a number.')
        return False

    has_upper = False
    for char in value:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        messagebox.showerror('Error', 'Password must include an uppercase letter.')
        return False
    
    has_lower = False
    for char in value:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        messagebox.showerror('Error', 'Password must include a lowercase letter.')
        return False

    special_characters = "@#$%^&_*"
    has_special = False
    for char in value:
        if char in special_characters:
            has_special = True
            break
    if not has_special:
        messagebox.showerror('Error', 'Password must include a special character (@, #, $, %, ^, &).')
        return False

    return True

password_valid = frame.register(validate_password)

#label   
header_label = Label(frame, text="USER LOGIN PAGE", font=("times new roman", 20, "bold"),bg="white")
header_label.place(x=260,y=40)
user_label = Label(frame, text="USER ID :", font=("times new roman", 18, "bold"),bg="white")
user_label.place(x=160,y=150)
pass_label = Label(frame, text="NAME :", font=("times new roman", 18, "bold"),bg="white")
pass_label.place(x=160,y=250)

# Entry
user = Entry(frame, font=("times new roman", 15, "bold"),bg="#f7e1e6",validate="focusout", validatecommand=(numeric,'%P'))
user.place(x=400,y=152)
passw = Entry(frame, font=("times new roman", 15, "bold"), bg='#f7e1e6')
passw.place(x=400,y=252)

# Buttons
log_but = Button(frame, text="LOGIN", font=("times new roman", 14, "bold"), bg='#f7e1e6', bd=3, command=login)
log_but.place(x=310,y=340)
reg_label = Label(frame, text="If new user , please register by clicking on register. ",font=("times new roman", 14, "bold"),bg="white")
reg_label.place(x=100,y=400)
reg_btn = Button(frame, text="Register", font=("times new roman", 15, "bold"), bd=3 , bg='#f7e1e6', command=register)
reg_btn.place(x=550,y=390)

userroot.mainloop()
