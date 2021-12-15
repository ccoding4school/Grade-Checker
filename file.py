# Grade Checker
# 12/14/2021

studentPoints = False
maxPoints = False
categoryWeight = False

print("DG\n------")
studentPoints = int(input("Student Points: "))
maxPoints = int(input("Max Points: "))
categoryWeight = int(input("Category Weight: "))
print("")

studentPoints2 = False
maxPoints2 = False
categoryWeight2 = False

print("AG\n------")
studentPoints2 = int(input("Student Points: "))
maxPoints2 = int(input("Max Points: "))
categoryWeight2 = int(input("Category Weight: "))
print("")

studentPoints3 = False
maxPoints3 = False
categoryWeight3 = False

print("MG\n------")
studentPoints3 = int(input("Student Points: "))
maxPoints3 = int(input("Max Points: "))
categoryWeight3 = int(input("Category Weight: "))
print("\n")

percent = studentPoints / maxPoints
percent2 = studentPoints2 / maxPoints2
percent3 = studentPoints3 / maxPoints3

categoryPoints = percent * categoryWeight
categoryPoints2 = percent2 * categoryWeight2
categoryPoints3 = percent3 * categoryWeight3

print("Your DG is: " + str(percent * 100))
print("Your AG is: " + str(percent2 * 100))
print("Your MG is: " + str(percent3 * 100))
print("Your grade is: " + str(categoryPoints + categoryPoints2 + categoryPoints3))
