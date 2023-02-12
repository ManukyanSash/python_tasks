def read_from_file(filename):
    with open(filename, "r") as file:
        words =  file.readlines()
    dictionary = {}    
    for word in words:
        if '-' in word:
            dictionary[word.split(" - ")[0]] = word.split(" - ")[1].replace("\n", "")         
    return dictionary

def add_new_word(word, translate, dictionary, filename):
    dictionary[word] = translate
    with open(filename, 'w') as file:
        for word in dictionary:
            file.write(f"{word} - {dictionary[word]}\n")
        

if __name__ == "__main__":
    translate = read_from_file("dictionary")
    print(translate)
    add_new_word("word", "Բառ", translate, "dictionary")
    translate = read_from_file("dictionary")
    print(translate)
    add_new_word("sequence", "հաջորդականություն", translate, "dictionary")