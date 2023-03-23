#Exercise 17: Write a program in Python that converts from canadian dollars to US dollars. 
# # You will receive a decimal number corresponding to the amount in CAD
# # and will answer with the corresponding amount in US dollars. Take the quotation of the dollar today.

amount = input("Please enter your amount in CAD: ")
canadian_dollar = int(amount)
american_dollar = float(canadian_dollar * 0.73)
print(american_dollar)
