from stats import num_words

from stats import char_freq

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()

def main(): 
	freq = {}
	file_path = "books/frankenstein.txt"
	file_contents = get_book_text(file_path)
	count = num_words(file_contents)
	freq = char_freq(file_path)
	print (f"{count} words found in the document")
	print (freq)



main()

