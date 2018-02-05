import sys
import math


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def find2(strng, ch, start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

print("find2 ",find2("apple","a" ))
ss = "Python strings  some interesting methods."
if(ss.find("some",77))>=0:
    print("have is in the string")
else:
    print("no have")
print(ss.find("have"))