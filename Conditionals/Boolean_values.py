#Boolean values

status = True
print(status)
print(type(status))

# = assinment operator
# == comparison operator

soda = 'coke'
print(soda == "coke")
print(soda == "pepsi")
print(soda == "Coke")
print(soda != "root beer")

names = ["mike","john","mary"]
mike_status = "mike" in names
print(mike_status)
bill_status = "bill" in names
print(bill_status)

not_bill_status = "bill" not in names
print(not_bill_status)