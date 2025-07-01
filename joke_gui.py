import requests
import tkinter as tk
from tkinter import messagebox

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()

        setup_label.config(text=joke_data['setup'])
        punchline_label.config(text="")  # Hide punchline initially
        punchline_label.joke_text = joke_data['punchline']

        show_punchline_btn.config(state=tk.NORMAL)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch joke:\n{e}")

def show_punchline():
    punchline_label.config(text=punchline_label.joke_text)
    show_punchline_btn.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Joke Fetcher 🤡")
root.geometry("500x300")
root.resizable(False, False)

setup_label = tk.Label(root, text="Click the button to get a joke!", wraplength=480, font=("Arial", 14))
setup_label.pack(pady=20)

punchline_label = tk.Label(root, text="", wraplength=480, font=("Arial", 14, "bold"), fg="green")
punchline_label.pack(pady=10)

fetch_btn = tk.Button(root, text="😂 Get Joke", command=fetch_joke, font=("Arial", 12))
fetch_btn.pack(pady=5)

show_punchline_btn = tk.Button(root, text="🤔 Show Punchline", command=show_punchline, state=tk.DISABLED, font=("Arial", 12))
show_punchline_btn.pack(pady=5)

root.mainloop()
