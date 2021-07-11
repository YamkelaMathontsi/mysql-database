# Yamkela Mathontsi class1 mysql EOM

import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Table")
root.geometry("700x300")
root.resizable(False, False)
root.config(bg="red")


connect = mysql.connector.connect(host="Localhost", user="lifechoices", password="@Lifechoices1234", database="LifeChoices_Online")
conn = connect.cursor()

conn.execute("SELECT * FROM LifeChoices_Online_User_info")

tree=ttk.Treeview(root)

tree['columns'] = ("id","time_in","name","surname","cell_num","identity_num")


tree.column("#0", width=0, stretch=NO)
tree.column("id",  width=60, minwidth=50, anchor=tk.CENTER)
tree.column("time_in", width=150, minwidth=50, anchor=tk.CENTER)
tree.column("name", width=120, minwidth=50, anchor=tk.CENTER)
tree.column("surname", width=120, minwidth=50, anchor=tk.CENTER)
tree.column("cell_num", width=120, minwidth=50, anchor=tk.CENTER)
tree.column("identity_num", width=120, minwidth=50, anchor=tk.CENTER)

tree.heading("#0", text="", anchor=tk.CENTER)
tree.heading("id", text="ID" ,anchor=tk.CENTER)
tree.heading("time_in",text="time_in", anchor=tk.CENTER)
tree.heading("name", text="name" ,anchor=tk.CENTER)
tree.heading("surname", text="surname",anchor=tk.CENTER)
tree.heading("cell_num", text="cell_num" ,anchor=tk.CENTER)
tree.heading("identity_num", text="identity_num" ,anchor=tk.CENTER)



def insert_info(name, surname, cell_num, identity_num):
    #   logged_in WILL HAVE ONLY TWO VALUES: 1 AND 0, 1 MEANS LOGGED IN AND 0 MEANS LOGGED OUT
    query = "INSERT INTO LifeChoices_Online_User_info ( name ,surname ,id_number ,phone_number ) " \
            "VALUES ( '" + name + "', '" + surname + "', '" + cell_num + "', '" + identity_num + "', '" + str(1) + "', curtime() );"

    my_cursor = connect.cursor()
    my_cursor.execute(query)

    connect.commit()

# frame1 = Frame(root)
# frame1.place(x=10, y=50)
#
# Nextofkin = Label(frame1, text="NextOfKin",)
# Nextofkin.place(x=50, y=380)

def signout():
    msg = messagebox.askquestion("Signing Out ? ", "See you soon")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()

def more():
    msg = messagebox.askquestion("view more ? ", "nextofkin")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()
        import user_kintable

logout = Button(root, text="Signout", command=signout)
logout.place(x=150, y=250)
more = Button(root, text="ViewMore", command=more)
more.place(x=10, y=250)


i = 0
for ro in conn:
    i = i + 1
    tree.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
tree.pack()
root.mainloop()
