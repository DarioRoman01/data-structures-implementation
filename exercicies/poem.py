"""poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
 You have to read this file in python and print every word and its count as show below:
 + 'diverged': 2,
 + 'in': 3,
 + 'I': 8 """


def count_words(files):
    """Handle count words of the text.""" 
    file=open(f'{files}',"r+")
    wordcount = {}
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    for k,v in wordcount.items():
        print(k, v)

if __name__ == "__main__":
    """The best data structures for this are hash table
    because we can save a word as key and in each iteration
    add 1 to that key."""
    count_words('poem.txt')