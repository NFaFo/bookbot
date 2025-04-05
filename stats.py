def get_num_words(string):
    return len(string.split())

def get_char_counts(string):
    char_counts = {}
    filtered_string = string.lower()

    for char in filtered_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_dict(char_dict):
    # Преобразуем в список словарей
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]

    #функция сортировки по num
    def sort_on(d):
        return d["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list