# library.py

#
# RPyTkGUICreator EXAMPLE LIBRARY
#
# ------------------------------------------------------------
# WIDGET EXAMPLE PROCEDURES
# In the example procedures below 'w' is the widget name
# All other input parameters are optional. Must have 'w' !!
# Example of this is:

# This 2 line example, Creates a Text widget, Writes the text, 'Hello World !' to the widget.
# mytext = tk.Text(root)
# write_to_text(mytext, "Hello World !")

# This 2 line example, Creates a Text widget, Writes the default text, 'Text' to the widget.
# mytext = tk.Text(root)
# write_to_text(mytext)

# This 2 line example, Creates a Label widget, Writes the text, 'Hello World !' to the widget.
# mylabel = tk.Label(root)
# update_label(mylabel, "Hello World !")

# This 2 line example, Creates a Label widget, Writes the default text, 'Label Text' to the widget.
# mylabel = tk.Label(root)
# update_label(mylabel)

# This 3 line example, Creates a Label widget, then changes the foreground and background colors.
# mylabel = tk.Label(root)
# update_label_background(mylabel, "#441111")     # changes background to dark red
# update_label_foreground(mylabel, "#aaaaaa")     # changes foreground to gray/white


# This 2 line example, Creates a Checkbutton widget, 'Checks' the box on the widget.
# myCheck = tk.Checkbutton(root)
# select_checkbutton(myCheck)

# This 2 line example, Creates a Checkbutton widget, 'Unchecks' the box on the widget.
# myCheck = tk.Checkbutton(root)
# deselect_checkbutton(myCheck)


# This 2 line example, Creates a Checkbutton widget, 'Unchecks' the box on the widget.
# myCheck = tk.Checkbutton(root)
# deselect_checkbutton(myCheck)


# This 4 line example, Creates a Listbox widget, then adds items to the listbox.
# myListbox= tk.Listbox(root)
# write_to_listbox(myListbox, "A1")
# write_to_listbox(myListbox, "B2")
# write_to_listbox(myListbox, "C3")


# This 6 line example, Creates a Listbox widget, then adds items to the listbox, then resizes it.
# myListbox = tk.Listbox(root)
# write_to_listbox(myListbox, "A1")
# write_to_listbox(myListbox, "All")
# write_to_listbox(myListbox, "None")
# myListbox.config(width = "10")
# myListbox.config(height = "5")


# ------------------------------------------------------------
# Entry Widget Example Procedures
def append_to_entry(w, text=""):
    if text == "":
        text = " Additional Text"
    w.insert(tk.END, text)


def write_to_entry(w, text=""):
    if text == "":
        text = "New Text"
    w.delete(0, tk.END)
    w.insert(tk.END, "New Text")


def read_from_entry(w):
    entry_input = w.get()
    return entry_input


def prepend_to_entry(w, text=""):
    if text == "":
        text = "Additional Text "
    w.insert(0, text)


def insert_in_entry(w, text="", idx=0):
    w.insert(idx, text)


# ------------------------------------------------------------
# Text Widget Example Procedures
def append_to_text(w, text=""):
    if text == "":
        text = " Additional Text"
    w.insert(tk.END, text)


def write_to_text(w, text=""):
    if text == "":
        text = "Text"
    w.delete(1.0, tk.END)
    w.insert(tk.END, text)


def read_from_text(w):
    text_content = w.get(1.0, tk.END)
    return text_content


def delete_all_text(w):
    # Delete all text from the beginning (1.0) to the end (tk.END)
    w.delete(1.0, tk.END)


 

# ------------------------------------------------------------
# Label Widget Example Procedure
def update_label(w, text=""):
    if text == "":
        text = "Label Text"
    w.config(text=text)
    

def update_label_background(w, color="white"):
    w.config(bg=color)
    

def update_label_foreground(w, color="black"):
    w.config(fg=color)
    


# ------------------------------------------------------------
# Listbox Widget Example Procedures
def write_to_listbox(w, text=""):
    if text == "":
        text = "New Item"
    w.insert(tk.END, text)


def read_from_listbox(w):
    selected_item = w.get(tk.ANCHOR)
    return selected_item


def set_listbox_height(w, i):
    w9.config(height = i)
    return 


def set_listbox_width(w, i):
    w9.config(width = i)
    return





# ------------------------------------------------------------
# Checkbutton Widget Example Procedures
def select_checkbutton(w):
    w.select()


def deselect_checkbutton(w):
    w.deselect()


def get_checkbutton():
    # # Uses: x = tk.IntVar() to make variables for each Checkbutton
    # # Note: Replace '?' with your widget's name. In the name of the '?_var = tk.IntVar()'
    # #       The '?' is the name of the widget that was created.
    # #       It should be the line before...
    # #       ? = tk.Checkbutton(root,...
    # # This function could handle multiple Checkbuttons, like so...

    # First Checkbutton
    # if check1_var.get() == 1:
        # return True
    # else:
        # return False
    
    # Second Checkbutton
    # if check2_var.get() == 1:
        # Instead of returning True or False
    # else:
        # You can of course run code conditionally here as well
            
            
    return



# ------------------------------------------------------------
# Button Widget Example Procedures
def write_to_button(w, text=""):
    if text == "":
        text = "Button"
    w.config(text=text)



# ------------------------------------------------------------
# Spinbox Widget Example Procedures
def write_to_spinbox(w, i=0):
    w.set(i)


# ------------------------------------------------------------
# Scale Widget Example Procedures
def write_to_scale(w, i=0):
    w.set(i)


def scale_changed(value):
    # Performed when the Scale widget is moved.
    # The 'value' argument automatically receives the current scale 'value' as a string
    messagebox.showinfo(f"Scale Value: {float(value):.2f}")
    


# ------------------------------------------------------------
# General GUI Example Procedures

# center window, uncomment to use separately from built-in center_window function
# def center_window(w):
    # w.withdraw()
    # w.update_idletasks()
    # x = (w.winfo_screenwidth() - w.winfo_width()) // 2
    # y = (w.winfo_screenheight() - w.winfo_height()) // 2
    # y = y - 15	# centers it better???? make up for titlebar??? in tkinter, not from tcl/tk
    # w.geometry(f'+{x}+{y}')
    # w.deiconify()


# --------------------------------
# Close App Function
# This is the way to close the app since we don't know toplevel.
# But we get it by passing one of the widgets to this function, then 
# it finds that widget's toplevel :) Then Destorys it.
# --------------------------------

# YOU CAN NOT DO THIS... !!!!!!!!!!!
# THE WIDGET 'myCloseButton' IS NOT 
# CREATED YET WHEN ASSIGNING THE PROCEDURE TO 'command'
# myCloseButton = tk.Button(root, text='Close', command=close_app(myCloseButton))


def close_app(w):
    # Use a widget to find the topmost window frame and destroy it
    top_window = w.winfo_toplevel()
    top_window.destroy()


