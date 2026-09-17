def fee_status(fee,paid):
    if fee < 0 or paid < 0:
        return None
    if paid > fee:
        return None
    pending=fee-paid
    status="fully paid" if pending==0 else "pending"
    return pending,status

print(fee_status(6500,2000))
print(fee_status(0,2000))
print(fee_status(6500,5000))
print(fee_status(6500,6500))
