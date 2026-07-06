# freecodecamp-python

> A structured Python learning portfolio built through the **freeCodeCamp Python Certification**, with a long-term focus on scientific computing, numerical modeling, and coastal engineering applications.

![Python](https://img.shields.io/badge/Python-Learning-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Projects](https://img.shields.io/badge/Projects_Completed-24-success)
![Workshops](https://img.shields.io/badge/Workshops-13-2563EB)
![Labs](https://img.shields.io/badge/Labs-8-16A34A)
![Certification Projects](https://img.shields.io/badge/Certification_Projects-3-7C3AED)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

This repository documents my progression from Python fundamentals to object-oriented programming, validation, debugging, inheritance, polymorphism, custom exceptions, abstract base classes, strategy-based design, formatted reporting, and larger certification projects.

The immediate goal is to complete the freeCodeCamp Python Certification with correct, readable, well-documented implementations. The long-term objective is to apply Python to coastal and environmental engineering workflows such as hydrodynamic modeling, salinity intrusion analysis, environmental data processing, numerical methods, scientific visualization, and engineering automation.

---

## Table of Contents

- [Repository at a Glance](#repository-at-a-glance)
- [Learning Progress](#learning-progress)
- [Repository Structure](#repository-structure)
- [Workshops](#workshops)
- [Labs](#labs)
- [Certification Projects](#certification-projects)
- [Technical Competencies](#technical-competencies)
- [Selected Project Highlights](#selected-project-highlights)
- [Object-Oriented Learning Progression](#object-oriented-learning-progression)
- [Development Methodology](#development-methodology)
- [Common Debugging Lessons](#common-debugging-lessons)
- [Engineering-Oriented Direction](#engineering-oriented-direction)
- [Current Roadmap](#current-roadmap)
- [Resources](#resources)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

---

## Repository at a Glance

| Area | Purpose | Completed |
| --- | --- | ---: |
| Workshops | Guided projects introducing new Python concepts incrementally | 13 |
| Labs | Independent implementations based on user stories and automated tests | 8 |
| Certification Projects | Larger projects combining multiple programming concepts | 3 |
| **Total** | **Documented Python projects** | **24** |

```text
Workshops              █████████████  13 completed
Labs                   ████████░░   8 completed
Certification Projects ███░░░░░░░   3 completed
Overall                ████████████████████████  24 completed
```

### Current Learning Stage

```text
Python Fundamentals
        ↓
Functions and Validation
        ↓
Collections and Text Processing
        ↓
Debugging Existing Programs
        ↓
Classes and Object Construction
        ↓
Object Composition
        ↓
Properties and Encapsulation
        ↓
Validated Object State
        ↓
Inheritance and Subclassing
        ↓
Polymorphism and Method Overriding
        ↓
Custom Exceptions
        ↓
Abstract Base Classes
        ↓
Interface-Oriented Inheritance
        ↓
Reusable Class Hierarchies and Object Invariants
        ↓
Strategy Pattern and Polymorphic Algorithms
        ↓
Custom Data Structures
        ↓
Linked Lists, Nodes, and References
        ↓
Formatted Reports and Visualizations
```

---

## Learning Progress

### Workshops

| # | Project | Primary Concepts | Status |
| -: | --- | --- | :---: |
| 1 | Report Card Printer | Variables, arithmetic, formatted output | ✅ |
| 2 | Employee Profile Generator | Functions, parameters, strings | ✅ |
| 3 | Bill Splitter | User input, calculations, validation | ✅ |
| 4 | Movie Ticket Booking Calculator | Conditional logic, pricing rules | ✅ |
| 5 | Build a Caesar Cipher | Translation tables, encryption, string processing | ✅ |
| 6 | Build a PIN Extractor | Regular expressions, structured text extraction | ✅ |
| 7 | Build a Medical Data Validator | Dictionaries, validation, error reporting | ✅ |
| 8 | Build a Musical Instrument Inventory | Classes, objects, attributes, methods | ✅ |
| 9 | Build an Email Simulator | Object composition, inbox management, timestamps | ✅ |
| 10 | Build a Salary Tracker | Properties, setters, encapsulation, class state | ✅ |
| 11 | Build a Media Catalogue | Inheritance, polymorphism, custom exceptions, collection filtering | ✅ |
| 12 | Build a Discount Calculator | Abstract base classes, strategy pattern, polymorphic pricing, type hints | ✅ |
| 13 | Build a Linked List | Nodes, references, traversal, insertion, removal, custom data structures | ✅ |

### Labs

| # | Project | Primary Concepts | Status |
| -: | --- | --- | :---: |
| 1 | Travel Weather Planner | Conditions, input, validation, decision logic | ✅ |
| 2 | Apply Discount Function | Functions, calculations, business rules | ✅ |
| 3 | Build an RPG Character | Dictionaries, constraints, structured validation | ✅ |
| 4 | Build a Number Pattern Generator | Loops, ranges, pattern generation | ✅ |
| 5 | Debug an ISBN Validator | Debugging, checksum logic, control flow | ✅ |
| 6 | Build a Planet Class | Classes, exceptions, methods, object representation | ✅ |
| 7 | Build a Game Character Stats Tracker | Properties, getters, setters, encapsulation | ✅ |
| 8 | Build a Player Interface | Abstract base classes, inheritance, random movement, path tracking | ✅ |

### Certification Projects

| # | Project | Primary Concepts | Status |
| -: | --- | --- | :---: |
| 1 | Build a User Configuration Manager | CRUD operations, dictionaries, configuration management | ✅ |
| 2 | Build a Budget App | Classes, ledgers, transfers, validation, reports, charts | ✅ |
| 3 | Build a Polygon Area Calculator | Inheritance, method overriding, geometry, object invariants | ✅ |

---

## Repository Structure

```text
freecodecamp-python/
├── workshops/
│   ├── report-card-printer/
│   ├── employee-profile-generator/
│   ├── bill-splitter/
│   ├── movie-ticket-booking-calculator/
│   ├── build-a-caesar-cipher/
│   ├── build-a-pin-extractor/
│   ├── build-a-medical-data-validator/
│   ├── build-a-musical-instrument-inventory/
│   ├── build-an-email-simulator/
│   ├── build-a-salary-tracker/
│   ├── build-a-media-catalogue/
│   ├── build-a-discount-calculator/
│   ├── build-a-linked-list/
│   └── README.md
│
├── labs/
│   ├── travel-weather-planner.py
│   ├── apply-discount-function.py
│   ├── build-an-rpg-character.py
│   ├── build-a-number-pattern-generator.py
│   ├── debug-an-isbn-validator.py
│   ├── build-a-planet-class.py
│   ├── build-a-game-character-stats-tracker.py
│   ├── build-a-player-interface.py
│   └── README.md
│
├── certification-projects/
│   ├── build-a-user-configuration-manager/
│   │   ├── main.py
│   │   └── README.md
│   │
│   ├── build-a-budget-app/
│   │   ├── main.py
│   │   └── README.md
│   │
│   ├── build-a-polygon-area-calculator/
│   │   ├── main.py
│   │   └── README.md
│   │
│   └── README.md
│
└── README.md
```

### Organization Principles

- **Workshops** use separate directories because they are developed through multiple guided stages and often include dedicated documentation.
- **Labs** are stored as individual Python files because they are compact, independent exercises.
- **Certification projects** use dedicated directories because they combine multiple concepts and require their own project-level documentation.
- The root README provides the overall learning narrative, while subdirectory READMEs document detailed progress in each category.

---

## Workshops

Workshops introduce new concepts through guided implementation.

They are used to:

- Learn unfamiliar syntax
- Observe implementation patterns
- Practice one concept at a time
- Build confidence before independent work
- Develop reusable programming habits

The workshop sequence has progressed from basic formatting and functions to regular expressions, structured validation, object composition, properties, setters, controlled class state, inheritance, polymorphism, custom exceptions, abstract base classes, strategy-based software design, and custom reference-based data structures.

The latest completed workshop, **Build a Linked List**, introduced custom node objects, a `head` reference, `.next` links, linked-list traversal, insertion at the end of a chain, removal by link reassignment, and manual length tracking.

Detailed workshop documentation is maintained in [`workshops/README.md`](workshops/README.md).

---

## Labs

Labs require independent interpretation of requirements and user stories.

They are used to practice:

- Translating specifications into code
- Designing solutions without step-by-step instructions
- Mapping automated tests to implementation tasks
- Diagnosing failed tests
- Handling boundary conditions
- Matching exact output formats
- Refactoring final solutions for clarity

The latest completed lab, **Build a Player Interface**, introduced abstract base classes, required subclass methods, parent-constructor reuse with `super()`, tuple-based movement vectors, random movement selection, and path-history tracking.

Detailed lab documentation is maintained in [`labs/README.md`](labs/README.md).

---

## Certification Projects

Certification projects combine multiple Python concepts into larger implementations.

### Build a User Configuration Manager

A dictionary-based settings manager supporting:

- Add
- Update
- Delete
- Retrieve
- Normalize
- Validate
- Display

The project reinforced CRUD-style workflows, reusable functions, and consistent configuration handling.


### Build a Polygon Area Calculator

Implemented a reusable geometric class hierarchy with a `Rectangle` parent class and a
`Square` subclass.

The completed certification project includes:

- Width and height state
- Rectangle and square construction
- Area calculation
- Perimeter calculation
- Diagonal calculation
- Text-based shape rendering
- Shape-containment calculation
- Parent-constructor reuse with `super()`
- Method overriding
- Custom `__str__()` representations

Class relationship:

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

The square constructor reuses rectangle initialization:

```python
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
```

The square overrides both dimension setters because changing only one dimension would
invalidate the square:

```python
def set_width(self, side):
    self.width = side
    self.height = side


def set_height(self, side):
    self.width = side
    self.height = side
```

This protects the object invariant:

```text
width == height
```

Geometry methods are implemented once in the parent class:

```python
def get_area(self):
    return self.width * self.height


def get_perimeter(self):
    return 2 * (self.width + self.height)


def get_diagonal(self):
    return math.sqrt(
        self.width ** 2 + self.height ** 2
    )
```

The picture method uses string multiplication:

```python
def get_picture(self):
    if self.width > 50 or self.height > 50:
        return "Too big for picture."

    return ("*" * self.width + "\n") * self.height
```

Containment is calculated without rotation:

```python
def get_amount_inside(self, shape):
    return (
        self.width // shape.width
    ) * (
        self.height // shape.height
    )
```

Calculation flow:

```text
Outer width // inner width
            ↓
Outer height // inner height
            ↓
Multiply complete horizontal and vertical fits
            ↓
Return total contained shapes
```

Example:

```python
rect = Rectangle(16, 8)
square = Square(4)

print(rect.get_amount_inside(square))
```

Expected output:

```text
8
```

This certification project strengthened:

- Inheritance
- Parent-constructor reuse
- Method overriding
- Object invariants
- Reusable calculations
- Pythagorean geometry
- Floor division
- String multiplication
- Exact output formatting
- Object-to-object method interaction

---

### Build a Budget App

A class-based financial tracking application supporting:

- Deposits
- Withdrawals
- Transfers
- Balance checks
- Transaction ledgers
- Formatted reports
- Spending percentages
- Text-based charts

The project passed all required automated tests:

```text
Automated tests: 24/24 passed
Status: Completed
```


### Build a Polygon Area Calculator

An inheritance-based geometry application featuring:

- A reusable `Rectangle` parent class
- A specialized `Square` subclass
- Area, perimeter, and diagonal calculations
- Parent-constructor reuse with `super()`
- Method overriding to preserve square dimensions
- Text-based shape rendering
- Shape-containment calculations
- Custom string representations

The project passed all required automated tests:

```text
Automated tests: 22/22 passed
Status: Completed
```

The project reinforced the principle that a subclass should reuse shared behavior while
protecting its own stricter rules. `Square` inherits the rectangle calculations, but overrides
dimension setters so that `width == height` remains true.

Detailed certification-project documentation is maintained in
[`certification-projects/README.md`](certification-projects/README.md).

---

## Technical Competencies

### Python Fundamentals

- Variables and data types
- Assignment and arithmetic
- User input and output
- String formatting
- Multi-line output
- Naming conventions
- Indentation and syntax
- Type hints
- Docstrings
- Code comments
- Main execution guards

### Functions and Program Design

- Function definitions
- Positional and keyword arguments
- Default parameters
- Return values
- Reusable calculations
- Separation of responsibilities
- Guard clauses
- Early returns
- Small, testable units of logic
- Constructor-based dependency injection
- Strategy orchestration through dedicated engine classes

### Programming Logic

- `if`, `elif`, and `else`
- Comparison and membership operators
- Boolean logic
- Nested conditions
- State-dependent behavior
- Boundary-condition handling
- Business-rule validation
- Controlled program flow
- Geometry-based condition handling
- Complete-fit calculations with floor division

### Collections and Structured Data

- Lists
- Dictionaries
- Nested collections
- Lists of dictionaries
- Class-level dictionaries
- Membership tests
- Key lookup
- Data aggregation
- Filtering
- Summation
- Record-based modeling
- List comprehensions
- Mixed collections of related objects
- Filtering objects by exact class or subclass type
- Storing interchangeable strategy objects in a list
- Aggregating candidate numeric results
- Selecting an optimal result with `min()`
- Passing related objects into methods
- Comparing outer and inner object dimensions
- Storing two-dimensional movement vectors as tuples
- Recording position history in lists
- Extending movement sets with `list.extend()`
- Building custom node-based data structures
- Maintaining a linked-list `head` reference
- Connecting objects through `.next` references
- Updating links during insertion and removal
- Maintaining a manual collection length

### Data Structures

- Custom linked lists
- Nested `Node` classes
- Node objects storing elements
- Reference-based object chains
- The `head` reference
- The `next` reference
- Empty-list detection
- Appending nodes to the end of a linked list
- Removing the first matching node
- Bypassing removed nodes through reference reassignment
- Handling head-node removal
- Handling missing elements safely
- Comparing linked lists with built-in Python lists

### Loops and Iteration

- `for` loops
- `range()`
- `enumerate()`
- Nested loops
- Descending ranges
- Pattern generation
- Numbered output
- Iterative text construction
- Dynamic row and column generation
- String repetition for shape rendering
- Random selection with `random.choice()`
- Traversal with `while` loops
- Stopping traversal at `None`
- Moving from one node to the next through object references

### Text Processing

- String indexing
- String slicing
- `split()`
- Translation tables
- Caesar cipher logic
- Multi-line parsing
- Fixed-width formatting
- Alignment
- Truncation
- Exact whitespace control

### Regular Expressions

- `re.search()`
- `re.fullmatch()`
- Pattern matching
- Structured extraction
- Formatted-text validation
- Multi-line record processing

### Data Validation

- `isinstance()`
- Multiple-type checks
- `hasattr()`
- Required-key validation
- Empty-string validation
- Range validation
- Sequence validation
- Object-state validation
- Invalid-record detection
- Minimum-value enforcement
- Duplicate-state prevention
- Downward-transition prevention

### Error and Exception Handling

- `try` and `except`
- `raise`
- `TypeError`
- `ValueError`
- `AttributeError`
- `IndexError`
- `KeyError`
- Custom exception classes
- Inheriting from `Exception`
- Passing messages through `super().__init__()`
- Storing the invalid object inside an exception
- Catching multiple exception types
- Defensive programming
- Validation before mutation
- Explicit error messages

### Object-Oriented Programming

- Classes and instances
- `__init__()`
- Instance attributes
- Class attributes
- Instance methods
- Parent and child classes
- Inheritance and subclassing
- Reusing parent initialization with `super()`
- Method overriding
- Polymorphism
- Exact type checks with `type() is`
- Inheritance-aware checks with `isinstance()`
- Object composition
- Passing objects as arguments
- Object interaction
- Encapsulation
- Internal backing attributes
- `@property`
- Property setters
- Read-only properties
- Controlled state mutation
- Object invariants
- `__str__()`
- `__repr__()`
- Transaction-based object models
- State-aware validation
- Abstract base classes with `ABC`
- Required subclass interfaces with `@abstractmethod`
- Strategy-pattern implementations
- Runtime polymorphism through a shared contract
- Separation of algorithm selection from algorithm implementation
- Abstract parent classes for shared state and behavior
- Concrete subclasses that implement required methods
- Parent-constructor reuse with `super()`
- Interface-oriented inheritance
- Reusable geometric parent classes
- Subclass invariants such as `width == height`
- Method overriding to preserve valid subclass state
- Nested classes for implementation details
- Reference-based relationships between objects
- Object chains created through attributes

### Date and Time

- `datetime.datetime.now()`
- Timestamp storage
- `strftime()`
- Date-time format codes
- Timestamp display in object representations

### Formatting and Text-Based Visualization

- Fixed-width columns
- Centered headings
- Left and right alignment
- Two-decimal-place formatting
- Vertical percentage axes
- Horizontal chart axes
- Character-based bars
- Vertical labels
- Precise newline handling
- Asterisk-based geometric rendering
- Shape dimensions represented through formatted strings

### Debugging and Testing

- Reading tracebacks
- Syntax-error diagnosis
- Indentation-error correction
- Name-error diagnosis
- Missing-argument detection
- Attribute initialization issues
- Off-by-one detection
- Index-boundary debugging
- Dictionary-key debugging
- Exact-output test failures
- Automated test interpretation
- Edge-case testing
- Incremental correction
- Diagnosing parameter-name mismatches
- Distinguishing built-in functions from collection methods
- Debugging variable scope and execution-order problems
- Distinguishing tuple concatenation from coordinate arithmetic
- Diagnosing incomplete abstract subclass implementations
- Verifying inherited initialization and state
- Diagnosing misspelled method names
- Preserving subclass invariants after state changes
- Debugging exact newline requirements in generated pictures
- Debugging assignment direction in linked structures
- Checking `None` with `is None` and `is not None`
- Avoiding infinite traversal loops
- Updating `head` correctly when removing the first node

---

## Selected Project Highlights



### Build a Linked List

Implemented a custom linked list using a nested `Node` class and object references.

The completed workshop includes:

- A `LinkedList` class
- A nested `Node` class
- A `length` counter
- A `head` reference
- An `is_empty()` method
- An `add()` method
- A `remove()` method
- Node traversal through `.next`
- Safe handling of missing elements
- Removal from the head of the list
- Removal from the middle or end of the list

The `Node` class stores one element and a reference to the next node:

```python
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
```

The linked list starts empty:

```python
def __init__(self):
    self.length = 0
    self.head = None
```

The `head` attribute points to the first node. If the list is empty, `head` is
`None`.

Adding a node follows this flow:

```text
Create a new node
        ↓
Check whether the list is empty
        ↓
If empty, assign the new node to head
        ↓
If not empty, traverse to the final node
        ↓
Connect the final node to the new node
        ↓
Increase length
```

The empty-list case requires this assignment:

```python
self.head = node
```

The direction matters. `self.head = node` makes the list point to the new node.
The reverse assignment, `node = self.head`, would only overwrite the local
variable and would not update the linked list.

For a non-empty list, the code traverses the chain until it reaches the final
node:

```python
while current_node.next is not None:
    current_node = current_node.next
```

This checks whether another node exists after the current one. The condition uses
`is not None` because `None` should be checked by identity in Python.

Removal uses both `previous_node` and `current_node`:

```python
previous_node = None
current_node = self.head
```

The search loop moves forward until the target element is found or the end of
the list is reached:

```python
while current_node is not None and current_node.element != element:
    previous_node = current_node
    current_node = current_node.next
```

If the element is not found, the method returns without changing the list:

```python
if current_node is None:
    return
```

If the node to remove is not the head, the previous node bypasses it:

```python
previous_node.next = current_node.next
```

If the node to remove is the head, the list entry point must move forward:

```python
self.head = current_node.next
```

Structure after adding two elements:

```text
LinkedList
    ├── length = 2
    └── head ──▶ Node(element=1)
                   └── next ──▶ Node(element=2)
                                   └── next ──▶ None
```

Example:

```python
my_list = LinkedList()
print(my_list.is_empty())

my_list.add(1)
my_list.add(2)

print(my_list.is_empty())
print(my_list.length)

my_list.remove(1)
print(my_list.length)
```

Expected output:

```text
True
False
2
1
```

This workshop strengthened:

- Custom data structures
- Nested classes
- Object references
- Linked nodes
- Manual length tracking
- Linked-list traversal
- Reference assignment
- Head-node handling
- Node removal by bypassing links
- `None` checks with `is not None`
- The difference between a built-in list and a custom linked structure

---

### Build a Discount Calculator

Implemented a strategy-driven pricing engine that evaluates multiple discount
algorithms and returns the lowest valid price.

The completed workshop includes:

- A `Product` model
- An abstract `DiscountStrategy` interface
- `PercentageDiscount`
- `FixedAmountDiscount`
- `PremiumUserDiscount`
- A `DiscountEngine` responsible for evaluating strategies
- Type hints for products, prices, user tiers, and strategy collections
- A main execution guard
- Currency output formatted to two decimal places

The shared strategy contract is defined with `ABC` and `@abstractmethod`:

```python
class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(
        self,
        product: Product,
        user_tier: str,
    ) -> bool:
        pass

    @abstractmethod
    def apply_discount(
        self,
        product: Product,
    ) -> float:
        pass
```

Each concrete strategy implements the same interface while preserving its own
business rule:

```text
PercentageDiscount
        ↓
Valid only up to 70%

FixedAmountDiscount
        ↓
Valid only when the amount is below 90% of the original price

PremiumUserDiscount
        ↓
Valid only for premium users
```

The engine receives the strategies through its constructor:

```python
strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount(),
]

engine = DiscountEngine(strategies)
```

Calculation flow:

```text
Original price
      ↓
Evaluate each strategy
      ↓
Check is_applicable(...)
      ↓
Apply valid discounts
      ↓
Collect candidate prices
      ↓
Return min(prices)
```

Example:

```python
product = Product("Wireless Mouse", 50.0)
user_tier = "Premium"

best_price = engine.calculate_best_price(
    product,
    user_tier,
)

print(
    f"Best price for {product.name} "
    f"for {user_tier} user: ${best_price:.2f}"
)
```

Expected output:

```text
Best price for Wireless Mouse for Premium user: $40.00
```

This workshop strengthened:

- Abstract interface design
- Runtime polymorphism
- Strategy-pattern architecture
- Dependency injection
- Separation of responsibilities
- Business-rule encapsulation
- Candidate-result comparison
- Type annotations
- Exact monetary formatting

---

### Build a Media Catalogue

Built a catalogue that stores, validates, filters, and displays movies and television series.

The completed workshop includes:

- A `Movie` parent class
- A `TVSeries` child class
- A `MediaCatalogue` management class
- A custom `MediaError` exception
- Shared validation through inheritance
- Parent-constructor reuse with `super().__init__()`
- Overridden `__str__()` methods
- Mixed collections containing parent and child objects
- Separate filtering methods for movies and TV series
- Conditional, numbered catalogue output

Example:

```python
catalogue = MediaCatalogue()

movie = Movie(
    "The Matrix",
    1999,
    "The Wachowskis",
    136,
)

series = TVSeries(
    "Breaking Bad",
    2008,
    "Vince Gilligan",
    47,
    5,
    62,
)

catalogue.add(movie)
catalogue.add(series)
print(catalogue)
```

Class relationship:

```text
Movie
  ↓
TVSeries inherits shared Movie behavior
  ↓
MediaCatalogue stores both object types
  ↓
Filtering methods separate movies and TV series
```

The workshop also clarified the difference between these checks:

```python
isinstance(item, Movie)
```

This accepts both `Movie` objects and instances of subclasses such as `TVSeries`.

```python
type(item) is Movie
```

This accepts only objects created directly from the `Movie` class.

Custom exception flow:

```text
Unsupported object
        ↓
MediaCatalogue.add()
        ↓
Raise MediaError(message, object)
        ↓
Catch the exception
        ↓
Report both the message and invalid object
```

This workshop introduced inheritance, method overriding, polymorphic string representations, custom exception design, and type-based collection filtering.

---

### Build a Salary Tracker

Developed an employee salary-tracking system with:

- A class-level salary table
- Validated `name`, `level`, and `salary` properties
- Automatic salary updates during promotion
- Protection against invalid or downward level changes
- Protection against salaries below the level minimum
- Custom `__str__()` and `__repr__()`
- Explicit exception messages

Example:

```python
charlie_brown = Employee(
    "Charlie Brown",
    "trainee",
)

print(charlie_brown)
print(f"Base salary: ${charlie_brown.salary}")

charlie_brown.level = "junior"
```

State transition:

```text
Assign new level
      ↓
Validate type
      ↓
Check supported level
      ↓
Reject duplicates
      ↓
Reject downward movement
      ↓
Look up base salary
      ↓
Update salary through setter
      ↓
Store level
```

This workshop introduced disciplined object-oriented design in which the object is responsible for preserving its own valid state.

---


### Build a Player Interface

Implemented an extensible movement system using an abstract parent class and a
concrete pawn subclass.

The completed lab includes:

- An abstract `Player` class
- A concrete `Pawn` class
- Shared player state
- Random movement selection
- Two-dimensional coordinate updates
- Path-history tracking
- An abstract `level_up()` contract
- Diagonal movement upgrades

The parent class defines the shared state:

```python
class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
```

The shared movement logic is implemented once in the parent class:

```python
def make_move(self):
    move = random.choice(self.moves)

    self.position = (
        self.position[0] + move[0],
        self.position[1] + move[1],
    )

    self.path.append(self.position)
    return self.position
```

The parent class requires every concrete player type to implement its own
level-up behavior:

```python
@abstractmethod
def level_up(self):
    pass
```

The `Pawn` subclass reuses the common initialization and defines four initial
movement vectors:

```python
class Pawn(Player):
    def __init__(self):
        super().__init__()

        self.moves = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0),
        ]
```

After leveling up, the pawn receives four diagonal movements:

```python
def level_up(self):
    self.moves.extend([
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ])
```

Class relationship:

```text
Player (abstract)
    ├── position
    ├── path
    ├── make_move()
    └── level_up() contract
              ↓
Pawn (concrete)
    ├── cardinal movements
    └── diagonal level-up movements
```

Movement flow:

```text
Current position
      ↓
Choose a random movement vector
      ↓
Add x and y offsets
      ↓
Update position
      ↓
Append position to path
      ↓
Return the new position
```

This lab strengthened:

- Abstract base classes
- Abstract methods
- Inheritance
- Parent-constructor reuse
- Concrete subclass implementation
- Random selection
- Tuple-based coordinates
- Movement-vector arithmetic
- Path-history tracking
- Interface-oriented design

---

### Build a Game Character Stats Tracker

Created a `GameCharacter` class with:

- Read-only `name`
- Validated `health`
- Validated `mana`
- Read-only `level`
- A `level_up()` method
- A formatted `__str__()` representation

Range constraints:

```text
0 ≤ health ≤ 100
0 ≤ mana ≤ 50
```

Example:

```python
hero = GameCharacter("Kratos")

hero.health -= 30
hero.mana -= 10

print(hero)

hero.level_up()
print(hero)
```

Expected output:

```text
Name: Kratos
Level: 1
Health: 70
Mana: 40

Kratos leveled up to 2!

Name: Kratos
Level: 2
Health: 100
Mana: 50
```

The implementation separates internal storage from public access:

```python
@property
def health(self):
    return self._health


@health.setter
def health(self, value):
    if value < 0:
        self._health = 0
    elif value > 100:
        self._health = 100
    else:
        self._health = value
```

This lab reinforced encapsulation, property-based validation, and controlled object state.

---

### Build an Email Simulator

Built a small object-oriented application with three cooperating classes:

```text
User
 ├── owns an Inbox
 └── sends an Email
          ↓
    receiver's Inbox
          ↓
      stores Email
```

Supported operations include:

- Sending email
- Storing sender and receiver data
- Recording timestamps
- Tracking read status
- Listing messages
- Reading messages
- Deleting messages
- Validating message numbers

This workshop marked the transition from isolated classes to interacting objects with distributed responsibilities.

---

### Build a Medical Data Validator

Validated structured records using:

- Lists of dictionaries
- Required fields
- Type checking
- Regular expressions
- Invalid-record reporting
- Clear validation messages

This project demonstrated how Python can inspect and protect the integrity of record-based datasets.

---

### Debug an ISBN Validator

Repaired an existing validation algorithm by analyzing:

- Program flow
- Index handling
- Off-by-one errors
- Input normalization
- Checksum logic
- Exception behavior

The lab strengthened the ability to understand and correct an unfamiliar implementation.

---

### Build a Budget App

Developed a reusable `Category` class with:

- Transaction ledgers
- Deposits
- Withdrawals
- Transfers
- Balance calculations
- Fund checks
- Fixed-width output
- Spending percentages
- Vertical text-based charts

Example transaction flow:

```text
Category object
      ↓
stores ledger entries
      ↓
calculates current balance
      ↓
validates withdrawals
      ↓
transfers funds to another Category
      ↓
produces formatted financial output
```

The project combines object-oriented programming, validation, aggregation, percentage calculations, nested loops, and exact string formatting.

---

## Object-Oriented Learning Progression

Object-oriented concepts were introduced incrementally:

```text
MusicalInstrument
        ↓
One class with attributes and methods
        ↓
Planet
        ↓
Validation, exceptions, and __str__()
        ↓
Email + User + Inbox
        ↓
Object composition and interaction
        ↓
Employee
        ↓
Properties, setters, and coordinated attributes
        ↓
GameCharacter
        ↓
Read-only properties and clamped state
        ↓
Player + Pawn
        ↓
Abstract inheritance, shared movement logic, and required subclass behavior
        ↓
Movie + TVSeries + MediaCatalogue
        ↓
Inheritance, polymorphism, filtering, and custom exceptions
        ↓
DiscountStrategy + DiscountEngine
        ↓
Abstract interfaces, strategy objects, and best-result selection
        ↓
LinkedList + Node
        ↓
Reference-based data structures, traversal, and link updates
        ↓
Rectangle + Square
        ↓
Reusable geometry, method overriding, and subclass invariants
        ↓
Category
        ↓
Ledgers, transfers, reporting, and visualization
```

### Concepts Added at Each Stage

| Stage | New Capability |
| --- | --- |
| MusicalInstrument | Basic class construction |
| Planet | Validation and readable representation |
| Email Simulator | Multiple interacting classes |
| Salary Tracker | Encapsulation and controlled state transitions |
| Game Character Tracker | Read-only properties and bounded attributes |
| Player Interface | Abstract inheritance, shared behavior, movement vectors, and path tracking |
| Media Catalogue | Inheritance, polymorphism, custom exceptions, and collection filtering |
| Discount Calculator | Abstract interfaces, strategy pattern, dependency injection, and runtime polymorphism |
| Linked List | Custom node objects, references, traversal, insertion, and removal |
| Polygon Area Calculator | Reusable geometry, method overriding, object invariants, and containment logic |
| Budget App | Transaction systems, cross-object transfers, reporting |

This progression establishes a foundation for maintainable engineering software. The Linked List workshop adds an important lower-level perspective: objects can be connected directly through references rather than stored only inside built-in containers.

---

## Development Methodology

Each project follows a repeatable implementation process.

### Standard Workflow

1. Read the full specification.
2. Identify required classes, functions, inputs, outputs, and constraints.
3. Convert user stories into implementation tasks.
4. Build the smallest working version.
5. Run automated tests.
6. Inspect the first failing test.
7. Identify the exact technical cause.
8. Apply a focused correction.
9. Test boundary values and invalid inputs.
10. Refactor for readability.
11. Preserve required behavior while improving readability.
12. Add comments, docstrings, and README documentation.
13. Commit the completed project.

### Test-Driven Feedback Loop

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

### Code Quality Principles

- Prefer descriptive names.
- Keep indentation and formatting consistent.
- Separate data validation from presentation.
- Return reusable values instead of printing unnecessarily.
- Preserve valid object state after every public operation.
- Reuse property setters when appropriate.
- Avoid duplicate logic.
- Match required output exactly.
- Add comments that explain intent.
- Refactor only after the behavior is correct.
- Preserve the original workshop contract when documenting completed code.
- Prefer interfaces that allow new behavior without modifying existing orchestration logic.
- Keep shared behavior in parent classes and subclass-specific behavior in concrete classes.
- Use abstract methods when every subclass must provide a required operation.
- Override inherited methods when a subclass must enforce stricter state rules.
- Preserve object invariants after every public state-changing operation.

---

## Common Debugging Lessons

| Error | Typical Cause | Practical Lesson |
| --- | --- | --- |
| `SyntaxError` | Invalid syntax or incomplete statements | Check the exact failing line first |
| `IndentationError` | Incorrect block alignment | Verify class, method, and branch indentation |
| `NameError` | Undefined variable or function | Check scope and spelling |
| `TypeError` | Wrong argument count or data type | Compare the call with the function signature |
| `AttributeError` | Attribute used before initialization | Review constructor and setter order |
| `ValueError` | Valid type but invalid content | Separate type validation from value validation |
| `IndexError` | Invalid sequence position | Review zero-based indexing and boundaries |
| `KeyError` | Missing dictionary key | Validate keys before access |
| Test mismatch | Exact output differs | Inspect whitespace, punctuation, and newlines |
| Logic failure | Conditions overlap or execute incorrectly | Use `if` / `elif` / `else` for exclusive branches |

### Important Lessons Reinforced

- A small whitespace difference can fail an exact-output test.
- Two independent `if` statements are not equivalent to `if` / `elif` / `else`.
- Initialization order matters when setters depend on existing attributes.
- Constructors must be named exactly `__init__()`.
- Instance methods require `self` as their first parameter.
- A method must explicitly `return` a value when its result is needed.
- `isinstance()` includes subclasses, while `type() is` checks the exact class.
- Custom exceptions must receive every argument declared by their constructor.
- Automated tests often check both behavior and implementation structure.
- A readable object representation greatly improves debugging.
- Parameter names must match the identifiers used inside the method body.
- Built-in functions such as `min(prices)` are different from collection methods.
- Instance methods must be called through an object, such as `engine.calculate_best_price(...)`.
- Variables must be defined before they are passed into constructors.
- Code inside `if __name__ == '__main__':` must remain consistently indented.
- Abstract subclasses must implement every required abstract method before they can be instantiated.
- Adding tuples concatenates them; coordinate arithmetic requires adding x and y components separately.
- Tests for parent-class behavior may rely on a concrete subclass being instantiable.
- Shared initialization should be reused through `super().__init__()` when required.
- Method names must match the specification exactly; `set_heigth` and `set_height` are different identifiers.
- Floor division is appropriate when only complete contained objects should be counted.
- Generated text pictures may require a newline after the final row.
- A subclass setter may need to update multiple attributes to preserve a valid invariant.
- Assignment direction matters in reference-based structures: `self.head = node` and `node = self.head` do not mean the same thing.
- `None` should be checked with `is None` or `is not None`.
- Traversal loops must advance to the next node to avoid infinite loops.
- Removing the head node requires updating `self.head`.
- Removing a non-head node requires updating `previous_node.next`.
- A manual `length` counter must be updated after successful insertion or removal.

---

## Engineering-Oriented Direction

This repository is the programming foundation for future coastal and environmental engineering software.

### Intended Applications

- Hydrodynamic model pre-processing
- Salinity-intrusion analysis
- Water-level and tide processing
- Environmental dataset validation
- Numerical-model result analysis
- Calibration and validation metrics
- Scientific visualization
- Engineering automation
- Research reproducibility
- AI-assisted technical workflows

### Planned Engineering Project Structure

```text
coastal-engineering-python/
├── tide-data-analysis/
├── water-level-processing/
├── salinity-analysis/
├── hydrodynamic-result-processing/
├── model-validation-metrics/
├── environmental-data-cleaning/
├── numerical-methods/
└── scientific-visualization/
```

### Potential Engineering Classes

```python
class MonitoringStation:
    pass


class Observation:
    pass


class WaterLevelObservation(Observation):
    pass


class SalinityObservation(Observation):
    pass


class SimulationScenario:
    pass


class HydrodynamicModel:
    pass
```

Possible interaction:

```text
MonitoringStation
        ↓
produces Observation subclasses
        ↓
ObservationCatalogue stores and filters them
        ↓
SimulationScenario references selected observations
        ↓
HydrodynamicModel produces results
        ↓
Validation tools evaluate model performance
```

A property-based validation pattern can protect engineering parameters:

```python
class MonitoringStation:
    def __init__(self, station_id):
        self._station_id = station_id
        self._salinity = 0.0

    @property
    def salinity(self):
        return self._salinity

    @salinity.setter
    def salinity(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("'salinity' must be numeric.")

        if value < 0:
            raise ValueError("'salinity' cannot be negative.")

        self._salinity = value
```

This is directly related to the validation and encapsulation patterns practiced in the Salary Tracker and Game Character Stats Tracker.

The Strategy pattern from the Discount Calculator also maps naturally to engineering software. Different calibration metrics, numerical solvers, boundary-condition treatments, or model-selection rules can implement a shared interface and be evaluated by one orchestration engine.

The Player Interface lab adds another directly relevant pattern: an abstract parent class can define shared state and movement logic, while concrete subclasses provide specialized behavior. The same structure can be used for particles, drifters, monitoring platforms, or multiple numerical-model types.


A strategy-oriented engineering design could look like this:

```python
class ValidationMetric(ABC):
    @abstractmethod
    def calculate(self, observed, simulated):
        pass


class RMSEMetric(ValidationMetric):
    def calculate(self, observed, simulated):
        pass


class NSEMetric(ValidationMetric):
    def calculate(self, observed, simulated):
        pass
```

This allows a validation engine to compare interchangeable metrics without
hard-coding the details of each calculation.


A trajectory-oriented engineering model could use the same pattern:

```python
class MovingEntity(ABC):
    def __init__(self):
        self.position = (0.0, 0.0)
        self.path = [self.position]

    @abstractmethod
    def update_position(self):
        pass


class SurfaceDrifter(MovingEntity):
    def update_position(self):
        pass


class NumericalParticle(MovingEntity):
    def update_position(self):
        pass
```

This structure separates:

- Shared trajectory state
- Common path-history storage
- Specialized movement or transport rules

It can later support particle tracking, Lagrangian transport, sensor trajectories,
or model-specific movement behavior.


The geometry and containment patterns from the Polygon Area Calculator can also support
engineering software.

A simplified computational-domain hierarchy could look like this:

```python
class RectangularDomain:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class SquareDomain(RectangularDomain):
    def __init__(self, side):
        super().__init__(side, side)
```

Possible applications include:

- Rectangular numerical-model domains
- Square grid patches
- Survey-area subdivision
- Raster-cell allocation
- Laboratory-flume dimensions
- Sensor-layout planning
- Domain-packing calculations

The same invariant-preservation principle applies to engineering objects. If a square grid
patch must always have equal dimensions, every public update operation should preserve that
relationship.


The Linked List workshop also maps to engineering workflows where data or operations form
a chain.

A linked processing chain could be represented as:

```python
class ProcessingStepNode:
    def __init__(self, step):
        self.step = step
        self.next = None
```

Possible engineering uses include:

- Chaining preprocessing steps
- Sequencing validation operations
- Connecting time-ordered observations
- Building simple workflow pipelines
- Representing ordered model-processing stages
- Creating custom containers when built-in lists are not the desired abstraction

For example, a hydrodynamic workflow might be organized as:

```text
Read raw data
        ↓
Clean missing values
        ↓
Interpolate time series
        ↓
Compare with model output
        ↓
Generate validation metrics
```

A linked structure can represent that kind of ordered sequence explicitly, where each node
points to the next processing step.


---

## Current Roadmap

### Immediate Priorities

- Continue the freeCodeCamp Python Certification
- Complete additional workshops and labs
- Deepen object-oriented programming skills
- Strengthen inheritance and polymorphism
- Improve custom exception design
- Strengthen abstract interface design
- Practice reusable class hierarchies and parent-child contracts
- Strengthen object invariants and method overriding
- Apply design patterns to larger applications
- Practice automated testing
- Strengthen custom data-structure understanding
- Practice linked-list traversal and reference updates
- Strengthen documentation quality

### Next Technical Stage

| Technology | Intended Application |
| --- | --- |
| NumPy | Arrays, vectorized calculations, numerical workflows |
| pandas | Tabular and time-series data |
| Matplotlib | Scientific and engineering visualization |
| SciPy | Numerical methods and scientific algorithms |
| pytest | Automated testing |
| Jupyter | Research notebooks and exploratory analysis |
| openpyxl | Automated Excel processing |
| Git | Version control and project management |

### Long-Term Progression

```text
Python Fundamentals
        ↓
Functions and Program Logic
        ↓
Validation and Data Processing
        ↓
Object-Oriented Programming
        ↓
Object Composition
        ↓
Encapsulation and Validated State
        ↓
Inheritance, Polymorphism, and Custom Exceptions
        ↓
Abstract Interfaces and Strategy-Based Design
        ↓
Reusable Class Hierarchies and Movement Models
        ↓
Custom Data Structures and Linked References
        ↓
Geometric Models and Object Invariants
        ↓
Testing and Documentation
        ↓
NumPy and pandas
        ↓
Scientific Visualization
        ↓
Numerical Methods
        ↓
Hydrodynamic and Salinity Analysis
        ↓
Research Automation
        ↓
AI-Assisted Engineering Workflows
```

---

## Project Status

This repository is actively maintained as part of an ongoing learning process.

```text
Workshops:               13
Labs:                     8
Certification Projects:   3
Total Projects:          24
```

Latest completed workshop:

```text
Build a Linked List
```

Latest completed lab:

```text
Build a Player Interface
```

Latest completed certification project:

```text
Build a Polygon Area Calculator
Automated tests: 22/22 passed
```

---

## Resources

- [freeCodeCamp](https://www.freecodecamp.org/)
- [Python Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [pytest Documentation](https://docs.pytest.org/)

---

## Acknowledgements

The workshop, lab, and certification-project requirements are provided through the **freeCodeCamp Python Certification**.

The implementations, comments, documentation, repository organization, and engineering-oriented extensions reflect my independent learning process and technical portfolio development.

---

## Author

**Duong Kim Cuong**

Coastal Engineering · Scientific Computing · Python · Artificial Intelligence

GitHub: [github.com/kcduong994](https://github.com/kcduong994)
