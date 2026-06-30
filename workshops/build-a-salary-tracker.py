class Employee:
    """
    Represent an employee with a name, professional level, and salary.

    The employee's level determines the minimum permitted salary.
    Properties and setters are used to validate updates to the employee's
    name, level, and salary.
    """

    # Minimum base salary assigned to each employee level.
    # This is a class attribute because all Employee objects share it.
    _base_salaries = {
        "trainee": 1000,
        "junior": 2000,
        "mid-level": 3000,
        "senior": 4000,
    }

    def __init__(self, name: str, level: str) -> None:
        """
        Initialize a new Employee instance.

        Args:
            name: The employee's name.
            level: The employee's professional level.

        The property setters are used instead of assigning directly to
        _name, _level, and _salary. This ensures that the same validation
        rules are applied during both initialization and later updates.
        """
        self.name = name
        self.level = level
        self.salary = Employee._base_salaries[level]

    def __str__(self) -> str:
        """
        Return a readable representation of the employee.

        Example:
            Charlie Brown: trainee
        """
        return f"{self.name}: {self.level}"

    def __repr__(self) -> str:
        """
        Return a representation that resembles the code used to create
        the Employee object.

        Example:
            Employee('Charlie Brown', 'trainee')
        """
        return f"Employee({self.name!r}, {self.level!r})"

    @property
    def name(self) -> str:
        """Return the employee's current name."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Validate and update the employee's name.

        Raises:
            TypeError: If new_name is not a string.
        """
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")

        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property
    def level(self) -> str:
        """Return the employee's current professional level."""
        return self._level

    @level.setter
    def level(self, new_level: str) -> None:
        """
        Validate and update the employee's professional level.

        An employee can only move to a level with an equal or higher base
        salary. Moving to a lower level is not permitted.

        Raises:
            TypeError:
                If new_level is not a string.

            ValueError:
                If new_level is not a valid employee level.
                If new_level is already the selected level.
                If new_level has a lower base salary than the current level.
        """
        # The level must be provided as text.
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")

        # The level must exist in the class-level salary dictionary.
        if new_level not in Employee._base_salaries:
            raise ValueError(
                f"Invalid value '{new_level}' for 'level' attribute."
            )

        # During initialization, _level does not exist yet.
        # Therefore, check for the attribute before comparing levels.
        if hasattr(self, "_level") and new_level == self.level:
            raise ValueError(
                f"'{self.level}' is already the selected level."
            )

        # Prevent the employee from being moved to a lower-paying level.
        if (
            hasattr(self, "_level")
            and Employee._base_salaries[new_level]
            < Employee._base_salaries[self.level]
        ):
            raise ValueError("Cannot change to lower level.")

        print(f"'{self.name}' promoted to '{new_level}'.")

        # Update the salary before storing the new level.
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

    @property
    def salary(self) -> int | float:
        """Return the employee's current salary."""
        return self._salary

    @salary.setter
    def salary(self, new_salary: int | float) -> None:
        """
        Validate and update the employee's salary.

        The new salary cannot be lower than the minimum base salary
        associated with the employee's current level.

        Raises:
            TypeError:
                If new_salary is not an integer or floating-point number.

            ValueError:
                If new_salary is lower than the minimum salary for the
                employee's current level.
        """
        # Accept both whole-number and decimal salary values.
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")

        # During initialization, _level may not exist yet.
        # Only perform minimum-salary validation after a level is available.
        if (
            hasattr(self, "_level")
            and new_salary < Employee._base_salaries[self.level]
        ):
            minimum_salary = Employee._base_salaries[self.level]

            raise ValueError(
                "Salary must be higher than minimum salary "
                f"${minimum_salary}."
            )

        self._salary = new_salary
        print(f"Salary updated to ${self.salary}.")


def main() -> None:
    """Demonstrate the Employee salary-tracking system."""

    # Create an employee at the trainee level.
    charlie_brown = Employee("Charlie Brown", "trainee")

    # __str__ is called automatically by print().
    print(charlie_brown)

    # Display the employee's initial salary.
    print(f"Base salary: ${charlie_brown.salary}")

    # Promote the employee from trainee to junior.
    # The level setter also updates the salary automatically.
    charlie_brown.level = "junior"


if __name__ == "__main__":
    main()
