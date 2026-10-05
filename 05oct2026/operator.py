price = float(input("enter the  food price:"))
quantity = int(input("enter the  food quantity:"))
delivery_charges = float(input("enter the delivery_charges:"))
discount_percentage = float(input("enter the discouunt_percentage:"))
final_bill = (price * quantity + delivery_charges) - discount_percentage
print(final_bill)