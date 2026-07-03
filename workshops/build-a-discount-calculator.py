from abc import ABC, abstractmethod


class Product:
    # Initialize a product with a name and price.
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    # Return a readable representation of the product.
    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'


class DiscountStrategy(ABC):
    # Require every discount strategy to define when it can be applied.
    @abstractmethod
    def is_applicable(
        self,
        product: Product,
        user_tier: str,
    ) -> bool:
        pass

    # Require every discount strategy to calculate a discounted price.
    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass


class PercentageDiscount(DiscountStrategy):
    # Store the percentage used by this discount strategy.
    def __init__(self, percent: int) -> None:
        self.percent = percent

    # Accept percentage discounts up to and including 70 percent.
    def is_applicable(
        self,
        product: Product,
        user_tier: str,
    ) -> bool:
        return self.percent <= 70

    # Reduce the original price by the configured percentage.
    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)


class FixedAmountDiscount(DiscountStrategy):
    # Store the fixed amount to subtract from the product price.
    def __init__(self, amount: int) -> None:
        self.amount = amount

    # Apply the discount only when it is less than 90 percent
    # of the original product price.
    def is_applicable(
        self,
        product: Product,
        user_tier: str,
    ) -> bool:
        return product.price * 0.9 > self.amount

    # Subtract the fixed discount amount from the original price.
    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount


class PremiumUserDiscount(DiscountStrategy):
    # Apply this strategy only to premium users.
    # lower() makes the comparison case-insensitive.
    def is_applicable(
        self,
        product: Product,
        user_tier: str,
    ) -> bool:
        return user_tier.lower() == 'premium'

    # Give premium users a 20 percent discount.
    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8


class DiscountEngine:
    # Store all available discount strategies.
    def __init__(
        self,
        strategies: list[DiscountStrategy],
    ) -> None:
        self.strategies = strategies

    # Calculate every applicable discounted price and return
    # the lowest price available.
    def calculate_best_price(
        self,
        product: Product,
        user_tier: str,
    ) -> float:
        # Include the original price so it remains available when
        # no discount applies or when a discount produces a higher price.
        prices = [product.price]

        # Check each discount strategy individually.
        for strategy in self.strategies:
            # Calculate the discounted price only when the strategy applies.
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)

                # Add the discounted price to the list of possible prices.
                prices.append(discounted)

        # Return the lowest value among the original and discounted prices.
        return min(prices)


if __name__ == '__main__':
    # Create the product whose best price will be calculated.
    product = Product('Wireless Mouse', 50.0)

    # Define the user's membership tier.
    user_tier = 'Premium'

    # Create the available discount strategies.
    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount(),
    ]

    # Create the discount engine with all available strategies.
    engine = DiscountEngine(strategies)

    # Calculate the lowest price produced by the applicable strategies.
    best_price = engine.calculate_best_price(product, user_tier)

    # Display the final price with exactly two decimal places.
    print(
        f'Best price for {product.name} '
        f'for {user_tier} user: ${best_price:.2f}'
    )
