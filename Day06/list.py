#day06
#here we work on list

cart = []

while True:
    print("\n--- shopping cart menu ---")
    print("1. add to cart")
    print("2. remove from cart")
    print("3. view cart")
    print("4. exit")
   
 
    choice = input("enter your choice: ")

    
    if choice == "1":
        item = input("enter item name: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == "2":
        item = input("enter item name: ")
        if item in cart:
            cart.remove(item)
            
        else:
            print("item not found in cart:  ")

    elif choice == "3":
        print("your crt items: ", cart)

    elif choice == "4":
        print("thankyou for shopping! ")
        break

    else:
        print("invalid chooice! please try again.")
    
    
    