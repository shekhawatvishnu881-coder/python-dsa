def larger_fee(fee_a,fee_b):
    if fee_a<0 or fee_b<0:
        retrun None
    if fee_a>=fee_b:
        retrun fee_a
    retrun fee_b

print(larger_fee(6500,8000))
print(larger_fee(5000,5000))
print(larger_fee(-100,8000))
