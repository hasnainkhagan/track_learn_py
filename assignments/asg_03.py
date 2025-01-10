# Create random function according to your brain storming and submit it asap. 
# 1. Create a function using the parameter 
# 2. return should be included inside a function with detailed print statements. 
# 3.  Include function scope alongside global scope variables.

# global scope variable
tax_rate = 0.05  # 5% tax

def calculate_price(original_price, discount):
    """
    This function calculates the final price after applying a discount and adding tax.
    """
    # func. scope var.
    tax = original_price * tax_rate
    
    # calculating disc. price
    discounted_price = original_price - (original_price * (discount / 100))
    final_price = discounted_price + tax
    
    # detailed print stats.
    print(f"Original Price: ${original_price}")
    print(f"Discount Applied: {discount}%")
    print(f"Price After Discount: ${discounted_price}")
    print(f"Tax (5%): ${tax}")
    print(f"Final Price to Pay: ${final_price}")
    
    return final_price

# calling the func.
item_price = 100  # glob. var. for item price
discount_percentage = 10  # glob. var for dis.

# invoke the func. & display the result
final_amount = calculate_price(item_price, discount_percentage)
print(f"\nFinal Amount to be Paid: ${final_amount}")
