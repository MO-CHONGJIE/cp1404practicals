"""
guitar
Estimate:  minutes
Actual:    minutes
"""

CURRENT_YEAR = 2022

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar ."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        return CURRENT_YEAR - self.year
