def sales_total():
    num=0
    count=0
    total=0
    while num !=-1:
         num = int(input("Enter sales amount : "))
         if num>=0:
            count+=1
            total+=num
    else:
        print(f"Numbers Entered are {count} and their sum is {total}")
sales_total()
        
            
        
   
