"""
Word Occurrences
Estimate: 25 minutes
Actual:   minutes
"""

text = input("Text: ").lower()
words = text.split()
word_counts = {}

# Count word occurrences
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1



