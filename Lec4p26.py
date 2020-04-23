words = 'Prince Charming'
length = len(words)

print(length)

letter1 = words[3]
letter2 = words[-5]
letter3 = words[len(words) - 2]

print(letter1, letter2, letter3)

letters1 = words[3:6]
letters2 = words[:6]
letters3 = words[6:]
letters4 = words[len(words) - 3:]

print(letters1, letters2, letters3, letters4)


word2 = letter1 + letter2
phrase = word2 + ' ' + letter3

print(letters1, letters2, letters3, letters4, phrase)
