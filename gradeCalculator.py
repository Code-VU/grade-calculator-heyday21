def calculateGrade():
    # Implement your solution in between the two comment blocks
    # This first line is provided for you
    print("Calculating Grade")
    grade = float(input("Enter Score: "))
    if grade >.9999:
        print ("Bad Grade")
    elif (1.0> grade >=.9):
        print ("A")
    elif (.9> grade >=.8):
        print ("B")
    elif (.8> grade >=.7):
        print ("C")
    elif (.7 >grade >=.6):
        print ("D")
    elif (0 <=grade <.6):
        print ("F")
    elif grade <0:
        print ("Bad Grade")
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
calculateGrade()