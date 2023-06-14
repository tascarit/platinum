import random

x = ''
chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789._-+=,*#&"
for i in range(64):
    random_char = random.choice(chars)
    x += random_char
