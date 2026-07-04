import random
from abc import ABC, abstractmethod


class Player(ABC):
    # Initialize the shared state used by all concrete player classes.
    def __init__(self):
        # Store the movement options available to the player.
        # Concrete subclasses will replace this empty list with
        # their own permitted movements.
        self.moves = []

        # Store the player's current position as an (x, y) coordinate.
        # Every player begins at the origin.
        self.position = (0, 0)

        # Record every position visited by the player.
        # The initial position is the first item in the path.
        self.path = [self.position]

    # Select and perform one random movement from the available moves.
    def make_move(self):
        # Choose one movement tuple from the moves defined
        # by the concrete player class.
        move = random.choice(self.moves)

        # Calculate the new position by adding the selected movement's
        # x and y values to the current x and y coordinates.
        self.position = (
            self.position[0] + move[0],
            self.position[1] + move[1],
        )

        # Add the updated position to the movement history.
        self.path.append(self.position)

        # Return the player's new position.
        return self.position

    # Require every concrete player class to define how it levels up.
    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    # Initialize a pawn with the shared Player state and basic movements.
    def __init__(self):
        # Call Player.__init__() to create moves, position, and path.
        super().__init__()

        # Define the pawn's four initial one-unit movements:
        # up, down, left, and right.
        self.moves = [
            (0, 1),   # Move up by one unit.
            (0, -1),  # Move down by one unit.
            (-1, 0),  # Move left by one unit.
            (1, 0),   # Move right by one unit.
        ]

    # Upgrade the pawn by adding four diagonal movement options.
    def level_up(self):
        # extend() adds every tuple from the new list to self.moves.
        self.moves.extend([
            (1, 1),    # Move diagonally up and right.
            (1, -1),   # Move diagonally down and right.
            (-1, 1),   # Move diagonally up and left.
            (-1, -1),  # Move diagonally down and left.
        ])
