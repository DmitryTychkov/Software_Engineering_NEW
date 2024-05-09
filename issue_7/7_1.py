with open("text/7_1.txt", 'r') as file:
    content = file.read()

words = content.split()

word_count = len(words)
print("Количество слов в файле: ", word_count)

word_dict = {}
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

common_word = max(word_dict, key=word_dict.get)
quantiti_of_word = word_dict[common_word]

print("самое часто встречающееся слово: ", common_word)
print("Количество повторений этого слова: ", quantiti_of_word)
