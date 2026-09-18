def second_largest_distinct(a,b,c):
    largest=a
    if b>largest:
        largest=b
    if c>largest:
        largest=c

    second=None
    if a<largest:
        second=a
    if b<largest:
        if second is None or b > second:
            second=b
    if c<largest:
        if second is None or c > second:
            second=c
    return second
print(second_largest_distinct(9,9,4))
print(second_largest_distinct(4,5,6))
print(second_largest_distinct(9,8,4))
print(second_largest_distinct(9,10,4))
