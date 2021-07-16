a = int(input("คะแนนเก็บ "))
b = int(input("คะแนนสอบกลางภาค"))
c = int(input("คะแนนสอบปลายภาค"))
p = a+b+c
if (80<=p<=100):
    print("Grade A")
elif (75<=p<=79):
    print("Grade B+")
elif (70<=p<=74):
    print("Grade B")
elif (65<=p<=69):
    print("Grade C+")
elif (60<=p<=64):
    print("Grade C")
elif (55<=p<=59):
    print("Grade D+")
elif (50<=p<=54):
    print("Grade D")
else :
    print("Grade F")
