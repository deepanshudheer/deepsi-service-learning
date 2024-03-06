import tkinter as tk
from tkinter import messagebox
import random
import os

class MemoryGame:
    def __init__(self, root, rows, cols, images):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.images = images
        self.cards = []
        self.selected_cards = []
        self.create_cards() 
        
    def create_cards(self):
        for i in range(self.rows):
            for j in range(self.cols):
                card = tk.Button(self.root, width=100, height=100, command=lambda row=i, col=j: self.flip_card(row, col))
                card.grid(row=i, column=j)
                self.cards.append(card)
        self.shuffle_images()
        
    def shuffle_images(self):
        image_pairs = [(img, img) for img in self.images]
        images = image_pairs * (self.rows * self.cols // len(image_pairs))
        random.shuffle(images)
        for card, img in zip(self.cards, images):
            card.img = img
            card.config(image='', bg='blue', state=tk.NORMAL)
            
    def flip_card(self, row, col):
        selected_card = self.buttons[row][col]
        selected_card.config(image=self.images[row][col], bg='white', state=tk.DISABLED)
        card_index = row * self.cols + col
        selected_card = self.cards[card_index]
        selected_card.config(image=selected_card.img, bg='white', state=tk.DISABLED)
        self.selected_cards.append(selected_card)
        
        if len(self.selected_cards) == 2:
            self.root.after(1000, self.check_match)
            
    def check_match(self):
        if self.selected_cards[0].img == self.selected_cards[1].img:
            messagebox.showinfo('Match', 'You found a match!')
            for card in self.selected_cards:
                card.config(state=tk.DISABLED)
        else:
            messagebox.showinfo('No Match', 'Try again!')
            for card in self.selected_cards:
                card.config(image='', bg='blue', state=tk.NORMAL)
        self.selected_cards = []

# Define the root window
root = tk.Tk()
root.title("Memory Game")

import os

# Define the root directory and the path to the images folder
root_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(root_dir, "images")

# List all files in the images folder
image_files = os.listdir(images_dir)

# Filter only the .png files
png_files = [f for f in image_files if f.endswith(".png")]

# Provide paths to the PNG image files
images = [os.path.join(images_dir, img) for img in png_files]

# Create and start the game
game = MemoryGame(root, 4, 4, images)

# Run the Tkinter event loop
root.mainloop()
