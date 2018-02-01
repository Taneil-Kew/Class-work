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
    count = 0
    while count < len(strng):
        tempvar = strng[count]
        if strng[count] == ch:
            return count
        count += 1
    return -1

test(find("Compsci", "p") == 3)
test(find("Compsci", "C") == 0)
test(find("Compsci", "i") == 6)
test(find("Compsci", "x") == -1)