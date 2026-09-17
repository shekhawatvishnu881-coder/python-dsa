def count_even(n):
    if n<0:
        return (None)
    for i in range(1,n+1):
        if n%2==0:
            count=+1
    return count
n=int(input(" Enter  number "))
print(count_even(n))
