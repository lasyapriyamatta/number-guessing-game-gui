import tkinter as tk
import random

# Global variables
number_to_guess = 0
attempts_left = 0
max_attempts = 0

# Function to start or restart the game
def start_game():
    global number_to_guess, attempts_left, max_attempts

    # Hide the main menu and show the game interface
    main_menu_frame.pack_forget()
    game_frame.pack()

    # Reset guess field and result
    entry.delete(0, tk.END)
    result_label.config(text="", fg="black")
    guess_button.config(state="normal")

    # Get difficulty
    difficulty = difficulty_var.get()
    if difficulty == "Easy":
        max_attempts = 15
    elif difficulty == "Medium":
        max_attempts = 10
    elif difficulty == "Hard":
        max_attempts = 5

    number_to_guess = random.randint(1, 100)
    attempts_left = max_attempts

    attempts_label.config(text=f"Attempts Left: {attempts_left}")

# Function to check the user's guess
def check_guess():
    global attempts_left

    guess = entry.get()
    if not guess.isdigit():
        result_label.config(text="Please enter a valid number!", fg="red")
        return

    guess = int(guess)
    attempts_left -= 1
    attempts_label.config(text=f"Attempts Left: {attempts_left}")

    if guess < number_to_guess:
        result_label.config(text="📉 Too low!", fg="blue")
    elif guess > number_to_guess:
        result_label.config(text="📈 Too high!", fg="orange")
    else:
        result_label.config(text="🎉 Correct! You win!", fg="green")
        guess_button.config(state="disabled")
        restart_button.pack(pady=10)  # Show restart button if correct guess
        return

    if attempts_left == 0:
        result_label.config(text=f"❌ Game Over! Number was {number_to_guess}", fg="red")
        guess_button.config(state="disabled")
        restart_button.pack(pady=10)  # Show restart button when attempts are over

# Function to restart the game and go back to main menu
def restart_game():
    # Reset game state
    start_game()
    # Hide the game interface and show the main menu
    game_frame.pack_forget()
    main_menu_frame.pack()

# --- GUI SETUP ---

# Create main window
window = tk.Tk()

# Set the title and window size
window.title("🎯 Number Guessing Game")
window.geometry("420x300")
window.config(bg="#f0f8ff")  # Light blue background

# --- Main Menu Frame ---
main_menu_frame = tk.Frame(window)

# Difficulty dropdown
difficulty_var = tk.StringVar(value="Medium")
difficulty_label = tk.Label(main_menu_frame, text="Select Difficulty:", bg="#f0f8ff", font=("Arial", 10))
difficulty_label.pack(pady=(10, 0))
difficulty_menu = tk.OptionMenu(main_menu_frame, difficulty_var, "Easy", "Medium", "Hard")
difficulty_menu.config(width=10)
difficulty_menu.pack()

# Start Game Button (appears on main menu)
start_button = tk.Button(main_menu_frame, text="Start Game", command=start_game, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
start_button.pack(pady=(5, 10))

# Pack main menu frame as default
main_menu_frame.pack()

# --- Game Frame ---
game_frame = tk.Frame(window)

# Restart Game Button (hidden initially)
restart_button = tk.Button(game_frame, text="Restart Game", command=restart_game, bg="#FF5722", fg="white", font=("Arial", 12, "bold"))

# Prompt Label
prompt_label = tk.Label(game_frame, text="Guess a number between 1 and 100", bg="#f0f8ff", font=("Arial", 12))
prompt_label.pack()

# Entry
entry = tk.Entry(game_frame, font=("Arial", 12))
entry.pack()

# Guess Button
guess_button = tk.Button(game_frame, text="Guess", command=check_guess, font=("Arial", 12), bg="#2196F3", fg="white")
guess_button.pack(pady=5)

# Result Label
result_label = tk.Label(game_frame, text="", bg="#f0f8ff", font=("Arial", 12))
result_label.pack()

# Attempts Label
attempts_label = tk.Label(game_frame, text="", bg="#f0f8ff", font=("Arial", 11))
attempts_label.pack(pady=(5, 10))

# Run the window
window.mainloop()
