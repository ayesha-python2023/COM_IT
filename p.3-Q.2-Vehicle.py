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

type_1 = family
type_2 = transportation
type_3 = load
#First thing is that how we going to store that data of 20 vehicles and we need to make dictionaries for that

Vehicle_information = {
    "type_1": "20,000,000"
    "type_1": "30,000,000"
    "type_1": "40,000,000"
    "type_1": "50,000,000"
    "type_1": "60,000,000"
    "type_1": "70,000,000"
    "type_2": "81,000,000"
    "type_2": "90,000,000"
    "type_3": "101,000,000"
    "type_2": "110,000,000"
    "type_2": "100,000,000"
    "type_2": "105,000,000"
    "type_3": "80,000,000"
    "type_3": "50,000,000"
    "type_3": "20,000,000"
    "type_2": "40,000,000"
    "type_2": "30,000,000"
    "type_1": "100,000,000"
    "type_2": "60,000,000"
    "type_3": "90,000,000"
}


