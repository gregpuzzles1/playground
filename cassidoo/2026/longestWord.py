# Cassidoo question of the week:
# September 13th, 2026
#
# Question:
# Given a sentence, return the longest word whose letters appear in alphabetical order.

import string

def longestSorted(sentence):
    longestWord = ""

    for word in sentence.split():
        word = word.strip(string.punctuation)
        lowercaseWord = word.lower()

        if all(a <= b for a, b in zip(lowercaseWord, lowercaseWord[1:])):
            if len(word) > len(longestWord):
                longestWord = word

    return longestWord


print(longestSorted("Shelly sells sea shells by the seashore"))
# Expected output: by

print(longestSorted("The autumn leaves almost glow."))
# Expected output: almost

print(longestSorted("A cool sheep sleeps."))
# Expected output: A
