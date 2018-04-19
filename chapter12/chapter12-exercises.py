import calendar
import copy

#import os, sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #adds parent folder to our path
import unit_tester

unit_tester.test(1==8)
x=27
y=copy.deepcopy(x)
y+=1
print(y,x)
