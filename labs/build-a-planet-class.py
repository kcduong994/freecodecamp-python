```python
"""
Build a Planet Class

This lab demonstrates fundamental object-oriented programming concepts
by defining a Planet class, validating initialization data, creating
planet objects, and implementing instance methods.

Concepts practiced:
- Classes and objects
- The __init__ constructor
- Instance attributes
- Instance methods
- Type and value validation
- Raising exceptions
- The __str__ special method
- Formatted strings
"""


class Planet:
    """
    Represent a planet and its relationship with a star.

    Attributes:
        name: The name of the planet.
        planet_type: The category or type of the planet.
        star: The name of the star the planet orbits.
    """

    def __init__(self, name, planet_type, star):
        """
        Initialize a Planet instance.

        Args:
            name: The name of the planet.
            planet_type: The planet's category.
            star: The star around which the planet orbits.

        Raises:
            TypeError: If any argument is not a string.
            ValueError: If any argument is an empty string.
        """

        # Validate that all arguments have the required string type.
        if (
            not isinstance(name, str)
            or not isinstance(planet_type, str)
            or not isinstance(star, str)
        ):
            raise TypeError(
                "name, planet type, and star must be strings"
            )

        # Validate that none of the supplied strings are empty.
        if not name or not planet_type or not star:
            raise ValueError(
                "name, planet_type, and star must be non-empty strings"
            )

        # Store the validated values as instance attributes.
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        """
        Return a sentence describing the planet's orbit.

        Returns:
            A formatted string containing the planet and star names.
        """

        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        """
        Return a readable string representation of the planet.

        This method is called automatically when a Planet object
        is passed to print().
        """

        return (
            f"Planet: {self.name} | "
            f"Type: {self.planet_type} | "
            f"Star: {self.star}"
        )


# Create three Planet instances with different characteristics.
planet_1 = Planet("Earth", "terrestrial", "Sun")
planet_2 = Planet("Jupiter", "gas giant", "Sun")
planet_3 = Planet("Kepler-452b", "super-Earth", "Kepler-452")


# Print each object to display the value returned by __str__().
print(planet_1)
print(planet_2)
print(planet_3)


# Call orbit() for each planet and print the returned description.
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
```
