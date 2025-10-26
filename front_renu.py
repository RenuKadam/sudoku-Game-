import tkinter
from tkinter import *
import subprocess


def register_pg():
    subprocess.Popen(['python','register.py'])
    root.destroy()

def admin_pg():
    subprocess.Popen(['PYTHON','admin.py'])
    root.destroy()

def user_pg():
    subprocess.Popen(['python','USER.py'])
    root.destroy() 

root = Tk()
root.title("Suduko Game")
root.geometry("1500x900")

header = Label(root,text="SUDUKO GAME",font=("Arail",23,"bold"),bg="green")
header.place(x="600",y="5")

rules = Label(root,text="RULES FOR SUDUKO :-",font=("Arail",15,"bold"))
rules.place(x="30",y="50")

rules_line1 = Label(root, text="1. Each row must contain all numbers from 1 to 9, with no repetition.",font=("Arial",14,"bold"),fg="blue")
rules_line1.place(x="50",y="100")

rules_line1 = Label(root, text="2. Each column must contain all numbers from 1 to 9, with no repetition.",font=("Arial",14,"bold"),fg="blue")
rules_line1.place(x="50",y="140")

rules_line1 = Label(root, text="3. Each 3x3 box (subgrid) must contain all numbers from 1 to 9, with no repetition.",font=("Arial",14,"bold"),fg="blue")
rules_line1.place(x="50",y="180")

new_user = Label(root,text="If new user please register , else login",font=("Arial",14,"bold"))
new_user.place(x="30",y="240")

reg_btn = Button(root, text="Register",font=("Arial",14,"bold"),bg="#9CF2BA",command=register_pg)
reg_btn.place(x="400",y="235")

log = Label(root,text="Login as : ",font=("Arial",17,"bold"))
log.place(x="660",y="340")

admin_btn = Button(root, text="Admin Login",font=("Arial",18,"bold"),bg="#C293F5",command=admin_pg)
admin_btn.place(x="640",y="400")

user_btn = Button(root, text="User Login",font=("Arial",18,"bold"),bg="#C293F5",command=user_pg)
user_btn.place(x="650",y="550")


root.mainloop()