from tkinter import *
from tkinter import messagebox
import subprocess
import sqlite3
import re


def reg_save():
    name = name_e.get()
    age = age_e.get()
    contact = cont_e.get()
    
    if name == '' and age == '' and contact == '':
        messagebox.showerror('error','Blank entry not allowed')
        
    # Collect all validation results
    is_valid_name = validate_alpha(name, show_message=False)
    is_valid_age = on_validates(age, show_message=False)
    is_valid_contact = on_validate(contact, show_message=False)
    
    # Check if any validation failed
    if not (is_valid_name and is_valid_age and is_valid_contact):
        messagebox.showerror('Error', 'Incorrect Data Format')
        return
    else:
        
    # # database
    # # create
     connection = sqlite3.connect('register_1.db')

    # cursor made
     mycursor = connection.cursor()
     
     mycursor.execute("""CREATE TABLE IF NOT EXISTS user(
                  userid INTEGER PRIMARY KEY AUTOINCREMENT, 
                  name TEXT, 
                  age INTEGER,
                  contact INTEGER 
      )""")
    
    # insert into table      
     mycursor.execute("INSERT INTO user (name, age, contact) VALUES (?, ?, ?)",(name_e.get(),age_e.get(),cont_e.get()))
     
    # commit changes
     connection.commit()

    # close connection
     connection.close()
     
     show(name_e.get(),age_e.get(),cont_e.get())
      
     name_e.delete(0,END)
     age_e.delete(0,END)
     cont_e.delete(0,END)
      
      
     
def show(name, age, contact):
    
    # # database
    # # create
     connection = sqlite3.connect('register_1.db')

    # cursor made
     mycursor = connection.cursor()

    # insert into table      
     mycursor.execute("SELECT userid FROM user WHERE name=? AND age=? AND contact=?",(name,age,contact))
     result = mycursor.fetchone()
     
     id = result[0]
    # commit changes
     connection.commit()

    # close connection
     connection.close()
    
     var = messagebox.showinfo('resgister','Registered Successfully,\nYour user id is :'+str(id)+"\nPlease save for future reference")
     if var:
       continue_label = Label(frame,text="Click on continue to Login")
       continue_label.place(x="100",y="350")
       
       log_btn = Button(frame,text="login",command=user_log)
       log_btn.place(x="300",y="350")


def user_log():
    subprocess.Popen(['python','USER.py'])

admin_log = Tk()
admin_log.title("REGISTER")
admin_log.geometry("1366x768")
admin_log.configure(bg="#7CC7F9")

# Create a new frame
frame = Frame(admin_log, bg="white")  # Set the background color as needed
frame.place(relx=0.2, rely=0.2, relwidth=0.57, relheight=0.6)   

# # letters and spaces validation
def validate_alpha(name, show_message=True):
    if not name.strip():
        return True
    if re.match(r'^[a-zA-Z\s]+$', name):
        return True
    if show_message:
        messagebox.showerror('Error', 'Invalid name. Please use only letters and spaces.')
    return False
    
alpha = frame.register(validate_alpha)
    
# #  phone number validation
def on_validate(value, show_message=True):
    if not value:
        return True
    if value.isdigit() and len(value) == 10:
        return True
    if show_message:
        messagebox.showerror('Error', 'Please enter a valid 10-digit phone number.')
    return False 

validate_phone = frame.register(on_validate)

# # digit
def on_validates(value, show_message=True):
    if not value:
        return True
    if value.isdigit():
        return True
    if show_message:
        messagebox.showerror('Error', 'Please enter age in digits.')
    return False       

digit = frame.register(on_validates)

header_label = Label(frame, text="REGISTER", font=("times new roman", 20, "bold"),bg="white")
header_label.place(x=300,y=40)
N_label = Label(frame, text="NAME :", font=("times new roman", 18, "bold"),bg="white")
N_label.place(x=160,y=100)
A_label = Label(frame, text="AGE :", font=("times new roman", 18, "bold"),bg="white")
A_label.place(x=160,y=160)
PHN_label = Label(frame, text="CONTACT NO. :", font=("times new roman", 18, "bold"),bg="white")
PHN_label.place(x=160,y=220)


# Create entry fields
name_e = Entry(frame, font=("times new roman", 15, "bold"),bg="#C1E0FA",validate="focusout",validatecommand=(alpha, "%P"))
name_e.place(x=400,y=102)
age_e = Entry(frame, font=("times new roman", 15, "bold"), bg='#C1E0FA',validate="focusout",validatecommand=(digit, "%P"))
age_e.place(x=400,y=162)
cont_e = Entry(frame, font=("times new roman", 15, "bold"), bg='#C1E0FA',validate="focusout",validatecommand=(validate_phone, "%P"))
cont_e.place(x=400,y=222)

# Create login button
reg_but = Button(frame, text="REGISTER", font=("times new roman", 14, "bold"), bg='#b8b6b6', bd=3, command=reg_save)
reg_but.place(x=310,y=300)

admin_log.mainloop()