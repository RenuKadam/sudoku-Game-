from tkinter import *
from tkinter import messagebox
import subprocess
import sqlite3
import sys

global userid
userid = sys.argv[1]
print(userid)

root = Tk()
root.title("User mode")
root.geometry("650x500")
root.configure(bg="#30613b")

def play():
    subprocess.Popen(['python','new.py',str(userid)])
    
def score_board():
    display_win = Tk()
    display_win.title("Display Data")
    display_win.geometry("400x500")

    #databases
    # create a db or connect to one 
    connection = sqlite3.connect('sudoku.db')

    # cursor made
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT * FROM game WHERE userid=?",(userid))
    records = mycursor.fetchall()
    
    header_label = Label(display_win, text="SUDOKU SCOREBOARD", font=("times new roman", 14, "bold"))
    header_label.grid(row=0,columnspan=20)
    
    # Manually specify column names
    columns = ['gameid', 'userid', 'score','Time Remaining']
    
    k=0
    for column in columns:
        header = Label(display_win, width=13, fg="black", text=column, anchor="center" )
        header.grid(row=1,column=k)
        k=k+1
        
    i=2
    for record in records:
        for j in range(len(record)):
          e= Label(display_win, width=13,fg="blue",text=record[j], anchor="center")
          e.grid(row=i,column=j)
        i=i+1
        
    # commit changes
    connection.commit()

    # close connection
    connection.close()
    display_win.mainloop()
       
header_label = Label(root, text="SUDOKU GAME", font=("times new roman", 23, "bold"),fg="white",bg="#30613b")
header_label.place(x=210,y=10)

# Create login button
add_but = Button(root, text="PLAY GAME", font=("times new roman", 14, "bold"), bg='white', bd=3,command=play)
add_but.place(x=270,y=140)

add_but = Button(root, text="SCORE BOARD", font=("times new roman", 14, "bold"), bg='white', bd=3,command=score_board)
add_but.place(x=260,y=240)


root.mainloop()