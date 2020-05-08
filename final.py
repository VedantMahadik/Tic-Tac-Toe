from tkinter import *
from tkinter import messagebox 
import random as r

def button(frame):
    # relief is the way button looks
    b = Button(frame, padx= 1, bg= "light yellow", width= 3, text= " ", font= ('arial', 50, 'bold'),relief= "groove", bd= 10)
    return b

    # Functions

def change_user():
    global user
    for i in ['O', 'X']:
        if (i != user):
            user = i
            break

def reset():
    global user
    for i in range(3):
        for j in range(3):
            b[i][j]["text"] = " "         # Changes all elements to ' '
            b[i][j]["state"] = NORMAL     # Changes state of buttons from disabled to normal
            b[i][j]["relief"] = "groove"
    user =r.choice(['O', 'X'])            # Restart loop with a random user



def check():
    # Horizontal or vertical line check
    for i in range (3):
        if(b[i][0]["text"]== b[i][1]["text"]== b[i][2]["text"]== user or b[0][i]["text"]== b[1][i]["text"]== b[2][i]["text"]== user):
            messagebox.showinfo("CONGRATULATIONS " , user + " HAS WON!")
            reset()

    # Diagonal check
    if(b[0][0]["text"]== b[1][1]["text"]== b[2][2]["text"]== user or b[0][2]["text"]== b[1][1]["text"]== b[2][0]["text"]== user ):
        messagebox.showinfo("CONGRATULATIONS " , user + " HAS WON!")
        reset()
    
    # Tie case
    if(b[0][0]["state"]== b[0][1]["state"]== b[0][2]["state"]== b[1][0]["state"]== b[1][1]["state"]== b[1][2]["state"]== b[2][0]["state"]== b[2][1]["state"]== b[2][2]["state"]== DISABLED):
        messagebox.showinfo("Tie", "THE MATCH ENDED WITH A TIE")
        reset()

def click(row, col):
    b[row][col].config(text= user, state= DISABLED, relief= "sunken", disabledforeground=colour[user])
    check()
    change_user()
    label.config(text = user +"'s turn")

# Main loop

root = Tk()
root.title("TIC-TAC-TOE")
user= r.choice(['O', 'X'])

colour = {'O':"deep sky blue", 'X':"red"}

b=[[], [], []]    # Initialize 3X3 array system

for i in range(3):
    for j in range(3):
        b[i].append(button(root))
        b[i][j].config(command= lambda row=i,col=j:click(row,col))
        b[i][j].grid(row=i,column=j)

label =Label(text= user + "'s Turn", font=('arial', 20, "bold"))
label.grid(row=3,column=0,columnspan=3)

root.mainloop()