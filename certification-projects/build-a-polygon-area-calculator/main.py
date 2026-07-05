import math


class Rectangle:
    # Initialize a rectangle with its width and height.
    def __init__(self, width, height):
        # Store the horizontal dimension of the rectangle.
        self.width = width

        # Store the vertical dimension of the rectangle.
        self.height = height

    # Return a readable string representation of the rectangle.
    def __str__(self):
        return (
            f'Rectangle(width={self.width}, '
            f'height={self.height})'
        )

    # Update the width of the rectangle.
    def set_width(self, width):
        self.width = width

    # Update the height of the rectangle.
    def set_height(self, height):
        self.height = height

    # Calculate and return the area of the rectangle.
    def get_area(self):
        return self.width * self.height

    # Calculate and return the perimeter of the rectangle.
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # Calculate and return the diagonal length using
    # the Pythagorean theorem.
    def get_diagonal(self):
        return math.sqrt(
            self.width ** 2 + self.height ** 2
        )

    # Create a text-based picture of the rectangle using asterisks.
    def get_picture(self):
        # Prevent excessively large text representations.
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        # Create one row containing a number of asterisks equal
        # to the width, then repeat that row for the height.
        #
        # Every row ends with a newline character, including
        # the final row.
        return ('*' * self.width + '\n') * self.height

    # Calculate how many times another shape can fit inside
    # this rectangle without rotating either shape.
    def get_amount_inside(self, shape):
        # Determine how many copies fit horizontally.
        amount_across = self.width // shape.width

        # Determine how many copies fit vertically.
        amount_down = self.height // shape.height

        # Multiply both values to get the total number of copies.
        return amount_across * amount_down


class Square(Rectangle):
    # Initialize a square using one side length.
    def __init__(self, side):
        # A square has equal width and height, so the same side
        # value is passed to both Rectangle dimensions.
        super().__init__(side, side)

    # Override Rectangle.set_width() so the shape remains a square.
    def set_width(self, side):
        self.width = side
        self.height = side

    # Override Rectangle.set_height() so the shape remains a square.
    def set_height(self, side):
        self.width = side
        self.height = side

    # Update both dimensions using one side length.
    def set_side(self, side):
        self.width = side
        self.height = side

    # Return a square-specific string representation.
    def __str__(self):
        return f'Square(side={self.width})'


# Demonstrate the Rectangle class.
rect = Rectangle(10, 5)

# Calculate the original area.
print(rect.get_area())

# Change the height and calculate the updated perimeter.
rect.set_height(3)
print(rect.get_perimeter())

# Display the rectangle's dimensions.
print(rect)

# Display the rectangle as an asterisk-based picture.
print(rect.get_picture())


# Demonstrate the Square class.
sq = Square(9)

# Square inherits get_area() from Rectangle.
print(sq.get_area())

# Change the side length while keeping width and height equal.
sq.set_side(4)

# Square inherits get_diagonal() from Rectangle.
print(sq.get_diagonal())

# Display the square's side length.
print(sq)

# Square inherits get_picture() from Rectangle.
print(sq.get_picture())


# Resize the rectangle and calculate how many squares fit inside it.
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
