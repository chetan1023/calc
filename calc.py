import tkinter as tk

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def append_to_expression(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for input
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create and place buttons
for (text, row, column) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, command=clear_entry)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: append_to_expression(t))
    
    btn.grid(row=row, column=column)

# Run the application
root.mainloop()
