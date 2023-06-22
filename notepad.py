import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Untitled - Notepad")
        self.textarea = tk.Text(self.master, undo=True)
        self.textarea.pack(fill='both', expand=True)
        self.filename = None
        
        # Create menu bar
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)
        
        # Add file menu
        self.file_menu = tk.Menu(self.menubar, tearoff=False)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        
        # Add edit menu
        self.edit_menu = tk.Menu(self.menubar, tearoff=False)
        self.edit_menu.add_command(label="Undo", command=self.textarea.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.textarea.edit_redo)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
    
    def new_file(self):
        self.master.title("Untitled - Notepad")
        self.filename = None
        self.textarea.delete(1.0, tk.END)
        
    def open_file(self):
        self.filename = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            self.master.title(f"{self.filename} - Notepad")
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
    
    def save_file(self):
        if not self.filename:
            self.filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.textarea.get(1.0, tk.END))
            self.master.title(f"{self.filename} - Notepad")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()