def main():
    text = read_file()
    word_count = count_words(text)
    char_count = count_letters(text)
    print_report(word_count, char_count)


def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_letters(text):
    letter_dict = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return (letter_dict)
    
def print_report(words, letters):


    list_dicts = []
    for key in letters:
        list_dicts.append({"name": key, "num":letters[key]})
    list_dicts.sort(reverse=True, key=sort_on)

    print ("--- Begin report of books/fransenstein.txt ---")
    print (f"{words} words found in the document \n")
    for item in list_dicts:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print ("--- End report ---")

def sort_on(dict):
    return dict["num"]

main()