from random import randint

clean_words = []
correct_letters = set()
sorted_correct_letters = []

with open('word-list.txt', 'r') as file:
    words = file.readlines()
    for word in words:
        clean_words.append(word.strip())

word = words[randint(0,len(words))]
word = word.lower().strip()
print(word)

print("Welcome to the word game! Guess the word!")
print(f"The word to guess is {len(words)} letters long.")
print("You have 5 guesses.")

for i in range(5):
    guess = input(f"Enter your guess ({i}/5)")
    if guess.lower().strip() == word:
        print(f"You got it! The word was {word}.")
        break

    for char in guess.lower().strip():
        if char in word:
            correct_letters.add(char)
            sorted_correct_letters = [i for i in correct_letters]
            sorted_correct_letters.sort()

    if len(correct_letters) != 0:
        print("Correctly guessed letters (alphabetical) are:")
        for letter in sorted_correct_letters:
            print(letter)
else:
    print(f"Game Over. You did not guess the word. It was {word}. :(")
