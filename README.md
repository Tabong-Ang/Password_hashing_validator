# 🔐 Password Validation App (Tkinter + bcrypt)

A simple desktop GUI application built with Python and Tkinter that validates a user's password against a securely hashed value using `bcrypt`.

---

## 🚀 Features

- 🧠 Password input via a clean Tkinter interface
- 🔒 Secure password verification using `bcrypt`
- ✅ Success and error feedback via message boxes
- 🎨 Styled UI with custom fonts and colors

---

## 🛠️ Installation

### Requirements

- Python 3.10+
- Required libraries:
  - `tkinter` (built-in)
  - `bcrypt`

Install `bcrypt` via pip:

```bash
pip install bcrypt

📦 Usage
1. Clone or download the project.

2. Run the script:
python app.py

3. Enter a password in the input field.
4. Click Validate to check if it matches the stored hash.

🔐 Security Notes
The hashed password is hardcoded in the script:
hash = b'$2b$12$t7uxThk3mnj.sUVETGLIcux874fxXlaovqWhOF3vryrxCc7uk/Zna'
This hash corresponds to a specific plaintext password (e.g., "admin123").

To generate your own hash:
import bcrypt
password = b"your_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

Replace the hardcoded hash with your own for production use.

📁 Project Structure
demo.py
password_validator.py
README.md

👤 Author
Tabong 
Python Developer | GUI Designer | Security Enthusiast 
📍 Kumba, Cameroon
email: tabongphilip@gmail.com
Tel: +(237) 675 552 594
website: www.philipstek.com

📜 License
This project is open-source and free to use for educational and personal purposes.

