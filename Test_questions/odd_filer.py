# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

# print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

def odd_filer(user_list):
    list_item = ready_list(user_list)
    odd = odd_selector(list_item)
    print(odd)


def ready_list(user_list):
    ready_list = []
    ready_list = user_list.split(" ")
    return ready_list


def odd_selector(list_item):
    odds = []
    for i in list_item:
        i = int(i)
        if i % 2 == 1:
            odds.append(i)
        else:
            pass
    return odds

user_list = input("Please provide a list on numbers separated by a single space, like this: \"1 2 3 4 5\" ")

odd_filer(user_list)