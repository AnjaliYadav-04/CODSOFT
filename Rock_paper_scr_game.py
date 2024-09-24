import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.instructions = tk.Label(master, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.instructions.pack(pady=20)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.score_label = tk.Label(master, text="You: 0  |  Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

    def play(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = self.determine_winner(user_choice, computer_choice)

        self.update_scores(result)
        self.display_result(user_choice, computer_choice, result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"

    def update_scores(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

        self.score_label.config(text=f"You: {self.user_score}  |  Computer: {self.computer_score}")

    def display_result(self, user_choice, computer_choice, result):
        messagebox.showinfo("Round Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
