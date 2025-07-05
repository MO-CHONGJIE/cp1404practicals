"""
guitar_text
Estimate:  minutes
Actual:    minutes
"""

from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")

main()