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
    print("\ncount_odd")
    test(count_odd(xs)==4)
    
    print("\nsum_even")
    test(sum_even(xs)==96)
    
    print("\nsum negative")
    test(neg_sum(xs)==-60)
    
    print("\nsum_to_even")
    test(sum_to_even(xs)==-2)
    
    print("\nwords_5")
    test(words_5(names) == 4)
    
    print("\nsam")
    test(sam(names2)==5)
    test(sam(names)==10)
    
    print("\nis_prime")
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(is_prime(19701013))

xs=[1,-3,2,4,14,23,34,42,-57]
names = ["Gen","Kayla","Justis","Leo","maikel","Tian","Owen","Mikki","Steph","Annie"]
names2 = ["Gen","Kayla","Justis","Leo","Sam","maikel","Tian","Owen","Mikki","Steph","Annie"]


def count_odd(lst):
    """Ex 1  Write a function to count how many odd numbers are in a list"""    
    count = 0
    for i in lst:
        if i%2 != 0:
            count += 1           
    return count



def sum_even(list):
    """Ex 2 Sum up all the even numbers in a list"""
    mysum=0
    for i in list:
        if i%2 == 0:
            mysum = mysum +i           
    return mysum



def neg_sum(nlist):
    """ex 3: sum of negative nums in list"""
    total = 0
    for i in nlist:
        if i < 0:
            total+=i
    return total


def words_5(words):
    """Ex 4: Count how many words in a list have length 5"""
    count = 0
    for i in words:
        if len(i) == 5:
            count += 1
    return count
            

def sum_to_even(nlist):
    """ Ex 5: Sum all the elements in a list up to but not including the
    first even number."""
    sum = 0
    for i in nlist:
        if i % 2 == 0:
            break
        else:
            sum+=i
    return sum

def sam(names):
    """Ex 6: Count how many words occur in a list up to
    and including the first occurrence of the word sam"""
    count = 0
    for i in names:
        if i == "Sam":
            count += 1
            break
        
        count += 1
    return count






def sqrt(n):
    """Ex 7:Newtons square root function -"""
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print("better",better)
        if abs(approx - better) < 0.001:
            return better
        approx = better


print("sqrt",sqrt(25.0))

def is_prime(n):
    """Write a function, is_prime, which takes a single integer
    argument and returns True when the argument is a prime number and False otherwise"""
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    


test_suite()