# Yamkela Mathontsi class1 mysql EOM
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Table")
root.geometry("750x500")
root.resizable(False, False)
root.config(bg="tan")


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

nam = Label(root, text="Name:")
nam.place(x=10, y=230)
name_ent = Entry(root, text="")
name_ent.place(x=10, y=250)

suname = Label(root, text="Surname:")
suname.place(x=200, y=230)
surname_ent = Entry(root, text="")
surname_ent.place(x=200, y=250)

cell_num = Label(root, text="cell_num:")
cell_num.place(x=400, y=230)
cell_num_ent = Entry(root, text="")
cell_num_ent.place(x=400, y=250)

id_num = Label(root, text="ID NUMBER:")
id_num.place(x=580, y=230)
identity_ent = Entry(root, text="")
identity_ent.place(x=580, y=250)



def insert_info(name, surname, cell_num, identity_num):
    #   logged_in WILL HAVE ONLY TWO VALUES: 1 AND 0, 1 MEANS LOGGED IN AND 0 MEANS LOGGED OUT
    query = "INSERT INTO LifeChoices_Online_User_info ( name ,surname ,id_number ,phone_number ,logged_in ,time_in ) " \
            "VALUES ( '" + name + "', '" + surname + "', '" + cell_num + "', '" + identity_num + "', '" + str(1) + "', curtime() );"

    my_cursor = connect.cursor()
    my_cursor.execute(query)

    connect.commit()


def signout():
    msg = messagebox.askquestion("Signing Out ? ", "See you soon")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()


def more():
    msg = messagebox.askquestion("view more?", "nextofkin")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()
        import nextofkin_adminonly

def add():
    if name_ent.get() == "" or surname_ent.get() == "" or cell_num_ent.get() == "" or identity_ent.get() == "":
        messagebox.showerror("INVALID", "PLEASE ENTER CORRECT DETAILS")
    else:
            connect = mysql.connector.connect(host="Localhost", user="lifechoices", password="@Lifechoices1234", database="LifeChoices_Online")
            conn = connect.cursor()

            conn.execute("SELECT * FROM LifeChoices_Online_User_info")
            root.destroy()
            import accessofadmin



logout = Button(root, text="Signout", command=signout)
logout.place(x=580, y=300)
details = Button(root, text="details")
details.place(x=150, y=300)
more = Button(root, text="ViewMore", command=more)
more.place(x=10, y=300)
add = Button(root, text="InsertRecord", command=add)
add.place(x=370, y=300)
delete = Button(root, text="delete", command=add)
delete.place(x=260, y=300)



i = 0
for ro in conn:
    i = i + 1
    tree.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
tree.pack()
root.mainloop()
