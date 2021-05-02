from app import app
from flask import render_template
from ctypes import *
from Autocoder import Autocoder


lib = Autocoder.lib
a = lib.createAutocoder(c_int(8), c_int(8))
lib.learn(a, 'Ohayo gozaimasen'.encode('utf-8'))
code = lib.encode(a, 'Ohayo'.encode('utf-8'))
# print(code.decode('utf-8'))
# decode = lib.decode(a, code)
# print(decode.decode('utf-8'))
# print((lib.stupid_function('I\'m so stupid!'.encode('utf-8')).decode('utf-8')))
lib.deleteVector(lib.stupid_function('I\'m so stupid!'.encode('utf-8')))
lib.deleteAutocoder(a)


@app.route('/')
def start():
    return render_template('main_page.html')
