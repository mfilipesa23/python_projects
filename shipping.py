# Sal's shipping

# This program informs the user of the package weight and determines the cheapest shipping method for that package. 
# There are three possible shippment methods: Ground Shipping, Ground Shipping Premium, Drone Shipping.

price = 0                      # Variable assignment
price_ground = 0          # auxiliary variable Ground Shipping
price_ground_premium = 125.00  # aux variable Ground Shipping Premium
price_drone = 0                # aux variable Drone Shipping
weight = 15                   # Weight package (lb)

# to be determined
method_shipping = "\nOur best choice: " 
# Calculate the final price for each available method and determinate the cheapest alternative.

if (weight <= 2):
  price_ground += 1.50 * weight + 20
  price_drone += 4.50 * weight
elif (weight <= 6):
  price_ground += 3.00 * weight + 20
  price_drone += 9.00 * weight
elif (weight <= 10):
  price_ground += 4.00 * weight + 20
  price_drone += 12.00 * weight
else:
  price_ground += 4.75 * weight + 20
  price_drone += 14.25 * weight

# Logging prices
print("***************  Sal's Shipping  *************** \n     Delivering the best shipping experience"
+"\n   Specialized delivery in the tri-county area")
print("************************************************")
print("\nPackage weight: "+ str(weight) + " lb")
print("\nGround Shipping: " + "$" + str(price_ground))
print("Ground Premium Shipping: " + "$"  + str(price_ground_premium))
print("Drone Shipping: " + "$"  + str(price_drone))

# Cheapest shipping method
if (price_ground < price_ground_premium):
  if price_ground < price_drone:
    print(method_shipping + "Ground Shipping")
    price += price_ground
  else: # price_drone <= price_ground
    print(method_shipping + "Drone Shipping")
    price += price_drone
else: # price_ground_premium <= price_ground
  if (price_drone < price_ground_premium):
    price += price_drone
    print(method_shipping + "Drone Shipping")
  else: # price_ground_premium <= price_drone
    price += price_ground_premium
    print(method_shipping + "Ground Premium Shipping")

# Print price of cheapest method
print("Delivery price: " + "$" + str(price))
print("\n************************************************")
print("           Thank you for choosing us!")
print("************************************************")
