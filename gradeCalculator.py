def calculateGrade():
    # Implement your solution in between the two comment blocks
    # This first line is provided for you
    print("Calculating Grade")
    grade = float(input("Enter Score: "))
   
    if grade <0:
        print ("Bad score")
    elif (grade <.6):
        print ("F")
    elif (grade <.7):
        print ("D")
    elif (grade <.8):
        print ("C")
    elif (grade <.9):
        print ("B")
    elif (.9 <=grade <=1.0):
        print ("A")
    else:
        print ("Bad score")
        
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
calculateGrade()