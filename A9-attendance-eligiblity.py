def is_eligible(attended,held):
    if held<=0:
        return None
    if attended<0 or attended > held:
        return None
    percentage=(attended/held)*100
    eligible=percentage>=75
    return percentage,eligible
print(is_eligible(12,15))
