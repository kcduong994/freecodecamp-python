# Python Workshops

A collection of guided Python workshop projects completed while studying the
**freeCodeCamp Python Certification**.

These workshops document my progress from Python fundamentals to text processing,
structured data validation, regular expressions, object-oriented programming,
object composition, encapsulation, properties, setters, inheritance, polymorphism,
custom exceptions, and interactions between multiple objects.

![Python](https://img.shields.io/badge/Python-Learning-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Workshops](https://img.shields.io/badge/Workshops_Completed-11-success)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

---

## Learning Progress

| Category               |   Completed |
| ---------------------- | ----------: |
| Workshops              |          11 |
| Guided Python Projects |          11 |
| Current Status         | In Progress |

```text
Progress: ███████████  11 workshops completed
```

---

## Completed Workshops

|  # | Workshop                             | Primary Concepts                                                | Status |
| -: | ------------------------------------ | --------------------------------------------------------------- | :----: |
|  1 | Report Card Printer                  | Variables, arithmetic, formatted output                         |   ✅   |
|  2 | Employee Profile Generator           | Functions, parameters, strings                                  |   ✅   |
|  3 | Bill Splitter                        | User input, calculations, validation                            |   ✅   |
|  4 | Movie Ticket Booking Calculator      | Conditional logic, pricing rules                                |   ✅   |
|  5 | Build a Caesar Cipher                | String translation, encryption                                  |   ✅   |
|  6 | Build a PIN Extractor                | Regular expressions, text parsing                               |   ✅   |
|  7 | Build a Medical Data Validator       | Dictionaries, validation, error reporting                       |   ✅   |
|  8 | Build a Musical Instrument Inventory | Classes, objects, attributes, methods                           |   ✅   |
|  9 | Build an Email Simulator             | Object composition, inbox management, timestamps                |   ✅   |
| 10 | Build a Salary Tracker               | Properties, setters, encapsulation, validation, class state     |   ✅   |
| 11 | Build a Media Catalogue              | Inheritance, polymorphism, custom exceptions, collection filtering |   ✅   |

---

## Repository Structure

```text
workshops/
├── report-card-printer/
├── employee-profile-generator/
├── bill-splitter/
├── movie-ticket-booking-calculator/
├── build-a-caesar-cipher/
├── build-a-pin-extractor/
├── build-a-medical-data-validator/
├── build-a-musical-instrument-inventory/
├── build-an-email-simulator/
├── build-a-salary-tracker/
├── build-a-media-catalogue/
└── README.md
```

A typical workshop directory contains:

```text
workshop-name/
├── main.py
└── README.md
```

- `main.py` contains the completed Python implementation.
- `README.md` documents the workshop objective, concepts, and learning outcomes.

---

## Skills Practiced

### Python Fundamentals

- Variables and data types
- Arithmetic operations
- Assignment statements
- User input and output
- String formatting
- Formatted string literals
- String manipulation
- Python syntax and indentation
- Code organization
- Readable naming conventions
- Type annotations
- Docstrings
- Code comments

### Programming Logic

- Conditional statements
- Boolean logic
- Comparison operators
- Membership operators
- Branching program behavior
- Input validation
- Error detection
- Data constraints
- Guard clauses
- Early returns
- Index range validation
- State-dependent validation
- Conditional output sections
- Validation before object creation

### Functions

- Function definitions
- Parameters and arguments
- Positional arguments
- Keyword arguments
- Return values
- Function reusability
- Separation of responsibilities
- Returning data versus printing output
- Defining and calling a `main()` function
- Using functions and methods to filter data

### Object-Oriented Programming

- Class definitions
- Object creation
- Class instances
- Parent and child classes
- Inheritance
- Subclassing
- Method overriding
- Polymorphic behavior
- The `super()` function
- Reusing parent-class initialization
- The `__init__()` constructor
- The `self` parameter
- Instance attributes
- Class attributes
- Instance methods
- Object-specific state
- Shared class-level state
- Dot notation
- Method return values
- The `__str__()` special method
- The `__repr__()` special method
- Readable and developer-oriented object representations
- Encapsulation with internal attributes
- Properties and property getters
- Property setters
- Validation inside setters
- Reusing setter logic during initialization
- Object composition
- Interactions between multiple objects
- Mixed collections of related objects
- Grouping objects by class
- Validating object types before storage

### Inheritance and Polymorphism

- Creating a child class from a parent class
- Inheriting common attributes and methods
- Calling a parent constructor with `super().__init__()`
- Adding child-specific attributes
- Overriding inherited methods
- Storing parent and child objects in the same collection
- Treating subclass instances as parent-class instances
- Distinguishing exact class matches from inherited matches
- Using polymorphic `__str__()` output

### Working with Text

- String indexing
- String slicing
- String splitting
- Multi-line text processing
- Pattern matching
- Regular expressions
- Translation tables
- Text encryption and decryption
- Structured information extraction
- Dynamic output with f-strings
- Exact error-message formatting
- Multi-section formatted output
- Adding newline characters with `\n`
- Building output strings incrementally

### Working with Collections

- Lists
- Dictionaries
- Nested data structures
- Class-level dictionaries
- Dictionary key lookup
- Dictionary membership testing
- List appending
- List indexing
- Element deletion with `del`
- Dictionary iteration
- Nested loops
- Iteration with `enumerate()`
- One-based and zero-based indexing
- List comprehensions
- Record-based data modeling
- Filtering objects by type
- Storing different subclasses in one list
- Creating filtered views of a collection
- Counting collection items with `len()`

### Type Inspection

- Type checking with `isinstance()`
- Exact class checking with `type() is`
- Understanding inheritance-aware type checks
- Accepting subclasses through `isinstance()`
- Excluding subclasses through exact type comparison
- Inspecting an object with `type()`
- Validating supported object types

### Data Validation

- Type checking with `isinstance()`
- Multiple-type checking with tuples
- Attribute existence checks with `hasattr()`
- Regular expressions with the `re` module
- Dictionary key validation
- Sequence validation
- Required field checking
- Invalid record detection
- Data integrity checks
- Index boundary checking
- Validation messages
- Error reporting
- Preventing invalid state transitions
- Preventing salary values below a level minimum
- Preventing duplicate or downward level changes
- Rejecting empty or whitespace-only strings
- Validating numeric lower bounds
- Validating release years
- Validating movie duration
- Validating season and episode counts
- Rejecting unsupported catalogue objects

### Exceptions and Error Handling

- Raising `TypeError`
- Raising `ValueError`
- Creating custom exception classes
- Inheriting from `Exception`
- Calling `super().__init__()` in an exception class
- Attaching additional context to an exception
- Storing the invalid object in an exception
- Catching multiple exception types
- Reading tracebacks
- Distinguishing syntax, runtime, and logic errors
- Writing exact exception messages
- Validating before assigning object state
- Avoiding `AttributeError` during initialization
- Reporting the object that caused an error

### Date and Time Handling

- Importing the `datetime` module
- Creating timestamps with `datetime.datetime.now()`
- Storing timestamps as instance attributes
- Formatting dates and times with `strftime()`
- Using date-time format codes
- Displaying timestamps in object representations

### Program Structure

- Defining a main execution flow
- Using the `if __name__ == "__main__":` guard
- Separating classes from demonstration code
- Organizing related responsibilities
- Building interactions across multiple classes
- Incremental program development
- Keeping validation close to the data it protects
- Separating models from catalogue management
- Reusing parent-class logic
- Organizing output by media category

---

## Workshop Highlights

### Report Card Printer

Introduced basic calculations and formatted output using:

- Variables
- Numeric data
- Arithmetic operations
- f-strings
- Console output

---

### Employee Profile Generator

Practiced creating reusable output logic with:

- Functions
- Parameters
- String formatting
- Structured profile information

---

### Bill Splitter

Applied mathematical operations to a practical calculation problem using:

- User input
- Arithmetic
- Percentage calculations
- Validation logic
- Formatted results

---

### Movie Ticket Booking Calculator

Introduced rule-based pricing using:

- Conditional statements
- Age-based conditions
- Business rules
- Decision-making logic

---

### Caesar Cipher

Implemented text encryption and decryption using:

- Character translation
- Alphabet shifting
- `str.maketrans()`
- `str.translate()`
- Reusable encryption functions
- String transformation logic

---

### PIN Extractor

Extracted structured information from text using:

- Regular expressions
- Pattern matching
- Multi-line input
- List processing
- Match validation

---

### Medical Data Validator

Validated structured medical records using:

- Lists of dictionaries
- Required keys
- Type checking
- Regular expressions
- Validation rules
- Error messages
- Invalid record reporting
- Data integrity checks

---

### Musical Instrument Inventory

Introduced object-oriented programming through a class representing musical instruments.

Key concepts included:

- Creating a class
- Initializing objects with `__init__()`
- Storing data in instance attributes
- Defining instance methods
- Accessing attributes with dot notation
- Printing method output
- Returning reusable values from methods

Example:

```python
instrument_1 = MusicalInstrument("Oboe", "woodwind")
instrument_2 = MusicalInstrument("Trumpet", "brass")

instrument_1.play()
print(instrument_1.get_fact())
```

---

### Email Simulator

Expanded object-oriented programming by creating multiple classes that interact with one another.

The completed simulator contains:

- An `Email` class for message data
- A `User` class for sending and managing email actions
- An `Inbox` class for storing and organizing received emails
- Read and unread email states
- Email timestamps
- Inbox listing
- Full email display
- Email deletion
- Validation for invalid email numbers

Key concepts included:

- Object composition
- Passing objects as arguments
- Managing object state
- Creating relationships between classes
- Adding objects to lists
- Reading list elements by index
- Converting one-based numbers to zero-based indices
- Formatting timestamps
- Implementing `__str__()`
- Using the main execution guard

Example:

```python
tory = User("Tory")
ramy = User("Ramy")

tory.send_email(
    ramy,
    "Hello",
    "Hi Ramy, just saying hello!",
)

ramy.check_inbox()
ramy.read_email(1)
ramy.delete_email(1)
```

The relationship between the objects can be summarized as:

```text
User
 ├── owns an Inbox
 └── sends an Email
          ↓
    receiver's Inbox
          ↓
      stores Email
```

---

### Salary Tracker

Built an employee salary-tracking system with validated properties and controlled state updates.

The completed project contains:

- An `Employee` class
- A shared `_base_salaries` dictionary
- Validated `name`, `level`, and `salary` properties
- Property getters and setters
- Automatic salary updates during promotion
- Protection against duplicate level assignments
- Protection against moving to a lower-paying level
- Protection against salaries below the minimum for the current level
- Readable `__str__()` output
- Reconstructable-style `__repr__()` output
- Explicit `TypeError` and `ValueError` messages

Key concepts included:

- Encapsulation
- Internal attributes such as `_name`, `_level`, and `_salary`
- The `@property` decorator
- Setter decorators such as `@name.setter`
- Shared class attributes
- Dictionary-based business rules
- State-aware validation with `hasattr()`
- Reusing setters from `__init__()`
- Coordinating level and salary changes
- Preventing invalid object states

Example:

```python
charlie_brown = Employee("Charlie Brown", "trainee")

print(charlie_brown)
print(f"Base salary: ${charlie_brown.salary}")

charlie_brown.level = "junior"
```

The internal update flow can be summarized as:

```text
Employee level update
        ↓
Validate new level
        ↓
Reject duplicate or lower level
        ↓
Look up the new base salary
        ↓
Update salary through its setter
        ↓
Store the new level
```

The salary validation flow is:

```text
New salary
    ↓
Check numeric type
    ↓
Compare with current level minimum
    ↓
Reject invalid salary or update _salary
```

---

### Media Catalogue

Built a catalogue capable of storing, validating, filtering, and displaying movies and television series.

The completed project contains:

- A `Movie` parent class
- A `TVSeries` child class
- A `MediaCatalogue` management class
- A custom `MediaError` exception
- Validation for movie and television-series data
- Inheritance through `class TVSeries(Movie)`
- Parent constructor reuse with `super().__init__()`
- Overridden `__str__()` methods
- A mixed collection containing related object types
- Separate movie and TV-series filtering methods
- Numbered catalogue output
- Conditional output sections
- Multiple exception handlers

The `Movie` class validates:

- Non-empty titles
- Release years from 1895 onward
- Non-empty director names
- Positive duration values

The `TVSeries` class adds:

- A positive number of seasons
- A positive total episode count
- Average episode duration
- A specialized string representation

The `MediaCatalogue` class supports:

- Adding `Movie` objects
- Adding `TVSeries` objects
- Rejecting unsupported objects
- Returning movies only
- Returning television series only
- Formatting grouped catalogue output
- Displaying an empty-catalogue message

Example:

```python
catalogue = MediaCatalogue()

movie1 = Movie(
    "The Matrix",
    1999,
    "The Wachowskis",
    136,
)

series1 = TVSeries(
    "Scrubs",
    2001,
    "Bill Lawrence",
    24,
    9,
    182,
)

catalogue.add(movie1)
catalogue.add(series1)

print(catalogue)
```

Example output:

```text
Media Catalogue (2 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
=== TV SERIES ===
1. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
```

Class relationship:

```text
Movie
  ↓
TVSeries inherits Movie
  ↓
Both can be stored in MediaCatalogue
  ↓
MediaCatalogue filters and groups them
```

Inheritance flow:

```text
TVSeries(...)
    ↓
super().__init__(...)
    ↓
Movie validates shared attributes
    ↓
TVSeries validates seasons and episodes
    ↓
Complete TVSeries object is created
```

Catalogue filtering flow:

```text
MediaCatalogue.items
        ↓
get_movies()
        ↓
type(item) is Movie
        ↓
Exact Movie objects only
```

```text
MediaCatalogue.items
        ↓
get_tv_series()
        ↓
isinstance(item, TVSeries)
        ↓
TVSeries objects
```

The distinction between the two type checks is important:

```python
type(item) is Movie
```

returns only objects created directly from `Movie`, while:

```python
isinstance(item, Movie)
```

also accepts objects created from subclasses such as `TVSeries`.

Custom exception handling:

```python
class MediaError(Exception):
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj
```

This exception stores both:

- The error message
- The invalid object that caused the error

Example:

```python
try:
    catalogue.add("invalid item")
except MediaError as error:
    print(f"Media Error: {error}")
    print(
        f"Unable to add {error.obj}: "
        f"{type(error.obj)}"
    )
```

Key concepts reinforced:

- Inheritance
- Subclassing
- Method overriding
- Polymorphism
- Parent constructor reuse
- Custom exception classes
- Additional exception context
- Type inspection
- List comprehensions
- Collection filtering
- Conditional formatting
- Mixed object collections
- Separation of responsibilities

---

## Object-Oriented Progression

The object-oriented workshops introduced concepts incrementally:

```text
MusicalInstrument
        ↓
One class with attributes and methods
        ↓
Email, User, and Inbox
        ↓
Multiple classes with shared responsibilities
        ↓
Objects interacting with other objects
        ↓
Employee Salary Tracker
        ↓
Properties, setters, encapsulation, and controlled state changes
        ↓
Movie and TVSeries
        ↓
Inheritance and method overriding
        ↓
MediaCatalogue
        ↓
Mixed object collections and filtering
        ↓
MediaError
        ↓
Custom exceptions with additional context
```

The Salary Tracker extended the progression from basic classes and object composition
toward reliable object models that enforce business rules internally.

The Media Catalogue introduced inheritance by placing shared media data and validation
inside the `Movie` parent class. `TVSeries` then reused and extended this behavior through
`super()`.

The project also introduced polymorphism. Calling `str()` on a `Movie` object and a
`TVSeries` object executes different `__str__()` implementations even though both objects
can be stored in the same catalogue.

---

## Development Approach

Each workshop is completed through guided, incremental steps.

The general learning process is:

1. Read and interpret the requirement.
2. Identify the relevant Python concept.
3. Implement one change at a time.
4. Run the automated tests.
5. Inspect console output and error messages.
6. Diagnose syntax, runtime, and logic errors.
7. Correct indexing, validation, inheritance, and state-management issues.
8. Refactor the completed code for readability without changing required behavior.
9. Add comments and documentation.
10. Save the completed implementation to GitHub.

This process reinforces Python syntax, debugging skills, program organization,
object-oriented design, inheritance, error handling, and practical problem-solving habits.

---

## Error Types Encountered

The workshops have provided practical experience with common Python errors:

| Error            | Typical Cause                                                       |
| ---------------- | ------------------------------------------------------------------- |
| `SyntaxError`    | Invalid syntax, missing punctuation, or incorrect keyword placement |
| `IndentationError` | A statement is placed at an invalid indentation level             |
| `NameError`      | Using a variable or function that has not been defined              |
| `TypeError`      | Passing the wrong number or type of arguments                       |
| `AttributeError` | Accessing an attribute before it exists or using a missing method   |
| `ValueError`     | Supplying a correctly typed value that violates a rule              |
| `IndexError`     | Attempting to access an invalid list position                       |
| `KeyError`       | Looking up a dictionary key that does not exist                     |

Understanding these errors improves debugging speed, validation design, and code reliability.

The Media Catalogue workshop also reinforced several specific debugging lessons:

- Instance methods require `self`.
- Constructors must be named exactly `__init__`.
- Custom exception constructors require all declared arguments.
- `enumerate()` is a built-in function, not a list method.
- `type(item) is Movie` and `isinstance(item, Movie)` behave differently.
- A subclass instance also passes an `isinstance()` check for its parent class.
- A method must explicitly `return` its result.
- Output-building code must maintain valid indentation.

---

## Current Progress

```text
Completed:  ███████████  11
Continuing: ░░░░░░░░░░  More workshops will be added
```

The current progression includes:

```text
Python Fundamentals
        ↓
Functions and Program Logic
        ↓
String Processing
        ↓
Regular Expressions
        ↓
Structured Data Validation
        ↓
Classes and Objects
        ↓
Object Composition
        ↓
Small Object-Oriented Applications
        ↓
Properties, Setters, and Encapsulation
        ↓
Validated Object State
        ↓
Inheritance and Subclassing
        ↓
Polymorphism and Method Overriding
        ↓
Custom Exceptions
        ↓
Mixed Object Collections
```

---

## Current Learning Focus

Current priorities include:

- Strengthening Python fundamentals
- Improving object-oriented programming skills
- Understanding relationships between classes
- Applying encapsulation consistently
- Writing property getters and setters
- Coordinating related object attributes
- Understanding parent and child classes
- Reusing logic through inheritance
- Applying `super()` correctly
- Overriding inherited methods
- Understanding polymorphic behavior
- Creating custom exception classes
- Adding useful context to exceptions
- Filtering mixed object collections
- Writing clean and readable methods
- Managing object state safely
- Working safely with list indices
- Formatting dates and times
- Developing reliable validation logic
- Improving debugging ability
- Preparing for larger labs and certification projects

---

## Engineering Relevance

The concepts developed through these workshops can later support coastal and environmental engineering applications.

Potential examples include:

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

Validated properties could enforce engineering constraints:

```python
class MonitoringStation:
    @property
    def water_level(self):
        return self._water_level

    @water_level.setter
    def water_level(self, new_value):
        if not isinstance(new_value, (int, float)):
            raise TypeError(
                "'water_level' must be numeric."
            )

        self._water_level = new_value
```

Inheritance could organize related engineering data types:

```text
Observation
    ├── WaterLevelObservation
    ├── SalinityObservation
    ├── WaveObservation
    └── CurrentObservation
```

A catalogue-like system could manage engineering datasets:

```python
class ObservationCatalogue:
    def __init__(self):
        self.items = []

    def add(self, observation):
        self.items.append(observation)
```

The relationship could be organized as:

```text
MonitoringStation
        ↓
produces Observation objects
        ↓
ObservationCatalogue stores them
        ↓
Observation subclasses are filtered by type
        ↓
SimulationScenario uses selected observations
        ↓
HydrodynamicModel produces results
        ↓
Validation tools evaluate performance
```

Relevant future applications include:

- Environmental monitoring systems
- Water-level and salinity data storage
- Numerical model configuration
- Simulation scenario management
- Model result validation
- Time-series processing
- Research workflow automation
- Validation of physical parameter ranges
- Controlled updates to model state
- Classification of observation types
- Filtering model results by variable
- Custom exceptions for invalid engineering data

---

## Learning Goals

These workshops provide the foundation for more advanced Python topics, including:

- Larger program architecture
- Advanced object-oriented programming
- Inheritance and polymorphism
- Abstract classes
- Multiple inheritance
- File processing
- Exception handling
- Custom exceptions
- Automated testing
- Data analysis
- Scientific computing
- Engineering-oriented Python applications

The long-term objective is to apply Python to practical engineering workflows, particularly:

- Coastal engineering
- Hydrodynamic data processing
- Salinity intrusion analysis
- Scientific visualization
- Numerical modeling support
- Environmental data validation
- Research automation
- AI-assisted engineering workflows

---

## Future Technical Areas

Future workshops and projects will gradually introduce:

| Technology or Concept | Intended Application                         |
| --------------------- | -------------------------------------------- |
| File I/O              | Reading and writing engineering data         |
| Exception Handling    | Reliable processing of invalid input         |
| Unit Testing          | Verifying calculation and validation logic   |
| Inheritance           | Organizing related engineering data models   |
| Abstract Classes      | Defining shared interfaces for model types   |
| NumPy                 | Numerical arrays and scientific calculations |
| pandas                | Tabular and time-series data processing      |
| Matplotlib            | Scientific visualization                     |
| SciPy                 | Numerical and scientific methods             |
| Jupyter               | Research and exploratory analysis            |

---

## Notes

This directory is part of a personal Python learning portfolio.

The projects are educational exercises completed through the freeCodeCamp curriculum.
The implementations, comments, documentation, and repository organization reflect my
personal learning process.

Additional workshops will be added as progress continues through the freeCodeCamp
Python Certification.

---

## Acknowledgements

Workshop instructions and learning materials are provided by
[freeCodeCamp](https://www.freecodecamp.org/).

The completed implementations and supporting documentation were developed as part of
my independent learning and technical portfolio.
