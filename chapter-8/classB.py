import sys
import string


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def count_letters(string,ltr):
    count = 0
    repeats =0
    while repeats < len(string):
        str_index = string.find(ltr,repeats, repeats+1)
        if string.find(ltr,repeats, repeats+1)>=0:
            count+=1
        repeats +=1
     return count

print(count_letters("bananaa","b"))