def pass_count():
    count=0
    for i in range(1,6):
        try:
            num=int(input(" enter marks : "))
            if num>40:
                count=+1
        except:
            print(" Invalid input ")
            break
    else:
        print(f" final pass count is {count}")
pass_count()
