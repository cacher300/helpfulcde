search_words = ['apple','orange']
words = ['apple','apple','apple','orange']
occurrences = []
length = len(search_words)
for i in range(length):
    occurrences.append(0)
for i in range(len(search_words)):
    for j in words:
        if search_words[i] == j:
            occurrences[i] += 1
print(sum(occurrences))
