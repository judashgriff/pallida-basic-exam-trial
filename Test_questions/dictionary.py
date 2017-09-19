dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def querry(user_input):
    if user_input == 0:
        hun = input("What is the hungarian version of the word?:\n ")
        eng = input("What is the english version of the word?:\n ")
        add_word(hun, eng)
    elif user_input == 1:
        question = int(input("If the word is an english word -press \"0\", or if it\'s a hungarian word, - press \"1\" again.\n "))
        second_level(question)
    else:
        print("invalid input. Please enter a \"0\" or a \"1\".")
    return


def second_level(question):
    if question == 0:
        eng = input("What is this english word you want to translate?:\n ")
        translate_to_hun(eng)
    if question == 1:
        hun = input("What is this hungarian word you want to translate?:\n")
        translate_to_eng(hun)


def add_word(hun_word, eng_word):
    dictionary.append({hun_word: eng_word})
    print(dictionary)

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_hun(eng_word):
    for i in dictionary:
        key = list(i.keys())[0]
        if i[key] == eng_word:
            print(key)
            return
    print("Invalid or not in dictionary. Feel free to enter new values.")


def translate_to_eng(hun_word):
    for i in dictionary:
        if hun_word == list(i.keys())[0]:
            print(i[hun_word])
            return
    print("Invalid or not in dictionary. Feel free to enter new values.")


user_input = int(input("Please press \"0\" and enter if you want to add something to the dictionary, or if you want to translate press \"1\" and enter.:\n "))

querry(user_input)