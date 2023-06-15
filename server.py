import socket
import sqlite3
import random

sql = sqlite3.connect('users.db')
cur = sql.cursor()
con = cur.connection


cur.execute("""CREATE TABLE IF NOT EXISTS users(
username TEXT,
userid INT,
xfingerprint TEXT,
password TEXT,
email TEXT,
isemailverified INT,
avatarid INT,
islocked INT,
phone TEXT,
status TEXT,
badges TEXT,
about TEXT
)""")
            
print("table checked")

ip = "localhost"
port = 9996


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((ip, port))
sock.listen(0)

print("socket started at {}:{}".format(ip, port))

while True:
    conn, attr = sock.accept()

    data = conn.recv(2048).decode()

    if "register?" in data:
        last_index_raw = open("index.txt", "w")
        last_index = last_index_raw.read()
        index, login, passw, email = data.split("|")
        x = ''
        chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789._-+=,*#&"
        for i in range(64):
            random_char = random.choice(chars)
            x += random_char

        try:
            check1 = cur.execute("SELECT userid FROM users WHERE username = ? OR email = ?", (str(login), str(email), )).fetchone()[0]

            if check1 is not None or str(check1) != "":
                conn.send("exists".encode())

        except Exception or TypeError:

            cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(login), int(last_index), str(x), str(passw), str(email), 0, 0, 0, None, None, None, None))
            con.commit()
            last_index_raw.write(str(int(int(last_index) + 1)))
            conn.send("valid".encode())


    elif "on_email_login?" in data:

        index, email, passw = data.split("|")

        try:
            userid = cur.execute("SELECT userid FROM users WHERE email = ? AND password = ?", (str(email), str(passw), )).fetchone()[0]
            if userid is not None:
                conn.send("valid".encode())
            else:
                conn.send("invalid".encode())

        except Exception:
            conn.send("invalid".encode())
        
    elif "on_uname_login?" in data:

        index, login, passw = data.split("|")

        try:

            userid = cur.execute("SELECT userid FROM users WHERE username = ? AND password = ?", (str(login), str(passw), )).fetchone()[0]
            if userid is not None:
                conn.send("valid".encode())
            else:
                conn.send("invalid".encode())
        except Exception:
            conn.send("invalid".encode())

    elif "get_xf?" in data:

        index, login, passw = data.split("|")

        try:

            xf = cur.execute("SELECT xfingerprint FROM users WHERE username = ? AND password = ?", (str(login), str(passw), )).fetchone()[0]

            if xf is not None:
                conn.send(str(xf).encode())
            else:
                conn.send("invalid".encode())

        except Exception:
            conn.send("invalid".encode())

    elif "check_xf?" in data:

        index, xf = data.split("|")

        try:

            userid = cur.execute("SELECT userid FROM users WHERE xfingerprint = ?", (str(xf), )).fetchone()[0]

            if userid is not None:
                conn.send("valid".encode())
            else:
                conn.send("invalid".encode())

        except Exception:
            conn.send("invalid".encode())

    elif "get_username?" in data:
        index, xf = data.split("|")

        try:

            username = cur.execute("SELECT username FROM users WHERE xfingerprint = ?", (str(xf), )).fetchone()[0]
            email = cur.execute("SELECT email FROM users WHERE xfingerprint = ?", (str(xf), )).fetchone()[0]
            avatar_id = cur.execute("SELECT avatarid FROM users WHERE xfingerprint = ?", (str(xf), )).fetchone()[0]

            if username is not None and email is not None:
                bytes_string = username + "|" + email
                conn.send(bytes_string.encode())
            elif username is None and email is not None:
                bytes_string = "error_username_fail" + "|" + email
                conn.send(bytes_string.encode())
            elif username is not None and email is None:
                bytes_string = username + "|" + "error_email_fail"
                conn.send(bytes_string.encode())
            elif username is None and email is None:
                bytes_string = "error_username_fail" + "|" + "error_email_fail"
                conn.send(bytes_string.encode())
        except Exception:
            conn.send("error_username_fail".encode())

    elif "get_profile_attrs?" in data:
        index, xf = data.split("|")

        try:

            status = cur.execute("SELECT status FROM users WHERE xfingerprint = ?", (str(xf), )).fetchone()[0]
            badges = cur.execute("SELECT badges FROM users WHERE xfingerprint = ?", (str(xf), )).fetchone()[0]
            about = cur.execute("SELECT about FROM users WHERE xfingerprint = ?", (str(xf), )).fetchone()[0]

            if status is not None and badges is not None and about is not None:
                bytes_string = status + "|" + badges + "|" + about
                conn.send(bytes_string.encode())
            elif status is None and badges is not None and about is not None:
                bytes_string = "None" + "|" + badges + "|" + about
                conn.send(bytes_string.encode())
            elif status is not None and badges is None and about is not None:
                bytes_string = status + "|" + "None" + "|" + about
                conn.send(bytes_string.encode())
            elif status is None and badges is None and about is not None:
                bytes_string = "None" + "|" + "None" + "|" + about
                conn.send(bytes_string.encode())
            elif status is None and badges is None and about is None:
                bytes_string = "None" + "|" + "None" + "|" + "None"
                conn.send(bytes_string.encode())
            elif status is None and badges is not None and about is None:
                bytes_string = "None" + "|" + badges + "|" + "None"
                conn.send(bytes_string.encode())
            elif status is not None and badges is not None and about is None:
                bytes_string = status + "|" + badges + "|" + "None"
                conn.send(bytes_string.encode())

        except Exception:
            conn.send("invalid".encode())


    
