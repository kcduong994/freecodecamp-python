# Python Workshops

A collection of guided Python workshop projects completed while studying the
**freeCodeCamp Python Certification**.

These workshops document my progress from Python fundamentals to text processing, structured data validation, regular expressions, object-oriented programming, and interactions between multiple objects.

![Python](https://img.shields.io/badge/Python-Learning-3776AB?logo=python\&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp\&logoColor=white)
![Workshops](https://img.shields.io/badge/Workshops_Completed-9-success)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

---

## Learning Progress

| Category               |   Completed |
| ---------------------- | ----------: |
| Workshops              |           9 |
| Guided Python Projects |           9 |
| Current Status         | In Progress |

```text
Progress: █████████░  9 workshops completed
```

---

## Completed Workshops

|  # | Workshop                             | Primary Concepts                                 | Status |
| -: | ------------------------------------ | ------------------------------------------------ | :----: |
|  1 | Report Card Printer                  | Variables, arithmetic, formatted output          |    ✅   |
|  2 | Employee Profile Generator           | Functions, parameters, strings                   |    ✅   |
|  3 | Bill Splitter                        | User input, calculations, validation             |    ✅   |
|  4 | Movie Ticket Booking Calculator      | Conditional logic, pricing rules                 |    ✅   |
|  5 | Build a Caesar Cipher                | String translation, encryption                   |    ✅   |
|  6 | Build a PIN Extractor                | Regular expressions, text parsing                |    ✅   |
|  7 | Build a Medical Data Validator       | Dictionaries, validation, error reporting        |    ✅   |
|  8 | Build a Musical Instrument Inventory | Classes, objects, attributes, methods            |    ✅   |
|  9 | Build an Email Simulator             | Object composition, inbox management, timestamps |    ✅   |

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
└── README.md
```

A typical workshop directory contains:

```text
workshop-name/
├── main.py
└── README.md
```

* `main.py` contains the completed Python implementation.
* `README.md` documents the workshop objective, concepts, and learning outcomes.

---

## Skills Practiced

### Python Fundamentals

* Variables and data types
* Arithmetic operations
* Assignment statements
* User input and output
* String formatting
* Formatted string literals
* String manipulation
* Python syntax and indentation
* Code organization
* Readable naming conventions

### Programming Logic

* Conditional statements
* Boolean logic
* Comparison operators
* Branching program behavior
* Input validation
* Error detection
* Data constraints
* Guard clauses
* Early returns
* Index range validation

### Functions

* Function definitions
* Parameters and arguments
* Positional arguments
* Keyword arguments
* Return values
* Function reusability
* Separation of responsibilities
* Returning data versus printing output
* Defining and calling a `main()` function

### Object-Oriented Programming

* Class definitions
* Object creation
* Class instances
* The `__init__()` constructor
* The `self` parameter
* Instance attributes
* Instance methods
* Object-specific state
* Dot notation
* Method return values
* The `__str__()` special method
* Readable object representations
* Object composition
* Interactions between multiple objects

### Working with Text

* String indexing
* String slicing
* String splitting
* Multi-line text processing
* Pattern matching
* Regular expressions
* Translation tables
* Text encryption and decryption
* Structured information extraction
* Dynamic output with f-strings

### Working with Collections

* Lists
* Dictionaries
* Nested data structures
* List appending
* List indexing
* Element deletion with `del`
* Dictionary iteration
* Nested loops
* Iteration with `enumerate()`
* One-based and zero-based indexing
* List comprehensions
* Record-based data modeling

### Data Validation

* Type checking with `isinstance()`
* Regular expressions with the `re` module
* Dictionary key validation
* Sequence validation
* Required field checking
* Invalid record detection
* Data integrity checks
* Index boundary checking
* Validation messages
* Error reporting

### Date and Time Handling

* Importing the `datetime` module
* Creating timestamps with `datetime.datetime.now()`
* Storing timestamps as instance attributes
* Formatting dates and times with `strftime()`
* Using date-time format codes
* Displaying timestamps in object representations

### Program Structure

* Defining a main execution flow
* Using the `if __name__ == "__main__":` guard
* Separating classes from demonstration code
* Organizing related responsibilities
* Building interactions across multiple classes
* Incremental program development

---

## Workshop Highlights

### Report Card Printer

Introduced basic calculations and formatted output using:

* Variables
* Numeric data
* Arithmetic operations
* f-strings
* Console output

---

### Employee Profile Generator

Practiced creating reusable output logic with:

* Functions
* Parameters
* String formatting
* Structured profile information

---

### Bill Splitter

Applied mathematical operations to a practical calculation problem using:

* User input
* Arithmetic
* Percentage calculations
* Validation logic
* Formatted results

---

### Movie Ticket Booking Calculator

Introduced rule-based pricing using:

* Conditional statements
* Age-based conditions
* Business rules
* Decision-making logic

---

### Caesar Cipher

Implemented text encryption and decryption using:

* Character translation
* Alphabet shifting
* `str.maketrans()`
* `str.translate()`
* Reusable encryption functions
* String transformation logic

---

### PIN Extractor

Extracted structured information from text using:

* Regular expressions
* Pattern matching
* Multi-line input
* List processing
* Match validation

---

### Medical Data Validator

Validated structured medical records using:

* Lists of dictionaries
* Required keys
* Type checking
* Regular expressions
* Validation rules
* Error messages
* Invalid record reporting
* Data integrity checks

---

### Musical Instrument Inventory

Introduced object-oriented programming through a class representing musical instruments.

Key concepts included:

* Creating a class
* Initializing objects with `__init__()`
* Storing data in instance attributes
* Defining instance methods
* Accessing attributes with dot notation
* Printing method output
* Returning reusable values from methods

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

* An `Email` class for message data
* A `User` class for sending and managing email actions
* An `Inbox` class for storing and organizing received emails
* Read and unread email states
* Email timestamps
* Inbox listing
* Full email display
* Email deletion
* Validation for invalid email numbers

Key concepts included:

* Object composition
* Passing objects as arguments
* Managing object state
* Creating relationships between classes
* Adding objects to lists
* Reading list elements by index
* Converting one-based numbers to zero-based indices
* Formatting timestamps
* Implementing `__str__()`
* Using the main execution guard

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
```

The Email Simulator represents an important step from isolated class definitions toward a small object-oriented application.

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
7. Correct indexing and validation issues.
8. Refactor the completed code for readability.
9. Add comments and documentation.
10. Save the completed implementation to GitHub.

This process reinforces Python syntax, debugging skills, program organization, and practical problem-solving habits.

---

## Error Types Encountered

The workshops have provided practical experience with common Python errors:

| Error            | Typical Cause                                                       |
| ---------------- | ------------------------------------------------------------------- |
| `SyntaxError`    | Invalid syntax, missing parentheses, or incorrect keyword placement |
| `NameError`      | Using a variable or function that has not been defined              |
| `TypeError`      | Passing the wrong number or type of arguments                       |
| `AttributeError` | Accessing an attribute or method that an object does not have       |
| `ValueError`     | Supplying a value that has the correct type but is not acceptable   |
| `IndexError`     | Attempting to access an invalid list position                       |

Understanding these errors helps improve debugging speed and code reliability.

---

## Current Progress

```text
Completed:  █████████░  9
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
```

---

## Current Learning Focus

Current priorities include:

* Strengthening Python fundamentals
* Improving object-oriented programming skills
* Understanding relationships between classes
* Writing clean and readable methods
* Managing object state
* Working safely with list indices
* Formatting dates and times
* Developing reliable validation logic
* Improving debugging ability
* Preparing for larger labs and certification projects

---

## Engineering Relevance

The concepts developed through these workshops can later support coastal and environmental engineering applications.

Potential examples include:

```python
class MonitoringStation:
    pass


class Observation:
    pass


class SimulationScenario:
    pass


class HydrodynamicModel:
    pass
```

These classes could interact in ways similar to the Email Simulator:

```text
MonitoringStation
        ↓
stores Observation objects
        ↓
SimulationScenario uses observations
        ↓
HydrodynamicModel produces results
```

Relevant future applications include:

* Environmental monitoring systems
* Water-level and salinity data storage
* Numerical model configuration
* Simulation scenario management
* Model result validation
* Time-series processing
* Research workflow automation

---

## Learning Goals

These workshops provide the foundation for more advanced Python topics, including:

* Larger program architecture
* Advanced object-oriented programming
* Inheritance and polymorphism
* File processing
* Exception handling
* Automated testing
* Data analysis
* Scientific computing
* Engineering-oriented Python applications

The long-term objective is to apply Python to practical engineering workflows, particularly:

* Coastal engineering
* Hydrodynamic data processing
* Salinity intrusion analysis
* Scientific visualization
* Numerical modeling support
* Environmental data validation
* Research automation
* AI-assisted engineering workflows

---

## Future Technical Areas

Future workshops and projects will gradually introduce:

| Technology or Concept | Intended Application                         |
| --------------------- | -------------------------------------------- |
| File I/O              | Reading and writing engineering data         |
| Exception Handling    | Reliable processing of invalid input         |
| Unit Testing          | Verifying calculation and validation logic   |
| NumPy                 | Numerical arrays and scientific calculations |
| pandas                | Tabular and time-series data processing      |
| Matplotlib            | Scientific visualization                     |
| SciPy                 | Numerical and scientific methods             |
| Jupyter               | Research and exploratory analysis            |

---

## Notes

This directory is part of a personal Python learning portfolio.

The projects are educational exercises completed through the freeCodeCamp curriculum. The implementations, comments, documentation, and repository organization reflect my personal learning process.

Additional workshops will be added as progress continues through the freeCodeCamp Python Certification.

---

## Acknowledgements

Workshop instructions and learning materials are provided by
[freeCodeCamp](https://www.freecodecamp.org/).

The completed implementations and supporting documentation were developed as part of my independent learning and technical portfolio.
