def num_words(file_contents):
	words = file_contents.split()
	return len(words)

def char_freq(file_path):
    with open(file_path) as f:
        book = f.read()
        lower_case = book.lower()
        freq = {}
        for ch in lower_case:
            freq[ch] = freq.get(ch, 0) + 1
    return freq

def sort_char(freq):
    freq_list = []
    for char, value in freq.items():
        freq_list.append({"char": char, "num": value})

    print (freq_list)
    return freq_list