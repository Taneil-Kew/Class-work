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




ss = "Python strings have some interesting methods."

print(ss.find("s",8,16))
test(ss.find("s") == 7)
test(ss.find("s", 7) == 7)
test(ss.find("s", 8) == 13)
test(ss.find("s", 8, 13) == -1)
test(ss.find(".") == len(ss)-1)
