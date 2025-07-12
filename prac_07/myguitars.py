import csv
from guitar import Guitar


def main():
    """Load from a CSV file and return a list ."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)

# Display guitars from oldest to newest
    guitars.sort()
    print("\nSorted by year:")
    for guitar in guitars:
        print(guitar)

main()