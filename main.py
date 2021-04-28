# from helper import tax, inventory, stateTaxes

def tax(total, state):
  tax = stateTaxes[state]
  return "{:.2f}".format(total*tax)

inventory = {
  "banana" : {"qty": 12, "price": 1.97},
  "milk" : {"qty": 20, "price": 2.45},
  "eggs" : {"qty" : 30, "price": 4.39},
  "beef" : {"qty" : 10, "price": 10.49},
  "toilet paper" : {"qty" : 40, "price": 6.59}
}

stateTaxes = {
  "FL": 1.07,
  "NY": 1.30,
  "CO": 1.25
}

cart = {
}

item = ''
total = 0
i = 0
state = ''

name = input("Enter your name? ")
print( f"*** Welcome to Sedano's, {name} ***")
state = input("What state do you live in? 2 letter code: ").upper()



while item != "done":
  item = input("What item would you like to buy? ").lower()
  
  if item == "done":
    break
  if item in inventory:
    quantity = int(input("How many? " ))
    #if quantity is less than qty in inventory 
    if quantity <= inventory[item]['qty']:
      inventory[item]['qty'] = inventory[item]['qty'] - quantity
      print(f"{inventory[item]['qty']}")
    elif quantity > inventory[item]['qty']: 
      print(f"We don't have any more {item}.")

  else:
    print("Item not in stock")
  
  #for loop that adds the items that the user typed in and generated a total.
for (name , itemQuantity) in cart.items():
  # print(name, itemQuantity)
  price = inventory[name]
  itemTotal = itemQuantity * price

  total+=itemTotal
  # CostOfGroceries = cart[item] * inventory.values[i]
  # total = total + CostOfGroceries

print( tax(total, state) )
