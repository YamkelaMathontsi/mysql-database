# Yamkela Mathontsi class1 mysql EOM
from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk();
root.title("Login Page")
root.geometry("500x500")
root.config(bg="aqua")
root.resizable(False, False)

photo = PhotoImage(file="lf.png")
pic_label = Label(root, image=photo)
pic_label.place(x=180, y=180)



lb1 = Label(root, text=" USER LOGIN" ,font=("bold", 20), fg="black", bg="white")
lb1.place(x=200, y=10)
lb1 = Label(root, text="Name:", fg="black", bg="white")
lb1.place(x=10, y=50)
lb1Ent = Entry(root, text="")
lb1Ent.place(x=200, y=50)

lb2 = Label(root, text="Password:", fg="black", bg="white")
lb2.place(x=10, y=90)
lb2Ent = Entry(root, text="")
lb2Ent.place(x=200, y=90)

lb2 = Label(root, text="Forgot to Register?", fg="black", bg="white")
lb2.place(x=270, y=130)


def login():
    if lb1Ent.get() == "" or lb2Ent.get() == "":
        root.destroy()
        messagebox.showerror("INVALID", "PLEASE ENTER YOUR DETAILS")
        import userlogin
        root.destroy()


    else:
        msg = messagebox.askquestion("SUCCESSFULLY LOGGED IN", "DO YOU WANT TO CONTINUE")
        if msg == "yes":
            import usertable
            root.destroy()


def register():
    msg = messagebox.askquestion("DO YOU WANT TO GO REGISTER ? ", "leave the LOGIN PAGE?")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN

        root.destroy()
        import registration

def go():
    try:
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1",
                                       database="LifeChoices_Online", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

        if lb1Ent.get() == "" or lb2Ent.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            mycursor.execute('select * from LifeChoices_Nextofkin where name=%s and identity_num=%s',
                             (lb1Ent.get(), lb2Ent.get()))

            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("USER DOES NOT EXIST", "PLEASE REGISTER DETAILS")
                msg = messagebox.askquestion("Error", "TRY AGAIN ?")
                if msg == "yes":
                    root.destroy()
                    import userlogin
            else:
                messagebox.showinfo("SUCCESSFULLY DETAILS", "")
                root.destroy()
                import usertable


    except ValueError:
        messagebox.showerror("OOPS", "INVALID NAME OR ID")
        lb1Ent.delete(0, END)
        lb2Ent.delete(0, END)
        lb1Ent.focus()







login = Button(root, text="FINISH", command=go)
login.place(x=10, y=150)

register = Button(root, text="REGISTER", command=go)
register.place(x=270, y=150)



root.mainloop()
