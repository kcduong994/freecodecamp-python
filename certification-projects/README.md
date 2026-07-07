# Certification Projects

This directory contains the certification projects completed as part of my
**freeCodeCamp Python Certification** learning path.

These projects are larger than individual workshops or labs. They combine Python
fundamentals, object-oriented programming, data structures, validation, exact
formatted output, and debugging through automated test feedback.

Each project has its own folder, source file, and project-specific README.

![Python](https://img.shields.io/badge/Python-Certification_Projects-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Projects](https://img.shields.io/badge/Projects_Completed-4-success)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

---

## Table of Contents

- [Overview](#overview)
- [Completed Projects](#completed-projects)
- [Project Highlights](#project-highlights)
  - [1. Build a User Configuration Manager](#1-build-a-user-configuration-manager)
  - [2. Build a Budget App](#2-build-a-budget-app)
  - [3. Build a Polygon Area Calculator](#3-build-a-polygon-area-calculator)
  - [4. Build a Hash Table](#4-build-a-hash-table)
- [Repository Structure](#repository-structure)
- [Skills Practiced](#skills-practiced)
- [Development Workflow](#development-workflow)
- [Testing and Validation](#testing-and-validation)
- [Progress](#progress)
- [Long-Term Goal](#long-term-goal)
- [Acknowledgements](#acknowledgements)

---

## Overview

The certification projects are designed to test whether individual Python
concepts can be combined into complete working programs.

They require more independent implementation than guided lessons. Each project
starts from user stories and must pass an automated test suite.

The main goals of this directory are to:

- Document completed certification projects.
- Preserve the reasoning behind each implementation.
- Track progress across the Python certification path.
- Show practical use of Python data structures and object-oriented programming.
- Build a portfolio-style record of tested Python projects.

---

## Completed Projects

| # | Project | Primary Concepts | Tests | Status |
| -: | --- | --- | :---: | :---: |
| 1 | Build a User Configuration Manager | Dictionaries, functions, CRUD operations, validation | 27/27 | ✅ |
| 2 | Build a Budget App | Classes, ledgers, transfers, aggregation, text charts | 24/24 | ✅ |
| 3 | Build a Polygon Area Calculator | Inheritance, method overriding, geometry, object representation | 22/22 | ✅ |
| 4 | Build a Hash Table | Hashing, nested dictionaries, collision handling, lookup and deletion | 22/22 | ✅ |

---

## Project Highlights

### 1. Build a User Configuration Manager

A Python-based configuration management system developed as part of the
freeCodeCamp Python Certification.

This project implements a simple user settings manager that allows users to add,
update, delete, and display configuration settings.

---

#### Objective

Develop a configuration-management system using Python dictionaries and
functions while applying input validation, string processing, and data
manipulation techniques.

---

#### Features

- Add new settings
- Update existing settings
- Delete existing settings
- Display all settings
- Normalize input using lowercase conversion
- Validate existing keys
- Generate formatted output
- Prevent invalid changes to missing settings

---

#### Example Configuration

```python
test_settings = {
    "theme": "dark",
    "language": "vietnamese",
    "notifications": "enabled",
}
```

This structure stores user preferences as key-value pairs.

The key represents the setting name:

```text
theme
language
notifications
```

The value represents the selected option:

```text
dark
vietnamese
enabled
```

---

#### Functions Implemented

##### `add_setting()`

Adds a new setting to the dictionary.

```python
def add_setting(settings, setting):
```

Example:

```python
add_setting(
    test_settings,
    ("volume", "high")
)
```

Result:

```text
Setting 'volume' added with value 'high' successfully!
```

Why this matters:

- It demonstrates how to insert new key-value pairs.
- It reinforces tuple unpacking.
- It shows how a function can mutate a dictionary intentionally.

---

##### `update_setting()`

Updates an existing setting.

```python
def update_setting(settings, setting):
```

Example:

```python
update_setting(
    test_settings,
    ("theme", "light")
)
```

Result:

```text
Setting 'theme' updated to 'light' successfully!
```

Why this matters:

- Existing data should be changed only when the key exists.
- Validation prevents silent mistakes.
- The function models real configuration-update behavior.

---

##### `delete_setting()`

Removes a setting from the dictionary.

```python
def delete_setting(settings, key):
```

Example:

```python
delete_setting(
    test_settings,
    "theme"
)
```

Result:

```text
Setting 'theme' deleted successfully!
```

Why this matters:

- It practices safe dictionary deletion.
- It reinforces membership checks before mutation.
- It prevents errors when the requested key does not exist.

---

##### `view_settings()`

Displays all user settings.

```python
def view_settings(settings):
```

Output:

```text
Current User Settings:
Theme: dark
Language: vietnamese
Notifications: enabled
```

Why this matters:

- It practices dictionary iteration.
- It formats internal data for human-readable output.
- It separates data storage from presentation.

---

#### Concepts Practiced

##### Dictionaries

Store settings as key-value pairs.

```python
settings["theme"] = "dark"
```

---

##### Tuple Unpacking

Extract values from a tuple.

```python
key, value = setting
```

---

##### String Methods

Normalize and format text.

```python
key.lower()
key.capitalize()
```

---

##### Dictionary Operations

Add values:

```python
settings[key] = value
```

Delete values:

```python
del settings[key]
```

Check existing keys:

```python
if key in settings:
```

---

##### Conditional Statements

```python
if key in settings:
```

```python
if not settings:
```

---

##### Iteration

Loop through dictionary items.

```python
for key, value in settings.items():
```

---

#### Skills Developed

- Dictionary manipulation
- Configuration management
- Input normalization
- Data validation
- Function design
- String processing
- Conditional logic
- Formatted output
- Problem-solving

---

#### Test Results

```text
Automated tests: 27/27 passed
Status: Completed
```

---

#### Project Structure

```text
build-a-user-configuration-manager/
├── main.py
└── README.md
```

---

### 2. Build a Budget App

A Python object-oriented project that implements a simple budget-management
system.

The project uses category objects to record deposits, withdrawals, transfers,
balances, and a text-based spending chart.

---

#### Objective

Create a `Category` class and a `create_spend_chart()` function that satisfy the
project requirements and pass the automated tests.

---

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

---

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

---

#### Ledger Model

The ledger stores transaction dictionaries.

A deposit is stored as a positive amount:

```python
{
    "amount": 1000,
    "description": "initial deposit"
}
```

A withdrawal is stored as a negative amount:

```python
{
    "amount": -10.15,
    "description": "groceries"
}
```

Why this matters:

- A ledger preserves transaction history.
- Balance can be recalculated from the transaction list.
- Spending can be aggregated by category.
- Deposits and withdrawals can be distinguished by sign.

---

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

---

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

---

#### Why This Project Matters

The project models a small transaction system.

It demonstrates that an object can:

- Own internal data
- Validate operations
- Interact with other objects
- Produce reports
- Preserve consistent state

The transfer operation is especially important because it coordinates two
category objects:

```text
Source category
      ↓ withdrawal
Destination category
      ↓ deposit
Both ledgers updated
```

This is a practical introduction to transaction-oriented object design.

---

#### Test Results

```text
Automated tests: 24/24 passed
Status: Completed
```

---

#### Project Structure

```text
build-a-budget-app/
├── main.py
└── README.md
```

---

### 3. Build a Polygon Area Calculator

A Python object-oriented programming project that implements reusable
`Rectangle` and `Square` classes.

The project focuses on inheritance, method overriding, geometry calculations,
text-based shape rendering, object representation, and shape containment.

---

#### Objective

Create a `Rectangle` class and a `Square` subclass while preserving shared
geometry behavior and square-specific constraints.

---

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

---

#### Class Design

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

#### Why Inheritance Is Used

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

---

#### Why `super()` Is Used

The square constructor calls:

```python
super().__init__(side, side)
```

`super()` delegates initialization to the parent class.

This is useful because it:

- Reuses existing initialization logic
- Avoids duplicated assignments
- Makes the class relationship explicit
- Allows future parent-class improvements to be reused
- Keeps initialization consistent

---

#### Why Methods Are Overridden

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

This preserves the square invariant:

```text
width == height
```

---

#### Geometry Implemented

```text
Area:
width × height

Perimeter:
2 × (width + height)

Diagonal:
√(width² + height²)
```

---

#### Text-Based Shape Rendering

The `get_picture()` method renders the shape using asterisks.

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

The final newline is important because the automated tests compare exact string
values.

---

#### Shape Containment

The project calculates how many copies of another shape fit without rotation:

```python
amount_across = self.width // shape.width
amount_down = self.height // shape.height

return amount_across * amount_down
```

Floor division is used because partial shapes do not count.

Example:

```python
Rectangle(15, 10).get_amount_inside(Square(5))
```

Calculation:

```text
15 // 5 = 3
10 // 5 = 2
3 × 2 = 6
```

---

#### Usage Example

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

---

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

---

#### Test Results

```text
Automated tests: 22/22 passed
Status: Completed
```

---

#### Project Structure

```text
build-a-polygon-area-calculator/
├── main.py
└── README.md
```

---

### 4. Build a Hash Table

A Python data-structure project that implements a simple hash table from
scratch.

The project demonstrates key-value storage, hashing, nested dictionaries,
collision handling, safe deletion, and lookup behavior.

---

#### Objective

Create a `HashTable` class that stores key-value pairs by converting string keys
into numeric hash values.

The project uses a simple hashing rule:

```text
hash value = sum of Unicode values of all characters in the key
```

---

#### Features

- Define a `HashTable` class
- Initialize an empty `collection` dictionary
- Compute hash values using `ord()`
- Add key-value pairs
- Store data using a nested dictionary
- Handle hash collisions
- Remove a key-value pair safely
- Look up values by key
- Return `None` when a key does not exist

---

#### Final Data Structure

The hash table stores data in this format:

```python
{
    hashed_key: {
        original_key: value
    }
}
```

Example:

```python
{
    424: {
        'golf': 'sport'
    }
}
```

The outer dictionary uses the computed hash value.

The inner dictionary stores the original key and the associated value.

This is necessary because multiple original keys can produce the same hash
value.

---

#### Hash Function

The `hash()` method converts a string into a numeric value:

```python
def hash(self, string):
    return sum(ord(char) for char in string)
```

Example:

```python
HashTable().hash('golf')
```

Calculation:

```text
ord('g') + ord('o') + ord('l') + ord('f')
= 103 + 111 + 108 + 102
= 424
```

Result:

```text
424
```

---

#### Add Operation

The `add()` method stores a key-value pair.

```python
def add(self, key, value):
    hashed_key = self.hash(key)

    if hashed_key not in self.collection:
        self.collection[hashed_key] = {}

    self.collection[hashed_key][key] = value
```

Flow:

```text
Original key
     ↓
Compute hash
     ↓
Create bucket if missing
     ↓
Store original key and value in bucket
```

Example:

```python
table = HashTable()
table.add('rose', 'flower')

print(table.collection)
```

Result:

```python
{441: {'rose': 'flower'}}
```

---

#### Collision Handling

A collision happens when two different keys produce the same hash value.

Example:

```python
HashTable().hash('fcc')  # 300
HashTable().hash('cfc')  # 300
```

Both keys hash to `300`.

The collection should preserve both values:

```python
{
    300: {
        'fcc': 'coding',
        'cfc': 'chemical'
    }
}
```

The nested dictionary prevents one key-value pair from overwriting another.

---

#### Remove Operation

The `remove()` method deletes only the requested key-value pair:

```python
def remove(self, key):
    hashed_key = self.hash(key)

    if hashed_key in self.collection and key in self.collection[hashed_key]:
        del self.collection[hashed_key][key]
```

The method checks both levels before deleting:

```python
hashed_key in self.collection
```

confirms the bucket exists.

```python
key in self.collection[hashed_key]
```

confirms the original key exists inside the bucket.

This prevents a `KeyError`.

It also prevents deleting an entire collision bucket.

---

#### Lookup Operation

The `lookup()` method returns the value for a key if it exists:

```python
def lookup(self, key):
    hashed_key = self.hash(key)

    if hashed_key in self.collection and key in self.collection[hashed_key]:
        return self.collection[hashed_key][key]

    return None
```

If the key exists:

```python
table = HashTable()
table.add('golf', 'sport')

print(table.lookup('golf'))
```

Output:

```text
sport
```

If the key does not exist:

```python
table = HashTable()

print(table.lookup('golf'))
```

Output:

```python
None
```

---

#### Why This Project Matters

This project introduces an important data-structure concept behind many real
systems.

Hash tables are used for:

- Dictionaries
- Caches
- Indexes
- Lookup tables
- Symbol tables
- Fast key-based retrieval
- Duplicate detection

Python's built-in `dict` uses hash-table principles internally. This project
builds a simplified version to make those mechanics visible.

---

#### Debugging Lessons

Important issues fixed during development:

- `collection` must be `{}`, not `[]`.
- `__init__()` should not take an unnecessary `collection` parameter.
- English instructions are not executable Python code.
- `ord()` is needed to convert characters into Unicode values.
- `add()` must write into `self.collection`, not just `self.key` and `self.value`.
- Collision buckets must be nested dictionaries.
- `remove()` must delete only the specific original key.
- `lookup()` must check both the hash bucket and the original key.
- Missing keys should return `None`, not raise an error.

---

#### Test Results

```text
Automated tests: 22/22 passed
Status: Completed
```

---

#### Project Structure

```text
build-a-hash-table/
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
├── build-a-hash-table/
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
- Built-in functions such as `ord()` and `sum()`

---

### Collections and Data Modeling

- Dictionaries
- Nested dictionaries
- Lists
- Lists of dictionaries
- Transaction ledgers
- Key-value configuration data
- Key-value hash-table storage
- Data aggregation
- Object collections
- Buckets for collision handling

---

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

---

### Data Structures

- Configuration dictionaries
- Transaction ledgers
- Object-based category systems
- Rectangle and square models
- Hash tables
- Hash functions
- Collision buckets
- Key-based lookup
- Safe deletion
- Nested storage models

---

### Validation and Reliability

- Input normalization
- Required-value checks
- Sufficient-funds validation
- Invalid-operation prevention
- Boundary handling
- State preservation
- Exact output validation
- Defensive programming
- Safe lookup of missing keys
- Safe deletion of missing keys

---

### Formatting and Reporting

- Fixed-width columns
- Numeric formatting
- Text ledgers
- Vertical charts
- Shape rendering
- Exact spacing
- Newline control
- Human-readable object output
- Exact dictionary output

---

### Problem Solving

- Translating user stories into code
- Breaking large requirements into methods
- Reading automated tests
- Diagnosing tracebacks
- Fixing focused technical causes
- Refactoring after tests pass
- Documenting implementation decisions
- Explaining why each method exists

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

---

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
- Invalid actions are rejected safely
- Output formatting is exact
- Inheritance relationships are correct
- Subclass behavior preserves invariants
- Data structures match expected dictionary shapes
- Collision cases are handled correctly

Important lessons:

- A correct idea can still fail because of exact formatting.
- A misspelled method name creates a different method.
- A missing newline can fail a string-comparison test.
- A subclass may need to override inherited behavior.
- Tests often depend on both output and class structure.
- Hash collisions must preserve all original keys.
- Fixing the first actual error is more effective than changing unrelated code.

---

## Progress

| Category | Completed |
| --- | ---: |
| Certification Projects | 4 |
| Dictionary-Based Projects | 1 |
| Object-Oriented Projects | 2 |
| Data-Structure Projects | 1 |
| Projects with Automated Test Suites | 4 |
| Projects with Dedicated Documentation | 4 |

```text
Certification Projects Completed: 4
Progress: ████░░░░░░
Status: In Progress
```

Completed sequence:

```text
User Configuration Manager
        ↓
Budget App
        ↓
Polygon Area Calculator
        ↓
Hash Table
```

The progression moves from dictionary-based state management to class-based
transaction systems, inheritance-based object design, and finally custom
data-structure implementation.

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
Data Structures
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


class ResultIndex:
    pass
```

The same design principles apply:

- Store structured state
- Validate operations
- Reuse shared behavior
- Protect object invariants
- Handle lookup and deletion safely
- Produce clear technical output

---

## Acknowledgements

The certification-project requirements and automated tests are provided through
the **freeCodeCamp Python Certification**.

The implementations, documentation, debugging notes, repository organization, and
engineering-oriented explanations reflect my independent learning process.
