from collections import Counter

file_name = "text.txt"

def word_count():
        with open(file_name) as f:
                print(Counter(f.read().split()))
word_count()
