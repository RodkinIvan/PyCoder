from ctypes import *

lib = cdll.LoadLibrary("Autocoder/lib/libAutocoder.so")

lib.deleteVector.argtypes = [c_char_p]
lib.deleteVector.restype = None

lib.createAutocoder.argtypes = [c_int, c_int]
lib.createAutocoder.restype = c_void_p

lib.deleteAutocoder.argtypes = [c_void_p]
lib.deleteAutocoder.retype = None

lib.learn.argtypes = [c_void_p, c_char_p]
lib.learn.restype = None

lib.encode.argtypes = [c_void_p, c_char_p]
lib.encode.restype = c_char_p

lib.decode.argtypes = [c_void_p, c_char_p]
lib.decode.restype = c_char_p

lib.stupid_function.argtypes = [c_char_p]
lib.stupid_function.restype = c_char_p
