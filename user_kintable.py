# Yamkela Mathontsi class1 mysql EOM

import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Nextof_kinTable")
root.geometry("600x300")
root.resizable(False, False)
root.config(bg="red")

connect = mysql.connector.connect(host="Localhost", user="lifechoices", password="@Lifechoices1234", database="LifeChoices_Online")
conn = connect.cursor()

conn.execute("SELECT * FROM LifeChoices_Nextofkin")

tree=ttk.Treeview(root)

tree['columns'] = ("id","name","surname","cell_num","identity_num")


tree.column("#0", width=0, stretch=NO)
tree.column("id",  width=100, minwidth=50, anchor=tk.CENTER)
tree.column("name", width=120, minwidth=50, anchor=tk.CENTER)
tree.column("surname", width=120, minwidth=50, anchor=tk.CENTER)
tree.column("cell_num", width=120, minwidth=50, anchor=tk.CENTER)
tree.column("identity_num", width=120, minwidth=50, anchor=tk.CENTER)

tree.heading("#0", text="", anchor=tk.CENTER)
tree.heading("id", text="ID" ,anchor=tk.CENTER)
tree.heading("name", text="name" ,anchor=tk.CENTER)
tree.heading("surname", text="surname",anchor=tk.CENTER)
tree.heading("cell_num", text="cell_num" ,anchor=tk.CENTER)
tree.heading("identity_num", text="identity_num" ,anchor=tk.CENTER)



def insert_visitor(name, surname, cell_num, identity_num):
    #   logged_in WILL HAVE ONLY TWO VALUES: 1 AND 0, 1 MEANS LOGGED IN AND 0 MEANS LOGGED OUT
    query = "INSERT INTO LifeChoices_Nextofkin ( name ,surname ,id_number ,phone_number ,logged_in ,time_in ) " \
            "VALUES ( '" + name + "', '" + surname + "', '" + cell_num + "', '" + identity_num + "', '" + str(1) + ");"

    my_cursor = connect.cursor()
    my_cursor.execute(query)

    connect.commit()

def signout():
    msg = messagebox.askquestion("Signing Out ? ", "See you soon")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()


def less():
    msg = messagebox.askquestion("view less?", "userTable")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()
        import usertable

logout = Button(root, text="Signout", command=signout)
logout.place(x=300, y=250)
less = Button(root, text="ViewLess", command=less)
less.place(x=200, y=250)


i = 0
for ro in conn:
    i = i + 1
    tree.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
tree.pack()
root.mainloop()
