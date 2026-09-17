def print_integer(price,quantity,total):
  if price<0 or quantity<0:
     print("Rejected")
  else:
     print(f"price   : {price}")
     print(f"quantity  : {quantity}")
     print(f"total   : {total:.2f}")
price=float(input("Enter price :"))
quantity=int(input("Enter quantity :"))
total=price*quantity
print_integer(price,quantity,total)

