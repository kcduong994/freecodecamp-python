# Certification Projects

This directory contains the official certification projects completed as part of the
**freeCodeCamp Python Certification**.

These projects combine concepts developed through workshops and labs into larger,
independent implementations. Each project is built from written requirements, validated
against automated tests, documented in its own project directory, and committed as part
of a structured Python learning portfolio.

![Python](https://img.shields.io/badge/Python-Certification_Projects-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Projects](https://img.shields.io/badge/Projects_Completed-3-success)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

---

## Table of Contents

- [Overview](#overview)
- [Completed Projects](#completed-projects)
- [Project Highlights](#project-highlights)
  - [Build a User Configuration Manager](#1-build-a-user-configuration-manager)
  - [Build a Budget App](#2-build-a-budget-app)
  - [Build a Polygon Area Calculator](#3-build-a-polygon-area-calculator)
- [Repository Structure](#repository-structure)
- [Skills Practiced](#skills-practiced)
- [Development Workflow](#development-workflow)
- [Testing and Validation](#testing-and-validation)
- [Progress](#progress)
- [Long-Term Goal](#long-term-goal)
- [Acknowledgements](#acknowledgements)

---

## Overview

Certification projects are larger than individual labs and require several Python concepts
to work together in one complete program.

They are used to practice:

- Interpreting a complete software specification
- Designing classes, functions, and data structures
- Managing object state
- Applying validation rules
- Producing exact formatted output
- Reading and fixing automated test failures
- Refactoring completed code for readability
- Writing technical documentation
- Organizing finished work in a professional repository structure

Unlike guided workshops, certification projects require more independent design decisions.
They demonstrate whether previously learned concepts can be combined into reliable software.

---

## Completed Projects

| # | Project | Primary Concepts | Tests | Status |
| -: | --- | --- | :---: | :---: |
| 1 | Build a User Configuration Manager | Dictionaries, CRUD operations, normalization, validation | Passed | ✅ |
| 2 | Build a Budget App | Classes, ledgers, transfers, aggregation, text charts | 24/24 | ✅ |
| 3 | Build a Polygon Area Calculator | Inheritance, method overriding, geometry, object representation | 22/22 | ✅ |

---

## Project Highlights

### 1. Build a User Configuration Manager

Implemented a configuration-management system using Python dictionaries and reusable
functions.

#### Features

- Add settings
- Update settings
- Delete settings
- Retrieve settings
- Display all settings
- Normalize input
- Validate keys and values
- Prevent invalid configuration changes

#### Concepts Practiced

- Python dictionaries
- Functions
- Parameters and return values
- String manipulation
- Conditional logic
- CRUD-style operations
- Input normalization
- Data validation
- Formatted output

#### Why This Project Matters

Configuration management is a common pattern in real software.

Applications frequently need to store and update values such as:

```text
theme
language
notifications
display mode
user preferences
```

Using a dictionary provides a natural key-value representation:

```python
settings = {
    "theme": "dark",
    "language": "en",
}
```

The project introduced the idea that data should not only be stored, but also
validated and managed through clear operations.

#### Project Structure

```text
build-a-user-configuration-manager/
├── main.py
└── README.md
```

---

### 2. Build a Budget App

Implemented a class-based budget-management system that records transactions in different
spending categories and generates a vertical text chart showing the percentage spent by
category.

#### Features

- Create independent budget categories
- Record deposits
- Record withdrawals
- Calculate the current balance
- Check whether sufficient funds are available
- Transfer money between categories
- Print formatted transaction ledgers
- Calculate spending percentages
- Generate a vertical text-based spending chart

#### Core Design

Each `Category` object contains:

- A category name
- A transaction ledger
- Deposit and withdrawal methods
- Balance calculation
- Fund validation
- Transfers between category objects
- A custom string representation

Example:

```python
food = Category("Food")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(
    15.89,
    "restaurant and more food for dessert",
)

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
```

Expected output:

```text
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

#### Spending Chart

The `create_spend_chart()` function:

1. Calculates withdrawals from each category.
2. Excludes deposits.
3. Calculates each category's percentage of total spending.
4. Rounds each percentage down to the nearest ten.
5. Produces a vertically aligned text chart.

Example:

```python
print(
    create_spend_chart(
        [food, clothing, auto]
    )
)
```

Example output:

```text
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

#### Concepts Practiced

- Python classes and objects
- Instance attributes
- Instance methods
- Lists and dictionaries
- Transaction ledgers
- Default parameters
- Boolean return values
- Balance validation
- Object-to-object transfers
- Data aggregation
- Percentage calculations
- Nested loops
- Fixed-width string formatting
- Vertical text-chart generation

#### Why This Project Matters

The project models a small transaction system.

It demonstrates that an object can:

- Own internal data
- Validate operations
- Interact with other objects
- Produce reports
- Preserve consistent state

The transfer operation is especially important because it coordinates two category objects:

```text
Source category
      ↓ withdrawal
Destination category
      ↓ deposit
Both ledgers updated
```

This is a practical introduction to transaction-oriented object design.

#### Test Coverage

The freeCodeCamp test suite contains 24 automated tests covering:

- Deposits
- Withdrawals
- Balance calculations
- Transfers
- Fund validation
- Category formatting
- Spending percentages
- Chart spacing
- Chart alignment
- Exact output formatting

#### Project Structure

```text
build-a-budget-app/
├── main.py
└── README.md
```

---

### 3. Build a Polygon Area Calculator

Implemented reusable `Rectangle` and `Square` classes using inheritance and method
overriding.

#### Features

- Create rectangle objects
- Create square objects
- Update width and height
- Update square side length
- Calculate area
- Calculate perimeter
- Calculate diagonal length
- Render shapes using `*`
- Calculate how many smaller shapes fit inside another shape
- Display readable shape descriptions

#### Class Relationship

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

The `Square` class inherits the calculations from `Rectangle`, while overriding the
methods that must preserve equal dimensions.

#### Example

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

Expected output:

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

#### Geometry Implemented

```text
Area:
width × height

Perimeter:
2 × (width + height)

Diagonal:
√(width² + height²)
```

#### Shape Containment

The project calculates how many copies of another shape fit without rotation:

```python
amount_across = self.width // shape.width
amount_down = self.height // shape.height

return amount_across * amount_down
```

Floor division is used because partial shapes do not count.

#### Concepts Practiced

- Class inheritance
- Parent and child classes
- `super()`
- Method overriding
- Reusing inherited methods
- Object invariants
- `__str__()`
- Geometry formulas
- Pythagorean theorem
- Floor division
- String multiplication
- Exact text output
- Shape containment logic

#### Why This Project Matters

This project demonstrates how inheritance can reduce duplication.

The shared behavior belongs in `Rectangle`, while the stricter square rule belongs in
`Square`.

```text
Shared geometric behavior → Rectangle
Square-specific constraints → Square
```

It also demonstrates that subclasses may need to override parent methods to preserve valid
state.

For example, changing only the width of a square would make it invalid. Therefore,
`Square.set_width()` updates both dimensions.

#### Debugging Lesson

One important error encountered during development was a misspelled method name:

```python
set_heigth
```

instead of:

```python
set_height
```

Python treats these as different identifiers, which produced an `AttributeError`.

This reinforced the importance of:

- Exact method names
- Reading tracebacks carefully
- Matching the specification precisely
- Testing the operation that fails before changing unrelated code

#### Test Coverage

The project passed 22 automated tests covering:

- Class definitions
- Subclass relationships
- Object identity
- String representations
- Area calculations
- Perimeter calculations
- Diagonal calculations
- State updates
- Square invariants
- Picture generation
- Large-picture limits
- Shape containment

#### Project Structure

```text
build-a-polygon-area-calculator/
├── main.py
└── README.md
```

---

## Repository Structure

```text
certification-projects/
├── build-a-user-configuration-manager/
│   ├── main.py
│   └── README.md
│
├── build-a-budget-app/
│   ├── main.py
│   └── README.md
│
├── build-a-polygon-area-calculator/
│   ├── main.py
│   └── README.md
│
└── README.md
```

Each certification project uses a dedicated directory because it contains:

- A complete Python implementation
- Project-specific documentation
- Independent requirements
- Its own automated test expectations
- Distinct design and debugging lessons

---

## Skills Practiced

### Python Fundamentals

- Variables and data types
- Arithmetic operators
- Comparison operators
- Boolean logic
- Conditional statements
- Loops
- String manipulation
- String formatting
- Function definitions
- Parameters and arguments
- Return values
- Standard-library imports

### Collections and Data Modeling

- Dictionaries
- Lists
- Lists of dictionaries
- Transaction ledgers
- Key-value configuration data
- Data aggregation
- Nested data structures
- Object collections

### Object-Oriented Programming

- Classes and instances
- Constructors
- Instance attributes
- Instance methods
- Object state
- Object interaction
- Encapsulation
- Inheritance
- Parent and child classes
- `super()`
- Method overriding
- Polymorphism
- Object invariants
- `__str__()`

### Validation and Reliability

- Input normalization
- Required-value checks
- Sufficient-funds validation
- Invalid-operation prevention
- Boundary handling
- State preservation
- Exact output validation
- Defensive programming

### Formatting and Reporting

- Fixed-width columns
- Numeric formatting
- Text ledgers
- Vertical charts
- Shape rendering
- Exact spacing
- Newline control
- Human-readable object output

### Problem Solving

- Translating user stories into code
- Breaking large requirements into methods
- Reading automated tests
- Diagnosing tracebacks
- Fixing focused technical causes
- Refactoring after tests pass
- Documenting implementation decisions

---

## Development Workflow

Each certification project follows a structured process:

1. Read the complete specification.
2. Identify required classes, functions, attributes, and outputs.
3. Convert user stories into implementation tasks.
4. Build the smallest working version.
5. Run the automated tests.
6. Inspect the first failing test.
7. Identify the exact cause.
8. Apply a focused correction.
9. Run the tests again.
10. Test edge cases and exact formatting.
11. Refactor the completed solution.
12. Add explanatory comments.
13. Write project-specific documentation.
14. Commit the finished project.

### Feedback Loop

```text
Requirement
    ↓
Implementation
    ↓
Automated test
    ↓
Failure analysis
    ↓
Focused correction
    ↓
Regression check
```

This process reduces unrelated changes and makes debugging more precise.

---

## Testing and Validation

Automated tests are used to verify both behavior and implementation details.

Typical checks include:

- Required classes exist
- Required methods exist
- Method names are exact
- Objects store the expected state
- Calculations return the correct values
- Invalid actions are rejected
- Output formatting is exact
- Inheritance relationships are correct
- Subclass behavior preserves invariants

Important lessons:

- A correct idea can still fail because of exact formatting.
- A misspelled method name creates a different method.
- A missing newline can fail a string-comparison test.
- A subclass may need to override inherited behavior.
- Tests often depend on both output and class structure.
- Fixing the first actual error is more effective than changing unrelated code.

---

## Progress

| Category | Completed |
| --- | ---: |
| Certification Projects | 3 |
| Dictionary-Based Projects | 1 |
| Object-Oriented Projects | 2 |
| Projects with Automated Test Suites | 3 |
| Projects with Dedicated Documentation | 3 |

```text
Certification Projects Completed: 3
Progress: ███░░░░░░░
Status: In Progress
```

Completed sequence:

```text
User Configuration Manager
        ↓
Budget App
        ↓
Polygon Area Calculator
```

The progression moves from dictionary-based state management to class-based transaction
systems and then to inheritance-based object design.

---

## Long-Term Goal

The long-term goal is to develop practical Python skills for:

- Scientific computing
- Data analysis
- Numerical methods
- Environmental data validation
- Coastal-engineering workflows
- Research automation
- Engineering software development

The intended progression is:

```text
Python Fundamentals
        ↓
Independent Problem Solving
        ↓
Data Validation
        ↓
Object-Oriented Programming
        ↓
Inheritance and Reusable Design
        ↓
Scientific Data Processing
        ↓
Numerical Methods
        ↓
Engineering Automation
```

The patterns practiced here can later support engineering entities such as:

```python
class MonitoringStation:
    pass


class Observation:
    pass


class SimulationScenario:
    pass


class ComputationalDomain:
    pass
```

The same design principles apply:

- Store structured state
- Validate operations
- Reuse shared behavior
- Protect object invariants
- Produce clear technical output

---

## Acknowledgements

The certification-project requirements and automated tests are provided through the
**freeCodeCamp Python Certification**.

The implementations, documentation, debugging notes, repository organization, and
engineering-oriented explanations reflect my independent learning process.
