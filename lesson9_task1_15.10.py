def popular_words(text, words):
    word_list = text.lower().split()
    return {word: word_list.count(word) for word in words}


text = "When I was One I had just begun When I was Two I was nearly new"
words = ["i", "was", "three", "near"]


result = popular_words(text, words)
print(result) 