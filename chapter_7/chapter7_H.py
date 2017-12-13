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
    print("tests for 5 words")
    test(words_5(names) == 4)
    test(sum_to_even(xs)==-2)
    test(sam_count(names2)==5)
    test(sam_count(names)==len(names))
  

xs=[1,-3,2,4,14,23,34,42,-57]
names = ["Gen","Kayla","Justis","Leo","maikel","Tian","Owen","Mikki","Steph","Annie"]
names2 = ["Gen","Kayla","Justis","Leo","Sam","maikel","Tian","Owen","Mikki","Steph","Annie"]

def sam_count(lst):
    """Count how many words occur in a list up to and
    including the first occurrence of the word sam"""
    count = 0
    for i in lst:
        if i == "Sam":
            count += 1
            break
        count += 1
    return count
    

def sum_to_even(nlist):
    """Sum all the elements in a list up to but not including the
    first even number."""
    sum = 0
    for i in nlist:
        if i % 2 == 0:
            break
        else:
            sum+=i
    return sum

def neg_sum(nlist):
    """sum of negative nums in list"""
    total = 0
    for i in nlist:
        if i < 0:
            total+=i
    return total

            

def words_5(words):
    count = 0
    for i in words:
        if len(i) == 5:
            count += 1
    return count

def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print("better",better)
        
        if abs(approx - better) < 0.0000001:
            return better
        approx = better
def is_prime(n):
    for i in range(2,n):
   # print(i)
    if n % i == 0:
        print("factor",i)
  
# Test cases
print(sqrt(25.0))
#print(sqrt(49.0))
#print(sqrt(81.0))


test_suite()