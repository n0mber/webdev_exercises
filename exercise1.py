
def get_first_char(string):
    return s[0]

def get_last_char(string):
    return  s[len(s)-1]

s = input("Give me a string: ")
length = len(s)
length_without_spaces = len(s.replace(" ", ""))
print(f"Length: {length}")
print(f"Length without spaces: {length_without_spaces}")

if s:
    print(f"First character: {get_first_char(s)}")
    print(f"Last character: {get_last_char(s)}")

    l = s.lower()
    if l[::-1] == l[0::]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")

