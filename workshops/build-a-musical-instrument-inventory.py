"""
Build a Musical Instrument Inventory

This workshop demonstrates the basic principles of object-oriented
programming in Python by creating musical instrument objects.

Concepts practiced:
- Classes
- Objects and instances
- The __init__ constructor
- Instance attributes
- Instance methods
- f-strings
- print statements
- Returning values from methods
"""


class MusicalInstrument:
    """
    Represent a musical instrument in the inventory.

    Each MusicalInstrument object stores:
    - The instrument's name.
    - The family or type to which the instrument belongs.
    """

    def __init__(self, name, instrument_type):
        """
        Initialize a new musical instrument.

        Parameters:
            name: The name of the musical instrument.
            instrument_type: The instrument family or category.

        The values received through the parameters are stored as
        instance attributes so that each object can maintain its
        own instrument information.
        """

        # Store the instrument's name in the current object.
        self.name = name

        # Store the instrument's family or type in the current object.
        self.instrument_type = instrument_type

    def play(self):
        """
        Display a message describing the instrument as fun to play.

        This method prints the message directly to the console.
        It does not return a value.
        """

        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        """
        Return a fact about the instrument and its family.

        Unlike the play method, this method returns a string.
        The returned value can then be printed, stored in a variable,
        or used elsewhere in the program.
        """

        return (
            f'The {self.name} is part of the '
            f'{self.instrument_type} family of instruments.'
        )


# Create the first MusicalInstrument instance.
# This object represents an oboe from the woodwind family.
instrument_1 = MusicalInstrument('Oboe', 'woodwind')

# Create the second MusicalInstrument instance.
# This object represents a trumpet from the brass family.
instrument_2 = MusicalInstrument('Trumpet', 'brass')


# Call the play method of the first instrument.
# The method prints its message directly to the console.
instrument_1.play()

# Call get_fact and print the string returned by the method.
print(instrument_1.get_fact())


# Call the play method of the second instrument.
instrument_2.play()

# Print the fact returned for the second instrument.
print(instrument_2.get_fact())
