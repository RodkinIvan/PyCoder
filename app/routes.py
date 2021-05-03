from app import app
from flask import render_template
from ctypes import *
from Autocoder.Autocoder import Autocoder


a = Autocoder(8, 5)
a.learn('Ohayo')
code = a.encode('Ohayo')
print(a.decode(code))
# lib.print(code)
# print(code.decode('utf-8'))
# decode = lib.decode(a, code)
# print(decode.decode('utf-8'))
# print((lib.stupid_function('I\'m so stupid!'.encode('utf-8')).decode('utf-8')))


@app.route('/')
def start():
    return render_template('main_page.html')
