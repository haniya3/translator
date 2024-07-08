import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Function to translate text
def translate_text():
    translator = Translator()
    try:
        src_language = src_lang.get()
        dest_language = dest_lang.get()
        
        src_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(src_language)]
        dest_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest_language)]
        
        translated = translator.translate(src_text.get("1.0", tk.END).strip(), src=src_language_code, dest=dest_language_code)
        dest_text.delete("1.0", tk.END)
        dest_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def clear_text():
    src_text.delete("1.0", tk.END)
    dest_text.delete("1.0", tk.END)
        

app = tk.Tk()
app.title("Google Translate in Python")
app.geometry("800x400")
app.configure(bg="#282c34") 

style = ttk.Style()
style.configure("TLabel", background="#282c34", foreground="#ffffff", font=("Arial", 10))
style.configure("TButton", background="#61afef", foreground="#282c34", font=("Arial", 10))

src_label = ttk.Label(app, text="Source Text", font=("Palatino Linotype", 24))
src_label.grid(row=0, column=0, padx=10, pady=10)
src_text = tk.Text(app, height=10, width=30, bg="#abb2bf", fg="#282c34", font=("Palatino Linotype", 10))
src_text.grid(row=1, column=0, padx=10, pady=10)

src_lang_label = ttk.Label(app, text="Source Language", font=("Palatino Linotype", 20))
src_lang_label.grid(row=2, column=0, padx=10, pady=5)
src_lang = ttk.Combobox(app, values=list(LANGUAGES.values()), font=("Arial", 14))
src_lang.set("english")
src_lang.grid(row=3, column=0, padx=10, pady=5)

translate_button = ttk.Button(app, text="Translate", command=translate_text)
translate_button.grid(row=1, column=1, padx=20, pady=20)

clear_button = ttk.Button(app, text="Clear", command=clear_text)
clear_button.grid(row=1, column=2, padx=20, pady=20)

dest_label = ttk.Label(app, text="Translated Text", font=("Palatino Linotype", 24))
dest_label.grid(row=0, column=3, padx=10, pady=10)
dest_text = tk.Text(app, height=10, width=30, bg="#abb2bf", fg="#282c34", font=("Arial", 10))
dest_text.grid(row=1, column=3, padx=10, pady=10)

dest_lang_label = ttk.Label(app, text="Destination Language", font=("Palatino Linotype", 20))
dest_lang_label.grid(row=2, column=3, padx=10, pady=5)
dest_lang = ttk.Combobox(app, values=list(LANGUAGES.values()), font=("Arial", 14))
dest_lang.set("spanish")
dest_lang.grid(row=3, column=3, padx=10, pady=5)

app.mainloop()
