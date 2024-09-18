import random
import tkinter as tk

root = tk.Tk()
root.geometry("300x150")

options = ["rock", "paper", "scissors"]

def play_game(player_choice):
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        result_label.config(text="Tie! Computer chose " + computer_choice)
    elif player_choice == "rock" and computer_choice == "scissors":
        result_label.config(text="You win! Computer chose " + computer_choice)
    elif player_choice == "paper" and computer_choice == "rock":
        result_label.config(text="You win! Computer chose " + computer_choice)
    elif player_choice == "scissors" and computer_choice == "paper":
        result_label.config(text="You win! Computer chose " + computer_choice)
    else:
        result_label.config(text="You lose! Computer chose " + computer_choice)

btn = tk.Frame(root, bg="#ABABAB", relief="sunken", borderwidth=5)
rock_button = tk.Button(btn, text="Rock", height=5,width=10, relief="raised",command=lambda: play_game("rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(btn, text="Paper",height=5, width=10,relief="raised", command=lambda: play_game("paper"))
paper_button.pack(side=tk.LEFT)

scissors_button = tk.Button(btn, text="Scissors",height=5, width=10,relief="raised", command=lambda: play_game("scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="")
result_label.grid(row=0, column=0, pady=10)
btn.grid(row=1, column=0)

root.mainloop()
