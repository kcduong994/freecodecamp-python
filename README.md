# freecodecamp-python

> A structured Python learning portfolio built through the **freeCodeCamp Python Certification**, with a long-term focus on scientific computing, numerical modeling, environmental data processing, coastal engineering applications, and algorithmic problem solving.

![Python](https://img.shields.io/badge/Python-Learning-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Projects](https://img.shields.io/badge/Projects_Completed-26-success)
![Workshops](https://img.shields.io/badge/Workshops-14-2563EB)
![Labs](https://img.shields.io/badge/Labs-8-16A34A)
![Certification Projects](https://img.shields.io/badge/Certification_Projects-4-7C3AED)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

This repository documents my progression from Python fundamentals to functions, validation, debugging, object-oriented programming, inheritance, polymorphism, custom exceptions, abstract base classes, strategy-based design, custom data structures, search algorithms, formatted reporting, and larger certification projects.

The immediate goal is to complete the freeCodeCamp Python Certification with correct, readable, tested, and well-documented implementations. The long-term objective is to apply Python to coastal and environmental engineering workflows such as hydrodynamic modeling, salinity intrusion analysis, environmental data validation, numerical methods, scientific visualization, search/indexing utilities, and research automation.

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
- [Object-Oriented, Data-Structure, and Algorithm Progression](#object-oriented-data-structure-and-algorithm-progression)
- [Development Methodology](#development-methodology)
- [Common Debugging Lessons](#common-debugging-lessons)
- [Engineering-Oriented Direction](#engineering-oriented-direction)
- [Current Roadmap](#current-roadmap)
- [Project Status](#project-status)
- [Resources](#resources)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

---

## Repository at a Glance

| Area | Purpose | Completed |
| --- | --- | ---: |
| Workshops | Guided projects introducing new Python concepts incrementally | 14 |
| Labs | Independent implementations based on user stories and automated tests | 8 |
| Certification Projects | Larger projects combining multiple programming concepts | 4 |
| **Total** | **Documented Python projects** | **26** |

```text
Workshops              ██████████████  14 completed
Labs                   ████████░░░░░░  8 completed
Certification Projects ████░░░░░░░░░░  4 completed
Overall                ██████████████████████████  26 completed
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
Hash Tables, Buckets, and Collision Handling
        ↓
Binary Search and Algorithmic Thinking
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
| 14 | Build a Binary Search | Sorted data, midpoint comparison, boundary updates, algorithm tracing | ✅ |

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

| # | Project | Primary Concepts | Tests | Status |
| -: | --- | --- | :---: | :---: |
| 1 | Build a User Configuration Manager | CRUD operations, dictionaries, configuration management | 27/27 | ✅ |
| 2 | Build a Budget App | Classes, ledgers, transfers, validation, reports, charts | 24/24 | ✅ |
| 3 | Build a Polygon Area Calculator | Inheritance, method overriding, geometry, object invariants | 22/22 | ✅ |
| 4 | Build a Hash Table | Hashing, nested dictionaries, collision handling, lookup and deletion | 22/22 | ✅ |

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
│   ├── build-a-binary-search/
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
│   ├── build-a-hash-table/
│   │   ├── main.py
│   │   └── README.md
│   │
│   └── README.md
│
└── README.md
```

### Organization Principles

- **Workshops** use separate directories because they are developed through guided stages and often include dedicated documentation.
- **Labs** are stored as individual Python files because they are compact, independent exercises.
- **Certification projects** use dedicated directories because they combine multiple concepts and require project-level documentation.
- The root README provides the overall learning narrative, while subdirectory READMEs document category-specific progress.

---

## Workshops

Workshops introduce new concepts through guided implementation.

They are used to:

- Learn unfamiliar syntax
- Observe implementation patterns
- Practice one concept at a time
- Build confidence before independent work
- Develop reusable programming habits
- Connect syntax with algorithmic reasoning

The workshop sequence has progressed from basic formatting and functions to regular expressions, structured validation, object composition, properties, setters, controlled class state, inheritance, polymorphism, custom exceptions, abstract base classes, strategy-based software design, reference-based data structures, and algorithmic search.

The latest completed workshop, **Build a Binary Search**, introduced sorted-list search, midpoint calculation, `low` and `high` boundary management, iterative range reduction, early returns, not-found handling, and path tracing for algorithm explanation.

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

The latest completed certification project, **Build a Hash Table**, introduced manual key-value storage, hashing with `ord()`, nested dictionary buckets, collision-safe insertion, safe deletion, and lookup behavior.

Detailed certification-project documentation is maintained in [`certification-projects/README.md`](certification-projects/README.md).

### Completed Certification Sequence

```text
User Configuration Manager
        ↓
Budget App
        ↓
Polygon Area Calculator
        ↓
Hash Table
```

### Build a User Configuration Manager

A dictionary-based settings manager supporting add, update, delete, display, normalization, validation, and formatted output.

### Build a Budget App

A class-based financial tracking application supporting deposits, withdrawals, transfers, balance checks, transaction ledgers, formatted reports, spending percentages, and text-based charts.

### Build a Polygon Area Calculator

An inheritance-based geometry application featuring a reusable `Rectangle` parent class, a specialized `Square` subclass, area and perimeter calculations, diagonal calculation, method overriding, shape rendering, and object invariant preservation.

### Build a Hash Table

A data-structure implementation featuring a custom `HashTable` class, Unicode-based hashing with `ord()`, nested dictionary buckets, collision-safe storage, safe deletion, and lookup behavior.

The storage model is:

```python
{
    hashed_key: {
        original_key: value
    }
}
```

This project made the internal mechanics of dictionary-style key-value lookup more explicit. It also clarified why a hash value alone is not enough: different original keys can produce the same hash, so the original key must still be stored and checked inside the bucket.

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
- Built-in functions such as `sum()`, `ord()`, `min()`, `len()`, and `isinstance()`

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
- Method-level responsibilities for add, remove, lookup, validation, and search behavior

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
- Safe mutation after existence checks
- Search-space reduction through boundary updates

### Collections and Structured Data

- Lists
- Dictionaries
- Nested dictionaries
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
- Storing colliding hash keys in nested buckets
- Searching sorted collections efficiently
- Recording checked values during algorithm execution

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
- Hash tables
- Hash functions
- Unicode-based hashing with `ord()`
- Hash buckets
- Collision handling
- Key-value lookup
- Safe deletion
- Comparing custom data structures with built-in Python containers

### Algorithms

- Binary search
- Sorted input requirements
- Search boundaries
- `low`, `high`, and `mid` variables
- Midpoint calculation with integer division
- Middle-value comparison
- Discarding half of the search range
- Early return when the target is found
- Not-found handling
- Search-path tracing
- Algorithmic reasoning about efficiency

### Loops and Iteration

- `for` loops
- `while` loops
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
- Traversal until `None`
- Moving from one node to the next through object references
- Generator expressions such as `sum(ord(char) for char in string)`
- Iterative narrowing of a search interval

### Text Processing

- String indexing
- String slicing
- `split()`
- `lower()`
- `capitalize()`
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
- Validation before dictionary deletion
- Defensive lookup of missing keys
- Boundary validation for index-based algorithms

### Error and Exception Handling

- `try` and `except`
- `raise`
- `TypeError`
- `ValueError`
- `AttributeError`
- `IndexError`
- `KeyError`
- `SyntaxError`
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
- Exact dictionary output expected by tests
- Structured tuple output for algorithm results

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
- Preventing `KeyError` by checking nested dictionary membership
- Debugging hash collisions by checking the original key inside the bucket
- Debugging binary-search boundary updates
- Confirming whether a function return value is actually printed

---

## Selected Project Highlights

### Build a Binary Search

Implemented an iterative binary search algorithm for sorted lists.

The completed workshop includes:

- A `binary_search()` function
- A sorted input list
- A target value
- `low` and `high` search boundaries
- `mid` midpoint calculation
- Middle-value comparison
- Path tracing through `path_to_target`
- Early return when the target is found
- Not-found handling when the search range becomes invalid

Core implementation:

```python
def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return [], 'Value not found'
```

Search flow:

```text
Sorted list
        ↓
Set low and high boundaries
        ↓
Calculate middle index
        ↓
Compare target with middle value
        ↓
Discard half of the search range
        ↓
Repeat until found or range is empty
```

Example output:

```text
([3], 'Value found at index 2')
([3, 5, 4], 'Value found at index 3')
([], 'Value not found')
```

This workshop strengthened:

- Algorithmic thinking
- Search boundaries
- Integer division
- Index management
- Conditional branching
- Iterative search
- Search-path tracing
- Debugging off-by-one and direction errors

---

### Build a Hash Table

Implemented a simplified hash table that stores key-value pairs using computed hash values and nested buckets.

The completed certification project includes:

- `HashTable` class
- `collection` dictionary
- `hash()` method
- `add()` method
- `remove()` method
- `lookup()` method
- Collision-safe nested dictionaries
- Safe handling of missing keys
- Exact collection structures required by tests

This project strengthened hash-table concepts, Unicode-based hashing, nested dictionaries, collision handling, safe deletion, lookup design, defensive programming, and exact dictionary-structure matching.

---

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

Class relationship:

```text
LinkedList
    ├── length = 2
    └── head ──▶ Node(element=1)
                   └── next ──▶ Node(element=2)
                                   └── next ──▶ None
```

This workshop strengthened reference-based thinking, traversal with `while` loops, and safe link updates.

---

### Build a Discount Calculator

Implemented a strategy-driven pricing engine that evaluates multiple discount algorithms and returns the lowest valid price.

The completed workshop includes:

- A `Product` model
- An abstract `DiscountStrategy` interface
- `PercentageDiscount`
- `FixedAmountDiscount`
- `PremiumUserDiscount`
- A `DiscountEngine` responsible for evaluating strategies
- Type hints for products, prices, user tiers, and strategy collections
- Currency output formatted to two decimal places

This workshop strengthened abstract interface design, runtime polymorphism, strategy-pattern architecture, and exact monetary formatting.

---

### Build a Polygon Area Calculator

Implemented an inheritance-based geometry application with a reusable `Rectangle` parent class and a specialized `Square` subclass.

The completed certification project includes area calculation, perimeter calculation, diagonal calculation, shape rendering, shape containment, method overriding, and object invariant preservation.

---

### Build a Budget App

Developed a reusable `Category` class with transaction ledgers, deposits, withdrawals, transfers, balance calculations, fund checks, fixed-width output, spending percentages, and vertical text-based charts.

---

## Object-Oriented, Data-Structure, and Algorithm Progression

Object-oriented, data-structure, and algorithmic concepts were introduced incrementally:

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
HashTable
        ↓
Hashing, buckets, collision handling, safe lookup, and deletion
        ↓
Binary Search
        ↓
Sorted data, midpoint comparison, range reduction, and algorithm tracing
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
| Hash Table | Hashing, nested dictionaries, collision handling, lookup, and deletion |
| Binary Search | Sorted data, midpoint comparison, boundary updates, and logarithmic search thinking |
| Polygon Area Calculator | Reusable geometry, method overriding, object invariants, and containment logic |
| Budget App | Transaction systems, cross-object transfers, reporting |

This progression establishes a foundation for maintainable engineering software. The linked-list and hash-table projects add lower-level data-structure thinking, while binary search introduces algorithmic efficiency and systematic range reduction.

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
12. Add comments and README documentation.
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
- Add comments that explain intent, not obvious syntax.
- Refactor only after the behavior is correct.
- Preserve the original workshop or project contract when documenting completed code.
- Prefer interfaces that allow new behavior without modifying existing orchestration logic.
- Keep shared behavior in parent classes and subclass-specific behavior in concrete classes.
- Use abstract methods when every subclass must provide a required operation.
- Validate keys before accessing or deleting nested dictionary values.
- Maintain algorithm boundaries carefully when working with index-based search.

---

## Common Debugging Lessons

| Error | Typical Cause | Practical Lesson |
| --- | --- | --- |
| `SyntaxError` | Invalid syntax or copied instruction text | Check whether the failing line is executable Python |
| `IndentationError` | Incorrect block alignment | Verify class, method, and branch indentation |
| `NameError` | Undefined variable or function | Check scope and spelling |
| `TypeError` | Wrong argument count or data type | Compare the call with the function signature |
| `AttributeError` | Attribute or method does not exist | Review constructor, method spelling, and initialization |
| `ValueError` | Valid type but invalid content | Separate type validation from value validation |
| `IndexError` | Invalid sequence position | Review zero-based indexing and boundaries |
| `KeyError` | Missing dictionary key | Validate keys before access or deletion |
| Test mismatch | Exact output differs | Inspect whitespace, punctuation, newlines, and dictionary structure |
| Logic failure | Conditions overlap or execute incorrectly | Use focused condition checks and test one behavior at a time |

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
- Parameter names must match the identifiers used inside the method body.
- Built-in functions such as `min(prices)` are different from collection methods.
- Variables must be defined before they are passed into constructors.
- Abstract subclasses must implement every required abstract method before they can be instantiated.
- Tests for parent-class behavior may rely on a concrete subclass being instantiable.
- Shared initialization should be reused through `super().__init__()` when required.
- Method names must match the specification exactly; `set_heigth` and `set_height` are different identifiers.
- Floor division is appropriate when only complete contained objects should be counted.
- Generated text pictures may require a newline after the final row.
- Assignment direction matters in reference-based structures: `self.head = node` and `node = self.head` do not mean the same thing.
- `None` should be checked with `is None` or `is not None`.
- Traversal loops must advance to the next node to avoid infinite loops.
- Removing the head node requires updating `self.head`.
- A hash table should store original keys inside buckets because different keys can share one hash value.
- `remove()` should delete only the requested key-value pair, not the entire collision bucket.
- `lookup()` must check both the hash bucket and the original key.
- Binary search requires sorted input data.
- The midpoint should be calculated with integer division: `(low + high) // 2`.
- If the target is greater than the middle value, update the lower boundary with `low = mid + 1`.
- If the target is less than the middle value, update the upper boundary with `high = mid - 1`.
- A function call must be inside `print(...)` when the returned value needs to be displayed.
- Returning the checked path is useful for explaining and debugging the search process.

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


class ResultIndex:
    pass
```

### Validation Pattern

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

### Strategy Pattern for Engineering Metrics

The Strategy pattern from the Discount Calculator maps naturally to engineering software. Different calibration metrics, numerical solvers, boundary-condition treatments, or model-selection rules can implement a shared interface and be evaluated by one orchestration engine.

```python
class ValidationMetric(ABC):
    @abstractmethod
    def calculate(self, observed, simulated):
        pass
```

### Data Structures for Engineering Workflows

The Linked List workshop maps to workflows where data or operations form a chain.

```python
class ProcessingStepNode:
    def __init__(self, step):
        self.step = step
        self.next = None
```

Example workflow:

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

### Hash-Based Indexing

The Hash Table project maps to engineering tasks that require fast key-based access.

Possible uses include:

- Station ID lookup
- Scenario-name indexing
- Model-result indexing
- Parameter-set lookup
- Cached validation metrics
- Fast retrieval of processed observations
- Duplicate detection in environmental records

The same collision-handling principle applies: computed identifiers are useful for indexing, but original keys must still be preserved and checked.

### Binary Search for Sorted Engineering Data

Binary search maps directly to sorted engineering datasets such as timestamps, station lists, ordered result files, and model-output time steps.

```python
def find_time_index(times, target_time):
    low = 0
    high = len(times) - 1

    while low <= high:
        mid = (low + high) // 2

        if times[mid] == target_time:
            return mid
        elif target_time > times[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None
```

Possible uses include:

- Searching sorted observation timestamps
- Locating model-output time steps
- Matching calibration windows
- Finding ordered scenario identifiers
- Reducing lookup time before interpolation
- Supporting efficient time-series processing

The key engineering lesson is that algorithm choice matters. When data is sorted, binary search can avoid checking every element one by one.

---

## Current Roadmap

### Immediate Priorities

- Continue the freeCodeCamp Python Certification
- Complete additional workshops, labs, and certification projects
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
- Practice hash-table lookup, deletion, and collision handling
- Practice binary search and search-boundary management
- Strengthen documentation quality

### Next Technical Stage

| Technology or Concept | Intended Application |
| --- | --- |
| NumPy | Arrays, vectorized calculations, numerical workflows |
| pandas | Tabular and time-series data |
| Matplotlib | Scientific and engineering visualization |
| SciPy | Numerical methods and scientific algorithms |
| pytest | Automated testing |
| Jupyter | Research notebooks and exploratory analysis |
| openpyxl | Automated Excel processing |
| Git | Version control and project management |
| Search Algorithms | Efficient retrieval from sorted data |
| Algorithmic Complexity | Choosing appropriate algorithms for data size |

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
Hash-Based Storage and Lookup
        ↓
Search Algorithms and Algorithmic Efficiency
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
Workshops:               14
Labs:                     8
Certification Projects:   4
Total Projects:          26
```

Latest completed workshop:

```text
Build a Binary Search
```

Latest completed lab:

```text
Build a Player Interface
```

Latest completed certification project:

```text
Build a Hash Table
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
