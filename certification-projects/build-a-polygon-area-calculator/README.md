# Build a Polygon Area Calculator

A Python object-oriented programming project that implements reusable
`Rectangle` and `Square` classes.

The project focuses on inheritance, method overriding, geometry calculations,
text-based shape rendering, object representation, and shape containment.

![Python](https://img.shields.io/badge/Python-OOP-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Tests](https://img.shields.io/badge/Tests-Passed-success)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Requirements](#project-requirements)
- [Project Structure](#project-structure)
- [Class Design](#class-design)
- [Rectangle Class](#rectangle-class)
- [Square Class](#square-class)
- [Why Inheritance Is Used](#why-inheritance-is-used)
- [Why `super()` Is Used](#why-super-is-used)
- [Why Methods Are Overridden](#why-methods-are-overridden)
- [Geometry Calculations](#geometry-calculations)
- [Text-Based Shape Rendering](#text-based-shape-rendering)
- [Shape Containment](#shape-containment)
- [Usage Example](#usage-example)
- [Expected Output](#expected-output)
- [Implementation Decisions](#implementation-decisions)
- [Debugging Lessons](#debugging-lessons)
- [Time and Space Complexity](#time-and-space-complexity)
- [Skills Practiced](#skills-practiced)
- [How to Run](#how-to-run)
- [Project Status](#project-status)

---

## Project Overview

This project models two geometric shapes:

- `Rectangle`
- `Square`

The `Square` class is implemented as a subclass of `Rectangle`.

This is a natural object-oriented relationship because every square is also a
rectangle, but not every rectangle is a square.

A rectangle may have different width and height values:

```text
width = 10
height = 5
```

A square must always preserve the rule:

```text
width == height
```

The project supports:

- Creating rectangles and squares
- Updating dimensions
- Calculating area
- Calculating perimeter
- Calculating diagonal length
- Rendering shapes using `*`
- Calculating how many smaller shapes fit inside a larger shape
- Displaying readable object descriptions

---

## Project Requirements

The project must provide:

### Rectangle

A `Rectangle` object must store:

```python
width
height
```

It must implement:

```python
set_width()
set_height()
get_area()
get_perimeter()
get_diagonal()
get_picture()
get_amount_inside()
__str__()
```

### Square

A `Square` object must:

- Inherit from `Rectangle`
- Use one side length
- Store the side as both width and height
- Override `set_width()`
- Override `set_height()`
- Provide `set_side()`
- Override `__str__()`
- Reuse the inherited rectangle calculations

---

## Project Structure

```text
build-a-polygon-area-calculator/
├── main.py
└── README.md
```

- `main.py` contains the complete implementation.
- `README.md` explains the design and logic of this project.

---

## Class Design

The project separates shared behavior from specialized behavior.

```text
Rectangle
├── width
├── height
├── set_width()
├── set_height()
├── get_area()
├── get_perimeter()
├── get_diagonal()
├── get_picture()
├── get_amount_inside()
└── __str__()
        ↑
        │ inheritance
        │
Square
├── set_width()      overridden
├── set_height()     overridden
├── set_side()
└── __str__()        overridden
```

The shared geometric behavior is written once in `Rectangle`.

The square-specific rule is handled inside `Square`.

---

## Rectangle Class

### Constructor

```python
def __init__(self, width, height):
    self.width = width
    self.height = height
```

The constructor stores the rectangle dimensions as instance attributes.

Example:

```python
rect = Rectangle(10, 5)
```

The object now contains:

```text
width = 10
height = 5
```

### Why use instance attributes?

Each rectangle can have different dimensions.

```python
rect_1 = Rectangle(10, 5)
rect_2 = Rectangle(4, 8)
```

The values belong to each object, so they must be stored on `self`.

---

### String Representation

```python
def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
```

Example:

```python
print(Rectangle(3, 6))
```

Output:

```text
Rectangle(width=3, height=6)
```

### Why implement `__str__()`?

Without `__str__()`, Python displays an internal object reference such as:

```text
<__main__.Rectangle object at 0x...>
```

A custom representation is more useful for:

- Debugging
- Logging
- Automated tests
- Console output
- Understanding current object state

Because the string reads the current attributes, it updates automatically when
the rectangle is resized.

---

### Setting the Width

```python
def set_width(self, width):
    self.width = width
```

Example:

```python
rect.set_width(16)
```

### Why use a method instead of only direct assignment?

This creates a consistent public interface.

```python
rect.set_width(16)
```

is clearer than changing internal state from outside without a defined
operation.

It also allows validation to be added later without changing the calling code.

---

### Setting the Height

```python
def set_height(self, height):
    self.height = height
```

Example:

```python
rect.set_height(8)
```

The method name must be spelled exactly:

```text
set_height
```

A misspelling such as:

```text
set_heigth
```

creates a different identifier and causes an `AttributeError`.

---

## Square Class

The square inherits from the rectangle:

```python
class Square(Rectangle):
```

This gives the square access to:

```python
get_area()
get_perimeter()
get_diagonal()
get_picture()
get_amount_inside()
```

without duplicating those methods.

---

### Square Constructor

```python
def __init__(self, side):
    super().__init__(side, side)
```

A square receives one value:

```python
sq = Square(5)
```

The parent constructor stores:

```text
width = 5
height = 5
```

### Why pass the same value twice?

A square must have equal dimensions.

Using:

```python
super().__init__(side, side)
```

initializes the square through the existing rectangle constructor while
preserving the square rule.

---

### Overriding `set_width()`

```python
def set_width(self, side):
    self.width = side
    self.height = side
```

The rectangle implementation changes only the width.

That behavior would be invalid for a square because the dimensions could become
different.

The square version updates both dimensions.

---

### Overriding `set_height()`

```python
def set_height(self, side):
    self.width = side
    self.height = side
```

This also updates both values so that the square remains valid.

---

### Setting the Side

```python
def set_side(self, side):
    self.width = side
    self.height = side
```

This is the most natural square-specific operation.

Example:

```python
sq.set_side(4)
```

Result:

```text
width = 4
height = 4
```

---

### Square String Representation

```python
def __str__(self):
    return f'Square(side={self.width})'
```

Example:

```python
print(Square(5))
```

Output:

```text
Square(side=5)
```

### Why override `__str__()`?

If the square inherited the rectangle representation, it would display:

```text
Rectangle(width=5, height=5)
```

That describes the dimensions correctly but does not communicate that the
object is specifically a square.

The override represents the subclass more clearly.

---

## Why Inheritance Is Used

Inheritance is used because a square is a specialized rectangle.

Both shapes use the same formulas for:

- Area
- Perimeter
- Diagonal
- Picture generation
- Containment

Without inheritance, the same methods would need to be copied into both classes.

That would create duplicated code.

```text
Shared behavior       → Rectangle
Square-specific rules → Square
```

This design is easier to maintain and demonstrates code reuse.

---

## Why `super()` Is Used

The square constructor calls:

```python
super().__init__(side, side)
```

`super()` delegates initialization to the parent class.

### Benefits

- Reuses existing initialization logic
- Avoids duplicated assignments
- Makes the class relationship explicit
- Allows future parent-class improvements to be reused
- Keeps initialization consistent

The square could assign both values directly, but `super()` better expresses
that a square is initialized as a special type of rectangle.

---

## Why Methods Are Overridden

Method overriding allows a subclass to replace inherited behavior when the
parent implementation is too general.

For a rectangle:

```python
set_width()
```

changes only the width.

For a square:

```python
set_width()
```

must change both width and height.

The same operation has different behavior depending on the object type.

This is a basic form of polymorphism.

---

## Geometry Calculations

### Area

```python
def get_area(self):
    return self.width * self.height
```

Formula:

```text
area = width × height
```

Example:

```python
Rectangle(3, 6).get_area()
```

returns:

```text
18
```

### Why return the result?

Returning makes the method reusable.

The value can be:

- Printed
- Stored
- Compared
- Tested
- Used in another calculation

---

### Perimeter

```python
def get_perimeter(self):
    return 2 * (self.width + self.height)
```

Formula:

```text
perimeter = 2 × (width + height)
```

Example:

```python
Rectangle(3, 6).get_perimeter()
```

returns:

```text
18
```

The parentheses ensure that width and height are added before multiplication.

---

### Diagonal

```python
def get_diagonal(self):
    return math.sqrt(
        self.width ** 2 + self.height ** 2
    )
```

Formula:

```text
diagonal = √(width² + height²)
```

This comes from the Pythagorean theorem.

Example:

```python
Rectangle(3, 6).get_diagonal()
```

returns:

```text
6.708203932499369
```

### Why use `math.sqrt()`?

`math.sqrt()` clearly communicates that the calculation requires a square root.

The alternative:

```python
value ** 0.5
```

also works, but is less explicit.

---

## Text-Based Shape Rendering

The method:

```python
def get_picture(self):
    if self.width > 50 or self.height > 50:
        return 'Too big for picture.'

    return ('*' * self.width + '\n') * self.height
```

creates a text picture of the shape.

For:

```python
Rectangle(4, 3)
```

the returned value is:

```python
'****\n****\n****\n'
```

When printed:

```text
****
****
****
```

### How it works

One row:

```python
'*' * self.width
```

For width `4`:

```text
****
```

Add a newline:

```python
'*' * self.width + '\n'
```

Repeat by height:

```python
('*' * self.width + '\n') * self.height
```

### Why include a newline after the final row?

The specification requires every line to end with `\n`.

Automated tests compare exact string values, so the final newline matters.

---

### Picture Size Limit

If either dimension is greater than `50`, the method returns:

```text
Too big for picture.
```

### Why limit the size?

A large shape would generate an unnecessarily large string.

The limit prevents excessive output and keeps the method practical.

---

## Shape Containment

The method:

```python
def get_amount_inside(self, shape):
    amount_across = self.width // shape.width
    amount_down = self.height // shape.height

    return amount_across * amount_down
```

calculates how many copies of another shape fit inside the current shape.

Rotation is not allowed.

---

### Example

```python
Rectangle(15, 10).get_amount_inside(Square(5))
```

Horizontal fit:

```text
15 // 5 = 3
```

Vertical fit:

```text
10 // 5 = 2
```

Total:

```text
3 × 2 = 6
```

---

### Why use floor division?

Partial shapes do not count.

```text
10 / 3 = 3.333...
```

Only three complete shapes fit.

```text
10 // 3 = 3
```

Floor division directly returns the complete-fit count.

---

### Why multiply the two counts?

The smaller shapes form rows and columns.

```text
columns × rows = total
```

---

### Why no rotation?

The project explicitly requires fitting shapes without rotation.

Therefore, the calculation compares:

```text
outer width  with inner width
outer height with inner height
```

It does not test a rotated arrangement.

---

## Usage Example

```python
rect = Rectangle(10, 5)
print(rect.get_area())

rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())

sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

---

## Expected Output

```text
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

---

## Implementation Decisions

### Shared methods are defined in `Rectangle`

Why:

- Reduces duplication
- Keeps calculations consistent
- Makes maintenance easier
- Demonstrates inheritance

---

### Square setters update both dimensions

Why:

- Preserves the rule `width == height`
- Prevents invalid square state
- Keeps inherited calculations reliable

---

### Methods return values

Why:

- Supports testing
- Enables reuse
- Separates calculation from output

---

### `__str__()` reads current attributes

Why:

- Automatically reflects resized shapes
- Improves debugging
- Produces exact required output

---

### Picture generation uses string multiplication

Why:

- Concise
- Efficient
- Easy to understand
- Avoids unnecessary loops

Equivalent loop-based code would be longer:

```python
picture = ''

for _ in range(self.height):
    picture += '*' * self.width + '\n'

return picture
```

---

### Containment uses integer division

Why:

- Only complete shapes count
- Avoids floating-point results
- Matches the physical meaning of fitting

---

## Debugging Lessons

### Misspelled method name

Incorrect:

```python
def set_heigth(self, height):
```

Correct:

```python
def set_height(self, height):
```

Python treats these as different method names.

Calling:

```python
rect.set_height(3)
```

when only `set_heigth()` exists raises:

```text
AttributeError
```

---

### Missing multiplication operator

Incorrect:

```python
2(self.width + self.height)
```

Correct:

```python
2 * (self.width + self.height)
```

Python does not infer multiplication.

---

### Invalid assignment after `return`

Incorrect:

```python
return perimeter = 2 * (self.width + self.height)
```

Correct:

```python
return 2 * (self.width + self.height)
```

or:

```python
perimeter = 2 * (self.width + self.height)
return perimeter
```

---

### Missing method parameter

Incorrect:

```python
def get_amount_inside(self):
```

Correct:

```python
def get_amount_inside(self, shape):
```

The method needs access to the second shape.

---

### Updating only one square dimension

Incorrect:

```python
def set_width(self, side):
    self.width = side
```

Correct:

```python
def set_width(self, side):
    self.width = side
    self.height = side
```

The square must remain valid after every update.

---

### Missing final newline

Incorrect:

```python
'****\n****\n****'
```

Required:

```python
'****\n****\n****\n'
```

Exact formatting matters in tests.

---

## Time and Space Complexity

### Constant-time methods

The following methods use a fixed number of operations:

```text
get_area()
get_perimeter()
get_diagonal()
get_amount_inside()
```

Complexity:

```text
Time:  O(1)
Space: O(1)
```

### Picture generation

For width `w` and height `h`, the method creates approximately:

```text
w × h
```

characters.

Complexity:

```text
Time:  O(w × h)
Space: O(w × h)
```

The output string itself requires proportional memory.

---

## Skills Practiced

### Object-Oriented Programming

- Classes
- Objects
- Constructors
- Instance attributes
- Instance methods
- Inheritance
- Method overriding
- `super()`
- Polymorphism
- Object invariants
- `__str__()`

### Python Fundamentals

- Arithmetic operators
- Exponentiation
- Floor division
- String multiplication
- Formatted strings
- Conditional logic
- Return values
- Standard-library imports

### Geometry

- Area
- Perimeter
- Diagonal
- Pythagorean theorem
- Rectangular packing

### Debugging

- Reading failed tests
- Diagnosing `AttributeError`
- Correcting spelling mistakes
- Fixing method signatures
- Matching exact strings
- Preserving subclass rules

---

## How to Run

From the project directory:

```bash
python main.py
```

On systems where Python 3 uses a separate command:

```bash
python3 main.py
```

No external packages are required.

The project uses only the Python standard library:

```python
import math
```

---

## Project Status

```text
Project: Build a Polygon Area Calculator
Status: Completed
Automated Tests: Passed
Language: Python
Paradigm: Object-Oriented Programming
```
