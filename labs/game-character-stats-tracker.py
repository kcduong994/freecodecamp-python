class GameCharacter:
    """Represent a game character and manage its current stats."""

    def __init__(self, name):
        # Store the character's initial data.
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        # The character's name is read-only.
        return self._name

    @property
    def health(self):
        # Return the current health value.
        return self._health

    @health.setter
    def health(self, value):
        # Keep health between 0 and 100.
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        # Return the current mana value.
        return self._mana

    @mana.setter
    def mana(self, value):
        # Keep mana between 0 and 50.
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        # The level can only be changed through level_up().
        return self._level

    def level_up(self):
        # Increase the level and fully restore health and mana.
        self._level += 1
        self.health = 100
        self.mana = 50

        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        # Return the character's stats in the required format.
        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}"
        )
