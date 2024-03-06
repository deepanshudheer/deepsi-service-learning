import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import module_a
import module_b
import module_c
import module_d

def open_module_a(root):
    root.destroy()
    module_a.create_module_a()

def open_module_b(root):
    root.destroy()
    module_b.create_module_b()
    
def open_module_c(root):
    root.destroy()
    module_c.create_module_c()

def open_module_d(root):
    root.destroy()
    module_d.create_module_d()    

def exit_app(root):
    root.destroy()

def create_home_page():
    root = tk.Tk()
    root.title("Home Page")
    root.geometry("1000x800")

    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=50)

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 14), foreground="#000000", background="#4CAF50", padx=10, pady=5)
    style.map("TButton", background=[('active', '#45a049')])

    module_a_button = ttk.Button(button_frame, text="Alphabets Pronunciation", command=lambda: open_module_a(root))
    module_a_button.grid(row=0, column=0, padx=10)

    module_b_button = ttk.Button(button_frame, text="Image Matching", command=lambda: open_module_b(root))
    module_b_button.grid(row=0, column=1, padx=10)

    module_c_button = ttk.Button(button_frame, text="Jumbled Words", command=lambda: open_module_c(root))
    module_c_button.grid(row=0, column=2, padx=10)

    module_d_button = ttk.Button(button_frame, text="Color Matching", command=lambda: open_module_d(root))
    module_d_button.grid(row=0, column=3, padx=10)

    exit_button = ttk.Button(button_frame, text="Exit", command=lambda: exit_app(root))
    exit_button.grid(row=0, column=4, padx=10)

    root.mainloop()

if __name__ == "__main__":
    create_home_page()
