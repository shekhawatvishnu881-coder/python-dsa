def second_smallest(a,b,c):
    if a==b and a==c:
        return None
    minimum=a
    if b<minimum:
        minimum=b
    if c<minimum:
        minimum=c

    maximum=a
    if maximum<b:
        maximum=b
    if maximum<c:
        maximum=c

    second_minimum=maximum
    if a<second_minimum and a>maximum:
        second_minimum=a

    if b<second_minimum and b>maximum:
        second_minimum=b

    if c<second_minimum and c>maximum:
        second_minimum=c
    return second_minimum
print(second_smallest(2,2,7))
print(second_smallest(-9,-6,-3))
print(second_smallest(10,20,30))
