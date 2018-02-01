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




def find(strng, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    count = 0
    while ix < len(strng):
        if strng[ix] == ch:
            count += 1
        ix += 1
    return count

test(find("Compsci", "p") == 1)
test(find("Compsci", "C") == 0)
test(find("Compscii", "i") == 2 )
test(find("Compsci", "x") == -1)
