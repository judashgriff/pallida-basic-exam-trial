# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

# print(name_from_email("elek.viz@exam.com"))


def name_print(user_input):
    name = user_input.split("@")[0]
    name = name.split(".")
    name = name[1] + " " + name[0]
    name = name.title()
    print(name)


user_input = input("Please provide your email address in the following format: last_name first_name. example: \"elek.viz@exam.com\" ")

name_print(user_input)