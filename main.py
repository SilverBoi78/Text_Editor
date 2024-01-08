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


def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(1, minsize=400)
    window.columnconfigure(0, minsize=500)

    top_frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    top_frame.grid(row=0, column=0, sticky="ew")

    save_button = tk.Button(top_frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(top_frame, text="Open", command=lambda: open_file(window, text_edit))
    save_button.pack(side=tk.LEFT, padx=5, pady=5)
    open_button.pack(side=tk.LEFT, padx=5, pady=5)

    text_edit = tk.Text(window, font=("Arial", 12))
    text_edit.grid(row=1, column=0)

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()


main()
