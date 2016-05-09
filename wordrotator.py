""" Create a sorter that unscramble words by rotating the word
by 10 letters"""

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"] # from q to the rest = subtract instead

letter2 = ["k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def words(message):
	for a in str(message):
		if a in letters:
			if a in letters[0:26]:
				new = letters.index(a) + 10
				new_letter = letters[new]
				print new_letter,
			# elif a in letters[16:25]:
			# 	new = letters.index(a) - 16
			# 	new_letter = letters[new]
			# 	print new_letter

def words_backwards(n):
	for b in str(n):
		if b in letter2:
			if b in letter2[0:37]:
				new_word = letter2.index(b) - 10
				new_letters = letter2[new_word]

				print new_letters,
			# if a in letters[11:26]:
			# 	new = letters.index(a) - 10
			# 	new_letter = letters[new]
			# 	print new_letter,



print "Let's scramble a message and unscramble it!"
print "Please write a message."
answer = raw_input()
words(answer)
print "Now we will unscramble it!"
print "Type it up again:"
new_answer = raw_input()
words_backwards(new_answer)

