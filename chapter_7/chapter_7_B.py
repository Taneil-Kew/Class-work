import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(odd_count(newby_list)== 3)
  
    print("\nsum_to_even")
    test(sum_to_even(newby_list)== -3)
    test(sum_to_even(odd_list)== 9)
    
    print("\nsam")
    test(sam(names)==10)
    test(sam(names2)==5)
   
    
newby_list = [-3,0,4,14,23,34,42,-57]
my_list = [-2,0,4,14,22,34,42,-52]
odd_list=[3,1,5]
names = ["Gen","Kayla","Justis","Leo","maikel","Tian","Owen","Mikki","Steph","Annie"]
names2 = ["Genyy","Kayla","Justis","Leo","Sam","maikel","Tian","Owen","Mikki","Steph","Annie"]

def odd_count(lst):
    """ count how many odd numbers are in a list."""
    count = 0
    for i in lst:
        if i % 2 == 1:
            count += 1
    return count


def even_sum(lst):
    """ sum of all evens in a list."""
    mysum = 0
    for i in lst:
        if i % 2 == 0:
            mysum += i
    return mysum


def neg_sum(lst):
    """ sum of all negatives in a list."""
    mysum = 0
    for i in lst:
        if i < 0:
            mysum += i
    return mysum

def count_5(lst):
    """Count how many words in a list have length 5"""
    count = 0
    for i in lst:
        if len(i) == 5:
            count += 1
    return count

def sum_to_even(lst):
    """Sum all the elements in a list up to but not including the first even number."""
    mysum = 0
    for i in lst:
        if i % 2 == 0:
            break
        mysum += i
    return mysum

def sam(lst):
    """Count how many words occur in a list up to and including
    the first occurrence of the word sam"""
    count = 0
    for i in lst:
        if i == "Sam":
            count += 1
            break
        count += 1
    return count
test_suite()