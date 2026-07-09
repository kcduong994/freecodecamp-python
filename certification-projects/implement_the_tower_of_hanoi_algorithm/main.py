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
    #
    # Example:
    # number_of_disks = 3
    # rod_1 = [3, 2, 1]
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

        The format must match the freeCodeCamp tests exactly:
        [rod_1] [rod_2] [rod_3]

        Example:
        [3, 2, 1] [] []
        """
        moves.append(f"{rod_1} {rod_2} {rod_3}")

    def move_disk(source, target):
        """
        Move the top-most disk from the source rod to the target rod.

        In this implementation, the top-most disk is always the last item
        in the list. Therefore, list.pop() correctly removes the top disk,
        and list.append() places it on top of the target rod.

        Args:
            source: The rod from which the disk is moved.
            target: The rod to which the disk is moved.
        """
        disk = source.pop()
        target.append(disk)

        # After every valid move, record the new state of the puzzle.
        record_state()

    def solve(disks, source, target, auxiliary):
        """
        Recursively solve the Tower of Hanoi puzzle.

        To move n disks from source to target:
        1. Move n - 1 disks from source to auxiliary.
        2. Move the largest remaining disk from source to target.
        3. Move n - 1 disks from auxiliary to target.

        Args:
            disks: The number of disks to move.
            source: The rod where the disks currently are.
            target: The rod where the disks should end up.
            auxiliary: The helper rod used during the movement.
        """

        # Base case:
        # If there is only one disk, move it directly from source to target.
        if disks == 1:
            move_disk(source, target)
            return

        # Step 1:
        # Move the top disks - except the largest one - to the auxiliary rod.
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
