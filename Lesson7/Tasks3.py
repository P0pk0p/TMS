word = ["cat", "rewire", "level", "book", "stats", "list"]
palindromes = list(filter(lambda word: word == word[::-1], word))
print("Слова палиндромы: ", list(palindromes))