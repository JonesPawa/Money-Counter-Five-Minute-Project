import time
import sys

#Settings
moneyPerHour = 0.0

#Design
currency = u"\u20ac"
seperateLines = "---------------------------"
digitsAfterPoint = "2"

# Create the input question
def startInput():
    global moneyPerHour
    try:
        moneyPerHour = float(raw_input("Enter your money per hour in " + currency.encode("utf-8") + ": "))
    except:
        # Only continue if the user types in the moneyPerHour
        print("Please enter only numbers")
        startInput()
        
# Set the money per hour
startInput()
print("Money" + str(moneyPerHour))

mins = 0.0
total_money = 0.0

# Run forever
while True:
    money = float(moneyPerHour/ 60.0 / (1.0 / 0.1) / 60)
    
    
    for x in range(0, 50):
        print("\n")
    print("Mins: " + "%.1f" % mins)
    print(seperateLines)
    digits = "%."+digitsAfterPoint + "f"
    print("Money for my work: " + digits % total_money + u"\u20ac")
    print(seperateLines + "\n\n")
    
    # Sleep
    time.sleep(0.1)
    
    # Increment the total money
    total_money += money
    
    # Increment the minute total
    mins += (1.0/60.0 / (1.0 / 0.1))



