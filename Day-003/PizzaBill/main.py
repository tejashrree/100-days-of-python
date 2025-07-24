print("Welcome to python pizza deliveries")
size = input("What size Pizza do you want? S,M or L: ")
pepperoni = input("Do you want pepperoni or not ? Y or N: ")
extra_cheese = input("Do you want extra cheese or not? Y or N: ")


bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
if pepperoni == "Y":
 if size == "S":
  bill += 2
 elif size == "M" or "L":
   bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")