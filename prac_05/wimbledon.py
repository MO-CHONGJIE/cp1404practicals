def main():
    filename = "wimbledon.csv"
    data = read_file_data(filename)
    champ_count = count_championships(data)
    sorted_countries = get_countries(data)
    display_results(champ_count, sorted_countries)

def read_file_data(filename):
    """Read file and return data as a list"""


def count_championships(data):
    """Count the number of times each champion has won"""


def get_countries(data):
    """Get the countries of the champions in alphabetical order"""



def display_results(champ_count, sorted_countries):
    """Display the processed results"""


main()