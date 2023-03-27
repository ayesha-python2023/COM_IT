
# Develop a program to generate invoices to customers and purchase orders from suppliers.
#The system displays a menu asking if you want to make an invoice or purchase order
#In case of an invoice, it asks for the client’s data  and in case of being PO enter the supplier’s data.
##Then the program asks to enter up to 10 items (may be less) with description and its value

"""
At the end it calculates the net, GST, PST and finally shows on screen all the data of the invoice (or PO). One thing per line:
Invoice Number (PO)
Customer number (Supplier)
Customer name (Supplier)
————————
Items with the value of each
———————- 
Net
GST
PST
Total
"""
    
options = int(input("Press 1 for invoices, press 2 for Purchse orders and 3 to exit."))
if options == 1:

    i = 0
    while True:
        start_invoice = input('Please enter "start" to initialize a new invoice and "exit" cancel: ')
        if start_invoice == "start":
            print("Invoice number is " + str(1 + i))
            print("Customer number is " + str(1000000 + i ))
            input("Enter Customer name:  ")
            i += 1
            break
            
        elif start_invoice == "exit":
            print('It is cancelled.')
        
        else:
            print('Please enter a write command')
elif options == 2:
    i = 0
    while True:
        start_purchaseOrder = input('Please enter "start" to initialize a new invoice and "exit" cancel: ')
        if start_purchaseOrder == "start":
            print("Purchase Order number is " + str(1 + i))
            print("Supplier number is " + str(1000000 + i ))
            input("Enter Supplier name is :  ")
            i += 1
            break
            
        elif start_purchaseOrder == "exit":
            print('It is cancelled.')
        
        else:
            print('Please enter a write command')
else:
    print("you are out")

#for purchase orders
#shop = input("Please enter items description")
#shop_value = input('please enter value of the items')


shop_value = 0
for items in range(0, 10):
    shop = input("Please enter items description: ")

    print(shop)
    value = int(input("value: "))
    shop_value = value + shop_value
    Net = shop_value
    GST = shop_value * 10
    PST = shop_value * 3
    TOTAL = Net + GST + PST
print(f"Your net payment will be {Net}")
print(f"GST will be {GST}")
print(f"PST will be {PST}")





