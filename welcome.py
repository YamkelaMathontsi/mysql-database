# Yamkela Mathontsi class1 mysql EOM
from tkinter import *
from tkinter import messagebox


root = Tk();
root.title("Welcome Page")
root.geometry("700x700")
root.config(bg="blue")
root.resizable(False, False)

photo = PhotoImage(file="lf.png")
pic_label = Label(root, image=photo)
pic_label.place(x=200, y=110)


frame_left = Frame(root, width=200, height=100, bg="#346ab3")
frame_left.place(x=150, y=10)
title1 = Label(frame_left, text="WELCOME TO", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
title1.place(x=5, y=10)

frame_right = Frame(root, width=200, height=100, bg="#9ccb3b")
frame_right.place(x=350, y=10)
title2 = Label(frame_right, text="LIFE CHOICES", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
title2.place(x=5, y=10)

frame_bottom1= Frame(root, width=200, height=100, bg="#9ccb3b")
frame_bottom1.place(x=150, y=203)
title3 = Label(frame_bottom1, text="SELECT", font=("Ariel", 20), bg="#9ccb3b", fg="#346ab3")
title3.place(x=50, y=10)


frame_bottom2 = Frame(root, width=200, height=100, bg="#346ab3")
frame_bottom2.place(x=350, y=203)
title4 = Label(frame_bottom2, text="ONE", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
title4.place(x=70, y=10)

# title5 = Label(frame_bottom2, text="OR", font=("Ariel", 20), bg="black", fg="#346ab3")
# title5.place(y=70)

frame_bottom2 = Frame(root, width=200, height=100, bg="#346ab3")
frame_bottom2.place(x=350, y=203)
title4 = Label(frame_bottom2, text="ONE", font=("Ariel", 20), bg="#346ab3", fg="#9ccb3b")
title4.place(x=70, y=10)

def admin():
    msg = messagebox.askquestion("ADMIN OF LIFECHOICES ? ", "WELCOME BACK ADMIN")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()
        import admin_login


def register():
    msg = messagebox.askquestion("DO YOU WANT TO GO REGISTER ? ", "LEAVING THE HOME PAGE?")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()
        import registration


def login():
    msg = messagebox.askquestion("REGISTERED ALREADY? ", "WELCOME BACK?")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()
        import userlogin


admin = Button(root, text="admin", command=admin,bg="#9ccb3b", font=("bold", 20))
admin.place(x=280,y=300)

register = Button(root, text="register", command=register,bg="#9ccb3b", font=("bold", 20))
register.place(x=190, y=250)

login = Button(root, text="login", command=login,bg="#346ab3", font=("bold", 20))
login.place(x=410, y=250)



root.mainloop()
