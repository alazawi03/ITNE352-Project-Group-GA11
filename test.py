from tkinter import *
from tkinter import ttk

def on_select(event):
    selected_item = tree.selection()  # Get the selected item
    print(f"Selected Item: {selected_item}")

root = Tk()

# Create a Treeview widget
tree = ttk.Treeview(root, columns=('Column 1', 'Column 2'))
tree.grid(row=0, column=0)

# Insert some data into the tree
tree.insert('', 'end', values=('Item 1', 'Value 1'))
tree.insert('', 'end', values=('Item 2', 'Value 2'))
tree.insert('', 'end', values=('Item 3', 'Value 3'))

# Bind the function to the <<TreeviewSelect>> event
tree.bind("<<TreeviewSelect>>", on_select)

root.mainloop()