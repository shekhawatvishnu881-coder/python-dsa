def print_classifier(marks):
 if marks<0 or marks>100:
     print("Invalid mark")
 elif marks>=40:
     print(" Pass ")
 else:
     print("fail")
marks=float(input(" Enter marks: "))
print_classifier(marks)
