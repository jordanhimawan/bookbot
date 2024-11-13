def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = dict()
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def convert_dict(char_dict: dict):
    list_dict = list()
    for c in char_dict:
        new_dict = dict()
        if c.isalpha():
            new_dict["name"] = c
            new_dict["num"] = char_dict[c]
            list_dict.append(new_dict)

    return list_dict

def sort_on(dict: dict):
    return dict["num"]

def show_results(word_count: int, char_dict: list[dict]):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for d in char_dict:
        print(f"The \'{d['name']}\' character was found {d['num']} times")

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)

    list_char = convert_dict(char_count)
    list_char.sort(reverse=True, key=sort_on)

    show_results(word_count, list_char)


if __name__ == "__main__" :
    main()
