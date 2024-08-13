menu = {
    'pizza' :90,
    'burger' :80,
    'pasta' :60,
    'salad' :50,
    'coffee' :40,


}
print(" Welcome to our restaurant")
print("pizza : rs90\n burger : rs80\n pasta :rs60\n salad : rs50\n coffee : rs40\n")

order_total = 0

item_1 = input("enter the name of item you want to order =")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
       
  print(f"ordered item {item_1} is not available yet!")

another_order = input("do you want to add another item {item_1}? (yes/no)")
if another_order == "yes":
        item_2 = input("enter the name of second item =")
        if item_2 in menu:
            order_total +=menu[item_2]
            print(f"order item {item_2} has been added to your order")
        else:
            print(f"order item {item_2}is not available!")

            print(f"total amount of items to pay is {order_total} ")
