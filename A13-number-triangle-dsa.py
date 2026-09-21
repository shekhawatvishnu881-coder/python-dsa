def number_triangle():
    n = int(input("Enter n (1-9): "))
    if n < 1 or n > 9:
        print("Invalid number ")
        return
    for row in range(1,n+1):
        line = ""
        for num in range(1,row+1):
            line += str(num) + ""
        print(line)

number_triangle()
