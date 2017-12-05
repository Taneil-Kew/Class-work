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
    print("tests for turn clockwise")
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("   ") == None)
    
    print("\nday to name")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    
    print("\nday name to number")
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    
    

def turn_clockwise(dir):
    if dir == "N":
        return "E"
    elif dir == "E":
        return "S"
    elif dir == "S":
        return "W"
    elif dir == "W":
        return "N"
   
    

def day_name(num):
    if num == 0:
        return "Sunday"
    if num == 1:
        return "Monday"
    if num == 2:
        return "Tuesday"
    if num == 3:
        return "Wednesday"
    if num == 4:
        return "Thursday"
    if num == 5:
        return "Friday"
    if num == 6:
        return "Saturday"
    else:
        return None

def day_num(day_name):
    if day_name == "Sunday":
        return 0
    elif day_name ==  "Monday":
        return 1
    elif day_name == "Tuesday":
        return 2
    elif day_name == "Wednesday":
        return 3
    elif day_name == "Thursday":
        return 4
    elif day_name == "Friday":
        return 5
    elif day_name == 6:
        return 6
   


    
  
test_suite()        # Here is the call to run the tests
