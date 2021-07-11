# Yamkela Mathontsi class1 mysql EOM
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Nextof_kinTable")
root.geometry("800x400")
root.resizable(False, False)
root.config(bg="tan")


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
id_num.place(x=600, y=230)
identity_ent = Entry(root, text="")
identity_ent.place(x=600, y=250)



def insert_visitor(name, surname, cell_num, identity_num):
    #   logged_in WILL HAVE ONLY TWO VALUES: 1 AND 0, 1 MEANS LOGGED IN AND 0 MEANS LOGGED OUT
    query = "INSERT INTO LifeChoices_Nextofkin ( name ,surname ,id_number ,phone_number ,logged_in ,time_in ) " \
            "VALUES ( '" + name + "', '" + surname + "', '" + cell_num + "', '" + identity_num + "', '" + str(1) + ");"

    conn = connect.cursor()
    conn.execute(query)

    connect.commit()



def less():
    msg = messagebox.askquestion("view less?", "users logged in")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()
        import adminonly


def finish():

    if name_ent.get() == "" or surname_ent.get() == "" or cell_num_ent.get() == "" or identity_ent.get() == "":
        messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")

    else:
            conn = connect.cursor()
            # conn.execute("SELECT * FROM LifeChoices_Online_User_info")
            sql = (
            "INSERT INTO LifeChoices_Nextofkin (name, surname, cell_num, identity_num)"
            "VALUES (%s, %s, %s, %s)"
)
            #data = (x, y, z, m)
            data = (name_ent.get(), surname_ent.get(), cell_num_ent.get(), identity_ent.get())
            conn.execute(sql, data)

            connect.commit()
            # messagebox.showerror()
            root.destroy()
            import adminonly

add = Button(root, text="InsertRecord", command=finish)
add.place(x=250, y=300)
delete = Button(root, text="delete")
delete.place(x=150, y=300)
less = Button(root, text="ViewLess", command=less)
less.place(x=10, y=300)



i = 0
for ro in conn:
    i = i + 1
    tree.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
tree.pack()
root.mainloop()
