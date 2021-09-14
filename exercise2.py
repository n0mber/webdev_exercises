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

namelist = []
new_list = create_list(namelist)
print(new_list)
#print([name for name in random.shuffle(new_list)])
