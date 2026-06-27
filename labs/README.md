# Python Labs

A collection of practical Python labs completed as part of the
**freeCodeCamp Python Certification**.

Unlike guided workshops, labs require independently interpreting requirements, translating user stories into program logic, testing implementations, and correcting errors.

![Python](https://img.shields.io/badge/Python-Learning-3776AB?logo=python\&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp\&logoColor=white)
![Labs](https://img.shields.io/badge/Labs_Completed-6-success)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

---

## Completed Labs

|  # | Lab                              | Primary Concepts                           | Status |
| -: | -------------------------------- | ------------------------------------------ | :----: |
|  1 | Travel Weather Planner           | Conditional logic, user input, validation  |    ✅   |
|  2 | Apply Discount Function          | Functions, calculations, business rules    |    ✅   |
|  3 | Build an RPG Character           | Dictionaries, constraints, data validation |    ✅   |
|  4 | Build a Number Pattern Generator | Loops, ranges, pattern construction        |    ✅   |
|  5 | Debug an ISBN Validator          | Debugging, exceptions, checksum validation |    ✅   |
|  6 | Build a Planet Class             | Classes, objects, methods, exceptions      |    ✅   |

---

## Learning Progress

| Category             |   Completed |
| -------------------- | ----------: |
| Practical Labs       |           6 |
| Debugging Labs       |           1 |
| Object-Oriented Labs |           1 |
| Current Status       | In Progress |

```text
Labs Completed: 6
Progress:       ██████░░░░ 6 completed
```

---

## Repository Structure

```text
labs/
├── travel-weather-planner.py
├── apply-discount-function.py
├── build-an-rpg-character.py
├── build-a-number-pattern-generator.py
├── debug-an-isbn-validator.py
├── build-a-planet-class.py
└── README.md
```

Each lab is stored as an individual Python file.

The shared `README.md` documents:

* Completed labs
* Learning progress
* Concepts practiced
* Technical skills developed
* Project highlights
* Future learning directions

---

## Skills Practiced

### Python Fundamentals

* Variables and data types
* Assignment statements
* User input and output
* Arithmetic operations
* String formatting
* String manipulation
* Python syntax and indentation
* Readable naming conventions
* Basic code organization

### Functions

* Function definitions
* Parameters and arguments
* Return values
* Function reusability
* Early return patterns
* Separation of responsibilities
* Returning values versus printing output

### Input and Data Validation

* Type checking with `isinstance()`
* Integer validation
* Positive number validation
* Required value validation
* Length validation
* Character validation
* Empty-string validation
* User input verification
* Business rule validation
* Data constraint enforcement

### Programming Logic

* Conditional statements
* `if`, `elif`, and `else`
* Boolean logic
* `and`, `or`, and `not`
* Comparison operators
* Decision-making logic
* Nested conditions
* Guard clauses
* Early return patterns

### Object-Oriented Programming

* Class definitions
* Objects and instances
* The `__init__()` constructor
* The `self` parameter
* Instance attributes
* Instance methods
* Dot notation
* Object initialization
* The `__str__()` special method
* Readable object representations
* Class-based data modeling

### Data Types and Strings

* Integer values with `int`
* Floating-point values with `float`
* Text values with `str`
* String concatenation
* Formatted strings
* String slicing
* String splitting with `split()`
* Character inspection
* Multi-line text processing

### Collections and Structured Data

* Lists
* Dictionaries
* Key-value data storage
* Nested data structures
* List iteration
* Dictionary validation
* Data aggregation
* Record-based data modeling

### Loops and Iteration

* `for` loops
* Iteration with `range()`
* Iteration with `enumerate()`
* Number sequences
* Pattern generation
* String construction
* Loop control logic
* Repeated data processing

### Error and Exception Handling

* `try`
* `except`
* `TypeError`
* `ValueError`
* Raising exceptions with `raise`
* Input error handling
* Defensive programming
* Invalid value detection
* Clear validation messages

### Debugging

* Reading existing code
* Tracing program flow
* Fixing indentation errors
* Fixing syntax errors
* Fixing index errors
* Detecting off-by-one errors
* Exception debugging
* Testing expected output
* Testing edge cases
* Identifying incorrect assumptions

### Problem Solving

* Requirement analysis
* Translating user stories into code
* Breaking problems into smaller tasks
* Business logic implementation
* Independent solution design
* Debugging and testing
* Structured program design
* Refactoring for readability

---

## Lab Highlights

### Travel Weather Planner

Built a weather-based recommendation program using:

* User input
* Conditional statements
* Temperature rules
* Weather conditions
* Input validation
* Decision-making logic

This lab reinforced the process of translating practical conditions into program behavior.

---

### Apply Discount Function

Implemented reusable pricing and discount logic using:

* Function parameters
* Return values
* Percentage calculations
* Business rules
* Validation conditions
* Early returns

This lab demonstrated how functions can isolate and reuse calculation logic.

---

### Build an RPG Character

Created and validated structured character data using:

* Dictionaries
* Character attributes
* Statistic constraints
* Required key validation
* Type checking
* Business rules
* Structured data modeling

This lab introduced more advanced validation requirements and relationships between data values.

---

### Build a Number Pattern Generator

Generated structured number patterns using:

* `for` loops
* `range()`
* Number sequences
* String concatenation
* Repeated output construction
* Loop-based problem solving

This lab reinforced iteration and programmatic pattern generation.

---

### Debug an ISBN Validator

Inspected and repaired an existing ISBN validation program.

Key concepts included:

* Program flow tracing
* Exception handling
* Off-by-one error detection
* Index validation
* Input normalization
* Checksum calculation
* Defensive programming
* Debugging existing code

This lab emphasized understanding and correcting an existing implementation rather than building one entirely from scratch.

---

### Build a Planet Class

Introduced object-oriented programming by modeling planets as Python objects.

Key concepts included:

* Defining a `Planet` class
* Initializing instances with `__init__()`
* Validating constructor arguments
* Raising `TypeError` for invalid data types
* Raising `ValueError` for empty strings
* Storing instance attributes
* Defining an `orbit()` method
* Implementing `__str__()`
* Creating and printing multiple objects

Example:

```python
planet_1 = Planet("Earth", "terrestrial", "Sun")
planet_2 = Planet("Jupiter", "gas giant", "Sun")
planet_3 = Planet("Kepler-452b", "super-Earth", "Kepler-452")

print(planet_1)
print(planet_1.orbit())
```

Expected output:

```text
Planet: Earth | Type: terrestrial | Star: Sun
Earth is orbiting around Sun...
```

---

## Development Approach

Each lab follows an independent problem-solving workflow:

1. Read all requirements and user stories.
2. Identify the required inputs, outputs, and constraints.
3. Break the problem into smaller logical components.
4. Implement the solution incrementally.
5. Run the provided tests.
6. Inspect the program output.
7. Diagnose syntax, runtime, and logic errors.
8. Test invalid inputs and edge cases.
9. Refactor the final solution for readability.
10. Add comments and documentation.
11. Commit the completed lab to GitHub.

This process develops both Python knowledge and practical software-development habits.

---

## Workshops and Labs

Workshops and labs serve different learning purposes.

| Workshops                         | Labs                                 |
| --------------------------------- | ------------------------------------ |
| Guided step-by-step exercises     | Independent implementation           |
| Introduce new syntax and concepts | Apply previously learned concepts    |
| Provide incremental instructions  | Provide requirements and tests       |
| Focus on understanding            | Focus on problem solving             |
| Reduce implementation ambiguity   | Require independent design decisions |

Workshops establish the foundation, while labs test whether those concepts can be applied independently.

---

## Current Learning Focus

Current priorities include:

* Strengthening Python fundamentals
* Improving object-oriented programming skills
* Understanding classes, objects, and instances
* Writing reliable validation logic
* Using exceptions correctly
* Improving debugging ability
* Developing clean and readable code
* Preparing for larger certification projects
* Building engineering-oriented programming habits

---

## Engineering Relevance

The skills developed through these labs are applicable to future coastal and environmental engineering workflows.

Potential applications include:

* Validating environmental datasets
* Representing engineering entities with classes
* Detecting missing or invalid measurements
* Building reusable calculation functions
* Processing time-series data
* Processing numerical model output
* Debugging scientific analysis scripts
* Enforcing data integrity constraints
* Automating repetitive research tasks

Object-oriented programming can later support structures such as:

```python
class MonitoringStation:
    pass


class SalinityRecord:
    pass


class HydrodynamicModel:
    pass


class SimulationScenario:
    pass
```

These classes could organize environmental measurements, monitoring stations, simulation scenarios, and numerical model configurations into maintainable software systems.

---

## Future Learning Areas

Future labs will gradually support development in:

* Advanced object-oriented programming
* File input and output
* Exception handling
* Automated testing
* Data processing
* Scientific computing
* Numerical methods
* Scientific visualization
* Engineering automation
* Research-oriented programming

Planned Python tools include:

| Technology | Intended Use                      |
| ---------- | --------------------------------- |
| NumPy      | Numerical calculations and arrays |
| pandas     | Tabular and time-series data      |
| Matplotlib | Scientific visualization          |
| SciPy      | Numerical and scientific methods  |
| pytest     | Automated testing                 |
| Jupyter    | Research and exploratory analysis |
| openpyxl   | Automated Excel processing        |

---

## Long-Term Direction

The long-term objective is to connect Python programming with coastal and environmental engineering.

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
Scientific Data Processing
        ↓
Numerical Methods
        ↓
Hydrodynamic and Salinity Analysis
        ↓
Engineering Automation
        ↓
Research Software Development
```

Potential future projects include:

* Tide data analysis
* Water-level processing
* Salinity intrusion analysis
* Model validation metrics
* Environmental data cleaning
* Hydrodynamic result processing
* Scientific visualization
* Numerical modeling utilities

---

## Notes

Labs strengthen programming skills through independent implementation rather than step-by-step guidance.

Each completed lab documents progress in:

* Understanding requirements
* Designing program logic
* Validating input and data
* Debugging incorrect code
* Writing reusable solutions
* Applying Python concepts independently
* Improving technical documentation

Additional labs will be added as progress continues through the freeCodeCamp Python Certification.

---

## Acknowledgements

Lab requirements and automated tests are provided through the
**freeCodeCamp Python Certification**.

The implementations, comments, documentation, and repository organization reflect my personal learning process.
