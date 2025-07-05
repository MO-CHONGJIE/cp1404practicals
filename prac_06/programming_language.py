"""
ProgrammingLanguage
Estimate:  minutes
Actual:   minutes
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if language is dynamically typed, otherwise false ."""
        return self.typing == "Dynamic"