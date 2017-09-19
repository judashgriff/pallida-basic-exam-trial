# Create a function that takes a list of GitHub handles as input and returns a
# list of strings that represents
# GitHub url's under Green Fox Academy organization in the following format:
# "https://github.com/greenfox-academy/teststudent"

# example:
# input: ["ghhandle1", "ghhandle2"]
# output: ["https://github.com/greenfox-academy/ghhandle1", "https://github.com/greenfox-academy/ghhandle2"]

# names = ["ghhandle1", "ghhandle2"]
# print(urls_from_handles(names))

import requests

def make_list(githandles):
    githandles_list = []
    githandles_list = githandles.split(" ")
    print(githandles_list)
    remove_spaces(githandles_list)


def remove_spaces(githandles_list):
    for i in githandles_list:
        if i != '' and i != ' ':
            print("\"https://github.com/greenfox-academy/" + str(i) + "\"")
    return
            


githandles = input("Which github user's URL you would like to know? Please provide their github username separated by a space!: ")
make_list(githandles)
