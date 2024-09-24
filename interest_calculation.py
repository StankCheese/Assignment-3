investment = int(input("Enter the investment amount (greater than 0 and less than 50000): "))
while investment < 0 or investment > 50000:
    print ("Your investment is out of range!")
    investment = int(input("Enter the investment amount (greater than 0 and less than 50000): "))
rate = int(input("Enter the interest rate (greater than 0 and less than 15): "))
while rate < 0 or rate > 15:
     print ("Your rate is out of range!")
     rate = int(input("Enter the interest rate (greater than 0 and less than 15): "))
years = int(input("Enter the investment duration in years (greater then 0): "))
while years < 0:
    print ("years need to be greater than 0")
    years = int(input("Enter the investment duration in years (greater then 0): "))
month = years * 12
monthRate = (rate / 12) / 100
total = 0.0
counter = 0
for month in range(1, month+1):
    total += investment
    total += round((total * monthRate),2)
    if month % 12 == 0:
        print("Year", int(month/12), ": $", round((total),2))
    
print ("Investment Duration: " + str(years) + " years")
print ("Yearly Interest Rate: " + str(rate) + "%")
print ("Monthly investment Amount: $" + str(investment))
print ("Total Amount of Investment After Compounding: $" + str(round((total),2)))
print ("Completed by Samuel Simmons")