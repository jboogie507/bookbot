from stats import num_words

from stats import char_freq

from stats import sort_char

import sys

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()

def main(): 
	freq = {}
	#file_path = "books/frankenstein.txt"	
	if len(sys.argv) != 2:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	file_path = sys.argv[1]
	file_contents = get_book_text(file_path)
	count = num_words(file_contents)
	freq = char_freq(file_path)	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	print("----------- Word Count ----------")
	print (f"Found {count} total words")
	print ("--------- Character Count -------")
	dict_list = sort_char(freq)
	print("============= END ===============")
main()

