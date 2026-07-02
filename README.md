# freecodecamp-python

> A structured Python learning portfolio built through the **freeCodeCamp Python Certification**, with a long-term focus on scientific computing, numerical modeling, and coastal engineering applications.

![Python](https://img.shields.io/badge/Python-Learning-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Projects](https://img.shields.io/badge/Projects_Completed-20-success)
![Workshops](https://img.shields.io/badge/Workshops-11-2563EB)
![Labs](https://img.shields.io/badge/Labs-7-16A34A)
![Certification Projects](https://img.shields.io/badge/Certification_Projects-2-7C3AED)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

This repository documents my progression from Python fundamentals to object-oriented programming, validation, debugging, inheritance, polymorphism, custom exceptions, formatted reporting, and larger certification projects.

The immediate goal is to complete the freeCodeCamp Python Certification with clean, well-documented implementations. The long-term objective is to apply Python to coastal and environmental engineering workflows such as hydrodynamic modeling, salinity intrusion analysis, environmental data processing, numerical methods, scientific visualization, and engineering automation.

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
| Workshops | Guided projects introducing new Python concepts incrementally | 11 |
| Labs | Independent implementations based on user stories and automated tests | 7 |
| Certification Projects | Larger projects combining multiple programming concepts | 2 |
| **Total** | **Documented Python projects** | **20** |

```text
Workshops              ███████████  11 completed
Labs                   ███████░░░   7 completed
Certification Projects ██░░░░░░░░   2 completed
Overall                ████████████████████  20 completed
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

### Certification Projects

| # | Project | Primary Concepts | Status |
| -: | --- | --- | :---: |
| 1 | Build a User Configuration Manager | CRUD operations, dictionaries, configuration management | ✅ |
| 2 | Build a Budget App | Classes, ledgers, transfers, validation, reports, charts | ✅ |

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
│   └── README.md
│
├── certification-projects/
│   ├── build-a-user-configuration-manager/
│   │   ├── main.py
│   │   └── README.md
│   │
│   └── build-a-budget-app/
│       ├── main.py
│       └── README.md
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

The workshop sequence has progressed from basic formatting and functions to regular expressions, structured validation, object composition, properties, setters, controlled class state, inheritance, polymorphism, and custom exceptions.

The latest completed workshop, **Build a Media Catalogue**, introduced parent and child classes, `super()`, method overriding, custom exception objects, and type-based collection filtering.

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

The latest completed lab, **Build a Game Character Stats Tracker**, strengthened property-based state management through read-only properties, validated setters, clamped numeric ranges, and controlled level progression.

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

### Programming Logic

- `if`, `elif`, and `else`
- Comparison and membership operators
- Boolean logic
- Nested conditions
- State-dependent behavior
- Boundary-condition handling
- Business-rule validation
- Controlled program flow

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

---

## Selected Project Highlights

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
Movie + TVSeries + MediaCatalogue
        ↓
Inheritance, polymorphism, filtering, and custom exceptions
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
| Media Catalogue | Inheritance, polymorphism, custom exceptions, and collection filtering |
| Budget App | Transaction systems, cross-object transfers, reporting |

This progression establishes a foundation for maintainable engineering software.

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
11. Add comments, docstrings, and README documentation.
12. Commit the completed project.

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

---

## Current Roadmap

### Immediate Priorities

- Continue the freeCodeCamp Python Certification
- Complete additional workshops and labs
- Deepen object-oriented programming skills
- Strengthen inheritance and polymorphism
- Improve custom exception design
- Practice automated testing
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
Workshops:               11
Labs:                     7
Certification Projects:   2
Total Projects:          20
```

Latest completed workshop:

```text
Build a Media Catalogue
```

Latest completed lab:

```text
Build a Game Character Stats Tracker
```

Latest completed certification project:

```text
Build a Budget App
Automated tests: 24/24 passed
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

The implementations, comments, documentation, repository organization, and engineering-oriented extensions reflect my personal learning process.

---

## Author

**Duong Kim Cuong**

Coastal Engineering · Scientific Computing · Python · Artificial Intelligence

GitHub: [github.com/kcduong994](https://github.com/kcduong994)
