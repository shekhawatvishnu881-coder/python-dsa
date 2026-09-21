def count_divisible(start,end,divisor):
    if start>end or divisor<=0:
        return None
    count=0
    for value in range (start,end+1):
        if value%divisor==0:
            count+=1
    return count


print(count_divisible(10,5,15))
print(count_divisible(5,15,25))
print(count_divisible(10,50,15))
print(count_divisible(50,10,15))
