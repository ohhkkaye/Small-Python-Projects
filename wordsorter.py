""" Create a sorter that unscramble words by rotating the word
by 10 letters"""

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # from q to the rest = subtract instead


def words(message):
	for a in str(message):
		if a in letters:
			if a in letters[0:16]:
				new = letters.index(a) + 10
				new_letter = letters[new]
				print new_letter
			elif a in letters[18:25]:
				new = letters.index(a) - 16
				new_letter = letters[new]
				print new_letter




m = "rubbe"
words(m)