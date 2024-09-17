### Hangman Game in Python - Code Explanation

This Hangman game provides a basic implementation where the player has a limited number of attempts to guess a randomly selected word. Correct guesses reveal the positions of the letters in the word, while incorrect guesses reduce the player's remaining attempts. The game ends when the player either successfully guesses the word or exhausts all attempts. This script is a great way for beginners to practice control flow, string manipulation, and basic game logic in Python.

#### Code Breakdown

1. The `random` module is imported to allow the computer to select a random word from a predefined list of words.

2. A list of words is created, and a variable is initialized to track the total number of wrong guesses the player is allowed. This list provides the words that the player will have to guess during the game.

3. The computer randomly selects a word from the list using `random.choice()`. This chosen word is the one the player must guess.

4. A placeholder is created using dashes (`-`) to represent each letter of the chosen word. This serves as a visual aid to show the player how many letters they need to guess. Initially, only dashes are displayed.

5. The game loop runs while the player still has guesses remaining. It continues until the player either guesses the word correctly or exhausts all attempts.

6. The player is prompted to input a letter as their guess. The input is converted to uppercase to maintain consistency with the uppercase format of the word list.

7. The code checks if the guessed letter is present in the chosen word. If it is, the code updates the placeholder to replace the corresponding dashes with the correctly guessed letter(s). It then displays the updated placeholder to the player.

8. After each correct guess, the code checks if the player has successfully guessed the entire word by comparing the placeholder with the chosen word. If they match, a congratulatory message is displayed, and the game loop breaks, indicating that the player has won.

9. If the guessed letter is not in the word, the number of remaining guesses is decremented. A message is displayed to inform the player that their guess was incorrect, along with the number of guesses left.

10. If the player runs out of guesses, the game ends with a "GAME OVER" message, indicating that the player has lost the game.

11. At the end of the game, whether the player wins or loses, the correct word is revealed.

### How to Run the Code
- Ensure Python is installed on your system.
- Copy and paste the code into a Python script (e.g., `hangman.py`).
- Run the script in the terminal or a Python IDE.
- Follow the prompts to play the game.
