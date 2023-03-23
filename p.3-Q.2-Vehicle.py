# Write an algorithm (Vehicles.py) that, from reading and storing in vectors the commercial value of 20 vehicles and the type (family (1), 
# public transportation (2), load (3)), calculate the value based on:
# • For vehicles with a value greater than 100 million, charge VAT of 20%, for others VAT is 16%
# • For vehicles type 1, with value up to 50 million, apply a discount equivalent to 50% of the VAT charged
# • For vehicles type 2 and 3, with a value higher than 80 million, apply an additional cost of 5%
# • For all vehicles, if the final value is less than 80 million, apply an additional discount of 5% of the commercial value

"""
    Vehicle type 
    vehicle value
    charge VAT
    Apply discount and extra cost on vehicles
    """
import csv

# Open the CSV file for reading
with open('file.csv', 'r') as csvfile:
    # Create a reader object
    reader = csv.reader(csvfile)

    # Iterate over the rows in the CSV file
    for row in reader:
        # Process each row
        print(row)

vehicle_types = []
vehicle_prices = []

i = 0
while i < 1:
    price = int(input("Please enter the amount of your vehicle: "))
    vehicle_prices.append(vehicle_prices)
    vehicle_type = input("Please enter the type of your vehicle: ")
    vehicle_types.append(vehicle_type)
    i += 1

for vehicle_price in vehicle_prices:
    if vehicle_price > 100000000:
        charge_VAT = vehicle_price * .20
        print(charge_VAT)
    else:
        charge_VAT = vehicle_price * .16
        print(charge_VAT)
print(vehicle_types)
print(vehicle_prices)
print()
