# Build a Hash Table

A Python certification project that implements a simple hash table from scratch.

This project demonstrates how key-value storage works internally by using a custom hashing function, nested dictionaries, collision handling, insertion, deletion, and lookup operations.

![Python](https://img.shields.io/badge/Python-Data_Structures-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Tests](https://img.shields.io/badge/Tests-Passed-success)
![Topic](https://img.shields.io/badge/Topic-Hash_Table-7C3AED)

---

## Table of Contents

- [Project Overview](#project-overview)
- [What Is a Hash Table?](#what-is-a-hash-table)
- [Project Requirements](#project-requirements)
- [Project Structure](#project-structure)
- [Final Data Structure](#final-data-structure)
- [Step-by-Step Implementation](#step-by-step-implementation)
- [Complete Example Flow](#complete-example-flow)
- [Collision Example](#collision-example)
- [Why a Nested Dictionary Is Used](#why-a-nested-dictionary-is-used)
- [Why `ord()` Is Used](#why-ord-is-used)
- [Why `remove()` Checks Before Deleting](#why-remove-checks-before-deleting)
- [Why `lookup()` Returns `None`](#why-lookup-returns-none)
- [Full Source Code](#full-source-code)
- [Usage Examples](#usage-examples)
- [Expected Results](#expected-results)
- [Automated Test Coverage](#automated-test-coverage)
- [Common Mistakes and Debugging Notes](#common-mistakes-and-debugging-notes)
- [Time and Space Complexity](#time-and-space-complexity)
- [Skills Practiced](#skills-practiced)
- [How to Run](#how-to-run)
- [Project Status](#project-status)

---

## Project Overview

The goal of this project is to build a small hash table manually instead of using Python's built-in dictionary directly as the only abstraction.

A hash table stores data as key-value pairs:

```text
key -> value
```

For example:

```python
'golf' -> 'sport'
```

However, a hash table does not store the original key directly at the top level. It first converts the key into a numeric hash value.

In this project, the hash value is calculated by summing the Unicode value of each character in the key.

Example:

```text
'golf'
 ↓
ord('g') + ord('o') + ord('l') + ord('f')
 ↓
103 + 111 + 108 + 102
 ↓
424
```

The final storage becomes:

```python
{
    424: {
        'golf': 'sport'
    }
}
```

---

## What Is a Hash Table?

A hash table is a data structure used to store and retrieve values efficiently.

It works in three main steps:

```text
Original key
     ↓
Hash function
     ↓
Hash value / index
     ↓
Stored value
```

In this project:

```text
'golf'
     ↓
hash('golf')
     ↓
424
     ↓
collection[424]['golf']
     ↓
'sport'
```

Hash tables are widely used because they can provide very fast lookup, insertion, and deletion when designed well.

Python's built-in `dict` is implemented using hash-table principles internally. This project builds a simplified educational version to understand the concept.

---

## Project Requirements

The project requires a class named:

```python
HashTable
```

A new `HashTable` instance must have:

```python
self.collection = {}
```

The class must implement four instance methods:

```python
hash()
add()
remove()
lookup()
```

| Method | Purpose |
| --- | --- |
| `hash(string)` | Convert a string into a numeric hash value |
| `add(key, value)` | Store a key-value pair in the hash table |
| `remove(key)` | Remove a key-value pair if it exists |
| `lookup(key)` | Retrieve a value by key, or return `None` |

---

## Project Structure

The project is stored as a certification project:

```text
certification-projects/
└── build-a-hash-table/
    ├── main.py
    └── README.md
```

- `main.py` contains the implementation.
- `README.md` explains the design, steps, and reasoning.

---

## Final Data Structure

The final storage format is:

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
    441: {
        'rose': 'flower'
    }
}
```

The outer dictionary uses the numeric hash value.

The inner dictionary stores the original key and value.

This structure is necessary because different keys can produce the same hash value.

---

## Step-by-Step Implementation

### Step 1: Define the `HashTable` Class

The project starts with a class definition:

```python
class HashTable:
```

This class represents the custom hash table.

All data and operations belong inside this class.

---

### Step 2: Initialize the Collection

When a new hash table is created, it needs an empty dictionary to store data:

```python
def __init__(self):
    self.collection = {}
```

`collection` must be a dictionary because the hash table stores values using computed hash numbers as keys.

Incorrect:

```python
self.collection = []
```

Correct:

```python
self.collection = {}
```

Example:

```python
table = HashTable()
print(table.collection)
```

Output:

```text
{}
```

---

### Step 3: Create the Hash Function

The hash function receives a string and returns the sum of the Unicode values of its characters.

```python
def hash(self, string):
    return sum(ord(char) for char in string)
```

`ord()` converts one character into its Unicode value.

Example:

```python
ord('g')  # 103
ord('o')  # 111
ord('l')  # 108
ord('f')  # 102
```

Therefore:

```python
HashTable().hash('golf')
```

calculates:

```text
103 + 111 + 108 + 102 = 424
```

and returns:

```text
424
```

The expression:

```python
sum(ord(char) for char in string)
```

means:

```text
For each character in the string:
    convert it with ord()
Then:
    add all values together
```

Equivalent longer version:

```python
def hash(self, string):
    total = 0

    for char in string:
        total += ord(char)

    return total
```

---

### Step 4: Add a Key-Value Pair

The `add()` method stores a value using a key.

```python
def add(self, key, value):
    hashed_key = self.hash(key)

    if hashed_key not in self.collection:
        self.collection[hashed_key] = {}

    self.collection[hashed_key][key] = value
```

The method receives:

```python
key
value
```

Example:

```python
table.add('golf', 'sport')
```

The first line computes the hash:

```python
hashed_key = self.hash(key)
```

For `'golf'`, this becomes:

```python
hashed_key = 424
```

If the hash bucket does not exist yet, it is created:

```python
if hashed_key not in self.collection:
    self.collection[hashed_key] = {}
```

Then the original key-value pair is stored inside the bucket:

```python
self.collection[hashed_key][key] = value
```

Final result:

```python
{
    424: {
        'golf': 'sport'
    }
}
```

---

### Step 5: Handle Hash Collisions

A collision happens when two different keys produce the same hash value.

Example:

```python
HashTable().hash('dear')  # 412
HashTable().hash('read')  # 412
```

Both keys hash to:

```text
412
```

The hash table must store both key-value pairs under the same outer hash value:

```python
{
    412: {
        'dear': 'friend',
        'read': 'book'
    }
}
```

This is why each hash value points to an inner dictionary.

Without the inner dictionary, the second value could overwrite the first one.

---

### Step 6: Remove a Key-Value Pair

The `remove()` method deletes a specific key-value pair if it exists.

```python
def remove(self, key):
    hashed_key = self.hash(key)

    if hashed_key in self.collection and key in self.collection[hashed_key]:
        del self.collection[hashed_key][key]
```

The method first computes the hash:

```python
hashed_key = self.hash(key)
```

Then it checks two things:

```python
hashed_key in self.collection
```

This confirms that the bucket exists.

```python
key in self.collection[hashed_key]
```

This confirms that the original key exists inside that bucket.

Only then does it delete the key:

```python
del self.collection[hashed_key][key]
```

This prevents `KeyError` when the key does not exist.

It also prevents deleting the entire bucket when multiple keys share the same hash value.

---

### Step 7: Look Up a Value

The `lookup()` method retrieves a value by key.

```python
def lookup(self, key):
    hashed_key = self.hash(key)

    if hashed_key in self.collection and key in self.collection[hashed_key]:
        return self.collection[hashed_key][key]

    return None
```

The method computes the hash:

```python
hashed_key = self.hash(key)
```

Then it checks whether the bucket and original key exist.

If both exist, it returns the value:

```python
return self.collection[hashed_key][key]
```

If not, it returns:

```python
None
```

Example:

```python
table = HashTable()
table.add('golf', 'sport')

print(table.lookup('golf'))
```

Output:

```text
sport
```

Example with a missing key:

```python
table = HashTable()

print(table.lookup('golf'))
```

Output:

```text
None
```

---

## Complete Example Flow

```python
table = HashTable()
table.add('golf', 'sport')
```

Step-by-step:

```text
key = 'golf'
value = 'sport'

hash('golf') = 424

collection does not contain 424 yet
        ↓
create bucket:
collection[424] = {}

store original key:
collection[424]['golf'] = 'sport'
```

Final structure:

```python
{
    424: {
        'golf': 'sport'
    }
}
```

Lookup:

```python
table.lookup('golf')
```

Flow:

```text
hash('golf') = 424
        ↓
collection[424] exists
        ↓
'golf' exists inside collection[424]
        ↓
return 'sport'
```

Removal:

```python
table.remove('golf')
```

Flow:

```text
hash('golf') = 424
        ↓
collection[424] exists
        ↓
'golf' exists inside collection[424]
        ↓
delete collection[424]['golf']
```

---

## Collision Example

The keys `'fcc'` and `'cfc'` both produce the same hash value:

```python
HashTable().hash('fcc')  # 300
HashTable().hash('cfc')  # 300
```

Add both:

```python
table = HashTable()

table.add('fcc', 'coding')
table.add('cfc', 'chemical')
```

Final collection:

```python
{
    300: {
        'fcc': 'coding',
        'cfc': 'chemical'
    }
}
```

Lookup remains accurate:

```python
table.lookup('fcc')  # 'coding'
table.lookup('cfc')  # 'chemical'
```

If only `'fcc'` exists:

```python
table = HashTable()
table.add('fcc', 'coding')

print(table.lookup('cfc'))
```

The result is:

```python
None
```

Even though `'fcc'` and `'cfc'` have the same hash value, the original key `'cfc'` still must exist inside the bucket.

---

## Why a Nested Dictionary Is Used

The outer dictionary stores hash values:

```python
{
    300: ...
}
```

The inner dictionary stores original keys:

```python
{
    300: {
        'fcc': 'coding',
        'cfc': 'chemical'
    }
}
```

This design is important because the hash value alone is not always unique.

Different keys can produce the same hash value.

The nested dictionary allows the hash table to keep all colliding keys safely.

---

## Why `ord()` Is Used

`ord()` converts a character into its Unicode code point.

Example:

```python
ord('a')  # 97
ord('b')  # 98
ord('c')  # 99
```

The project's hash function is intentionally simple:

```text
hash value = sum of Unicode values
```

For `'fcc'`:

```text
ord('f') + ord('c') + ord('c')
= 102 + 99 + 99
= 300
```

For `'cfc'`:

```text
ord('c') + ord('f') + ord('c')
= 99 + 102 + 99
= 300
```

This explains why a collision occurs.

---

## Why `remove()` Checks Before Deleting

The `remove()` method must not raise an error if the key does not exist.

Unsafe version:

```python
del self.collection[hashed_key][key]
```

This can fail when:

- `hashed_key` does not exist in `collection`
- `key` does not exist inside the bucket

Safe version:

```python
if hashed_key in self.collection and key in self.collection[hashed_key]:
    del self.collection[hashed_key][key]
```

This ensures removal only happens when the exact key exists.

---

## Why `lookup()` Returns `None`

The project requires missing keys to return `None`.

This is useful because:

- It avoids raising an error for missing data.
- It clearly signals that the key was not found.
- It matches common dictionary-access behavior such as `dict.get()`.

Example:

```python
table = HashTable()
print(table.lookup('missing'))
```

Output:

```python
None
```

---

## Full Source Code

```python
class HashTable:
    # Initialize a new hash table.
    def __init__(self):
        # Store all key-value pairs in a dictionary.
        # The outer dictionary uses the computed hash value as its key.
        # Each hash value points to an inner dictionary that stores the
        # original key-value pairs.
        self.collection = {}

    # Compute a simple hash value for a string key.
    def hash(self, string):
        # ord(char) returns the Unicode value of one character.
        return sum(ord(char) for char in string)

    # Add a key-value pair to the hash table.
    def add(self, key, value):
        # Convert the original key into a numeric hash value.
        hashed_key = self.hash(key)

        # If this hash value does not exist yet, create a new bucket.
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        # Store the original key and value inside the bucket.
        self.collection[hashed_key][key] = value

    # Remove a key-value pair from the hash table.
    def remove(self, key):
        # Compute the hash value for the key.
        hashed_key = self.hash(key)

        # Delete only the specific key if it exists.
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]

    # Look up a value by key.
    def lookup(self, key):
        # Compute the hash value for the key.
        hashed_key = self.hash(key)

        # Return the stored value if the bucket and key exist.
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]

        # Return None when the key is not found.
        return None
```

---

## Usage Examples

### Example 1: Add and look up one key

```python
table = HashTable()

table.add('golf', 'sport')

print(table.collection)
print(table.lookup('golf'))
```

Expected output:

```python
{424: {'golf': 'sport'}}
sport
```

---

### Example 2: Add colliding keys

```python
table = HashTable()

table.add('dear', 'friend')
table.add('read', 'book')

print(table.collection)
```

Expected output:

```python
{412: {'dear': 'friend', 'read': 'book'}}
```

---

### Example 3: Remove one key from a collision bucket

```python
table = HashTable()

table.add('fcc', 'coding')
table.add('cfc', 'chemical')

table.remove('fcc')

print(table.collection)
```

Expected output:

```python
{300: {'cfc': 'chemical'}}
```

The entire bucket is not removed.

Only the specific key-value pair is deleted.

---

### Example 4: Missing lookup

```python
table = HashTable()

table.add('fcc', 'coding')

print(table.lookup('cfc'))
```

Expected output:

```python
None
```

Even though `'fcc'` and `'cfc'` share the same hash value, the original key `'cfc'` does not exist in the bucket.

---

## Expected Results

### Hash value

```python
HashTable().hash('golf')
```

Result:

```text
424
```

### Single insert

```python
table = HashTable()
table.add('rose', 'flower')
print(table.collection)
```

Result:

```python
{441: {'rose': 'flower'}}
```

### Collision insert

```python
table = HashTable()
table.add('fcc', 'coding')
table.add('cfc', 'chemical')
print(table.collection)
```

Result:

```python
{300: {'fcc': 'coding', 'cfc': 'chemical'}}
```

### Lookup existing key

```python
table = HashTable()
table.add('golf', 'sport')
print(table.lookup('golf'))
```

Result:

```text
sport
```

### Lookup missing key

```python
table = HashTable()
print(table.lookup('golf'))
```

Result:

```python
None
```

---

## Automated Test Coverage

The project passed all required tests covering:

- `HashTable` class definition
- `collection` initialization
- `hash()` method existence
- `hash()` method parameter
- Unicode-sum hash calculation
- `add()` method existence
- `add()` method parameters
- `remove()` method existence
- `remove()` method parameter
- Safe removal of missing keys
- Removal from collision buckets
- `lookup()` method existence
- `lookup()` method parameter
- Correct hash value for `'golf'`
- Correct insertion at hash key `424`
- Correct collision handling at hash key `412`
- Correct removal of existing keys
- Correct lookup of existing values
- Correct `None` result for missing values
- Correct behavior when two keys share a hash value
- Exact collection structure for `'rose'`
- Exact collection structure for `'fcc'` and `'cfc'`

---

## Common Mistakes and Debugging Notes

### Mistake 1: Initializing `collection` as a list

Incorrect:

```python
self.collection = []
```

Correct:

```python
self.collection = {}
```

The test expects an empty dictionary.

---

### Mistake 2: Adding an unnecessary constructor parameter

Incorrect:

```python
def __init__(self, collection):
```

Correct:

```python
def __init__(self):
```

The test creates the object with:

```python
HashTable()
```

No argument is passed.

---

### Mistake 3: Writing English instructions as Python code

Incorrect:

```python
return the sum of the Unicode values of each character
```

Correct:

```python
return sum(ord(char) for char in string)
```

Python needs executable expressions, not the text from the instructions.

---

### Mistake 4: Storing key and value as separate object attributes

Incorrect:

```python
self.key = key
self.value = value
```

This does not store anything in the hash table collection.

Correct:

```python
self.collection[hashed_key][key] = value
```

---

### Mistake 5: Ignoring collisions

Incorrect:

```python
self.collection[hashed_key] = value
```

This loses the original key and can overwrite data.

Correct:

```python
self.collection[hashed_key][key] = value
```

---

### Mistake 6: Deleting an entire bucket during removal

Incorrect:

```python
del self.collection[hashed_key]
```

This removes all keys that share the same hash value.

Correct:

```python
del self.collection[hashed_key][key]
```

Only the requested key-value pair is removed.

---

### Mistake 7: Returning a value based only on the hash

Incorrect logic:

```text
If hash exists:
    return the first value in the bucket
```

This fails when two keys have the same hash.

Correct logic:

```text
If hash exists and original key exists:
    return that key's value
Else:
    return None
```

---

## Time and Space Complexity

Let:

```text
n = number of characters in the key
```

### `hash()`

The method checks every character in the key.

```text
Time:  O(n)
Space: O(1)
```

### `add()`

The method hashes the key and performs dictionary assignments.

```text
Time:  O(n)
Space: O(1) additional, excluding stored data
```

### `remove()`

The method hashes the key and deletes the key if it exists.

```text
Time:  O(n)
Space: O(1)
```

### `lookup()`

The method hashes the key and retrieves the value if it exists.

```text
Time:  O(n)
Space: O(1)
```

The simplified hash function dominates the runtime because it must read every character of the input key.

---

## Skills Practiced

### Data Structures

- Hash tables
- Key-value storage
- Nested dictionaries
- Buckets
- Hash collisions
- Collision-safe lookup
- Collision-safe deletion

### Python Fundamentals

- Classes
- Instance attributes
- Instance methods
- Dictionaries
- Membership checks
- `if` statements
- `del`
- `return`
- `None`
- Generator expressions
- `sum()`
- `ord()`

### Debugging

- Reading test failures
- Fixing constructor signatures
- Correcting data structure type
- Understanding `SyntaxError`
- Avoiding `KeyError`
- Preserving collision buckets
- Matching exact expected dictionary output

### Software Design

- Encapsulation
- Method responsibilities
- Safe state updates
- Separation between hashing, insertion, deletion, and lookup
- Defensive checks before mutation

---

## How to Run

From this project directory:

```bash
python main.py
```

On systems where Python 3 uses a separate command:

```bash
python3 main.py
```

No external dependencies are required.

The project uses only built-in Python functionality.

---

## Project Status

```text
Project: Build a Hash Table
Category: Certification Project
Language: Python
Status: Completed
Automated Tests: Passed
```
