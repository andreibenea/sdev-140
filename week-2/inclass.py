"""
You have a store and give discount to 
customers based on the number of items purchased
> up to 10 items: no discount
> more than 10 up to 25 items: 10% discount
> more than 25 up to 50 items: 15% discount
> more than 50 items: 20% discount
"""
price = 20
items = int(input("Type in how many items you purchased: "))

CUT_OFF1 = 10
CUT_OFF2 = 25
CUT_OFF3 = 50

if items <= CUT_OFF1:
    discount = 0
elif items <= CUT_OFF2:
    discount = 0.1
elif items <= CUT_OFF3:
    discount = 0.15
else:
    discount = 0.2

gross_price = price * items
final_price = gross_price - gross_price * discount
print("Gross price is", gross_price)
print("Discount is", discount)
print("Final price is", final_price)
