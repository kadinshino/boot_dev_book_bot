# import sys
# from stats import (
#     get_num_words,
#     chars_dict_to_sorted_list,
#     get_chars_dict,
# )


# def main():
#     # Check if the correct number of arguments is provided
#     if len(sys.argv) != 2:
#         print("Usage: python3 main.py <path_to_book>")
#         sys.exit(1)

#     book_path = sys.argv[1]
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = get_chars_dict(text)
#     chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
#     print_report(book_path, num_words, chars_sorted_list)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# def print_report(book_path, num_words, chars_sorted_list):
#     print("============ BOOKBOT ============")
#     print(f"Analyzing book found at {book_path}...")
#     print("----------- Word Count ----------")
#     print(f"Found {num_words} total words")
#     print("--------- Character Count -------")
#     for item in chars_sorted_list:
#         if not item["char"].isalpha():
#             continue
#         print(f"{item['char']}: {item['num']}")

#     print("============= END ===============")


# main()

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)

class BookAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Analyzer")

        self.create_widgets()

    def create_widgets(self):
        # Open button
        self.open_button = tk.Button(self.root, text="Open Book File", command=self.open_file)
        self.open_button.pack(pady=10)

        # Results text box
        self.results_box = scrolledtext.ScrolledText(self.root, width=80, height=30, wrap=tk.WORD)
        self.results_box.pack(padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                self.analyze_book(file_path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to analyze book: {e}")

    def analyze_book(self, path):
        text = self.get_book_text(path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

        self.display_report(path, num_words, chars_sorted_list)

    def get_book_text(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def display_report(self, book_path, num_words, chars_sorted_list):
        self.results_box.delete("1.0", tk.END)
        self.results_box.insert(tk.END, "============ BOOKBOT ============\n")
        self.results_box.insert(tk.END, f"Analyzing book found at {book_path}\n")
        self.results_box.insert(tk.END, "----------- Word Count ----------\n")
        self.results_box.insert(tk.END, f"Found {num_words} total words\n")
        self.results_box.insert(tk.END, "--------- Character Count -------\n")
        for item in chars_sorted_list:
            if not item["char"].isalpha():
                continue
            self.results_box.insert(tk.END, f"{item['char']}: {item['num']}\n")
        self.results_box.insert(tk.END, "============= END ===============\n")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BookAnalyzerApp(root)
    root.mainloop()
