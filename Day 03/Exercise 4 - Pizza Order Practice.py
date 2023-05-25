# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Pizza prices
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_small_price = 2
pepperoni_medium_large_price = 3
extra_cheese_price = 1


# Calculate the base price based on the size
if size == "S":
    base_price = small_pizza_price
elif size == "M":
    base_price = medium_pizza_price
elif size == "L":
    base_price = large_pizza_price
else:
    print("Invalid size entered. Please try again.")
    exit()

# Add pepperoni cost
if add_pepperoni == "Y":
    if size == "S":
        base_price += pepperoni_small_price
    else:
        base_price += pepperoni_medium_large_price

# Add extra cheese cost
if extra_cheese == "Y":
    base_price += extra_cheese_price

# Print the final bill
print(f"Your final bill is: ${base_price}.")