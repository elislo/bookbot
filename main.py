def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    report = create_report(character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for i in range(0,len(report)):
        print(f"The '{report[i][0]}' character appeared {report[i][1]} times")
    print(f"--- End of Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    character_dict = {}
    lc_text = text.lower()
    for character in lc_text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def create_report(character_count):
    alpha_dict = {}
    for key in character_count:
        if key.isalpha() == True:
            alpha_dict[key] = character_count[key]
    sorted_dict = (sorted(alpha_dict.items(), key= lambda item: item[1], reverse=True))
    return sorted_dict

main()
