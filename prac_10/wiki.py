"""
Wikipedia API usage example
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    """A function to run wikipedia"""
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(title, auto_suggest=False))
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:5], "...")
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

main()
