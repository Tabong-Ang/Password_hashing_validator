from tkinter import *
import bcrypt
from tkinter import messagebox


root = Tk()
root.geometry('600x400')

def validate(password):
    hash = b'$2b$12$t7uxThk3mnj.sUVETGLIcux874fxXlaovqWhOF3vryrxCc7uk/Zna'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        messagebox.showinfo(title='Information', message='Login Successful')
    else:
        messagebox.showinfo(title='Information', message='Incorrect Password')

password_label = Label(root, text='Enter your password below to validate', 
                       font=('Arial', 13, 'bold'))
password_label.place(x=150, y=70)

password_entry = Entry(root, highlightbackground='blue', highlightthickness=2)
password_entry.place(x=250, y=100)

btn = Button(text='Validate', command=lambda: validate(password_entry.get()),
             bg='blue', fg='white', font=('Arial', 13, 'bold'))
btn.place(x=270, y=140)


root.mainloop()