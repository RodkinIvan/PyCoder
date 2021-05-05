from ctypes import *

lib = cdll.LoadLibrary("Autocoder/lib/libAutocoder.so")

lib.deleteVector.argtypes = [c_void_p]
lib.deleteVector.restype = None

lib.createAutocoder.argtypes = [c_int, c_int]
lib.createAutocoder.restype = c_void_p

lib.deleteAutocoder.argtypes = [c_void_p]
lib.deleteAutocoder.retype = None

lib.learn.argtypes = [c_void_p, c_char_p]
lib.learn.restype = None

lib.encode.argtypes = [c_void_p, c_char_p]
lib.encode.restype = c_void_p

lib.decode.argtypes = [c_void_p, c_char_p]
lib.decode.restype = c_void_p

lib.stupid_function.argtypes = [c_char_p]
lib.stupid_function.restype = c_void_p

lib.print.argtypes = [c_void_p]
lib.print.restype = None


class c_str:
    def __init__(self, void_p):
        self.obj = void_p

    def __char_p__(self):
        return cast(self.obj, c_char_p)

    def str(self):
        c_string = self.__char_p__().value
        return c_string.decode('utf-8')

    def __del__(self):
        lib.deleteVector(self.obj)


class Autocoder:
    def __init__(self, inp, out):
        self.obj = lib.createAutocoder(c_int(inp), c_int(out))
        self.inp = inp
        self.out = out

    def learn(self, string):
        if len(string)*8 % self.inp != 0:
            raise Exception('incorrect size!')
        lib.learn(self.obj, string.encode('utf-8'))

    def encode(self, string):
        if len(string)*8 % self.inp != 0:
            raise Exception('incorrect size!')
        c_s = c_str(lib.encode(self.obj, string.encode('utf-8')))
        return c_s.str()

    def decode(self, string):
        if len(string) % self.out != 0:
            raise Exception('incorrect size!')
        c_s = c_str(lib.decode(self.obj, string.encode('utf-8')))
        return c_s.str()

    def __del__(self):
        lib.deleteAutocoder(self.obj)
