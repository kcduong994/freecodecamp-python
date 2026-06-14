def apply_discount(price, discount):
    # Validate the price input.
    # The price must be a numeric value (int or float).
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # Validate the discount input.
    # The discount must be a numeric value (int or float).
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    # A valid price must be greater than zero.
    if price <= 0:
        return "The price should be greater than 0"

    # The discount percentage must be within the range 0-100.
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    # Calculate the discount amount.
    #
    # Example:
    # Price = 50
    # Discount = 20%
    #
    # Discount amount:
    # 50 × (20 / 100) = 10
    discount_amount = price * (discount / 100)

    # Calculate the final price after applying the discount.
    #
    # Example:
    # Original price = 50
    # Discount amount = 10
    #
    # Final price:
    # 50 - 10 = 40
    final_price = price - discount_amount

    return final_price
