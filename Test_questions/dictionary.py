def query(user_input):
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
    with open("dictionary.txt", "a") as f:
        f.write(hun_word + " : " + eng_word + "\n")
    return 


def import_dict():
    my_dict = { }
    with open("dictionary.txt") as f:
        for line in f:
            line = line.strip()
            words = line.split(" : ")
            my_dict[words[0]] = words[1]
    return my_dict


def translate_to_hun(eng_word):
    my_dict = import_dict()
    for i in my_dict:
        if my_dict[i] == eng_word:
            print(i)
            return
    print("Invalid or not in dictionary. Feel free to enter new values.")


def translate_to_eng(hun_word):
    my_dict = import_dict()
    for i in my_dict:
        if i == hun_word:
            print(my_dict[i])
            return
    print("Invalid or not in dictionary. Feel free to enter new values.")


user_input = int(input("Please press \"0\" and enter if you want to add something to the dictionary, or if you want to translate press \"1\" and enter.:\n "))

query(user_input)