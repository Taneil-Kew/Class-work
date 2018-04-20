

# myfile = open("test.csv", "w")
# myfile.write("Name, Grade\n")
# myfile.write("Genesis,12\n")
# myfile.write("Stefanos,12\n")
# myfile.close()

mynewhandle = open("test - test.csv", "r")
students = []
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    # Now process the line we've just read
    #print(theline, end="")
    thelist = theline.split(',')

   # thelist[1] = int(thelist[1])
    thenum = thelist[1].split('\\')
    thenum = thenum[0]
    thelist[1]=thenum
    students.append(thelist)

print(students)
mynewhandle.close()