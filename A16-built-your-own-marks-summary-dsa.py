def pass_or_fail(num1,num2,num3,num4,num5):
    return num1>=40 and num2>=40 and num3>=40 and num4>=40 and num5>=40
def is_valid_marks(num):
    try:
        num1=int(num)
        return num1>=0 and num1<=100
    except:
        return False
    
def get_result(n1,n2,n3,n4,n5):
    if is_valid_marks(n1) and is_valid_marks(n2) and is_valid_marks(n3) and is_valid_marks(n4) and is_valid_marks(n5):
        total=n1+n2+n3+n4+n5
        per=total/5
        pass_status= "Pass" if pass_or_fail(n1,n2,n3,n4,n5) else "Fail"
        return (total,per,pass_status)
    return None

def print_result(res):
    print(f"Total {res[0]}\nPercentage {res[1]}\nResult {res[2]}")


final_result=get_result(40,40,40,40,40)
if final_result is not None:
    print_result(final_result)
