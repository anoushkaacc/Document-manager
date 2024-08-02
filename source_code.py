import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry
import os

def submit_details():
    doc_num = entry_doc_num.get()
    doc_name = entry_doc_name.get()
    doc_date = entry_doc_date.get()
    doc_path = entry_doc_path.get()

    if not os.path.exists(doc_path):
        messagebox.showerror("Error", "The specified document path does not exist.")
        return

    # Display the entered details 
    label_display.config(text=f"Document Number: {doc_num} \n Document Name: {doc_name} \n Document Date: {doc_date} \n Document Path: {doc_path}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    entry_doc_path.delete(0, tk.END)
    entry_doc_path.insert(0, file_path)

def open_file():
    file_path = entry_doc_path.get()
    if os.path.exists(file_path):
        os.startfile(file_path)  # This will open the file with the default application

def on_enter_key(event):
    submit_details()

# Create the main window
root = tk.Tk()
root.title("Document Details Entry")

# Bind the Enter key to the submit_details function
root.bind('<Return>', on_enter_key)

# Create and place the labels and text entry boxes
label_doc_num = tk.Label(root, text="Document Number:")
label_doc_num.grid(row=0, column=0, padx=10, pady=5)
entry_doc_num = tk.Entry(root)
entry_doc_num.grid(row=0, column=1, padx=10, pady=5)

label_doc_name = tk.Label(root, text="Document Name:")
label_doc_name.grid(row=0, column=2, padx=10, pady=5)
entry_doc_name = tk.Entry(root)
entry_doc_name.grid(row=0, column=3, padx=10, pady=5)

label_doc_date = tk.Label(root, text="Document Date:")
label_doc_date.grid(row=0, column=4, padx=10, pady=5)
entry_doc_date = DateEntry(root, date_pattern='yyyy-mm-dd')
entry_doc_date.grid(row=0, column=5, padx=10, pady=5)

label_doc_path = tk.Label(root, text="Document Path:")
label_doc_path.grid(row=1, column=0, padx=10, pady=5)
entry_doc_path = tk.Entry(root, width=50)
entry_doc_path.grid(row=1, column=1, columnspan=4, padx=10, pady=5)

button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.grid(row=1, column=4, padx=10, pady=5)

# Create and place the submit button
button_submit = tk.Button(root, text="Submit", command=submit_details)
button_submit.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

# Create and place the open file button
button_open = tk.Button(root, text="Open File", command=open_file)
button_open.grid(row=1, column=5, columnspan=6, padx=10, pady=10)

# Create and place the label to display the entered details
label_display = tk.Label(root, text="", justify=tk.LEFT)
label_display.grid(row=4, column=0, columnspan=6, padx=10, pady=10)

# Run the application
root.mainloop()