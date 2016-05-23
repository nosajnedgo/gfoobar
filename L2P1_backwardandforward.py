# Challenge: http://pastebin.com/uF3fULCt

import string

def testBaseN(dec, base):
    symbols = string.printable
    result = ""
    while dec != 0:
        result += symbols[dec % base]
        dec /= base
    return result == result[::-1]

def answer(n):
    maxBase = len(string.printable)
    for base in range(2, maxBase):
        if testBaseN(n, base):
            return base;
    return "Exceeded max base"