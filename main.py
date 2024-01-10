import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            text_edit.insert(tk.END, content)
    except UnicodeDecodeError:
        with open(filepath, "r", encoding="cp1252") as f:
            content = f.read()
            text_edit.insert(tk.END, content)

    window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return

    if not filepath.lower().endswith(".txt"):
        filepath += ".txt"

    with open(filepath, "w", encoding="utf-8") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Saved: {filepath}")


def change_font_size(text_edit, size):
    text_edit.config(font=("Arial", size))


def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(1, weight=1)
    window.columnconfigure(0, weight=1)
    window.minsize(500, 400)
    window.geometry("500x400")

    top_frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    top_frame.grid(row=0, column=0, sticky="ew")
    window.rowconfigure(0, weight=0)

    save_button = tk.Button(top_frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(top_frame, text="Open", command=lambda: open_file(window, text_edit))
    save_button.pack(side=tk.LEFT, padx=5, pady=5)
    open_button.pack(side=tk.LEFT, padx=5, pady=5)

    font_sizes = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
    font_size = tk.StringVar()
    font_size.set("Font Size")
    font_size_dropdown = tk.OptionMenu(top_frame, font_size, *font_sizes, command=lambda x: change_font_size(text_edit, int(x)))
    font_size_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

    text_edit = tk.Text(window, font="Arial", width=80, height=24)
    text_edit.grid(row=1, column=0, sticky="nsew")

    scrollbar = tk.Scrollbar(window, command=text_edit.yview)
    scrollbar.grid(row=1, column=1, sticky="nsew")
    text_edit.config(yscrollcommand=scrollbar.set)

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()


main()
