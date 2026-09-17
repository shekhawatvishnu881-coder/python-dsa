def total_upto(n):
    if n<0:
      return None
    i=1
    total=0
    while i<=n:
      total+=i
      i+=1
    return total
print(total_upto(4))
print(total_upto(5))
print(total_upto(6))
