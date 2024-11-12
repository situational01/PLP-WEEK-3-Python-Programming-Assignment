def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Apply discount to the price
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {price:.2f}")
except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")