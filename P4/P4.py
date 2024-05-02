def wheel_of_fortune(solution, guesses):
    for letter in solution:
        if letter in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print()

def main():
    solution = "succotash"
    guesses = []

    while True:
        guess = input("Guess a letter: ")
        guesses.append(guess)
        wheel_of_fortune(solution, guesses)

        count = solution.count(guess)
        print(f"The letter {guess} appears {count} time(s) in the solution.")

        all_guessed = True
        for letter in solution:
            if letter not in guesses:
                all_guessed = False
                break

        if all_guessed:
            print("Congratulations! You've guessed all the letters.")
            break

main()
