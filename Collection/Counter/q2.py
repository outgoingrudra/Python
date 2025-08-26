from collections import Counter

sentence = "apple banana apple mango banana apple"
word_count = Counter(sentence.split())
print("Word Frequency:", word_count)
