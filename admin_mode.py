from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root.title("admin mode")
root.geometry("650x500")
root.configure(bg="#30613b")

def players():
    display_win = Tk()
    display_win.title("Display Data")
    display_win.geometry("480x700")

    #databases
    # create a db or connect to one 
    connection = sqlite3.connect('register_1.db')

    # cursor made
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT * FROM user")
    records = mycursor.fetchall()
    
    head = Label(display_win, text="PLAYERS DETAILS",anchor="center",font=("Arial",20,"bold"))
    head.grid(row=0,columnspan=16)
    
     # Manually specify column names
    columns = ['userid', 'name', 'age', 'contact']
    
    k=0
    for column in columns:
        header = Label(display_win, width=13, fg="black", text=column, anchor="center" )
        header.grid(row=1,column=k)
        k=k+1
        
    i=2
    for record in records:
        for j in range(len(record)):
          e=Label(display_win, width=13,fg="blue",text=record[j], anchor="center")
          e.grid(row=i,column=j)
        i=i+1
        
    # commit changes
    connection.commit()

    # close connection
    connection.close()
    
    
    
def score_board():
    display_win = Tk()
    display_win.title("Display Data")
    display_win.geometry("550x500")

    #databases
    # create a db or connect to one 
    connection = sqlite3.connect('sudoku.db')

    # cursor made
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT * FROM game")
    records = mycursor.fetchall()
    
     # Manually specify column names
    columns = ['gameid', 'userid', 'score','Time Remaining ']
    
    k=0
    for column in columns:
        header = Label(display_win, width=13, fg="black", text=column, anchor="center" )
        header.grid(row=0,column=k)
        k=k+1
        
    i=1
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
    
def delete():
     global display_win1        
     display_win1 = Tk()
     display_win1.title("SUDOKU")
     display_win1.geometry("450x650")
     # database
     # create a db or connect to one 
     connection = sqlite3.connect('register_1.db')
     # cursor made
     mycursor = connection.cursor()
    
     mycursor.execute("SELECT * FROM user")
     records = mycursor.fetchall()
    
     head = Label(display_win1, text="PLAYERS DETAILS",anchor="center",font=("Arial",20,"bold"))
     head.grid(row=0,columnspan=14)
     
     # column names
     columns = ['User Id', 'Name' ,'Age', 'Contact']

     k=0
     for column in columns:
        header = Label(display_win1, width=12, fg="black", text=column, anchor="center", font=("Arial",10,"bold") )
        header.grid(row=1,column=k)
        k=k+1
        
     i=2
     for record in records:
        for j in range(len(record)):
           e=Label(display_win1, width=12,fg="blue",text=record[j], anchor="center",font=("Arial",10,"bold"))
           e.grid(row=i,column=j)
        # adding delete sign to button in each row
        f=Button(display_win1,text="X",bg="red",fg="white",command=lambda d=record[0], fid=record[2]: del_record(d,fid),font=("Arial", 10))
        f.grid(row=i,column=j+1)
        i=i+1
        
     # commit changes
     connection.commit()
    
     # close connection
     connection.close()
     
     display_win1.mainloop()

def del_record(bid,fid):
    global display_win1 
    var = messagebox.askyesnocancel(master = display_win1, title="Delete ?",message="Delete Record of Booking Id : "+ str(bid),icon="warning",default="no")
    if var:
       # create a db or connect to one 
       connection = sqlite3.connect('register_1.db')
       # cursor made
       mycursor = connection.cursor()
    
       result = mycursor.execute("DELETE FROM user WHERE userid="+ str(bid))
       messagebox.showerror(master= display_win1, title="Deleted",message="No. of records deleted: "+ str(result.rowcount)) 
       
       # commit changes
       connection.commit()
    
       # close connection
       connection.close()
       
       display_win1.destroy()
            
       delete()
       
       display_win1.mainloop()
       
header_label = Label(root, text="SUDOKU GAME", font=("times new roman", 23, "bold"),fg="white",bg="#30613b")
header_label.place(x=210,y=10)

# Create login button
add_but = Button(root, text="VIEW PLAYERS", font=("times new roman", 14, "bold"), bg='white', bd=3,command=players)
add_but.place(x=270,y=140)

add_but = Button(root, text="DELETE PLAYERS", font=("times new roman", 14, "bold"), bg='white', bd=3,command=delete)
add_but.place(x=260,y=240)

view_but = Button(root, text="VIEW SCOREBOARD", font=("times new roman", 14, "bold"), bg='white', bd=3,command=score_board)
view_but.place(x=250,y=340)


root.mainloop()