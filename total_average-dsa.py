def total_and_average(marks):
    if not marks:
        return none
    total=sum(marks)
    return total,total/len(marks)
answer=total_and_average([60,80])
if answer is not None:
    total,average=answer
    print(total,average)
