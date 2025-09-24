from tkinter import *
import bcrypt
from tkinter import messagebox

# Initialize main window
root = Tk()
root.title("Secure Login")
root.geometry("600x400")
root.configure(bg="#f0f4f8")
root.resizable(True, True)

# Configure grid for responsiveness
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frame to center content
main_frame = Frame(root, bg="#ffffff", bd=2, relief=RIDGE)
main_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Validation function
def validate(password):
    stored_hash = b'$2b$12$t7uxThk3mnj.sUVETGLIcux874fxXlaovqWhOF3vryrxCc7uk/Zna'
    password_bytes = password.encode('utf-8')
    if bcrypt.checkpw(password_bytes, stored_hash):
        messagebox.showinfo(title='Login Status', message='✅ Login Successful')
    else:
        messagebox.showerror(title='Login Status', message='❌ Incorrect Password')

# Heading
heading = Label(main_frame, text="🔐 Password Validation", font=("Arial", 18, "bold"), bg="#ffffff", fg="#273b7a")
heading.pack(pady=(20, 10))

# Instruction
instruction = Label(main_frame, text="Enter your password below to validate", font=("Arial", 13), bg="#ffffff")
instruction.pack(pady=(0, 20))

# Entry field
password_entry = Entry(main_frame, font=("Arial", 13), show="*", width=30, bd=2, relief=SOLID)
password_entry.pack(pady=10)

# Validate button
validate_btn = Button(main_frame, text="Validate", font=("Arial", 13, "bold"), bg="#273b7a", fg="white",
                      activebackground="#1e2f5a", activeforeground="white",
                      command=lambda: validate(password_entry.get()))
validate_btn.pack(pady=20)

# Footer
footer = Label(root, text="© 2025 Tabong | Student Systems", font=("Arial", 10), bg="#f0f4f8", fg="#888")
footer.grid(row=1, column=0, pady=10)

# Run the app
root.mainloop()
