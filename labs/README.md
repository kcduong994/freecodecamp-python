# Python Labs

A growing collection of independently completed Python labs from the
**freeCodeCamp Python Certification**.

These labs focus on translating user stories into working software, designing program logic, validating data, debugging failures, and producing readable Python solutions without step-by-step implementation guidance.

![Python](https://img.shields.io/badge/Python-Learning-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Labs](https://img.shields.io/badge/Labs_Completed-7-success)
![OOP Labs](https://img.shields.io/badge/OOP_Labs-2-6f42c1)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

---

## Table of Contents

- [Learning Overview](#learning-overview)
- [Completed Labs](#completed-labs)
- [Progress Snapshot](#progress-snapshot)
- [Repository Structure](#repository-structure)
- [Skills Practiced](#skills-practiced)
- [Lab Highlights](#lab-highlights)
- [Development Workflow](#development-workflow)
- [Workshops and Labs](#workshops-and-labs)
- [Engineering Relevance](#engineering-relevance)
- [Future Learning Areas](#future-learning-areas)
- [Long-Term Direction](#long-term-direction)
- [Acknowledgements](#acknowledgements)

---

## Learning Overview

The labs in this directory are designed to strengthen independent software-development skills.

Each exercise requires some combination of:

- Interpreting written requirements
- Translating user stories into code
- Designing control flow and data structures
- Implementing validation rules
- Reading automated test feedback
- Debugging syntax, runtime, and logic errors
- Refactoring code for clarity
- Documenting the final implementation

The current learning path has progressed from fundamental control flow and functions to structured data, debugging, classes, properties, controlled state updates, and object-oriented design.

---

## Completed Labs

| # | Lab | Primary Concepts | Status |
| -: | --- | --- | :---: |
| 1 | Travel Weather Planner | Conditional logic, user input, validation | ✅ |
| 2 | Apply Discount Function | Functions, calculations, business rules | ✅ |
| 3 | Build an RPG Character | Dictionaries, constraints, structured validation | ✅ |
| 4 | Build a Number Pattern Generator | Loops, ranges, pattern construction | ✅ |
| 5 | Debug an ISBN Validator | Debugging, exceptions, checksum validation | ✅ |
| 6 | Build a Planet Class | Classes, constructors, methods, exceptions | ✅ |
| 7 | Build a Game Character Stats Tracker | Properties, getters, setters, encapsulation | ✅ |

---

## Progress Snapshot

| Category | Completed |
| --- | ---: |
| Total Labs | 7 |
| Debugging-Focused Labs | 1 |
| Object-Oriented Labs | 2 |
| Labs Using Validation Rules | 5 |
| Current Status | In Progress |

```text
Labs Completed: 7
Progress:       ███████░░░ 7 completed
Current Focus:  Object-oriented programming and controlled object state
```

### Concept Progression

```text
Conditions and Input
        ↓
Reusable Functions
        ↓
Dictionaries and Validation
        ↓
Loops and Pattern Generation
        ↓
Debugging Existing Programs
        ↓
Classes and Object Construction
        ↓
Properties, Getters, and Setters
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
├── build-a-game-character-stats-tracker.py
└── README.md
```

Each lab is stored as an individual Python file.

The shared `README.md` records:

- Completed labs
- Learning progress
- Concepts practiced
- Technical skills developed
- Important implementation patterns
- Engineering relevance
- Future learning directions

---

## Skills Practiced

### Python Fundamentals

- Variables and data types
- Assignment statements
- Arithmetic operations
- Comparison operators
- Boolean expressions
- User input and output
- String formatting
- Multi-line strings
- Python syntax and indentation
- Readable naming conventions
- Basic code organization

### Functions

- Function definitions
- Parameters and arguments
- Return values
- Function reuse
- Early return patterns
- Separation of responsibilities
- Returning values versus printing output
- Small, testable units of logic

### Input and Data Validation

- Type checking with `isinstance()`
- Integer and numeric validation
- Positive-number validation
- Required-value validation
- Length and character validation
- Empty-string validation
- Range enforcement
- Business-rule validation
- Data-constraint enforcement
- Defensive programming

### Programming Logic

- `if`, `elif`, and `else`
- Boolean logic with `and`, `or`, and `not`
- Nested conditions
- Guard clauses
- Decision-making logic
- Boundary-condition handling
- Exclusive branches with `if` / `elif` / `else`
- State-dependent behavior

### Object-Oriented Programming

- Class definitions
- Objects and instances
- The `__init__()` constructor
- The `self` parameter
- Instance attributes
- Instance methods
- Dot notation
- Object initialization
- Object state
- Encapsulation by convention
- Backing attributes such as `_health`
- Public properties
- Read-only properties
- Getter methods
- Setter methods
- Controlled state mutation
- The `__str__()` special method
- Readable object representations

### Properties and State Management

- Creating properties with `@property`
- Creating setters with `@property_name.setter`
- Separating public access from internal storage
- Preventing invalid state transitions
- Clamping values to valid ranges
- Resetting object state through public setters
- Using augmented assignment with properties
- Designing read-only public interfaces

Example:

```python
hero.health -= 30
hero.mana -= 10
```

The getter provides the current value, Python performs the arithmetic operation, and the setter validates the updated result before storing it.

### Data Types and Strings

- Integer values with `int`
- Floating-point values with `float`
- Text values with `str`
- String concatenation
- Formatted strings
- String slicing
- String splitting with `split()`
- Character inspection
- Multi-line output formatting

### Collections and Structured Data

- Lists
- Dictionaries
- Key-value data storage
- Nested data structures
- List iteration
- Dictionary validation
- Data aggregation
- Record-based data modeling

### Loops and Iteration

- `for` loops
- Iteration with `range()`
- Iteration with `enumerate()`
- Number sequences
- Pattern generation
- String construction
- Loop-control logic
- Repeated data processing

### Error and Exception Handling

- `try`
- `except`
- `TypeError`
- `ValueError`
- Raising exceptions with `raise`
- Input-error handling
- Invalid-value detection
- Clear validation messages
- Failure-oriented testing

### Debugging

- Reading existing code
- Tracing program flow
- Interpreting automated test failures
- Fixing indentation errors
- Fixing syntax errors
- Fixing index errors
- Detecting off-by-one errors
- Diagnosing incorrect conditional structure
- Exception debugging
- Testing expected output
- Testing edge cases
- Identifying incorrect assumptions

### Problem Solving

- Requirement analysis
- Translating user stories into code
- Breaking problems into smaller tasks
- Implementing business logic
- Independent solution design
- Debugging and testing
- Structured program design
- Refactoring for readability
- Matching exact output formats
- Distinguishing implementation requirements from runtime behavior

---

## Lab Highlights

### 1. Travel Weather Planner

Built a weather-based recommendation program using:

- User input
- Conditional statements
- Temperature rules
- Weather conditions
- Input validation
- Decision-making logic

This lab reinforced the process of translating practical conditions into program behavior.

---

### 2. Apply Discount Function

Implemented reusable pricing and discount logic using:

- Function parameters
- Return values
- Percentage calculations
- Business rules
- Validation conditions
- Early returns

This lab demonstrated how functions isolate and reuse calculation logic.

---

### 3. Build an RPG Character

Created and validated structured character data using:

- Dictionaries
- Character attributes
- Statistic constraints
- Required-key validation
- Type checking
- Business rules
- Structured data modeling

This lab introduced more advanced relationships between data values and validation rules.

---

### 4. Build a Number Pattern Generator

Generated structured number patterns using:

- `for` loops
- `range()`
- Number sequences
- String concatenation
- Repeated output construction
- Loop-based problem solving

This lab reinforced iteration and programmatic pattern generation.

---

### 5. Debug an ISBN Validator

Inspected and repaired an existing ISBN-validation program.

Key concepts included:

- Program-flow tracing
- Exception handling
- Off-by-one error detection
- Index validation
- Input normalization
- Checksum calculation
- Defensive programming
- Debugging existing code

This lab emphasized understanding and correcting an existing implementation rather than building one entirely from scratch.

---

### 6. Build a Planet Class

Introduced object-oriented programming by modeling planets as Python objects.

Key concepts included:

- Defining a `Planet` class
- Initializing instances with `__init__()`
- Validating constructor arguments
- Raising `TypeError` for invalid data types
- Raising `ValueError` for empty strings
- Storing instance attributes
- Defining an `orbit()` method
- Implementing `__str__()`
- Creating and printing multiple objects

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

### 7. Build a Game Character Stats Tracker

Built a class-based tracker for managing a game character's state.

The `GameCharacter` class stores:

- Character name
- Health
- Mana
- Level

The implementation uses:

- Private-style backing attributes
- Read-only properties
- Property getters
- Property setters
- Range constraints
- Controlled state updates
- A level-up operation
- A formatted `__str__()` representation

Core rules:

```text
0 ≤ health ≤ 100
0 ≤ mana ≤ 50
```

The `health` and `mana` setters clamp invalid values to the nearest valid boundary.

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

This lab strengthened understanding of encapsulation and demonstrated why public properties can provide a cleaner and safer interface than direct modification of internal attributes.

### Key Design Pattern

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

This separates:

- **Storage:** `_health`
- **Reading:** `health`
- **Validation and assignment:** `health` setter

The same pattern is used for mana.

---

## Development Workflow

Each lab follows an independent problem-solving workflow:

1. Read all requirements and user stories.
2. Identify required classes, functions, inputs, outputs, and constraints.
3. Translate each user story into a concrete implementation task.
4. Break the problem into smaller logical components.
5. Implement the solution incrementally.
6. Run the provided automated tests.
7. Inspect failures one test at a time.
8. Diagnose syntax, runtime, and logic errors.
9. Test boundary values and invalid inputs.
10. Refactor the final solution for readability.
11. Add comments and documentation.
12. Record the completed work in the repository.
13. Commit the finished lab to GitHub.

### Test-Driven Feedback Loop

```text
Read requirement
      ↓
Write implementation
      ↓
Run tests
      ↓
Inspect the first failure
      ↓
Identify the exact cause
      ↓
Apply a focused correction
      ↓
Run tests again
```

This workflow prevents unrelated changes and encourages precise debugging.

---

## Code Quality Principles

The completed labs aim to follow these principles:

- Use clear and descriptive names.
- Keep indentation consistent.
- Separate validation from presentation where practical.
- Return values when data is needed by other code.
- Use `print()` only for required user-facing output.
- Keep object state valid after every public operation.
- Avoid duplicate implementations.
- Match required output formats exactly.
- Prefer readable logic over unnecessarily compact expressions.
- Add comments that explain intent rather than restating syntax.

---

## Workshops and Labs

Workshops and labs serve different learning purposes.

| Workshops | Labs |
| --- | --- |
| Guided step-by-step exercises | Independent implementation |
| Introduce new syntax and concepts | Apply previously learned concepts |
| Provide incremental instructions | Provide requirements and tests |
| Focus on understanding | Focus on problem solving |
| Reduce implementation ambiguity | Require independent design decisions |
| Demonstrate patterns | Test whether patterns can be applied |

Workshops establish the foundation, while labs evaluate whether those concepts can be used independently.

---

## Current Learning Focus

Current priorities include:

- Strengthening Python fundamentals
- Deepening object-oriented programming knowledge
- Understanding properties and encapsulation
- Managing object state safely
- Writing reliable validation logic
- Using exceptions correctly
- Reading automated test feedback
- Improving debugging precision
- Developing clean and readable code
- Preparing for larger certification projects
- Building engineering-oriented programming habits

---

## Engineering Relevance

The skills developed through these labs are applicable to coastal and environmental engineering workflows.

Potential applications include:

- Validating environmental datasets
- Representing engineering entities with classes
- Protecting model parameters from invalid values
- Detecting missing or invalid measurements
- Building reusable calculation functions
- Processing time-series data
- Processing numerical-model output
- Debugging scientific-analysis scripts
- Enforcing data-integrity constraints
- Automating repetitive research tasks

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

A property-based validation pattern could also be applied to engineering data:

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
        if value < 0:
            raise ValueError("Salinity cannot be negative.")

        self._salinity = value
```

This pattern helps keep scientific data objects internally consistent.

---

## Future Learning Areas

Future labs will gradually support development in:

- Advanced object-oriented programming
- Inheritance and composition
- Class methods and static methods
- File input and output
- Exception handling
- Automated testing
- Data processing
- Scientific computing
- Numerical methods
- Scientific visualization
- Engineering automation
- Research-oriented programming

Planned Python tools include:

| Technology | Intended Use |
| --- | --- |
| NumPy | Numerical calculations and arrays |
| pandas | Tabular and time-series data |
| Matplotlib | Scientific visualization |
| SciPy | Numerical and scientific methods |
| pytest | Automated testing |
| Jupyter | Research and exploratory analysis |
| openpyxl | Automated Excel processing |

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

- Tide-data analysis
- Water-level processing
- Salinity-intrusion analysis
- Model-validation metrics
- Environmental-data cleaning
- Hydrodynamic-result processing
- Scientific visualization
- Numerical-modeling utilities
- Monitoring-station data models
- Simulation-scenario management
- Automated engineering reports

---

## Notes

Labs strengthen programming skills through independent implementation rather than step-by-step guidance.

Each completed lab documents progress in:

- Understanding requirements
- Designing program logic
- Validating input and data
- Debugging incorrect code
- Writing reusable solutions
- Applying Python concepts independently
- Managing object state
- Improving technical documentation

Additional labs will be added as progress continues through the freeCodeCamp Python Certification.

---

## Acknowledgements

Lab requirements and automated tests are provided through the
**freeCodeCamp Python Certification**.

The implementations, comments, documentation, repository organization, and engineering-oriented extensions reflect my personal learning process.
