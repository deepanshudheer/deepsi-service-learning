import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3  # Text-to-speech library
import os
import sys

def pronounce_word(word):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.say(word)
    engine.runAndWait()

def load_image(image_name):
    # Get the directory where the executable is located
    executable_dir = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(executable_dir, "images")  # Define images_dir here
    try:
        image_path = os.path.join(images_dir, f"{image_name.lower()}.png")
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.NEAREST)
        photo = ImageTk.PhotoImage(image)
        return photo
    except FileNotFoundError:
        return None

def create_module_a():
    root = tk.Tk()
    root.title("Alphabets Pronunciation")
    root.geometry("1000x1000")  # Set window size to 1000x1000

    alphabet_words = {
        'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog', 'E': 'Elephant',
        'F': 'Fish', 'G': 'Giraffe', 'H': 'Horse', 'I': 'Ice-cream', 'J': 'Jellyfish',
        'K': 'Kite', 'L': 'Lion', 'M': 'Monkey', 'N': 'Nest', 'O': 'Orange',
        'P': 'Penguin', 'Q': 'Queen', 'R': 'Rabbit', 'S': 'Sun', 'T': 'Tiger',
        'U': 'Umbrella', 'V': 'Violin', 'W': 'Watermelon', 'X': 'Xylophone',
        'Y': 'Yak', 'Z': 'Zebra'
    }

    english_to_kannada = {
        'Apple': 'ಆಪಲ್', 'Ball': 'ಬಾಲ್', 'Cat': 'ಕ್ಯಾಟ್', 'Dog': 'ಡಾಗ್', 'Elephant': 'ಎಲಿಫಂಟ್',
        'Fish': 'ಫಿಷ್', 'Giraffe': 'ಗಿರಾಫ್', 'Horse': 'ಹೋರ್ಸ್', 'Ice-cream': 'ಐಸ್-ಕ್ರೀಮ್', 'Jellyfish': 'ಜೆಲಿಫಿಷ್',
        'Kite': 'ಕೈಟ್', 'Lion': 'ಲಯನ್', 'Monkey': 'ಮಂಕಿ', 'Nest': 'ನೆಸ್ಟ್', 'Orange': 'ಒರೆಂಜ್',
        'Penguin': 'ಪೆಂಗ್ವಿನ್', 'Queen': 'ಕ್ಯೂನ್', 'Rabbit': 'ರ್ಯಾಬಿಟ್', 'Sun': 'ಸನ್', 'Tiger': 'ಟೈಗರ್',
        'Umbrella': 'ಅಂಬ್ರೆಲ್ಲಾ', 'Violin': 'ವಯಲಿನ್', 'Watermelon': 'ವಾಟರ್‌ಮೆಲನ್', 'Xylophone': 'ಸೈಲೋಫೋನ್',
        'Yak': 'ಯಾಕ್', 'Zebra': 'ಜೆಬ್ರಾ'
    }

    def create_alphabet_buttons():
        row = 0
        column = 0
        for letter, word in alphabet_words.items():
            photo = load_image(word)
            if photo:
                button = tk.Button(root, text=f'{letter} - {word}\n{english_to_kannada[word]}',
                                   image=photo, compound=tk.TOP, command=lambda w=word: pronounce_word(w))
                button.image = photo
                button.grid(row=row, column=column, padx=10, pady=10)
                column += 1
                if column > 4:
                    column = 0
                    row += 1

    create_alphabet_buttons()

    # Bind the escape key to close the window
    root.bind("<Escape>", lambda event: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    create_module_a()
