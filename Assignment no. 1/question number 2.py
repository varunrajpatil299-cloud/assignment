# Online Shopping Discount System (Compact Version)

# Taking inputs
customer_name = input("Enter customer name: ")
product_price = float(input("Enter product price: "))
is_premium = input("Is the customer a premium member? (True/False): ").strip().lower() == "true"
coupon_code = input("Enter coupon code: ")

# Applying discount using nested ternary operators with short-circuit logic
discount_percent = 20 if (product_price > 5000 and is_premium) \
    else 10 if (is_premium or coupon_code == "SAVE10") \
    else 0

# Calculations
discount_amount = product_price * discount_percent / 100
final_price = product_price - discount_amount

# Output
print("\n--- Shopping Bill ---")
print(f"Customer Name: {customer_name}")
print(f"Original Price: ₹{product_price:.2f}")
print(f"Discount Applied: {discount_percent}%")
print(f"Final Price: ₹{final_price:.2f}")
print("Premium benefits applied" if is_premium else "No premium benefits")
