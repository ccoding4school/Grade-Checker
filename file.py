# Grade Checker
# Updated 1/10/2022

print("DG")
S1 = input("Scores (Ex. 100,97,88): ")
CW1 = int(input("Category Weight: "))

print("\nAG")
S2 = input("Scores (Ex. 95,97,89): ")
CW2 = int(input("Category Weight: "))

print("\nMG")
S3 = input("Scores (Ex. 90,93,98): ")
CW3 = int(input("Category Weight: "))

def split(string):
    list = []
    list = string.split(",")
    return list

DG = split(S1)
AG = split(S2)
MG = split(S3)

def percent(list):
    score = 0
    maxScore = 100 * len(list)
    for i in range(len(list)):
        score += int(list[i])
    return score / maxScore

def gradeChecker():
    global CW1
    global CW2
    global CW3

    CP1 = percent(DG) * CW1
    CP2 = percent(AG) * CW2
    CP3 = percent(MG) * CW3

    print("\nYour grade is: " + str(CP1 + CP2 + CP3))

gradeChecker()
