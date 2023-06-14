import socket
import sqlite3
import random

sql = sqlite3.connect('users.db')
cur = sql.cursor()
con = cur.connection

def on_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    userid INT,
    xfingerprint TEXT,
    password TEXT,
    email TEXT,
    isemailverified INT,
    avatarid INT,
    islocked INT,
    phone TEXT
    )""")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost", 9999))
sock.listen(1)

conn, attr = sock.accept()

while True:
    data = conn.recv(1024).decode().strip()
    print(data)

    if "register?" in data:
        last_index = open("index.txt", "r+").read()
        index, login, passw, email = data.split("|")
        x = ''
        chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789._-+=,*#&"
        for i in range(64):
            random_char = random.choice(chars)
            x += random_char

        try:

            cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(login), int(last_index), str(x), str(passw), str(email), 0, 0, 0, None))
            con.commit()
            conn.send("valid".encode())

        except Exception:

            conn.send("invalid".encode())

    if "on_email_login?" in data:

        index, email, passw = data.split("|")

        try:
            userid = cur.execute("SELECT userid WHERE email = ? AND passw = ?", (str(email), str(passw), )).fetchone()[0]
            if userid is not None or str(userid) != "":
                conn.send("valid".encode())
            else:
                conn.send("invalid".encode())

        except Exception:
            conn.send("invalid".encode())
        
    if "on_uname_login?" in data:

        index, login, passw = data.split("|")

        try:
            userid = cur.execute("SELECT userid WHERE email = ? AND passw = ?", (str(login), str(passw), )).fetchone()[0]
            if userid is not None or str(userid) != "":
                conn.send("valid".encode())
            else:
                conn.send("invalid".encode())

        except Exception:
            conn.send("invalid".encode())

    
