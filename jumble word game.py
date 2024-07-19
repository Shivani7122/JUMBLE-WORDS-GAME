import random

# List of words for each difficulty level
easy_words = ["cat", "dog", "bat", "cow", "pig"]
medium_words = ["apple", "grape", "peach", "plum", "berry"]
hard_words = ["machine", "complex", "jumbled", "network", "problem"]

# Hints for each word
hints = {
    "cat": ["A common pet", "Says meow", "Likes milk", "Chases mice", "Has whiskers"],
    "dog": ["A common pet", "Says woof", "Loyal to humans", "Chases cats", "Has a tail"],
    "bat": ["A nocturnal animal", "Uses echolocation", "Associated with vampires", "Flies at night", "Lives in caves"],
    "cow": ["Farm animal", "Gives milk", "Moo sound", "Eats grass", "Has horns"],
    "pig": ["Farm animal", "Says oink", "Loves mud", "Eats anything", "Has a snout"],
    "apple": ["A fruit", "Keeps the doctor away", "Can be red or green", "Grows on trees", "Used in pies"],
    "grape": ["A fruit", "Grows in bunches", "Can be red or green", "Used in wine", "Small and round"],
    "peach": ["A fruit", "Has fuzzy skin", "Juicy and sweet", "Grows on trees", "Related to plums"],
    "plum": ["A fruit", "Can be purple or red", "Juicy and sweet", "Grows on trees", "Related to peaches"],
    "berry": ["A small fruit", "Can be blue or red", "Used in pies", "Grows on bushes", "Can be eaten fresh"],
    "machine": ["A mechanical device", "Used in factories", "Can be complex", "Helps in work", "Operated by humans"],
    "complex": ["Not simple", "Intricate and detailed", "Opposite of simple", "Involves many parts", "Difficult to understand"],
    "jumbled": ["Mixed up", "Not in order", "Confused state", "Needs sorting", "Disorganized"],
    "network": ["Connected system", "Used in computers", "Can be wireless", "Involves communication", "Consists of nodes"],
    "problem": ["Needs solving", "Can be difficult", "Requires thinking", "Needs a solution", "Can be mathematical"]
}

def jumble_word(word):
    jumbled = list(word)
    random.shuffle(jumbled)
    return ''.join(jumbled)

def play_game():
    print("Welcome to the Jumble Words Game!")
    while True:
        print("\nChoose a difficulty level:")
        print("1. Easy (3 letters)")
        print("2. Medium (5 letters)")
        print("3. Hard (7 letters)")
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                words = easy_words
                level = "Easy"
            elif choice == 2:
                words = medium_words
                level = "Medium"
            elif choice == 3:
                words = hard_words
                level = "Hard"
            else:
                print("Invalid choice, please try again.")
                continue
        except ValueError:
            print("Invalid input, please enter a number (1/2/3).")
            continue

        word = random.choice(words)
        jumbled = jumble_word(word)
        print(f"\nLevel: {level}")
        print(f"Jumbled word: {jumbled}")

        attempts = 5
        while attempts > 0:
            guess = input("Guess the word: ").strip().lower()
            if guess == word:
                print("Correct! You've guessed the word!")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    hint_index = 5 - attempts
                    print(f"Incorrect. Here's a hint: {hints[word][hint_index]}")
                    print(f"Attempts remaining: {attempts}")
                else:
                    print(f"Sorry, you've run out of attempts. The word was: {word}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
