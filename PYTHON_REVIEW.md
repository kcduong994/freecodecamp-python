# Python Certification Review

> An independently written study guide based on the concepts covered in the
> freeCodeCamp Python Certification and the projects completed in this repository.
>
> Original curriculum: https://www.freecodecamp.org/learn/python-v9/
>
> This document summarizes concepts in original wording and uses independently
> written examples. It is not a verbatim copy of the freeCodeCamp review page.

![Python](https://img.shields.io/badge/Python-Certification_Review-3776AB?logo=python&logoColor=white)
![Coverage](https://img.shields.io/badge/Coverage-Fundamentals_to_Algorithms-16A34A)
![Status](https://img.shields.io/badge/Status-Study_Guide-7C3AED)

---

## Table of Contents

- [1. Python Fundamentals](#1-python-fundamentals)
- [2. Variables, Types, and Mutability](#2-variables-types-and-mutability)
- [3. Strings](#3-strings)
- [4. Numbers and Operators](#4-numbers-and-operators)
- [5. Conditionals and Boolean Logic](#5-conditionals-and-boolean-logic)
- [6. Lists, Tuples, Sets, and Dictionaries](#6-lists-tuples-sets-and-dictionaries)
- [7. Loops, Ranges, and Comprehensions](#7-loops-ranges-and-comprehensions)
- [8. Functions, Scope, and Lambda Expressions](#8-functions-scope-and-lambda-expressions)
- [9. Modules, Exceptions, and File Handling](#9-modules-exceptions-and-file-handling)
- [10. Object-Oriented Programming](#10-object-oriented-programming)
- [11. Abstract Classes and Design Patterns](#11-abstract-classes-and-design-patterns)
- [12. Data Structures](#12-data-structures)
- [13. Searching and Sorting Algorithms](#13-searching-and-sorting-algorithms)
- [14. Graphs and Trees](#14-graphs-and-trees)
- [15. Recursion, Backtracking, and Dynamic Programming](#15-recursion-backtracking-and-dynamic-programming)
- [16. Numerical Methods and Validation Algorithms](#16-numerical-methods-and-validation-algorithms)
- [17. Complexity and Performance](#17-complexity-and-performance)
- [18. Common Exam Traps](#18-common-exam-traps)
- [19. Project-to-Concept Map](#19-project-to-concept-map)
- [20. Final Revision Checklist](#20-final-revision-checklist)

---

## 1. Python Fundamentals

Python is a general-purpose, dynamically typed programming language used in
automation, web development, data science, artificial intelligence, scientific
computing, cybersecurity, embedded systems, and engineering analysis.

A basic program:

```python
message = "Hello, Python!"
print(message)
```

### Running Python

A Python file can be executed from a terminal:

```bash
python main.py
```

The interactive shell uses a Read-Evaluate-Print Loop:

```text
Read input
    ↓
Evaluate expression
    ↓
Print result
    ↓
Wait for the next command
```

### Naming Rules

Valid variable names:

```python
station_id = "ST-01"
_model_version = 3
salinity_2026 = 18.4
```

Invalid variable names:

```python
# 2station = "A"    # Starts with a number
# model-version = 3 # Hyphen is not allowed
# class = "A"       # Reserved keyword
```

Use `snake_case` for variables and functions, `PascalCase` for classes, and
uppercase names for constants.

---

## 2. Variables, Types, and Mutability

Python determines a variable's type from the value assigned to it.

```python
count = 10
ratio = 0.75
name = "Station A"
is_active = True
```

### Common Built-in Types

| Type | Example | Mutable? |
| --- | --- | :---: |
| `int` | `42` | No |
| `float` | `3.14` | No |
| `complex` | `2 + 3j` | No |
| `bool` | `True` | No |
| `str` | `"coast"` | No |
| `tuple` | `(1, 2)` | No |
| `range` | `range(5)` | No |
| `NoneType` | `None` | No |
| `list` | `[1, 2]` | Yes |
| `set` | `{1, 2}` | Yes |
| `dict` | `{"id": 1}` | Yes |

### Type Inspection

```python
value = 12.5

print(type(value))                 # <class 'float'>
print(isinstance(value, float))    # True
print(isinstance(value, (int, float)))  # True
```

`type(x) is SomeClass` requires the exact type. `isinstance(x, SomeClass)`
also accepts subclasses.

### Mutability

Lists can be changed in place:

```python
values = [1, 2, 3]
values.append(4)
```

Strings cannot be changed in place:

```python
name = "Python"
name = name.upper()
```

### Identity vs Equality

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True: same contents
print(a is b)  # False: different objects
print(a is c)  # True: same object
```

Use `is None`, not `== None`.

---

## 3. Strings

Strings are ordered, immutable sequences of Unicode characters.

```python
text = "Python"
print(text[0])   # P
print(text[-1])  # n
```

### Slicing

```python
message = "coastal engineering"

print(message[0:7])   # coastal
print(message[8:])    # engineering
print(message[::2])   # every second character
print(message[::-1])  # reversed string
```

The stop index is exclusive.

### Escaping and Formatting

```python
quote = 'It\'s valid.'
path = "C:\\models\\run01"
station = "A12"
value = 18.25

print(f"{station}: {value:.2f}")
```

### Important String Methods

```python
raw = "  Salinity-Station-A  "

clean = raw.strip()
lower = clean.lower()
parts = clean.split("-")
joined = "_".join(parts)
replaced = clean.replace("Station", "Gauge")
```

Other important methods:

```python
text.startswith("Sal")
text.endswith("A")
text.find("Station")
text.count("a")
text.upper()
text.lower()
text.capitalize()
text.title()
text.isupper()
text.islower()
```

### Translation Tables

```python
table = str.maketrans("abc", "123")
print("cab".translate(table))  # 312
```

---

## 4. Numbers and Operators

### Arithmetic Operators

| Operator | Meaning |
| --- | --- |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | True division |
| `//` | Floor division |
| `%` | Remainder |
| `**` | Exponentiation |

```python
print(7 / 2)   # 3.5
print(7 // 2)  # 3
print(7 % 2)   # 1
print(2 ** 4)  # 16
```

### Conversion Functions

```python
print(int(3.9))       # 3
print(float(4))       # 4.0
print(int("42"))      # 42
print(str(42))        # "42"
print(bool(0))        # False
```

### Numeric Helpers

```python
print(round(7.6))     # 8
print(abs(-12))       # 12
print(pow(2, 5))      # 32
print(min(3, 7, 1))   # 1
print(max(3, 7, 1))   # 7
print(sum([1, 2, 3])) # 6
```

### Augmented Assignment

```python
total = 10
total += 5
total *= 2
total //= 3
```

---

## 5. Conditionals and Boolean Logic

### Comparison Operators

```python
x == y
x != y
x > y
x < y
x >= y
x <= y
```

### Conditional Branching

```python
water_level = 2.8

if water_level > 3.0:
    status = "warning"
elif water_level > 2.0:
    status = "watch"
else:
    status = "normal"
```

Only the first matching branch runs in an `if`/`elif`/`else` chain.

### Truthy and Falsy Values

Common falsy values:

```python
False
None
0
0.0
""
[]
{}
set()
```

Most other values are truthy.

### Boolean Operators

```python
is_valid = value >= 0 and value <= 35
is_special = name == "A" or name == "B"
is_missing = not records
```

`and` and `or` return operands, not necessarily `True` or `False`.

```python
print("" or "fallback")  # fallback
print("ready" and 42)    # 42
```

They short-circuit from left to right.

---

## 6. Lists, Tuples, Sets, and Dictionaries

## Lists

Lists are ordered, indexed, and mutable.

```python
values = [10, 20, 30]
values[1] = 25
```

Important methods:

```python
values.append(40)
values.extend([50, 60])
values.insert(1, 15)
values.remove(25)
last = values.pop()
values.sort()
values.reverse()
values.clear()
```

`append()` adds one object. `extend()` adds each item from an iterable.

```python
a = [1, 2]
a.append([3, 4])  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])  # [1, 2, 3, 4]
```

### Unpacking

```python
name, age, role = ["Alice", 30, "Engineer"]
first, *middle, last = [1, 2, 3, 4, 5]
```

## Tuples

Tuples are ordered and immutable.

```python
point = (128.5, 35.2)
x, y = point
```

A one-item tuple requires a comma:

```python
single = (5,)
```

Useful methods:

```python
point.count(128.5)
point.index(35.2)
```

## Sets

Sets are unordered collections of unique values.

```python
stations = {"A", "B", "C"}
stations.add("D")
stations.discard("B")
```

Set operations:

```python
a | b  # union
a & b  # intersection
a - b  # difference
a ^ b  # symmetric difference
```

## Dictionaries

Dictionaries store key-value pairs.

```python
station = {
    "id": "A01",
    "salinity": 18.4,
}
```

Access and update:

```python
station["salinity"] = 19.1
station["location"] = "estuary"

value = station.get("temperature", None)
```

Important methods:

```python
station.keys()
station.values()
station.items()
station.update({"depth": 5.2})
station.pop("depth")
```

Dictionary iteration:

```python
for key, value in station.items():
    print(key, value)
```

---

## 7. Loops, Ranges, and Comprehensions

### `for` Loops

```python
for station in ["A", "B", "C"]:
    print(station)
```

### `range()`

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```python
list(range(5))          # [0, 1, 2, 3, 4]
list(range(2, 6))       # [2, 3, 4, 5]
list(range(10, 0, -2))  # [10, 8, 6, 4, 2]
```

The stop value is exclusive.

### `while` Loops

```python
count = 3

while count > 0:
    print(count)
    count -= 1
```

### Loop Control

```python
for value in values:
    if value < 0:
        continue
    if value > 100:
        break
```

### `enumerate()` and `zip()`

```python
for index, value in enumerate(values):
    print(index, value)

for name, score in zip(names, scores):
    print(name, score)
```

### List Comprehensions

```python
squares = [number ** 2 for number in range(6)]
evens = [number for number in range(10) if number % 2 == 0]
```

Nested comprehension:

```python
matrix = [
    [0 for _ in range(4)]
    for _ in range(4)
]
```

---

## 8. Functions, Scope, and Lambda Expressions

### Functions

```python
def calculate_mean(values):
    if not values:
        return None

    return sum(values) / len(values)
```

A function without an explicit `return` returns `None`.

### Parameters

```python
def power(base, exponent=2):
    return base ** exponent
```

Keyword arguments:

```python
power(exponent=3, base=2)
```

### Variable-Length Arguments

```python
def total(*numbers):
    return sum(numbers)


def create_record(**fields):
    return fields
```

### Scope: LEGB

Python resolves names through:

```text
Local
  ↓
Enclosing
  ↓
Global
  ↓
Built-in
```

```python
tax = 0.1

def outer():
    discount = 0.05

    def inner(price):
        return price * (1 + tax - discount)

    return inner
```

Use `global` and `nonlocal` sparingly.

### Lambda Expressions

```python
square = lambda number: number ** 2
```

Common with `sorted()`, `map()`, and `filter()`:

```python
records = [
    {"id": "B", "value": 4},
    {"id": "A", "value": 7},
]

ordered = sorted(records, key=lambda record: record["id"])
```

### `map()` and `filter()`

```python
numbers = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

Comprehensions are often more readable.

---

## 9. Modules, Exceptions, and File Handling

### Importing Modules

```python
import math
from pathlib import Path
from statistics import mean
```

Aliases:

```python
import numpy as np
```

### Exception Handling

```python
try:
    value = float(user_input)
except ValueError:
    print("Enter a valid number.")
else:
    print("Conversion succeeded.")
finally:
    print("Operation finished.")
```

Raise an exception when an invariant is violated:

```python
if salinity < 0:
    raise ValueError("Salinity cannot be negative.")
```

### Custom Exceptions

```python
class InvalidStationError(Exception):
    pass
```

### File Handling

```python
from pathlib import Path

path = Path("data.txt")
content = path.read_text(encoding="utf-8")
path.write_text("processed", encoding="utf-8")
```

Context manager:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

---

## 10. Object-Oriented Programming

### Classes and Instances

```python
class MonitoringStation:
    def __init__(self, station_id, salinity=0.0):
        self.station_id = station_id
        self.salinity = salinity

    def report(self):
        return f"{self.station_id}: {self.salinity}"
```

### Instance and Class Attributes

```python
class Sensor:
    category = "environmental"

    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
```

`category` is shared by the class. `sensor_id` belongs to each instance.

### Encapsulation and Properties

```python
class Observation:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value cannot be negative.")

        self._value = new_value
```

### Special Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y
```

Common special methods:

```text
__init__   object initialization
__str__    user-friendly representation
__repr__   developer representation
__len__    len(obj)
__eq__     obj1 == obj2
__add__    obj1 + obj2
__iter__   iteration support
```

### Inheritance

```python
class NumericalModel:
    def __init__(self, name):
        self.name = name

    def run(self):
        return "base run"


class SalinityModel(NumericalModel):
    def __init__(self, name, layers):
        super().__init__(name)
        self.layers = layers

    def run(self):
        return "salinity simulation"
```

### Polymorphism

Different classes can provide the same method interface:

```python
for model in models:
    print(model.run())
```

---

## 11. Abstract Classes and Design Patterns

### Abstract Base Classes

```python
from abc import ABC, abstractmethod


class ValidationMetric(ABC):
    @abstractmethod
    def calculate(self, observed, simulated):
        raise NotImplementedError
```

Concrete subclasses must implement every abstract method before instantiation.

### Strategy Pattern

```python
class MeanAbsoluteError(ValidationMetric):
    def calculate(self, observed, simulated):
        differences = [
            abs(obs - sim)
            for obs, sim in zip(observed, simulated)
        ]
        return sum(differences) / len(differences)
```

An orchestration class can accept interchangeable strategies.

### Composition vs Inheritance

Use inheritance for an “is-a” relationship.

```text
SalinityModel is a NumericalModel
```

Use composition for a “has-a” relationship.

```text
Simulation has a ValidationMetric
```

---

## 12. Data Structures

### Stack

Last-In-First-Out:

```python
stack = []
stack.append("A")
stack.append("B")
current = stack.pop()  # B
```

Used by DFS and recursive algorithms.

### Queue

First-In-First-Out:

```python
from collections import deque

queue = deque(["A"])
queue.append("B")
current = queue.popleft()
```

A `deque` is preferable to repeated `list.pop(0)` in production code.

### Linked List

A linked list stores values in nodes connected by references.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Hash Table

A hash table maps keys to buckets using a hash function. Collision handling is
required because different keys can map to the same bucket.

### Adjacency List

Compact for sparse graphs:

```python
graph = {
    0: [1, 2],
    1: [2],
    2: [0],
}
```

### Adjacency Matrix

Direct edge lookup:

```python
matrix = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0],
]
```

---

## 13. Searching and Sorting Algorithms

### Binary Search

Requires sorted input.

```python
def binary_search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        middle = (low + high) // 2

        if values[middle] == target:
            return middle

        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return None
```

Time complexity: `O(log n)`.

### Selection Sort

Repeatedly selects the smallest remaining item.

Time complexity: `O(n²)`.

### Merge Sort

Splits, sorts recursively, and merges.

Time complexity: `O(n log n)`.
Typical auxiliary space: `O(n)`.

### Quicksort

Partitions around a pivot.

Average time: `O(n log n)`.
Worst case: `O(n²)`.

### In-Place vs New-List Sorting

```python
values.sort()          # Mutates values
ordered = sorted(values)  # Returns a new list
```

The completed labs intentionally distinguish these behaviors.

---

## 14. Graphs and Trees

### Graph Terminology

- Vertex/node: an entity in the graph.
- Edge: a connection between nodes.
- Directed graph: edges have direction.
- Undirected graph: edges work both ways.
- Weighted graph: edges have costs.
- Path: a sequence of connected nodes.
- Cycle: a path that returns to an earlier node.

### Breadth-First Search

BFS explores level by level using a queue.

```python
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited
```

Useful for unweighted shortest paths and level-order traversal.

### Depth-First Search

DFS explores one branch deeply using a stack or recursion.

```python
def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        stack.extend(graph[current])

    return visited
```

### Dijkstra's Algorithm

Dijkstra computes shortest paths in graphs with non-negative edge weights.

Core steps:

```text
Initialize distances
        ↓
Choose nearest unvisited node
        ↓
Relax outgoing edges
        ↓
Mark node visited
        ↓
Repeat
```

### Trees and Heaps

A tree is a connected acyclic graph. A binary tree has at most two children per
node. A heap is a specialized tree commonly used for priority queues.

```python
import heapq

heap = [5, 2, 8]
heapq.heapify(heap)
smallest = heapq.heappop(heap)
```

---

## 15. Recursion, Backtracking, and Dynamic Programming

### Recursion

A recursive function calls itself and requires a base case.

```python
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
```

### Tower of Hanoi

The project demonstrates recursive decomposition:

```text
Move n - 1 disks
Move the largest disk
Move n - 1 disks again
```

Minimum moves:

```text
2^n - 1
```

### Backtracking

Backtracking explores a choice, recurses, and then restores state.

```text
Choose
  ↓
Explore
  ↓
Undo
```

N-Queens state:

```python
columns
main_diagonals
anti_diagonals
placement
```

Diagonal identifiers:

```python
row - column
row + column
```

### Dynamic Programming

Dynamic programming stores intermediate results to avoid repeated work.

Bottom-up Fibonacci:

```python
def fibonacci(n):
    sequence = [0, 1]

    if n < 2:
        return sequence[n]

    for _ in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[n]
```

Time: `O(n)`.
Space: `O(n)`.

---

## 16. Numerical Methods and Validation Algorithms

### Bisection Method

Bisection repeatedly halves an interval containing a root.

```text
Choose lower and upper bounds
        ↓
Compute midpoint
        ↓
Evaluate midpoint
        ↓
Keep the valid half
        ↓
Stop within tolerance
```

Important concepts:

- tolerance
- maximum iterations
- convergence
- floating-point approximation
- valid initial interval

### Luhn Algorithm

The Luhn algorithm validates numeric identifiers using a checksum.

Core operations:

```text
Normalize input
        ↓
Process digits from right to left
        ↓
Double alternating digits
        ↓
Subtract 9 when necessary
        ↓
Sum digits
        ↓
Check total modulo 10
```

---

## 17. Complexity and Performance

Big O describes how resource use grows with input size.

| Complexity | Typical Example |
| --- | --- |
| `O(1)` | Dictionary lookup, set membership |
| `O(log n)` | Binary search |
| `O(n)` | Linear scan, iterative Fibonacci |
| `O(n log n)` | Merge sort, average quicksort |
| `O(n²)` | Selection sort, adjacency-matrix traversal |
| `O(2^n)` | Some naive recursive searches |
| `O(n!)` | N-Queens search in the worst case |

Important distinctions:

- Time complexity: how execution time grows.
- Space complexity: how memory use grows.
- Auxiliary space: extra memory excluding output storage.
- Average case and worst case may differ.

---

## 18. Common Exam Traps

### `print()` vs `return`

```python
def example():
    print(5)

result = example()
print(result)  # None
```

### `append()` vs `extend()`

```python
values.append([3, 4])
values.extend([3, 4])
```

### `pop()` vs `pop(0)`

```python
stack.pop()   # removes last
queue.pop(0)  # removes first, but inefficient for large lists
```

### `is` vs `==`

```python
a == b  # value equality
a is b  # object identity
```

### Mutable Aliasing

```python
a = [1, 2]
b = a
b.append(3)

print(a)  # [1, 2, 3]
```

### Shared Nested Lists

Wrong:

```python
matrix = [[0] * 3] * 3
```

Every row references the same list.

Correct:

```python
matrix = [[0] * 3 for _ in range(3)]
```

### Default Mutable Arguments

Avoid:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Prefer:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

### Off-by-One Errors

```python
range(2, n + 1)
```

is required when index `n` must be included.

### Recursive State Copies

```python
solutions.append(placement.copy())
```

stores a snapshot. Appending `placement` directly stores the same mutable object.

### Exact Output

Automated tests may check:

- spaces
- punctuation
- capitalization
- newline placement
- data type
- mutation behavior
- function signature

---

## 19. Project-to-Concept Map

| Repository Project | Main Concepts |
| --- | --- |
| Report Card Printer | Variables, arithmetic, formatting |
| Employee Profile Generator | Functions, parameters, strings |
| Caesar Cipher | Translation tables and string processing |
| PIN Extractor | Regular expressions |
| Medical Data Validator | Dictionaries and validation |
| Musical Instrument Inventory | Classes and methods |
| Email Simulator | Composition and timestamps |
| Salary Tracker | Properties and controlled state |
| Media Catalogue | Inheritance and polymorphism |
| Discount Calculator | Abstract classes and Strategy pattern |
| Linked List | Nodes and references |
| Binary Search | Logarithmic search |
| Merge Sort | Divide and conquer |
| Shortest Path | Dijkstra and weighted graphs |
| Breadth-First Search | FIFO state exploration |
| Bisection Method | Numerical approximation |
| Quicksort | Recursive partitioning |
| Selection Sort | In-place quadratic sorting |
| Luhn Algorithm | Checksum validation |
| Adjacency Converter | Graph representation conversion |
| Depth-First Search | LIFO graph traversal |
| N-Queens | Backtracking and constraint pruning |
| Fibonacci Calculator | Bottom-up dynamic programming |
| Hash Table | Hashing and collision handling |
| Tower of Hanoi | Recursive state generation |
| Budget App | OOP, ledgers, reporting |
| Polygon Area Calculator | Inheritance and invariants |

---

## 20. Final Revision Checklist

Before the certification exam, confirm that you can explain or predict:

- [ ] Mutable vs immutable types
- [ ] `type()` vs `isinstance()`
- [ ] `is` vs `==`
- [ ] String indexing and slicing
- [ ] List methods and mutation behavior
- [ ] Tuple unpacking
- [ ] Set operations
- [ ] Dictionary methods
- [ ] `range()` boundaries
- [ ] `for` vs `while`
- [ ] `break`, `continue`, and `pass`
- [ ] Function arguments and return values
- [ ] LEGB scope
- [ ] Exceptions and custom exceptions
- [ ] Class vs instance attributes
- [ ] Properties and setters
- [ ] Inheritance, overriding, and `super()`
- [ ] Abstract methods and polymorphism
- [ ] Stack vs queue
- [ ] Linked list and hash table fundamentals
- [ ] Binary search requirements
- [ ] Sorting complexity
- [ ] BFS vs DFS
- [ ] Dijkstra's non-negative-weight requirement
- [ ] Recursion and base cases
- [ ] Backtracking state restoration
- [ ] Dynamic programming state reuse
- [ ] Time and space complexity
- [ ] Exact-output and mutation requirements

---

## Attribution

The freeCodeCamp Python Certification curriculum and assessment structure are
provided by freeCodeCamp.

This study guide is an independently organized summary based on concepts covered
by the curriculum and on implementations completed in this repository. The
examples, explanations, organization, engineering applications, and debugging
notes are independently written.
