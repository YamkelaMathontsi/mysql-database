# Yamkela Mathontsi class1 mysql EOM
from tkinter import *
import mysql.connector
from datetime import *
from tkinter import messagebox
import rsaidnumber
import re

root = Tk();
root.title("Registration Page")
root.geometry("500x500")
root.config(bg="lightblue")
root.resizable(False, False)


now = datetime.now()

mydb = mysql.connector.connect(
    host="localhost",
    user="lifechoices",
    password="@Lifechoices1234",
    database="LifeChoices_Online"
)

photo = PhotoImage(file="lf.png")
pic_label = Label(root, image=photo)
pic_label.place(x=120, y=200)


heading = Label(root, text="Registration",font=("bold", 20))
heading.place(x=200, y=10)


name = Label(root, text="Name:")
name.place(x=10, y=50)
name_ent = Entry(root, text="")
name_ent.place(x=200, y=50)

suname = Label(root, text="Surname:")
suname.place(x=10, y=90)
surname_ent = Entry(root, text="")
surname_ent.place(x=200, y=90)

cell_num = Label(root, text="cell_num:")
cell_num.place(x=10, y=130)
cell_num_ent = Entry(root, text="")
cell_num_ent.place(x=200, y=130)

id_num = Label(root, text="ID NUMBER:")
id_num.place(x=10, y=170)
identity_ent = Entry(root, text="")
identity_ent.place(x=200, y=170)


def register():
    if name_ent.get() == "" or surname_ent.get() == "" or cell_num_ent.get() == "" or identity_ent.get() == "":
        messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")

    if identity_ent == rsaidnumber.parse(identity_ent.get()):
        messagebox.showinfo("INVALID", "Please Enter A Valid 13 Digit ID Number")
    #     messagebox.showerror("INVALID", "PLEASE ENTER PROPER ID NUMBER")



    else:
            cursor = mydb.cursor()
            # conn.execute("SELECT * FROM LifeChoices_Online_User_info")
            sql = (
            "INSERT INTO LifeChoices_Online_User_info (name, surname, cell_num, identity_num)"
            "VALUES (%s, %s, %s, %s)"
)
            #data = (x, y, z, m)
            data = (name_ent.get(), surname_ent.get(), cell_num_ent.get(), identity_ent.get())
            cursor.execute(sql, data)

            mydb.commit()
            # messagebox.showerror()
            root.destroy()
            import addinfo


register = Button(root, text="NEXT", command=register)
register.place(x=10, y=200)


root.mainloop()
