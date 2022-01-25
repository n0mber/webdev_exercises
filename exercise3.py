
def number_guess (number):
    answer = input(f"Is the number {guess} (y/n)?")
    return answer

print("Think of an integer between 1 and 100. Don't cheat.")

prev_guess = int (0)
guess = int(100/2)
guess_count = 1
user_input = number_guess(guess)

while user_input.lower() == "n":
    
    lower_higher = input(f"Is real number smaller than {guess}?")
    if lower_higher == "y":
        guess =int((guess+1)/2)
        guess_count += 1
        

    elif lower_higher == "n":
        guess = int((101 + guess)/2)
        guess_count += 1
        

    else:
        quit()

    user_input = number_guess(guess)
    

if not user_input:
    quit()

else:
    print(f"I guessed correct in {guess_count} attempts.")
