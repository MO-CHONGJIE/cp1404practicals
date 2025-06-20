def main():
    filename = "wimbledon.csv"
    data = read_file_data(filename)
    champ_count = count_championships(data)
    sorted_countries = get_countries(data)
    display_results(champ_count, sorted_countries)

def read_file_data(filename):
    """Read file and return data as a list"""
    data = []
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            for line in in_file:
                if line.strip():
                    data.append(line.strip().split(','))
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    return data


def count_championships(data):
    """Count the number of times each champion has won"""
    champ_count = {}
    for record in data[1:]:
        if len(record) > 2:
            champion = record[2].strip()
            champ_count[champion] = champ_count.get(champion, 0) + 1
    return champ_count


def get_countries(data):
    """Get the countries of the champions in alphabetical order"""
    countries = set()
    for record in data[1:]:
        if len(record) > 1:
            country = record[1].strip()
            countries.add(country)
    return sorted(countries)


def display_results(champ_count, sorted_countries):
    """Display the processed results"""

main()