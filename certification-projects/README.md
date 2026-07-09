# Certification Projects

This directory contains the certification projects completed as part of my
**freeCodeCamp Python Certification** learning path.

These projects are larger than individual workshops or labs. They combine Python
fundamentals, object-oriented programming, data structures, recursion, validation,
exact formatted output, and debugging through automated test feedback.

Each project has its own folder, source file, and project-specific README.

![Python](https://img.shields.io/badge/Python-Certification_Projects-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Projects](https://img.shields.io/badge/Projects_Completed-5-success)
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
  - [5. Implement the Tower of Hanoi Algorithm](#5-implement-the-tower-of-hanoi-algorithm)
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
- Show practical use of Python data structures, recursion, and object-oriented programming.
- Build a portfolio-style record of tested Python projects.
- Explain why each implementation decision was made.

---

## Completed Projects

| # | Project | Primary Concepts | Tests | Status |
| -: | --- | --- | :---: | :---: |
| 1 | Build a User Configuration Manager | Dictionaries, functions, CRUD operations, validation | 27/27 | ✅ |
| 2 | Build a Budget App | Classes, ledgers, transfers, aggregation, text charts | 24/24 | ✅ |
| 3 | Build a Polygon Area Calculator | Inheritance, method overriding, geometry, object representation | 22/22 | ✅ |
| 4 | Build a Hash Table | Hashing, nested dictionaries, collision handling, lookup and deletion | 22/22 | ✅ |
| 5 | Implement the Tower of Hanoi Algorithm | Recursion, lists, stack behavior, exact formatted output | 8/8 | ✅ |

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

- Dictionaries
- Tuple unpacking
- String normalization
- Conditional checks
- Dictionary mutation
- Dictionary deletion
- Iteration through dictionary items
- Human-readable formatted output

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

### 5. Implement the Tower of Hanoi Algorithm

A Python algorithm project that solves the classic **Tower of Hanoi** puzzle
using recursion.

The project focuses on recursive problem solving, list-based stack behavior,
state recording, exact output formatting, and automated test validation.

---

#### Objective

Create a function named `hanoi_solver()` that takes one integer argument and
returns the complete sequence of states required to solve the Tower of Hanoi
puzzle.

Required function:

```python
def hanoi_solver(number_of_disks: int) -> str:
```

The function must:

- Accept a positive number of disks
- Use three rods
- Move all disks from the first rod to the third rod
- Follow the Tower of Hanoi rules
- Solve the puzzle in `2^n - 1` moves
- Include the starting arrangement
- Return all states as a single string
- Put each state on a new line

---

#### Puzzle Rules

The Tower of Hanoi puzzle has three rods and several disks of different sizes.

The rules are:

1. Only one disk can be moved at a time.
2. Only the top-most disk can be moved.
3. A larger disk cannot be placed on top of a smaller disk.

Example starting state for three disks:

```text
[3, 2, 1] [] []
```

Example final state:

```text
[] [] [3, 2, 1]
```

---

#### Core Algorithm

The solution uses recursion.

To move `n` disks from a source rod to a target rod:

```text
1. Move n - 1 disks from source to auxiliary.
2. Move the largest remaining disk from source to target.
3. Move n - 1 disks from auxiliary to target.
```

This pattern repeats until the base case is reached.

The base case happens when there is only one disk:

```python
if disks == 1:
    move_disk(source, target)
    return
```

---

#### Why Recursion Is Used

Recursion is used because the Tower of Hanoi puzzle is naturally made of smaller
versions of the same problem.

For example, solving the puzzle with three disks means:

```text
Move 2 smaller disks away.
Move the largest disk to the target rod.
Move the 2 smaller disks onto the largest disk.
```

The instruction “move 2 smaller disks” is itself another Tower of Hanoi problem.

That is why recursion provides a clean and direct solution.

---

#### Why Lists Are Used

Each rod is represented as a Python list:

```python
rod_1 = [3, 2, 1]
rod_2 = []
rod_3 = []
```

The top-most disk is always the last item in the list.

This makes the list behave like a stack:

```python
disk = source.pop()
target.append(disk)
```

Why this works:

- `pop()` removes the top-most disk.
- `append()` places a disk on top of another rod.
- The list order matches the puzzle structure.
- The built-in list representation matches the required output format.

---

#### State Recording

The project does not only return the final state.

It returns:

- the initial arrangement
- every intermediate move
- the final solved arrangement

Each state is recorded with:

```python
moves.append(f"{rod_1} {rod_2} {rod_3}")
```

The rod order must always remain fixed:

```text
rod_1 rod_2 rod_3
```

This is important because the recursive function changes which rod is acting as
the source, target, or auxiliary rod. The output, however, must always display
the physical rods in the same order.

---

#### Example Output

Calling:

```python
hanoi_solver(3)
```

returns:

```text
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

---

#### Move Count

For `n` disks, the minimum number of moves is:

```text
2^n - 1
```

Because the output includes the starting arrangement, the total number of output
lines is:

```text
2^n
```

Examples:

| Number of disks | Moves | Output lines |
| ---: | ---: | ---: |
| 1 | 1 | 2 |
| 2 | 3 | 4 |
| 3 | 7 | 8 |
| 4 | 15 | 16 |
| 5 | 31 | 32 |

---

#### Concepts Practiced

- Recursive functions
- Base cases
- Helper functions
- Nested functions
- Lists as stacks
- `pop()`
- `append()`
- State recording
- Exact newline formatting
- Mathematical move counting
- Algorithmic decomposition

---

#### Why This Project Matters

This project is an important step beyond basic function writing.

It demonstrates how a difficult-looking problem can be solved by identifying a
repeating structure.

The key insight is:

```text
A large Tower of Hanoi problem is solved by solving smaller Tower of Hanoi problems.
```

This is the essence of recursion.

The project also reinforces that passing automated tests requires both:

- correct algorithmic behavior
- exact output formatting

A solution can be logically correct but still fail if the returned string has the
wrong spacing, wrong rod order, missing initial state, or missing newline
structure.

---

#### Debugging Lessons

Important issues encountered during development:

- Returning an empty string passes the return-type test but fails behavior tests.
- Recording only the initial state is not enough.
- The `move_disk()` helper must be defined before it is called.
- Recursive calls must be correctly indented inside the `solve()` function.
- The final function must return `"\n".join(moves)`.
- The output must always show `rod_1`, `rod_2`, and `rod_3` in fixed order.
- The algorithm must move from `rod_1` to `rod_3` using `rod_2` as the auxiliary rod.

---

#### Test Results

```text
Automated tests: 8/8 passed
Status: Completed
```

---

#### Project Structure

```text
implement_the_tower_of_hanoi_algorithm/
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
├── implement_the_tower_of_hanoi_algorithm/
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
- Lists as stacks
- Lists of dictionaries
- Transaction ledgers
- Key-value configuration data
- Key-value hash-table storage
- Data aggregation
- Object collections
- Buckets for collision handling
- State-history recording

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

### Algorithms and Recursion

- Recursive decomposition
- Base cases
- Recursive calls
- Stack-like behavior
- Minimum-move calculation
- Algorithmic state tracking
- Exponential time complexity
- Exact sequence generation

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
- Rods represented as list stacks

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
- Fixed-order output generation

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
- Exact multi-line algorithm output

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
- Recognizing repeated subproblems
- Choosing recursion when the problem structure requires it

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
- Required functions exist
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
- Recursive algorithms return the full expected sequence
- Multi-line strings match exactly

Important lessons:

- A correct idea can still fail because of exact formatting.
- A misspelled method name creates a different method.
- A missing newline can fail a string-comparison test.
- A subclass may need to override inherited behavior.
- Tests often depend on both output and class structure.
- Hash collisions must preserve all original keys.
- Recursive calls must be correctly indented.
- A function that returns a string can still fail if the string is incomplete.
- Fixing the first actual error is more effective than changing unrelated code.

---

## Progress

| Category | Completed |
| --- | ---: |
| Certification Projects | 5 |
| Dictionary-Based Projects | 1 |
| Object-Oriented Projects | 2 |
| Data-Structure Projects | 1 |
| Algorithm / Recursion Projects | 1 |
| Projects with Automated Test Suites | 5 |
| Projects with Dedicated Documentation | 5 |

```text
Certification Projects Completed: 5
Progress: █████░░░░░
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
        ↓
Tower of Hanoi Algorithm
```

The progression moves from dictionary-based state management to class-based
transaction systems, inheritance-based object design, custom data-structure
implementation, and recursive algorithmic problem solving.

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
Algorithms and Recursion
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


class RecursiveSolver:
    pass
```

The same design principles apply:

- Store structured state
- Validate operations
- Reuse shared behavior
- Protect object invariants
- Handle lookup and deletion safely
- Break large problems into smaller subproblems
- Record intermediate states when needed
- Produce clear technical output

---

## Acknowledgements

The certification-project requirements and automated tests are provided through
the **freeCodeCamp Python Certification**.

The implementations, documentation, debugging notes, repository organization, and
engineering-oriented explanations reflect my independent learning process.
