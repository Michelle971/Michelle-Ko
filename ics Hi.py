#Tittle 
print("""
Average of 3 Numbers
=====================
""")
#Get 3 scores
score1 = int(input("Enter your score: "))
score2 = int(input("Enter second score: "))
score3 = int(input("Enter third score: "))
#Calculate average
if (score1 + score2 +score3) /3 < 50:
    print("Good try, but you failed")
else:
    if (score1 + score2 +score3) /3 >= 90:
        print("Good job, you passed with scholars!")
    else:
        if (score1 + score2 +score3) /3 >= 80:
            print("Good job, you passed with honors!")
        else:
            print("You sure?")
#Extra words of encouragements
print("Goodluck! and don't forget you are always continously learning")
