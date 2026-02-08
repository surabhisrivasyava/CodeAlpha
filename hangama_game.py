import random

# Predefined word list
words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""
    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
    elif guess in word:
        print("✅ Correct guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        guessed_letters.append(guess)
        attempts -= 1

# Loss condition
if attempts == 0:
    print("\n😢 Game Over!")
    print("The word was:", word)
