# Write a Python program to find the list of words that are longer than n from a given list of words.

print("Enter some words separated by commas :")
words_input = input()
words_list = words_input.split(",")

print("Enter a number to find words longer than that length:")
n = int(input())

longer_words = []
for word in words_list:
    if len(word) > n:
        longer_words.append(word)

print("Words longer than", n, "are:")
for word in longer_words:
    print(word)
