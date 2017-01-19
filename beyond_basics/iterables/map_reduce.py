def count_words(doc):
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

documents = [
    'The opposing party also focused squarely on failed subprime lender IndyMac, which Mnuchin bought in 2009 and renamed OneWest.',
    'The bank has been accused of discriminating against minority borrowers, a charge that Mnuchin denied.',
    'Democratic senators asked sharp questions about whether OneWest worked hard enough to help struggling borrowers.',
    'They read out a number of anecdotes about homeowners, including families of military servicemembers, who lost their homes to foreclosure.'
]

counts = map(count_words, documents)

def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d

"""
to run:
from functools import reduce
from map_reduce import combine_counts, counts
total_counts = reduce(combine_counts, counts)
total_counts
"""