# Implement the Tower of Hanoi Algorithm

This project implements a Python solution for the classic **Tower of Hanoi** puzzle.

It was completed as part of a Python certification project. The main objective is to write a function named `hanoi_solver` that solves the puzzle for any positive number of disks and returns the complete sequence of moves as a formatted string.

---

## Project Objective

The goal of this project is to solve the Tower of Hanoi puzzle using Python.

The required function is:

```python
def hanoi_solver(number_of_disks: int) -> str:
```

The function must:

- take one integer argument representing the total number of disks;
- solve the puzzle using the minimum number of moves;
- follow the official Tower of Hanoi rules;
- return a string showing the starting arrangement and every move;
- format each puzzle state on a new line.

---

## What Is the Tower of Hanoi?

The **Tower of Hanoi** is a mathematical puzzle with three rods and a number of disks of different sizes.

The puzzle starts with all disks stacked on the first rod in decreasing size.

Example with three disks:

```text
[3, 2, 1] [] []
```

In this representation:

- `3` is the largest disk;
- `2` is the middle disk;
- `1` is the smallest disk;
- the last item in each list is the top-most disk.

The goal is to move all disks from the first rod to the third rod.

Final state for three disks:

```text
[] [] [3, 2, 1]
```

---

## Puzzle Rules

The solution must follow three rules:

1. Only one disk can be moved at a time.
2. Only the top-most disk can be moved.
3. A larger disk cannot be placed on top of a smaller disk.

These rules make the puzzle suitable for a recursive algorithm.

---

## Minimum Number of Moves

For `n` disks, the minimum number of moves is:

```text
2^n - 1
```

Examples:

| Number of disks | Minimum moves |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |
| 5 | 31 |

The function also includes the initial arrangement in the returned string, so the total number of output lines is:

```text
2^n
```

For example, with `3` disks:

```text
7 moves + 1 initial state = 8 lines
```

---

## Example Output

Calling:

```python
hanoi_solver(3)
```

returns:

```text
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

---

## Solution Approach

The solution uses recursion.

To move `n` disks from a source rod to a target rod:

1. Move `n - 1` disks from the source rod to the auxiliary rod.
2. Move the largest remaining disk from the source rod to the target rod.
3. Move the `n - 1` disks from the auxiliary rod to the target rod.

This recursive structure matches the natural logic of the Tower of Hanoi puzzle.

---

## Why Recursion Is Used

Recursion is used because the Tower of Hanoi puzzle is made of smaller versions of the same problem.

For example, to solve the puzzle with `3` disks:

```text
Move 2 smaller disks out of the way.
Move the largest disk to the target rod.
Move the 2 smaller disks onto the largest disk.
```

The step “move 2 smaller disks” is itself another Tower of Hanoi problem.

That is why recursion is a clean and natural solution here.

---

## Why Lists Are Used for Rods

Each rod is represented as a Python list.

Example:

```python
rod_1 = [3, 2, 1]
rod_2 = []
rod_3 = []
```

This works well because the top-most disk is always the last item in the list.

So moving a disk can be done with:

```python
disk = source.pop()
target.append(disk)
```

This is efficient and easy to understand:

- `pop()` removes the top-most disk;
- `append()` places the disk on top of another rod.

---

## Why the Initial Rod Uses `range`

The first rod is created with:

```python
rod_1 = list(range(number_of_disks, 0, -1))
```

This creates a descending list of disks.

For example:

```python
list(range(5, 0, -1))
```

produces:

```python
[5, 4, 3, 2, 1]
```

This matches the required starting arrangement, where the largest disk is at the bottom and the smallest disk is on top.

---

## Why the Function Returns a String Instead of Printing

The certification tests require the function to return a string.

That means this is incorrect:

```python
print(result)
```

The function must return the result:

```python
return result
```

To do this, each puzzle state is stored in a list named `moves`.

At the end, all states are joined into one string:

```python
return "\n".join(moves)
```

This creates the exact format required by the tests, with each move on a new line.

---

## Main Implementation

```python
def hanoi_solver(number_of_disks: int) -> str:
    """
    Solve the Tower of Hanoi puzzle for a given number of disks.

    The puzzle has three rods:
    - rod_1: the starting rod
    - rod_2: the auxiliary rod
    - rod_3: the target rod

    The goal is to move all disks from rod_1 to rod_3 while following
    the three Tower of Hanoi rules:
    1. Only one disk can be moved at a time.
    2. Only the top-most disk can be moved.
    3. A larger disk cannot be placed on top of a smaller disk.

    Args:
        number_of_disks: The total number of disks in the puzzle.

    Returns:
        A string containing the starting arrangement and every move taken
        to solve the puzzle. Each line represents the state of all three rods.
    """

    # Create the first rod with disks in descending order.
    # The largest disk is represented by number_of_disks.
    # The smallest disk is represented by 1.
    rod_1 = list(range(number_of_disks, 0, -1))

    # The second and third rods start empty.
    rod_2 = []
    rod_3 = []

    # Store every state of the puzzle as a string.
    # The final answer will be created by joining these states with new lines.
    moves = []

    def record_state():
        """
        Record the current state of all three rods.

        The format must match the certification tests exactly:
        [rod_1] [rod_2] [rod_3]
        """
        moves.append(f"{rod_1} {rod_2} {rod_3}")

    def move_disk(source, target):
        """
        Move the top-most disk from the source rod to the target rod.

        In this implementation, the top-most disk is always the last item
        in the list. Therefore, list.pop() correctly removes the top disk,
        and list.append() places it on top of the target rod.
        """
        disk = source.pop()
        target.append(disk)
        record_state()

    def solve(disks, source, target, auxiliary):
        """
        Recursively solve the Tower of Hanoi puzzle.

        To move n disks from source to target:
        1. Move n - 1 disks from source to auxiliary.
        2. Move the largest remaining disk from source to target.
        3. Move n - 1 disks from auxiliary to target.
        """

        # Base case:
        # If there is only one disk, move it directly from source to target.
        if disks == 1:
            move_disk(source, target)
            return

        # Step 1:
        # Move the top disks, except the largest one, to the auxiliary rod.
        solve(disks - 1, source, auxiliary, target)

        # Step 2:
        # Move the largest disk to the target rod.
        move_disk(source, target)

        # Step 3:
        # Move the smaller disks from auxiliary to target.
        solve(disks - 1, auxiliary, target, source)

    # Record the starting arrangement before any move is made.
    record_state()

    # Solve the full puzzle:
    # Move all disks from rod_1 to rod_3 using rod_2 as the auxiliary rod.
    solve(number_of_disks, rod_1, rod_3, rod_2)

    # Return all recorded states as one string.
    # Each state must be on a new line.
    return "\n".join(moves)
```

---

## Step-by-Step Explanation

### 1. Create the rods

```python
rod_1 = list(range(number_of_disks, 0, -1))
rod_2 = []
rod_3 = []
```

The first rod starts with all disks.

The second and third rods are empty.

For example, if `number_of_disks` is `4`, the rods start as:

```text
[4, 3, 2, 1] [] []
```

---

### 2. Store every puzzle state

```python
moves = []
```

The `moves` list stores every state of the puzzle as a string.

This is necessary because the final answer must contain all states, not only the final result.

---

### 3. Record the current state

```python
def record_state():
    moves.append(f"{rod_1} {rod_2} {rod_3}")
```

This function saves the current state of the three rods.

The format is important because the tests expect exactly this structure:

```text
[rod_1] [rod_2] [rod_3]
```

The order must always be:

```text
first rod, second rod, third rod
```

Even when the recursive function is moving disks between different rods, the output must still show the rods in this fixed order.

---

### 4. Move one disk

```python
def move_disk(source, target):
    disk = source.pop()
    target.append(disk)
    record_state()
```

This function performs one valid move.

The `source.pop()` operation removes the top-most disk from the source rod.

The `target.append(disk)` operation places that disk on top of the target rod.

After the move, `record_state()` is called immediately so that every move is included in the final output.

---

### 5. Solve the puzzle recursively

```python
def solve(disks, source, target, auxiliary):
```

This helper function solves the puzzle by breaking it into smaller problems.

The base case is:

```python
if disks == 1:
    move_disk(source, target)
    return
```

When there is only one disk, it can be moved directly.

For more than one disk, the recursive process is:

```python
solve(disks - 1, source, auxiliary, target)
move_disk(source, target)
solve(disks - 1, auxiliary, target, source)
```

This follows the standard Tower of Hanoi strategy.

---

## Why the Rod Order Is Important

The recursive function uses different rods as `source`, `target`, and `auxiliary`.

However, the output must always be shown in the same order:

```text
rod_1 rod_2 rod_3
```

That is why `record_state()` directly uses:

```python
moves.append(f"{rod_1} {rod_2} {rod_3}")
```

instead of formatting `source`, `target`, and `auxiliary`.

This keeps the output consistent with the required test format.

---

## Time Complexity

The time complexity is:

```text
O(2^n)
```

This is because the puzzle requires:

```text
2^n - 1
```

moves.

Every move must be performed and recorded, so the algorithm must do exponential work.

---

## Space Complexity

The space complexity is:

```text
O(2^n)
```

The `moves` list stores every state of the puzzle.

The recursion stack also uses additional space:

```text
O(n)
```

However, the stored output dominates memory usage because all moves are saved.

---

## Key Python Concepts Practiced

This project practices several important Python concepts:

- functions;
- nested helper functions;
- recursion;
- lists;
- `pop()`;
- `append()`;
- string formatting;
- newline joining with `"\n".join(...)`;
- algorithmic thinking;
- exact output formatting for automated tests.

---

## Key Terms

| Term | Pronunciation | Meaning |
|---|---|---|
| Algorithm | `/ˈæl.ɡə.rɪ.ðəm/` — al-guh-ri-thuhm | A step-by-step method for solving a problem |
| Recursion | `/rɪˈkɝː.ʒən/` — ri-kur-zhun | A method where a function calls itself |
| Source | `/sɔːrs/` — sors | The rod a disk is moved from |
| Target | `/ˈtɑːr.ɡɪt/` — tar-git | The rod a disk is moved to |
| Auxiliary | `/ɔːɡˈzɪl.i.er.i/` — awg-zil-ee-air-ee | A helper rod |
| Base case | `/beɪs keɪs/` — bays kays | The stopping condition in recursion |
| Stack | `/stæk/` — stak | A data structure where the last item added is removed first |

---

## What I Learned

Through this project, I learned how recursion can solve a complex-looking problem by breaking it into smaller repeated subproblems.

The most important lesson is that the Tower of Hanoi is not mainly about moving disks manually. It is about recognizing the recursive pattern:

```text
Move smaller disks away.
Move the largest disk.
Move smaller disks back.
```

I also learned that passing automated tests requires not only the correct algorithm, but also the exact output format.

In this project, every list representation, space, and newline matters.

---

## Conclusion

This project demonstrates a clean recursive solution to the Tower of Hanoi puzzle.

The implementation is simple, but it shows several important programming ideas:

- representing real-world objects with data structures;
- using recursion to solve repeated subproblems;
- recording algorithm states;
- returning formatted output that matches strict test requirements.

The final function works for any positive number of disks and solves the puzzle in the minimum number of moves.
