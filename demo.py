import bcrypt

password = b'Thisismypassword'
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

entered_password = input('Enter your password:')
entered_password = bytes(entered_password, encoding='utf-8')
if bcrypt.checkpw(entered_password, hashed):
    print('Login Successful')
else:
    print('Incorrect Password')