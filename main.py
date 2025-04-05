import sys

from stats import get_num_words, get_char_counts, sort_char_dict


def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found: {book_path}")
        sys.exit(1)


    word_count = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_dict(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():  # Только буквы
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    main()