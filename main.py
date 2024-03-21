import tkinter as tk
import random

def roll_dice():
    num = random.randint(1, 6)
    dice_value.set(num)
    update_dice_image(num)

def update_dice_image(num):
    image_path = f"dice{num}.png"
    dice_image = tk.PhotoImage(file=image_path)
    dice_label.config(image=dice_image)
    dice_label.image = dice_image  # Keep a reference to avoid garbage collection

# Create the main window
window = tk.Tk()
window.title("Dice Simulator")
window.config(padx=50, pady=50)

# Variable to hold the dice value
dice_value = tk.IntVar()

# Label to display the dice image
dice_label = tk.Label(window)
dice_label.pack(pady=10)

# Button to roll the dice
roll_button = tk.Button(window, text="Roll", command=roll_dice)
roll_button.pack(pady=10)

# Label to display the dice value
value_label = tk.Label(window, textvariable=dice_value, font=("Arial", 24))
value_label.pack(pady=10)

# Start with a random dice value and image
roll_dice()

# Start the Tkinter event loop
window.mainloop()
