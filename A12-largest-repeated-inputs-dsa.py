def print_max_val():
    count = int(input(" How many values you want to enter : "))
    max_val=0

    for i in range (0,count):
        num = int(input(" Enter integer: "))
        if i==0:
            max_val=num
        elif num>max_val:
            max_val=num
        else:
            print(f" Maximum of above entered values is {max_val}")

print_max_value()
