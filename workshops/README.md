# Python Workshops

A collection of guided Python workshop projects completed while studying the
**freeCodeCamp Python Certification**.

These workshops document my progress from Python fundamentals to text processing,
structured data validation, regular expressions, object-oriented programming,
object composition, encapsulation, properties, setters, inheritance, polymorphism,
custom exceptions, abstract base classes, polymorphic strategies, interactions between multiple objects, reference-based data structures, algorithmic search, recursion, divide-and-conquer sorting, weighted graphs, adjacency matrices, shortest-path algorithms, breadth-first search, FIFO queues, state-space exploration, and combinatorial generation.

![Python](https://img.shields.io/badge/Python-Learning-3776AB?logo=python&logoColor=white)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Python_Certification-0A0A23?logo=freecodecamp&logoColor=white)
![Workshops](https://img.shields.io/badge/Workshops_Completed-17-success)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

---

## Learning Progress

| Category               |   Completed |
| ---------------------- | ----------: |
| Workshops              |          17 |
| Guided Python Projects |          17 |
| Current Status         | In Progress |

```text
Progress: █████████████████  17 workshops completed
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
| 12 | Build a Discount Calculator          | Abstract base classes, strategy pattern, polymorphism, type hints   |   ✅   |
| 13 | Build a Linked List                  | Nodes, references, traversal, insertion, removal, custom data structures |   ✅   |
| 14 | Build a Binary Search                | Sorted data, midpoint comparison, search boundaries, algorithm tracing |   ✅   |
| 15 | Implement the Merge Sort Algorithm   | Recursion, divide and conquer, slice syntax, sorted merging, in-place updates |   ✅   |
| 16 | Implement the Shortest Path Algorithm | Weighted graphs, adjacency matrices, Dijkstra's algorithm, path reconstruction |   ✅   |
| 17 | Implement the Breadth-First Search Algorithm | BFS, FIFO queues, state-space exploration, balanced-parentheses generation |   ✅   |

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
├── build-a-discount-calculator/
├── build-a-linked-list/
├── build-a-binary-search/
├── implement-the-merge-sort-algorithm/
├── implement-the-shortest-path-algorithm/
├── implement-the-breadth-first-search-algorithm/
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
- Abstract base classes with `ABC`
- Abstract methods with `@abstractmethod`
- Strategy-pattern design
- Interchangeable algorithm objects

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
- Defining a shared strategy interface
- Implementing multiple concrete strategy classes
- Calling overridden methods through a common parent type

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
- Storing strategy objects in a list
- Collecting candidate numeric results
- Selecting the lowest result with `min()`
- Building a linked data structure from custom node objects
- Maintaining a `head` reference to the first node
- Traversing a chain of objects through `.next` references
- Updating links when adding or removing nodes
- Searching sorted collections efficiently
- Tracking values checked during an algorithm
- Returning structured search results
- Splitting lists into left and right halves
- Merging sorted sublists into the original list
- Updating sorted positions with multiple indexes
- Performing in-place sorting through recursive function calls
- Representing weighted graphs with adjacency matrices
- Storing unavailable edges with positive infinity
- Tracking shortest known distances in a list
- Tracking visited and unvisited graph nodes
- Reconstructing complete paths with nested lists
- Converting path nodes with generator expressions
- Formatting readable routes with `str.join()`
- Representing BFS states as tuples
- Using a list as a FIFO queue
- Removing the oldest state with `pop(0)`
- Expanding valid successor states
- Generating balanced-parentheses combinations

### Data Structures

- Custom linked lists
- Nested `Node` classes
- Node objects with stored elements
- Reference-based connections between objects
- The `head` reference
- The `next` reference
- Empty-list detection
- Appending a node to the end of a linked list
- Traversing nodes with a `while` loop
- Stopping traversal at `None`
- Removing the first matching node
- Updating links to bypass a removed node
- Handling removal from the head of the list
- Handling removal from the middle or end of the list
- Maintaining a manual `length` counter
- Understanding reference assignment direction
- Comparing linked lists with built-in Python lists

### Breadth-First Search and State-Space Exploration

- Breadth-first search (BFS)
- FIFO queue behavior
- Queue initialization
- Level-by-level state processing
- Tuple-based state representation
- Tuple unpacking
- Valid successor-state generation
- Constraint-based pruning
- Completion detection by target length
- Balanced-parentheses generation
- Distinguishing graph traversal from general state-space search

### Search Algorithms

- Linear search versus binary search
- Sorted input requirements
- Search boundaries
- `low`, `high`, and `mid` variables
- Integer division for midpoint calculation
- Middle-value comparison
- Reducing the search range by half
- Returning early when the target is found
- Returning a not-found result when the range is exhausted
- Tracing checked values during the search
- Understanding algorithmic efficiency

### Graph Algorithms

- Weighted graphs
- Adjacency matrices
- Nodes, edges, and edge weights
- Positive infinity as an unreachable-distance sentinel
- Dijkstra's shortest-path algorithm
- Selecting the unvisited node with the smallest known distance
- Edge relaxation
- Updating shortest known distances
- Reconstructing paths by extending the current path
- Skipping unreachable nodes
- Optional target-node selection
- Formatting complete paths for console output
- Understanding why negative edge weights are incompatible with Dijkstra's algorithm

### Sorting Algorithms

- Merge sort
- Divide-and-conquer problem solving
- Recursive sorting
- Base cases in recursive functions
- List splitting with slice syntax
- Left and right subarray management
- Merging two sorted lists
- Comparing current values from two halves
- Maintaining multiple index variables
- Updating the original list in place
- Copying remaining values after one side is exhausted
- Understanding stable sorting behavior conceptually
- Tracing recursive algorithm flow

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
- Preventing direct instantiation of incomplete abstract classes
- Enforcing required subclass methods

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
- Separating discount rules from calculation orchestration
- Injecting strategies into a calculation engine
- Selecting the best result from multiple algorithms
- Building a custom linked list from node objects
- Maintaining the head of a linked structure
- Traversing object references until `None`
- Updating links safely during removal
- Maintaining search boundaries during iterative algorithms
- Returning diagnostic information from algorithmic functions
- Using recursive function calls to solve smaller versions of the same problem
- Separating divide, sort, and merge phases in an algorithm
- Protecting base cases to prevent infinite recursion
- Using a main execution guard for algorithm demonstrations
- Separating graph representation from shortest-path processing
- Using optional parameters to support one-target or all-target output
- Maintaining synchronized distance, path, and visited-state collections
- Stopping early when no reachable unvisited node remains

---

## Workshop Highlights

### Breadth-First Search Algorithm

Implemented a breadth-first search solution that generates every valid combination of balanced parentheses for a specified number of pairs.

The completed workshop contains:

- A `gen_parentheses()` function
- Type and range validation
- A FIFO queue initialized with one empty state
- Tuple-based BFS states
- Queue processing with `pop(0)`
- Valid opening- and closing-parenthesis expansion
- Completion detection using the target string length
- A result list containing all valid combinations

Core implementation:

```python
def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'

    if pairs < 1:
        return 'The number of pairs should be at least 1'

    queue = [('', 0, 0)]
    result = []

    while queue:
        current, opens_used, closes_used = queue.pop(0)

        if len(current) == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append(
                    (current + '(', opens_used + 1, closes_used)
                )

            if closes_used < opens_used:
                queue.append(
                    (current + ')', opens_used, closes_used + 1)
                )

    return result
```

Each BFS state has the form:

```text
(current_string, opening_count, closing_count)
```

Traversal flow:

```text
Start with an empty state
        ↓
Remove the oldest queued state
        ↓
Check whether it is complete
        ↓
Store complete states
        ↓
Generate valid successor states
        ↓
Append successors to the back of the queue
        ↓
Continue until the queue is empty
```

Example results:

```text
gen_parentheses(2)
→ ['(())', '()()']

gen_parentheses(3)
→ ['((()))', '(()())', '(())()', '()(())', '()()()']
```

This workshop strengthened:

- Breadth-first search
- FIFO queue behavior
- State-space exploration
- Tuple unpacking
- Constraint-based branching
- Balanced-parentheses generation
- Validation before algorithm execution

---

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

### Binary Search

Implemented an iterative binary search algorithm for sorted lists.

The completed workshop contains:

- A `binary_search()` function
- A sorted input list
- A target value
- A `path_to_target` list for tracing checked values
- `low` and `high` search boundaries
- A `mid` index calculation
- Middle-value comparison
- Right-side search when the target is larger
- Left-side search when the target is smaller
- A found result with the target index
- A not-found result when the search range is exhausted

The function signature is:

```python
def binary_search(search_list, value):
```

The algorithm starts by defining the search range:

```python
low = 0
high = len(search_list) - 1
```

The loop continues while the range is valid:

```python
while low <= high:
```

On each iteration, the middle index is calculated:

```python
mid = (low + high) // 2
```

The value at the middle index is then checked:

```python
value_at_middle = search_list[mid]
path_to_target.append(value_at_middle)
```

If the target is found, the function returns both the checked path and the index:

```python
if value == value_at_middle:
    return path_to_target, f'Value found at index {mid}'
```

If the target is greater than the middle value, the left half can be ignored:

```python
elif value > value_at_middle:
    low = mid + 1
```

If the target is less than the middle value, the right half can be ignored:

```python
else:
    high = mid - 1
```

If the loop ends without finding the value, the target is not present:

```python
return [], 'Value not found'
```

Search flow:

```text
Sorted list
        ↓
Set low and high boundaries
        ↓
Find the middle index
        ↓
Compare target with middle value
        ↓
Discard half of the search range
        ↓
Repeat until found or range is empty
```

Example:

```python
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))
```

Expected output:

```text
([3], 'Value found at index 2')
([3, 5, 4], 'Value found at index 3')
([], 'Value not found')
```

Important condition:

```text
Binary search only works correctly when the input list is sorted.
```

Key concepts reinforced:

- Search algorithms
- Sorted data
- Integer division
- Index boundaries
- Loop conditions
- Midpoint comparison
- Algorithm tracing
- Early returns
- Not-found handling
- Debugging boundary updates

---

### Merge Sort

Implemented a recursive merge sort algorithm that sorts a list in ascending order by dividing the data into smaller parts and merging the sorted results back into the original list.

The completed workshop contains:

- A `merge_sort()` function
- A recursive base case for lists with 0 or 1 element
- A middle-point calculation
- Left and right list slicing
- Recursive sorting of each half
- Three index variables for merge control
- Comparison between current values from each sorted half
- In-place updates to the original list
- Cleanup loops for remaining left-side or right-side values
- A main execution guard for demonstration output

The function starts with the recursive base case:

```python
if len(array) <= 1:
    return
```

This prevents the function from endlessly calling itself. A list with zero or one element is already sorted.

The list is then divided into two halves:

```python
middle_point = len(array) // 2
left_part = array[:middle_point]
right_part = array[middle_point:]
```

Each half is sorted by calling the same function again:

```python
merge_sort(left_part)
merge_sort(right_part)
```

After both halves are sorted, the function merges them back into the original list using three indexes:

```python
left_array_index = 0
right_array_index = 0
sorted_index = 0
```

The main merge loop compares the current values from each half:

```python
while left_array_index < len(left_part) and right_array_index < len(right_part):
    if left_part[left_array_index] < right_part[right_array_index]:
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
    else:
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1

    sorted_index += 1
```

If one half still has values left after the other half has been fully copied, the remaining values are copied into the original list:

```python
while left_array_index < len(left_part):
    array[sorted_index] = left_part[left_array_index]
    left_array_index += 1
    sorted_index += 1

while right_array_index < len(right_part):
    array[sorted_index] = right_part[right_array_index]
    right_array_index += 1
    sorted_index += 1
```

Example:

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]

print("Unsorted array: ")
print(numbers)

merge_sort(numbers)

print("Sorted array: ")
print(numbers)
```

Expected output:

```text
Unsorted array:
[4, 10, 6, 14, 2, 1, 8, 5]
Sorted array:
[1, 2, 4, 5, 6, 8, 10, 14]
```

Merge sort flow:

```text
Original list
        ↓
Split into left and right halves
        ↓
Recursively sort each half
        ↓
Compare current values from both halves
        ↓
Write the smaller value back into the original list
        ↓
Copy any remaining values
        ↓
Sorted list
```

Recursive structure:

```text
merge_sort([4, 10, 6, 14, 2, 1, 8, 5])
        ↓
merge_sort([4, 10, 6, 14])        merge_sort([2, 1, 8, 5])
        ↓                                      ↓
merge_sort([4, 10])  merge_sort([6, 14])      merge_sort([2, 1])  merge_sort([8, 5])
        ↓                                      ↓
Single-element lists become the base cases
        ↓
Sorted halves are merged back together
```

Key concepts reinforced:

- Sorting algorithms
- Merge sort
- Recursion
- Base cases
- Divide-and-conquer design
- Slice syntax
- Integer division
- Multiple index variables
- In-place list updates
- Ordered merging
- Cleanup loops
- Main execution guards
- Algorithm tracing
- Debugging recursive flow

---

### Shortest Path Algorithm

Implemented Dijkstra's shortest-path algorithm for a weighted graph represented by an adjacency matrix.

The completed workshop contains:

- An `INF` constant representing missing direct connections
- A weighted adjacency matrix
- A `shortest_path()` function
- Distance initialization with positive infinity
- A `visited` list for finalized nodes
- A `paths` list for complete route reconstruction
- Selection of the nearest unvisited node
- Edge relaxation for neighboring nodes
- Optional output for one target node or all reachable nodes
- Generator expressions for converting node numbers to strings
- Readable route formatting with `" -> ".join(...)`
- A `main()` function and execution guard

The graph is represented by a two-dimensional list:

```python
INF = float("inf")

adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]
```

Each matrix position stores the edge weight from one node to another:

```text
matrix[current][neighbor]
        ↓
Direct edge weight
```

The algorithm begins by assigning infinity to every distance except the starting node:

```python
distances = [INF] * n
distances[start_node] = 0
```

On each iteration, the nearest unvisited node is selected:

```python
for node_no in range(n):
    if not visited[node_no] and distances[node_no] < min_distance:
        min_distance = distances[node_no]
        current = node_no
```

Neighboring routes are improved through the relaxation step:

```python
new_distance = distances[current] + distance

if new_distance < distances[node_no]:
    distances[node_no] = new_distance
    paths[node_no] = paths[current] + [node_no]
```

Shortest-path flow:

```text
Initialize distances and paths
        ↓
Select the nearest unvisited node
        ↓
Mark it as visited
        ↓
Inspect each reachable neighbor
        ↓
Calculate a candidate distance
        ↓
Update the distance and path if shorter
        ↓
Repeat until no reachable node remains
```

Example output:

```text
0-5 distance: 6
Path: 0 -> 2 -> 1 -> 5
```

Key concepts reinforced:

- Weighted graphs
- Adjacency matrices
- Dijkstra's algorithm
- Positive infinity
- Boolean visited-state tracking
- Minimum-distance node selection
- Edge relaxation
- Path reconstruction
- Nested lists
- Generator expressions
- Conditional expressions
- Optional function parameters
- Readable formatted output
- Algorithm tracing and debugging

---

### Linked List

Built a custom linked list implementation using nested node objects and reference-based traversal.

The completed workshop contains:

- A `LinkedList` class
- A nested `Node` class
- A `length` counter
- A `head` reference
- An `is_empty()` method
- An `add()` method for appending elements
- A `remove()` method for deleting the first matching element
- Traversal through `.next` references
- Safe handling of empty lists
- Safe handling of missing elements
- Removal from the head of the list
- Removal from the middle or end of the list

The `Node` class stores one value and a reference to the next node:

```python
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
```

The linked list itself stores the first node and the number of nodes:

```python
def __init__(self):
    self.length = 0
    self.head = None
```

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
Set the final node's next reference to the new node
        ↓
Increase length
```

The `add()` method uses `self.head = node` when the list is empty. The assignment direction is important because the list's head must point to the newly created node.

```python
if self.is_empty():
    self.head = node
```

For a non-empty list, traversal continues until the final node is found:

```python
while current_node.next is not None:
    current_node = current_node.next
```

The condition uses `is not None` because `None` is a singleton value in Python and should be checked by identity.

Removing a node follows this flow:

```text
Start at head
        ↓
Track previous_node and current_node
        ↓
Move forward until the target element is found
        ↓
If not found, return without changing the list
        ↓
If removing the head, move head to the next node
        ↓
Otherwise, bypass the current node
        ↓
Decrease length
```

The removal logic handles two important cases:

```python
elif previous_node is not None:
    previous_node.next = current_node.next
else:
    self.head = current_node.next
```

This distinction is necessary because removing the head changes the list entry point, while removing a later node only changes the previous node's `.next` reference.

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

Class relationship:

```text
LinkedList
    ├── length
    ├── head ──▶ Node(element=1)
    │              └── next ──▶ Node(element=2)
    │                              └── next ──▶ None
    └── methods
        ├── is_empty()
        ├── add(...)
        └── remove(...)
```

Key concepts reinforced:

- Custom data structures
- Nested classes
- Nodes and links
- Object references
- Manual length tracking
- Linked-list traversal
- `while` loops
- `None` checks with `is not None`
- Reference reassignment
- Head-node updates
- Removing elements by bypassing nodes
- Distinguishing an empty list from a non-empty list
- Understanding how linked lists differ from built-in Python lists

---

### Discount Calculator

Built a flexible discount-calculation system that evaluates multiple pricing
strategies and returns the lowest valid price.

The completed project contains:

- A `Product` class for product data
- An abstract `DiscountStrategy` base class
- A `PercentageDiscount` strategy
- A `FixedAmountDiscount` strategy
- A `PremiumUserDiscount` strategy
- A `DiscountEngine` that evaluates all available strategies
- Type hints for parameters, return values, and strategy collections
- A main execution guard
- Two-decimal-place currency formatting

The abstract strategy interface defines two required operations:

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

Each concrete strategy decides:

1. Whether it applies to the current product and user.
2. How it calculates the discounted price.

Example strategies:

```python
strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount(),
]
```

The discount engine accepts the strategies through its constructor:

```python
engine = DiscountEngine(strategies)
best_price = engine.calculate_best_price(
    product,
    user_tier,
)
```

Calculation flow:

```text
Original product price
        ↓
Check each discount strategy
        ↓
Call is_applicable(...)
        ↓
Apply valid discounts
        ↓
Store all candidate prices
        ↓
Return min(prices)
```

The original price is included in the list of candidates:

```python
prices = [product.price]
```

This ensures that the calculator can safely return the original price when no
discount applies.

Example:

```python
product = Product("Wireless Mouse", 50.0)
user_tier = "Premium"

strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount(),
]

engine = DiscountEngine(strategies)
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

Class relationship:

```text
DiscountStrategy
    ├── PercentageDiscount
    ├── FixedAmountDiscount
    └── PremiumUserDiscount
              ↓
        DiscountEngine
              ↓
Evaluates applicable strategies
              ↓
Returns the lowest price
```

Key concepts reinforced:

- Abstract base classes
- Abstract methods
- Inheritance
- Method overriding
- Runtime polymorphism
- Strategy pattern
- Dependency injection through constructors
- Type hints
- Lists of related objects
- Candidate-result aggregation
- Built-in `min()`
- Main execution guards
- Currency formatting with `:.2f`

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
        ↓
DiscountStrategy
        ↓
Abstract interfaces and required subclass behavior
        ↓
Percentage, fixed-amount, and premium strategies
        ↓
Polymorphic discount calculations
        ↓
DiscountEngine
        ↓
Strategy orchestration and best-price selection
        ↓
LinkedList and Node
        ↓
Reference-based data structures, traversal, and link updates
        ↓
Binary Search
        ↓
Sorted data, midpoint comparison, and logarithmic search
        ↓
Merge Sort
        ↓
Recursive divide-and-conquer sorting and ordered merging
        ↓
Shortest Path Algorithm
        ↓
Weighted graphs, adjacency matrices, edge relaxation, and path reconstruction
        ↓
Breadth-First Search Algorithm
        ↓
FIFO queues, state-space exploration, and valid-combination generation
```

The Salary Tracker extended the progression from basic classes and object composition
toward reliable object models that enforce business rules internally.

The Media Catalogue introduced inheritance by placing shared media data and validation
inside the `Movie` parent class. `TVSeries` then reused and extended this behavior through
`super()`.

The project also introduced polymorphism. Calling `str()` on a `Movie` object and a
`TVSeries` object executes different `__str__()` implementations even though both objects
can be stored in the same catalogue.

The Discount Calculator extended this progression with abstract base classes and the strategy pattern. Multiple discount algorithms implement the same interface, allowing `DiscountEngine` to evaluate them uniformly without depending on their individual calculation details.

The Linked List workshop then introduced a lower-level data-structure perspective. Instead of storing values directly in a built-in Python list, values are stored in `Node` objects connected through `.next` references. This reinforces how objects can form chains and how program state can be managed through references.

The Merge Sort workshop extended the algorithmic progression from searching sorted data to sorting unsorted data. It reinforced recursion, base cases, divide-and-conquer design, list slicing, and careful index management during the merge phase.

The Shortest Path Algorithm workshop then introduced weighted graph processing. It reinforced adjacency-matrix representation, minimum-distance node selection, visited-state tracking, edge relaxation, path reconstruction, generator expressions, and optional target-based output.

The Breadth-First Search workshop extended algorithmic thinking from path optimization to systematic state-space exploration. It reinforced FIFO queue behavior, tuple-based state tracking, constrained branching, and generation of all valid balanced-parentheses combinations.

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
object-oriented design, inheritance, abstract interfaces, design patterns, error handling, and practical problem-solving habits.

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

The Binary Search workshop also reinforced these debugging lessons:

- Binary search requires sorted input data.
- The middle index should be calculated with integer division: `(low + high) // 2`.
- If the target is greater than the middle value, move the lower boundary with `low = mid + 1`.
- If the target is less than the middle value, move the upper boundary with `high = mid - 1`.
- A function call must be placed inside `print(...)` when the returned result needs to be displayed.
- Returning a path of checked values is useful for understanding how the algorithm narrows the search range.

The Merge Sort workshop also reinforced these debugging lessons:

- The recursive base case must return before the list is split again.
- Slice syntax uses `array[:middle_point]` and `array[middle_point:]`, not the `slice()` constructor for this workshop.
- Recursive calls sort the left and right copies before merging them back into the original list.
- Three indexes are needed during the merge phase: one for the left half, one for the right half, and one for the original list.
- Each index must be incremented in the correct branch to avoid repeated values or infinite loops.
- Cleanup loops are required because one half may still contain remaining values after the main comparison loop ends.
- The `if __name__ == "__main__":` guard requires `==`, not `is`, when comparing `__name__` with `"__main__"`.
- Exact `print()` output matters in guided workshop steps.

The Breadth-First Search workshop also reinforced these debugging lessons:

- Use `while queue:` to continue while a queue is non-empty.
- `queue is not []` is incorrect because `is` checks identity, not list contents.
- `queue.pop(0)` removes and returns the oldest state.
- The popped tuple should be unpacked directly into the state variables.
- `append()` accepts one object, so a complete state must be appended as a tuple.
- Add an opening parenthesis only while `opens_used < pairs`.
- Add a closing parenthesis only while `closes_used < opens_used`.
- Return the completed result list separately from demonstration printing.

The Shortest Path Algorithm workshop also reinforced these debugging lessons:

- A two-dimensional list must use outer square brackets rather than a tuple when the workshop explicitly requires a list.
- An unvisited-state check uses `not visited[node_no]`.
- A conditional expression requires the complete form `value_if_true if condition else value_if_false`.
- `target_node is not None` is the correct identity comparison for an optional value.
- A path must be updated with `paths[current] + [node_no]`, not by adding two integer node indexes.
- A generator expression that converts node numbers uses `(str(n) for n in paths[node_no])`.
- Values inside an f-string require braces such as `{distances[node_no]}` and `{path}`.
- The algorithm must stop when no reachable unvisited node remains, represented by `current == -1`.
- `INF` represents an unavailable edge or an unreachable node, not a large ordinary distance.
- Dijkstra's algorithm assumes non-negative edge weights.

The Linked List workshop also reinforced these debugging lessons:

- Assignment direction matters: `self.head = node` and `node = self.head` mean completely different things.
- `None` should be checked with `is None` or `is not None`.
- A traversal loop must move to the next node, otherwise it can become an infinite loop.
- Removing the head node requires updating `self.head`.
- Removing a non-head node requires updating `previous_node.next`.
- A manual `length` counter must be updated when nodes are added or removed.
- Returning early is appropriate when the target element is not found.

The Discount Calculator workshop also reinforced these debugging lessons:

- Abstract subclasses must implement every required abstract method.
- Parameter names must match the names used inside a method body.
- A list uses the built-in `min(prices)` function rather than `prices.min()`.
- Objects must be created only after their required input variables exist.
- Instance methods must be called through an instance such as `engine.calculate_best_price(...)`.
- Variables inside the main execution block must remain correctly indented.
- Exact f-string syntax and `:.2f` formatting matter for required output.

---

## Current Progress

```text
Completed:  █████████████████  17
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
        ↓
Abstract Base Classes
        ↓
Strategy Pattern
        ↓
Polymorphic Algorithm Selection
        ↓
Custom Data Structures
        ↓
Linked Lists, Nodes, and References
        ↓
Binary Search and Algorithmic Thinking
        ↓
Merge Sort, Recursion, and Divide-and-Conquer Sorting
        ↓
Weighted Graphs, Dijkstra's Algorithm, and Shortest Paths
        ↓
Breadth-First Search, FIFO Queues, and State-Space Exploration
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
- Understanding abstract base classes
- Defining consistent interfaces with abstract methods
- Applying the strategy pattern
- Injecting interchangeable behaviors into an engine class
- Comparing candidate results safely
- Preparing for larger labs and certification projects
- Understanding custom data structures
- Traversing linked nodes through object references
- Updating links safely during insertion and deletion
- Understanding binary search on sorted lists
- Maintaining `low`, `high`, and `mid` boundaries
- Reducing the search space by half on each iteration
- Tracing algorithm paths for debugging and explanation
- Understanding merge sort
- Applying recursion with clear base cases
- Splitting lists with slice syntax
- Merging sorted sublists through index management
- Updating arrays in place during sorting
- Tracing divide-and-conquer algorithms
- Representing weighted graphs with adjacency matrices
- Understanding nodes, edges, and edge weights
- Implementing Dijkstra's shortest-path algorithm
- Selecting the nearest unvisited node
- Relaxing edges to improve known distances
- Reconstructing complete shortest paths
- Handling unreachable nodes safely
- Formatting algorithm results with generator expressions and `join()`
- Understanding breadth-first search
- Using FIFO queues to process states level by level
- Representing search states with tuples
- Generating valid successor states under explicit constraints
- Returning all valid balanced-parentheses combinations

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

A linked-list-like structure could model a chain of observations or processing steps:

```python
class ObservationNode:
    def __init__(self, observation):
        self.observation = observation
        self.next = None
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

Binary search can later support engineering workflows where sorted data must be searched efficiently.

For example, sorted time-series timestamps can be searched by narrowing the range:

```python
def find_nearest_time_index(times, target_time):
    low = 0
    high = len(times) - 1

    while low <= high:
        mid = (low + high) // 2

        if times[mid] == target_time:
            return mid
        elif times[mid] < target_time:
            low = mid + 1
        else:
            high = mid - 1

    return None
```

Possible engineering applications include:

- Searching sorted observation timestamps
- Locating model-output time steps
- Finding sorted station identifiers
- Matching calibration periods
- Looking up ordered scenario results
- Supporting efficient data retrieval before interpolation

Shortest-path algorithms can later support engineering workflows involving connected spatial or computational networks.

For example, a weighted network can represent monitoring stations, computational cells, channels, or transport links:

```python
def shortest_station_route(matrix, start_station, target_station):
    return shortest_path(
        matrix,
        start_station,
        target_station,
    )
```

Possible engineering applications include:

- Finding the lowest-cost route between monitoring stations
- Tracing minimum-distance paths through an observation network
- Selecting efficient inspection routes between coastal structures
- Representing channel or drainage connections as weighted graphs
- Finding minimum-cost data-transfer paths between computational nodes
- Supporting graph-based mesh or network preprocessing
- Comparing alternative routes through estuarine or river networks
- Modeling travel time, cost, or resistance as edge weights

Breadth-first search can later support engineering workflows involving unweighted connectivity, layered exploration, or discrete state transitions.

Possible applications include:

- Finding the minimum number of links between monitoring stations
- Traversing computational cells by connectivity level
- Exploring river or drainage networks one layer at a time
- Detecting all nodes reachable from a starting station
- Building unweighted shortest-path utilities
- Validating network connectivity before numerical analysis

Conceptual example:

```python
def reachable_stations(network, start_station):
    queue = [start_station]
    visited = {start_station}

    while queue:
        current = queue.pop(0)

        for neighbor in network[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited
```

BFS explores every state at one depth before moving to the next depth, which makes it useful for connectivity checks, level-by-level traversal, and shortest paths in unweighted networks.

Merge sort can later support engineering workflows where unsorted records must be ordered reliably before analysis.

For example, observation records can be sorted by timestamp:

```python
def merge_sort_records(records):
    if len(records) <= 1:
        return records

    middle = len(records) // 2
    left = merge_sort_records(records[:middle])
    right = merge_sort_records(records[middle:])

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index]["time"] <= right[right_index]["time"]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
```

Possible engineering applications include:

- Sorting environmental observations by time
- Ordering model-output records before comparison
- Preparing data before binary search
- Sorting station metadata by identifier
- Ordering calibration scenarios by score
- Sorting event records before report generation
- Organizing particle or trajectory outputs by timestamp
- Preparing time-series data for interpolation

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
- Strategy-based selection of calibration methods
- Interchangeable validation metrics
- Scenario-specific processing algorithms

---

## Learning Goals

These workshops provide the foundation for more advanced Python topics, including:

- Larger program architecture
- Advanced object-oriented programming
- Inheritance and polymorphism
- Abstract classes
- Design patterns
- Multiple inheritance
- File processing
- Exception handling
- Custom exceptions
- Automated testing
- Data analysis
- Search algorithms
- Sorting algorithms
- Recursion and divide-and-conquer design
- Algorithmic complexity
- Graph algorithms
- Shortest-path algorithms
- Breadth-first search
- Queue-based traversal
- State-space exploration
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
| Design Patterns       | Selecting interchangeable engineering logic  |
| Data Structures       | Building custom containers and processing chains |
| Search Algorithms     | Finding values efficiently in ordered data       |
| Sorting Algorithms     | Ordering records before analysis and reporting   |
| Graph Algorithms       | Finding minimum-cost routes through connected systems |
| Breadth-First Search   | Layered traversal, state exploration, and shortest unweighted paths |
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
