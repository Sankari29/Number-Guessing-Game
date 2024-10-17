import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("700x500")
        self.master.config(bg="light blue")

        self.rand_num = random.randint(0, 20)
        self.chances = 3
        
        self.var = tk.IntVar()
        self.message = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.master, text="Number Guessing Game (0 to 20)",
                                font=('Arial', 28, 'bold'), padx=10, pady=10, bg='white')
        title_label.pack(pady=(10, 0))

        # Entry for User Input
        self.entry = tk.Entry(self.master, textvariable=self.var, font=('Arial', 20))
        self.entry.pack(pady=(50, 10))

        # Submit Button
        submit_button = tk.Button(self.master, text="Submit", font=('Arial', 24), command=self.check_guess)
        submit_button.pack()

        # Message Label
        self.result_label = tk.Label(self.master, textvariable=self.message, bg='white', font=('Arial', 20))
        self.result_label.pack(pady=(20, 0))

        # Restart Button
        restart_button = tk.Button(self.master, text="Restart", font=('Arial', 24), command=self.restart_game)
        restart_button.pack(pady=(10, 0))

    def check_guess(self):
        usr_input = self.var.get()
        if self.chances > 0:
            if usr_input == self.rand_num:
                self.message.set(f'YOU WON!! {self.rand_num} is the right answer.')
                self.chances = 0  # End the game
            elif usr_input > self.rand_num:
                self.chances -= 1
                self.message.set(f'{usr_input} is greater. You have {self.chances} attempts left.')
            elif usr_input < self.rand_num:
                self.chances -= 1
                self.message.set(f'{usr_input} is smaller. You have {self.chances} attempts left.')
        if self.chances == 0 and usr_input != self.rand_num:
            self.message.set(f'You lost! The correct number was {self.rand_num}.')

    def restart_game(self):
        self.rand_num = random.randint(0, 20)
        self.chances = 3
        self.var.set(0)  # Reset the entry field
        self.message.set("")  # Clear the message

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

