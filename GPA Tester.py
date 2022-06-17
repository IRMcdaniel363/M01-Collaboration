#Isaiah Mcdaniel
#File Name GPA Tester
#This code tests to see if you made the deans list or the honner roll.
while True:
    lname = input("Enter a last name(Enter zzz to quit): ")
    #after getting the first name this checks to see if zzz is entered to quit
    if(lname == "zzz"):
        break
    #grabs the gpa and the first name
    fname = input("Enter a first name: ")
    gpa = float(input("Enter a  gpa: "))
    #checking to see what they made deans list, honner roll, or none
    if(gpa >= 3.5):
        print("You " + fname + " " + lname + " made the deans list!")
    elif(gpa >= 3.25):
        print("You " + fname + " " + lname + " made the honner roll!")
    else:
        print("You " + fname + " " + lname + " did not made the deans list or honner roll!")
