import random

def name_to_list(word):
    while True:  
        try:
            name = input(word)
            if name.isalpha() or not name:
                return name
            else:
                raise ValueError      
        except ValueError:
            print("Use alphabetical letters.")


def create_list(list_of_names):
    while True:
        new_name = name_to_list("Give me a name or press enter to exit")
        if  new_name:
            list_of_names.append(new_name)
        else:
            return list_of_names

def random_print(name_list):
    random.shuffle(name_list)
    print("Random Order:")
    [print(f"{chr}") for chr in name_list]

def sorted_print(name_list):
    name_list.sort()
    print("Sorted order:")
    [print(f"{chr}") for chr in name_list]

namelist = []
new_list = create_list(namelist)
random_print(new_list)
sorted_print(new_list)
    


