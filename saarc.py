saarc = ["Afganistan", "Bangladesh", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
country = input("Type a Country name and press Enter ")
if country in saarc:
    print(country, "is in Saarc!")
else:
    print(country, "is not in Saarc!")
print(type(country))
print("Program Terminated!")

