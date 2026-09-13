# RPyTkGUICreator.py
# Backup GOOD Latest: RPyTkGUICreatorV1c.py
# Backup Latest: RPyTkGUICreatorV1d.py
# REPO 3:03 PM 9/12/2026 
# Full Official APP Name: Rocks Python-Tkinter GUI Creator 1v1


# NAMES:
# Offcial Name:             Rocks Python-Tkinter GUI Creator
# App.EXE (.py) Name:       RPyTkGUICreator
# Development Name:         RPyTkGUICreator.py (RPyTkGUICreator.EXE)

# --------------------------------------------------------------------
# START of imports for PyInstaller External Python Script Launcher
# --------------------------------------------------------------------
from __future__ import annotations
import argparse
import os
import runpy
import subprocess
import sys
import traceback
from pathlib import Path
from typing import Iterable, Optional
# --------------------------------------------------------------------
# END of imports for PyInstaller External Python Script Launcher
# --------------------------------------------------------------------

# -----------------------------------------------------
# GUI start of imports
# -----------------------------------------------------
# imports (Tkinter common)
import tkinter as tk
from tkinter import filedialog, simpledialog, colorchooser, messagebox
from tkinter import scrolledtext
# my 'custom' dialog to override 'simpledialog' focus behavior
from tkinter.simpledialog import Dialog
import json
import textwrap		# may end up being removed
# --------------------------------------------------------------------
# Get the current Python version as a string
# Check if the Python version is greater than or equal to 3.11
if sys.version_info >= (3, 11):
    import tomllib  # Built-in python 3.11+. Use 'import toml' for older versions
else:
    import toml  # Not Built-in versions before python 3.11. Use 'import tomllib' for newer versions
# --------------------------------------------------------------------
# COLOR for chlorophyll: CodeView
from pygments.lexers import get_lexer_by_name
from chlorophyll import CodeView
# --------------------------------------------------------------------
from datetime import datetime
# --------------------------------------------------------------------
# GUI end of imports
# --------------------------------------------------------------------
   
# ------------------------------------------------------------------
# GUI start of Generated Application Properties/Configuration
# ------------------------------------------------------------------
RPYTKGUIC_S_TITLE = "My Python-Tkinter Application"
RPYTKGUIC_I_X_SIZE = 400
RPYTKGUIC_I_Y_SIZE = 350
RPYTKGUIC_I_AUTOCENTER = 1
RPYTKGUIC_I_TOPX = -1
RPYTKGUIC_I_TOPY = -1
RPYTKGUIC_I_RESIZE = 1
RPYTKGUIC_I_SCROLLEDBOXES = 0
RPYTKGUIC_I_AUTOFUNCTIONS = 0
RPYTKGUIC_I_FONT_SIZE = 12              # Edit Window - Code Window
RPYTKGUIC_S_FONT_NAME = "Consolas"      # Edit Window - Code Window
RPYTKGUIC_S_FONT = "Consolas 8"         # Edit Window - Cancel, Save OK buttons
RPYTKGUIC_I_GRID_SIZE = 10


# Reset Generated Application Global Properties/Configuration Expicitly by Name
# These are the settings when the GUI Creator starts up and after clicking the 'New' button.
def reset_app_config():
    global RPYTKGUIC_S_TITLE, RPYTKGUIC_I_X_SIZE, RPYTKGUIC_I_Y_SIZE, RPYTKGUIC_I_AUTOCENTER, RPYTKGUIC_I_TOPX, RPYTKGUIC_I_TOPY, RPYTKGUIC_I_RESIZE
    global RPYTKGUIC_I_SCROLLEDBOXES, RPYTKGUIC_I_AUTOFUNCTIONS
    global RPYTKGUIC_I_FONT_SIZE, RPYTKGUIC_S_FONT_NAME, RPYTKGUIC_S_FONT, RPYTKGUIC_I_GRID_SIZE
    RPYTKGUIC_S_TITLE = "My Python-Tkinter Application"
    RPYTKGUIC_I_X_SIZE = 400
    RPYTKGUIC_I_Y_SIZE = 350
    RPYTKGUIC_I_AUTOCENTER = 1
    RPYTKGUIC_I_TOPX = -1
    RPYTKGUIC_I_TOPY = -1
    RPYTKGUIC_I_RESIZE = 1
    RPYTKGUIC_I_SCROLLEDBOXES = 0
    RPYTKGUIC_I_AUTOFUNCTIONS = 0
    RPYTKGUIC_I_FONT_SIZE = 12              # Edit Window - Code Window
    RPYTKGUIC_S_FONT_NAME = "Consolas"      # Edit Window - Code Window
    RPYTKGUIC_S_FONT = "Consolas 8"         # Edit Window - Cancel, Save OK buttons
    RPYTKGUIC_I_GRID_SIZE = 10


# -----------------------------


# Load Generated Application Global Properties/Configuration
def load_app_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line and "=" in cleaned_line:
                var_name, var_value = cleaned_line.split("=", 1)
                var_name = var_name.strip()
                var_value = var_value.strip()
                if var_name.startswith("RPYTKGUIC_S"):
                    globals()[var_name] = str(var_value)
                if var_name.startswith("RPYTKGUIC_I"):
                    globals()[var_name] = int(var_value)


# -----------------------------


# Save Generated Application Global Properties/Configuration
def save_app_config(filename):
    with open(filename, "w", encoding="utf-8") as file:
        for var_name, var_value in list(globals().items()):
            if var_name.startswith("RPYTKGUIC_"):
                file.write(f"{var_name}={var_value}\n")


# ------------------------------------------------------------------
# GUI end of Generated Application Properties/Configuration
# ------------------------------------------------------------------

# -----------------------------------------------------
# GUI start of Constants
# -----------------------------------------------------


# --------- SET UP EXTERNAL FILES ---------------------

exe_files_folder = "app_files"
theme_filename = "theme.toml"
library_filename = "library.py"
config_filename = "config.txt"
real_full_path = ""
icons_path = "icons"
real_icons_path = ""
exe_environment = False


# Check if running in an executable environment (PyInstaller)
if hasattr(sys, '_MEIPASS'):
    # Running in a PyInstaller bundle
    base_path = sys._MEIPASS
    # Construct the real full path to the files, the files in EXE, are in 'app_files'
    real_full_path = os.path.join(base_path, exe_files_folder)
    real_icons_path = os.path.join(base_path, exe_files_folder)
    exe_environment = True
else:
    # Running from source code - command line
    base_path = os.path.abspath(".")
    # Construct the real full path to the file, the files is in same dir as this python app
    real_full_path = os.path.join(base_path)
    real_icons_path = os.path.join(base_path, icons_path)
    exe_environment = False



# --------- THEME FILE --------------------------
def read_create_themefile(file_path):
    global real_full_path, theme_filename
    try:
        if sys.version_info >= (3, 11):
            theme_dict = tomllib.load(file_path)
        else:
            theme_dict = toml.load(file_path)
        return theme_dict
    except FileNotFoundError:
        with open(os.path.join(real_full_path, theme_filename), 'r') as file:
            content = file.read()
            file.close()
        with open(os.path.join(file_path), 'w') as file:
            file.write(content)
            file.close()
        if sys.version_info >= (3, 11):
            theme_dict = tomllib.load(file_path)
        else:
            theme_dict = toml.load(file_path)
        return theme_dict

theme_file = os.path.join(".", theme_filename)
# load color theme for CodeView widget
custom_theme_dict = read_create_themefile(theme_file)



# --------- CONFIG FILE --------------------------
def read_create_configfile(file_path):
    global real_full_path, config_filename
    try:
        with open(file_path, "r") as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line and "=" in cleaned_line:
                    var_name, var_value = cleaned_line.split("=", 1)
                    var_name = var_name.strip()
                    var_value = var_value.strip()
                    if var_name.startswith("RPYTKGUIC_S"):
                        globals()[var_name] = str(var_value)
                    if var_name.startswith("RPYTKGUIC_I"):
                        globals()[var_name] = int(var_value)
    except FileNotFoundError:
        reset_app_config()
        save_app_config(file_path)
        load_app_config(file_path)
        
        
reset_app_config()  # init vars to start with, so load will have a place to load values
config_file = os.path.join(".", config_filename)
read_create_configfile(config_file)



# --------- LIBRARY FILE --------------------------
def read_library_file(file_path):
    global real_full_path, library_filename
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        with open(os.path.join(real_full_path, library_filename), 'r') as file:
            content = file.read()
            file.close()
        with open(os.path.join(file_path), 'w') as file:
            file.write(content)
            file.close()
        return content



library_file = os.path.join(".", library_filename)
# get the External Library File
EXT_LIBRARY = read_library_file(library_file)


# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------

def get_asset_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# --------- GLOBALS --------------------------------------------------
# functions/code
# Start with an empty dictionary
CODE_BASE = {}

# -----------------------------------------------------
# GUI end of Constants
# -----------------------------------------------------
  
   
# ---------------------------------------------------------------------------
# Constants - CmdLine arguments For Pyinstaller generated EXE
# ---------------------------------------------------------------------------
RUN_SCRIPT_FLAG = "--run-script"
CHILD_FLAG = "--launcher-child"
   

# ------------------------------------------------------------
# GUI start of MY 'CUSTOM' DIALOG TO OVERRIDE 'SIMPLEDIALOG'
# ------------------------------------------------------------
    
class MyInputDialog(Dialog):
    def __init__(self, parent, title=None, prompt="Enter something:"):
        self.prompt = prompt
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("275x150")
        self.label = tk.Label(master, text=self.prompt)
        self.label.pack(padx=5, pady=5, fill="x")
        self.entry = tk.Entry(master, width=40)
        self.entry.pack(padx=5, pady=5, fill="x")
        return self.entry  # Initial focus will be set to this :)

    def apply(self):
        self.result = self.entry.get()

def focused_dialog(title, prompt):
    root = tk.Tk()
    root.withdraw()
    dialog = MyInputDialog(root, title=title, prompt=prompt)
    root.destroy()
    return dialog.result

# ------------------------------------------------------------
# GUI end of MY 'CUSTOM' DIALOG TO OVERRIDE 'SIMPLEDIALOG'
# ------------------------------------------------------------



# ------------------------------------------------------------
# GUI start of MY 'TOOLTIP' CLASS
# ------------------------------------------------------------

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.after_id = None
        self.close_id = None

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.close_id:
            self.widget.after_cancel(self.close_id)
            self.close_id = None
            
        if self.tip_window or not self.text:
            return
            
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20

        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(tw, text=self.text, justify=tk.LEFT, background="#ffffe0", relief=tk.SOLID, borderwidth=1, font=("tahoma", "10", "normal"))
        label.pack(ipadx=1)

        self.close_id = self.widget.after(3000, self.hide_tooltip)

    def hide_tooltip(self, event=None):
        if self.close_id:
            self.widget.after_cancel(self.close_id)
            self.close_id = None
            
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None



# ------------------------------------------------------------
# GUI end of MY 'TOOLTIP' CLASS
# ------------------------------------------------------------
    

# -----------------------------------------------------
# GUI start of Global Functions
# -----------------------------------------------------


def center_window(w):
    w.withdraw()
    w.update_idletasks()
    x = (w.winfo_screenwidth() - w.winfo_width()) // 2
    y = (w.winfo_screenheight() - w.winfo_height()) // 2
    y = y - 15	# centers it better???? make up for titlebar??? in tkinter, not from tcl/tk
    w.geometry(f'+{x}+{y}')
    w.deiconify()

# -----------------------------------------------------
# GUI end of Global Functions
# -----------------------------------------------------


# -----------------------------------------------------
# GUI start of Project Configuration Window
# -----------------------------------------------------

def open_configuration_window(): 
    global RPYTKGUIC_S_TITLE, RPYTKGUIC_I_X_SIZE, RPYTKGUIC_I_Y_SIZE, RPYTKGUIC_I_AUTOCENTER, RPYTKGUIC_I_TOPX, RPYTKGUIC_I_TOPY, RPYTKGUIC_I_RESIZE
    global RPYTKGUIC_I_SCROLLEDBOXES, RPYTKGUIC_I_AUTOFUNCTIONS
    global RPYTKGUIC_I_FONT_SIZE, RPYTKGUIC_S_FONT_NAME, RPYTKGUIC_S_FONT, RPYTKGUIC_I_GRID_SIZE

    # Create the new window (toplevel)
    config_win = tk.Toplevel()
    config_win.title("Project Configuration - Rocks Python-Tkinter GUI Creator")
    config_win.geometry("550x380")
    center_window(config_win)
    # Load the favicon dynamically
    config_win.iconbitmap(get_asset_path("favicon.ico")) 

    # Force 'config_win' to the front and lock focus
    config_win.lift()          # Pulls it to the top
    config_win.grab_set()      # Freezes interaction with the root window

 
    # Function f_btnOk() for Button Widget: btnOk - (command)
    def f_btnOk():
        global RPYTKGUIC_S_TITLE, RPYTKGUIC_I_X_SIZE, RPYTKGUIC_I_Y_SIZE, RPYTKGUIC_I_AUTOCENTER, RPYTKGUIC_I_TOPX, RPYTKGUIC_I_TOPY, RPYTKGUIC_I_RESIZE
        global RPYTKGUIC_I_SCROLLEDBOXES, RPYTKGUIC_I_AUTOFUNCTIONS
        global RPYTKGUIC_I_FONT_SIZE, RPYTKGUIC_S_FONT_NAME, RPYTKGUIC_S_FONT, RPYTKGUIC_I_GRID_SIZE
        RPYTKGUIC_S_TITLE = str(entTitle.get())
        RPYTKGUIC_I_X_SIZE = int(entWinXSize.get())
        RPYTKGUIC_I_Y_SIZE = int(entWinYSize.get())
        RPYTKGUIC_I_AUTOCENTER = int(chkAutoCenterWin_var.get())
        RPYTKGUIC_I_TOPX = int(entTopXPos.get())
        RPYTKGUIC_I_TOPY = int(entTopYPos.get())
        RPYTKGUIC_I_RESIZE = int(chkWindowResizable_var.get())
        RPYTKGUIC_I_SCROLLEDBOXES = int(chkAutoAddScrollBars_var.get())
        RPYTKGUIC_I_AUTOFUNCTIONS = int(chkAddAutoFunctions_var.get())
        RPYTKGUIC_I_FONT_SIZE = int(entFontSizeEditor.get())          # Edit Window - Code Window
        RPYTKGUIC_S_FONT_NAME = str(entFontNameEditor.get())      # Edit Window - Code Window
        RPYTKGUIC_S_FONT = str(entFontSizeButtons.get())         # Edit Window - Cancel, Save OK buttons
        RPYTKGUIC_I_GRID_SIZE = int(entGridSize.get())
        config_win.destroy()


    # Function f_btnCancel() for Button Widget: btnCancel - (command)
    def f_btnCancel():
        config_win.destroy()


    # --- WIDGETS GUI CODE ---
    lblTitle=tk.Label(config_win,text='Project Window Title', fg='SystemButtonText',bg='SystemButtonFace')
    lblTitle.place(x=11,y=11,width=116,height=21)

    entTitle=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entTitle.place(x=141,y=11,width=304,height=19)

    lblWinXSize=tk.Label(config_win,text='Project Window X Size', fg='SystemButtonText',bg='SystemButtonFace')
    lblWinXSize.place(x=11,y=41,width=123,height=21)

    entWinXSize=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entWinXSize.place(x=142,y=42,width=64,height=19)

    lblWinYSize=tk.Label(config_win,text='Project Window Y Size', fg='SystemButtonText',bg='SystemButtonFace')
    lblWinYSize.place(x=11,y=71,width=123,height=21)

    entWinYSize=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entWinYSize.place(x=142,y=72,width=64,height=19)

    chkAutoCenterWin_var = tk.IntVar()
    chkAutoCenterWin=tk.Checkbutton(config_win,text='Auto Center Project Window', variable=chkAutoCenterWin_var, fg='SystemWindowText',bg='SystemButtonFace')
    chkAutoCenterWin.place(x=231,y=41,width=179,height=25)

    lblTopXPos=tk.Label(config_win,text='Project Top X Position', fg='SystemButtonText',bg='SystemButtonFace')
    lblTopXPos.place(x=11,y=111,width=123,height=21)

    lblTopYPos=tk.Label(config_win,text='Project Top Y Position', fg='SystemButtonText',bg='SystemButtonFace')
    lblTopYPos.place(x=12,y=142,width=123,height=21)

    entTopXPos=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entTopXPos.place(x=142,y=112,width=64,height=19)

    entTopYPos=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entTopYPos.place(x=141,y=141,width=64,height=19)

    chkWindowResizable_var = tk.IntVar()
    chkWindowResizable=tk.Checkbutton(config_win,text='Project Window Resizable', variable=chkWindowResizable_var, fg='SystemWindowText',bg='SystemButtonFace')
    chkWindowResizable.place(x=231,y=71,width=163,height=25)

    chkAutoAddScrollBars_var = tk.IntVar()
    chkAutoAddScrollBars=tk.Checkbutton(config_win,text='Auto Add Scrollbars to Text and Listbox Widgets', variable=chkAutoAddScrollBars_var, fg='SystemWindowText',bg='SystemButtonFace')
    chkAutoAddScrollBars.place(x=231,y=111,width=281,height=25)

    chkAddAutoFunctions_var = tk.IntVar()
    chkAddAutoFunctions=tk.Checkbutton(config_win,text='Automatically Add Placeholder Functions for Widgets', variable=chkAddAutoFunctions_var, fg='SystemWindowText',bg='SystemButtonFace')
    chkAddAutoFunctions.place(x=231,y=141,width=311,height=25)

    lblSnapToGrid=tk.Label(config_win,text='Snap To Grid Size', fg='SystemButtonText',bg='SystemButtonFace')
    lblSnapToGrid.place(x=11,y=181,width=97,height=21)

    entGridSize=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entGridSize.place(x=151,y=181,width=64,height=19)

    lblFontSizeButtons=tk.Label(config_win,text='Font and Size Buttons', fg='SystemButtonText',bg='SystemButtonFace')
    lblFontSizeButtons.place(x=12,y=212,width=120,height=21)

    entFontSizeButtons=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entFontSizeButtons.place(x=151,y=211,width=85,height=19)

    lblFontNameEditor=tk.Label(config_win,text='Font Name for Editor', fg='SystemButtonText',bg='SystemButtonFace')
    lblFontNameEditor.place(x=11,y=241,width=117,height=21)

    entFontNameEditor=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entFontNameEditor.place(x=151,y=241,width=85,height=19)

    lblFontSizeEditor=tk.Label(config_win,text='Font Size for Editor', fg='SystemButtonText',bg='SystemButtonFace')
    lblFontSizeEditor.place(x=11,y=271,width=105,height=21)

    entFontSizeEditor=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')
    entFontSizeEditor.place(x=151,y=271,width=64,height=19)

    btnOk=tk.Button(config_win,text='Ok', command=f_btnOk, fg='SystemButtonText',bg='SystemButtonFace')
    btnOk.place(x=381,y=321,width=66,height=26)

    btnCancel=tk.Button(config_win,text='Cancel', command=f_btnCancel, fg='SystemButtonText',bg='SystemButtonFace')
    btnCancel.place(x=121,y=321,width=66,height=26)

    # --- LOAD GUI WIDGETS VALUES ---

    entTitle.delete(0, tk.END)
    entTitle.insert(tk.END, str(RPYTKGUIC_S_TITLE))

    entWinXSize.delete(0, tk.END)
    entWinXSize.insert(tk.END, str(RPYTKGUIC_I_X_SIZE))

    entWinYSize.delete(0, tk.END)
    entWinYSize.insert(tk.END, str(RPYTKGUIC_I_Y_SIZE))

    if int(RPYTKGUIC_I_AUTOCENTER) == 1:
        chkAutoCenterWin.select()
    else:
        chkAutoCenterWin.deselect()

    entTopXPos.delete(0, tk.END)
    entTopXPos.insert(tk.END, str(RPYTKGUIC_I_TOPX))

    entTopYPos.delete(0, tk.END)
    entTopYPos.insert(tk.END, str(RPYTKGUIC_I_TOPY))

    if int(RPYTKGUIC_I_RESIZE) == 1:
        chkWindowResizable.select()
    else:
        chkWindowResizable.deselect()

    if int(RPYTKGUIC_I_SCROLLEDBOXES) == 1:
        chkAutoAddScrollBars.select()
    else:
        chkAutoAddScrollBars.deselect()

    if int(RPYTKGUIC_I_AUTOFUNCTIONS) == 1:
        chkAddAutoFunctions.select()
    else:
        chkAddAutoFunctions.deselect()

    entFontSizeEditor.delete(0, tk.END)
    entFontSizeEditor.insert(tk.END, str(RPYTKGUIC_I_FONT_SIZE))

    entFontNameEditor.delete(0, tk.END)
    entFontNameEditor.insert(tk.END, str(RPYTKGUIC_S_FONT_NAME))

    entFontSizeButtons.delete(0, tk.END)
    entFontSizeButtons.insert(tk.END, str(RPYTKGUIC_S_FONT))

    entGridSize.delete(0, tk.END)
    entGridSize.insert(tk.END, str(RPYTKGUIC_I_GRID_SIZE))


# -----------------------------------------------------
# GUI end of Project Configuration Window
# -----------------------------------------------------


# -----------------------------------------------------
# GUI start of Code Edit Window
# -----------------------------------------------------
    
def open_edit_window(input_func_name, guicreator_ref, extra): 
    global CODE_BASE

    # Create the new window (toplevel)
    edit_win = tk.Toplevel()
    edit_win.title("Rocks Py/Tk GUI Creator Code Editor")
    edit_win.geometry("720x600")
    center_window(edit_win)
    # Load the favicon dynamically
    edit_win.iconbitmap(get_asset_path("favicon.ico")) 

    # Force 'edit_win' to the front and lock focus
    edit_win.lift()          # Pulls it to the top
    edit_win.grab_set()      # Freezes interaction with the root window


    # Decide what type of code we are opening
    function_name = input_func_name
    functions_to_skip = ["init", "library", "main", "pregui", "postgui"]
    # Check if the function is NOT a built-in function
    if function_name not in functions_to_skip:
        func_name = function_name

    if extra == 1:   # is a widget function - opened via widget_tree
        if not function_name.startswith('f_'):
            func_name = "f_" + func_name
        
    if extra == 0:   # is NOT an automatic widget function - opened via functions_tree
        func_name = input_func_name


    if extra == 2:   # is 'debug_test.py' input_func_name='debug_test.py'
        func_name = input_func_name

    message_binfo1 = "Debug View Mode"
    message_binfo2 = "Feature diabled in Debug View Mode\nClick 'Cancel' to close edit window."
    
    def clear_edit_window():
        if extra == 2:
            messagebox.showinfo(message_binfo1, message_binfo2, parent=edit_win)
            return
        result = messagebox.askyesno("Clear all code from edit window", "Do you want to continue?", parent=edit_win)
        if result is True:
            text_area.delete("1.0", tk.END)
            builtin_functions = ["init", "library", "main", "pregui", "postgui"]
            # Check if the function is a built-in function
            if func_name in builtin_functions:
                text_area.insert("1.0", "#\n# ---- " + func_name.upper() + " ----\n#\n\n")
            else:
                text_area.insert("1.0", "#\n# Function Named: " + func_name + "\n#\n\n")
            

    def loadinsertfile():
        if extra == 2:
            messagebox.showinfo(message_binfo1, message_binfo2, parent=edit_win)
            return
        f = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("All files", "*.*")], parent=edit_win)
        if not f: return
        fileX = open(f, 'r', encoding='utf-8')
        content = fileX.read()
        fileX.close()
        text_area.insert(tk.INSERT, "\n" + content)
        
    
    def saveasfile():
        f = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("All files", "*.*")], parent=edit_win)
        if not f: return
        content = text_area.get("1.0", tk.END).strip()
        fileX = open(f, 'w', encoding='utf-8')
        fileX.write(content)
        fileX.close()


    def on_ok():
        if extra == 2:
            messagebox.showinfo(message_binfo1, message_binfo2, parent=edit_win)
            return
        updated_content = text_area.get("1.0", tk.END).strip()
        CODE_BASE[func_name] = updated_content
        guicreator_ref.functions.delete(0, tk.END) 
        for key, value in CODE_BASE.items():
            guicreator_ref.functions.insert(tk.END, key)
            
        edit_win.destroy()


    def on_save():
        if extra == 2:
            messagebox.showinfo(message_binfo1, message_binfo2, parent=edit_win)
            return
        updated_content = text_area.get("1.0", tk.END).strip()
        CODE_BASE[func_name] = updated_content
        guicreator_ref.functions.delete(0, tk.END) 
        for key, value in CODE_BASE.items():
            guicreator_ref.functions.insert(tk.END, key)
        
        messagebox.showinfo("Saved Function: ", func_name, parent=edit_win)


    def on_cancel():
        edit_win.destroy()

   
    # --- MENU GUI SECTION ---
    menubar=tk.Menu(edit_win)
    # --- File MENU---
    File=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='File',menu=File)
    if extra != 2: File.add_command(label='Clear Edit Window', command=clear_edit_window)
    if extra != 2: File.add_command(label='Open Insert *.py File', command=loadinsertfile)
    File.add_command(label='Save as *.py File', command=saveasfile)
    File.add_command(label='Exit', command=on_cancel)

    # --- ADD MENU TO WINDOW ---
    edit_win.config(menu=menubar)
    
    # Create a frame for buttons at the bottom
    top_frame = tk.Frame(edit_win)
    top_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

    # Using CodeView for code editor widget
    my_lexer = get_lexer_by_name("python")
    text_area = CodeView(edit_win, lexer=my_lexer, color_scheme=custom_theme_dict, font=(RPYTKGUIC_S_FONT_NAME, RPYTKGUIC_I_FONT_SIZE, ""))

    text_area.insert(tk.INSERT, "")
    text_area.pack(padx=10, pady=10, fill="both", expand=True)

    # Create a frame for buttons at the bottom
    bottom_frame = tk.Frame(edit_win)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

    # check for debug view mode
    if extra == 2:   # is 'debug_test.py' input_func_name='debug_test.py'
        script_path = os.path.join(".", "debug_test.py")
        file = open(script_path, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        text_area.insert(tk.INSERT, content)
        edit_win.title("Debug View Mode - Loaded : " + func_name)
    else:
        # get CODE from dict
        content = CODE_BASE.get(func_name, "")
        if len(content) > 0:
            text_area.insert(tk.INSERT, content)
            edit_win.title("Code Editor - Function Loaded : " + func_name)
        else:
            empty_template = "# No Saved Function Named: " + func_name + "\n"
            if func_name.startswith('f_'):
                empty_template = empty_template + "# Widget: " + func_name + "\n"
            empty_template = empty_template + "\n"
            empty_template = empty_template + "# ***Placeholder Template Function***\n"
            empty_template = empty_template + "\n"
            empty_template = empty_template + "def " + func_name + "():" + "\n"
            empty_template = empty_template + "\n"
            empty_template = empty_template + "    # Code goes here..." + "\n"
            empty_template = empty_template + "\n"
            empty_template = empty_template + "    return" + "\n"
            empty_template = empty_template + "\n"
            empty_template = empty_template + "\n"
            text_area.insert(tk.INSERT, empty_template)
            edit_win.title("Code Editor - No Saved Function Loaded : " + func_name)


    if extra != 2:
        # is 'debug_test.py' input_func_name='debug_test.py'    # Add Save, Cancel and OK buttons
        ok_button = tk.Button(bottom_frame, text="OK", width=10, command=on_ok, font=RPYTKGUIC_S_FONT)
        ok_button.pack(side=tk.RIGHT, padx=5)

        save_button = tk.Button(bottom_frame, text="Save", width=10, command=on_save, font=RPYTKGUIC_S_FONT)
        save_button.pack(side=tk.RIGHT, padx=5)

    cancel_button = tk.Button(bottom_frame, text="Cancel", width=10, command=on_cancel, font=RPYTKGUIC_S_FONT)
    cancel_button.pack(side=tk.RIGHT, padx=5)

    if extra != 2:
        ok_buttont = tk.Button(top_frame, text="OK", width=10, command=on_ok, font=RPYTKGUIC_S_FONT)
        ok_buttont.pack(side=tk.RIGHT, padx=5)

        save_buttont = tk.Button(top_frame, text="Save", width=10, command=on_save, font=RPYTKGUIC_S_FONT)
        save_buttont.pack(side=tk.RIGHT, padx=5)

    cancel_buttont = tk.Button(top_frame, text="Cancel", width=10, command=on_cancel, font=RPYTKGUIC_S_FONT)
    cancel_buttont.pack(side=tk.RIGHT, padx=5)


# -----------------------------------------------------
# GUI end of Code Edit Window
# -----------------------------------------------------


# -----------------------------------------------------
# GUI start of class 'GuiCreator' for RPyTkGUICreator
# -----------------------------------------------------

class GuiCreator:

    def __init__(self, root):
        self.root = root
        root.title("Rocks Python/Tkinter GUI Creator 1v1")

        self.widgets = []
        self.selected = None
        self.clip = None
        self.menus = []
        
        global CODE_BASE, real_icons_path
        CODE_BASE = {}

        main = tk.Frame(root)
           
        main.pack(fill="both", expand=1)

        # LEFT ----------
        left = tk.Frame(main)

        left.pack(side="left", fill="y")

        tk.Label(left, text="Widgets").pack()

        # ----------------------------------------------------------------------------------

        toolbar = tk.Frame(left, bg="#f0f0f0", bd=1, relief="flat", padx=6, pady=6)
        toolbar.pack()

        widget_definitions = [
            {"name": "Label",           "file": "label.png"},
            {"name": "Text",            "file": "text.png"},
            {"name": "Button",          "file": "button.png"},
            {"name": "Checkbutton",     "file": "checkbutton.png"},
            {"name": "Listbox",         "file": "listbox.png"},
            {"name": "Entry",           "file": "entry.png"},
            {"name": "Spinbox",         "file": "spinbox.png"},
            {"name": "Scale",           "file": "scale.png"},
            {"name": "Canvas",          "file": "canvas.png"}
        ]

        loaded_icons = []

        # ----------------------------------------------------------

        def on_icon_click(clicked_label, widget_name):
             self.add_widget(widget_name)

        # ----------------------------------------------------------

        for index, item in enumerate(widget_definitions):
            row = index % 5
            col = index // 5
            tk_image = tk.PhotoImage(file=os.path.join(real_icons_path, item["file"]))
            loaded_icons.append(tk_image)
            lbl = tk.Label(
                toolbar, 
                image=tk_image, 
                bg="#f0f0f0",
                cursor="hand2",  # Hand cursor on hover
                padx=6, 
                pady=6
            )
            lbl.image = tk_image  # Keeps a persistent reference so Python doesn't delete it
            lbl.grid(row=row, column=col, padx=4, pady=4)
            lbl.bind("<Button-1>", lambda event, l=lbl, n=item["name"]: on_icon_click(l, n))
            ToolTip(lbl, f'{item["name"]} Widget')
            
        # ----------------------------------------------------------------------------------

           
        tk.Label(left, text="Edit").pack()
        tk.Button(left, text="Copy", command=self.copy).pack(fill="x")
        tk.Button(left, text="Paste", command=self.paste).pack(fill="x")
        tk.Button(left, text="Delete", command=self.delete).pack(fill="x")
        tk.Label(left, text="Menu").pack()
        tk.Button(left, text="Add Menu", command=self.add_menu).pack(fill="x")
        tk.Label(left, text="Test App").pack()
        self.launch_button = tk.Button(left, text="Launch", command=self.test_app)
        self.launch_button.pack(fill="x")
        self.debug_button = tk.Button(left, text="Debug View", command=self.debug_view)
        self.debug_button.pack(fill="x")

        # CANVAS ----------
        self.canvas = tk.Frame(main, bd=1, relief="solid")  # show GUI border
            
        self.canvas.pack(side="left", fill="both", expand=1)
        self.selection_box = tk.Frame(self.canvas, bd=0, relief="flat")		# was... bd=1, relief="solid"
        self.selection_box.place_forget()

        # RIGHT ----------
        right = tk.Frame(main, width=150)
            
        right.pack_propagate(False)
        right.pack(side="right", fill="y", padx=5)
 
 
        # Widget tree header
        wd=tk.Label(right, text="Widgets")
        wd.pack(anchor="w")
        ToolTip(wd, f"List of Widgets in GUI.\nDouble-Click this list to bring up\na code window to edit the widget function.")
        tree_frame = tk.Frame(right)
        tree_frame.pack(fill="x", pady=5)
        v_scroll_tree = tk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        h_scroll_tree = tk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        self.tree=tk.Listbox(tree_frame, height=6, xscrollcommand=h_scroll_tree.set, yscrollcommand=v_scroll_tree.set, fg="SystemButtonText",bg="SystemWindow")
        v_scroll_tree.config(command=self.tree.yview)
        h_scroll_tree.config(command=self.tree.xview)
        v_scroll_tree.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll_tree.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree.bind("<<ListboxSelect>>", self.tree_select)


        # Properties
        wp = tk.Label(right, text="Widget Properties")
        wp.pack(anchor="w")
        ToolTip(wp, f"Widget Properties\nClick on a widget in the GUI to select it.")
        self.props = {}

        for i, p in enumerate(["name", "text", "bg", "fg", "x", "y", "width", "height"]):
            f = tk.Frame(right); f.pack(fill="x")
            var_name = f"wz{i}"
            globals()[var_name] = tk.Label(f, text=p, width=6)
            globals()[var_name].pack(side="left")
            ToolTip(globals()[var_name], f"Index: {i}, Value: {p}")
            v = tk.StringVar()
            tk.Entry(f, textvariable=v).pack(side="right", fill="y", expand=1)
            self.props[p] = v

        # Property buttons
        tk.Button(right, text="Apply", command=self.apply).pack(fill="x")
        tk.Button(right, text="Pick BG", command=lambda:self.pick_color("bg")).pack(fill="x")
        tk.Button(right, text="Pick FG", command=lambda:self.pick_color("fg")).pack(fill="x")

        # Functions header
        wf=tk.Label(right, text="Functions")
        wf.pack(anchor="w")
        ToolTip(wf, f"Double-Click this list to bring up\na code window to edit the code.")
        functions_frame = tk.Frame(right)
        functions_frame.pack(fill="x", pady=5)
        v_scroll_functions = tk.Scrollbar(functions_frame, orient=tk.VERTICAL)
        h_scroll_functions = tk.Scrollbar(functions_frame, orient=tk.HORIZONTAL)
        self.functions=tk.Listbox(functions_frame, height=6, xscrollcommand=h_scroll_functions.set, yscrollcommand=v_scroll_functions.set, fg="SystemButtonText",bg="SystemWindow")
        v_scroll_functions.config(command=self.functions.yview)
        h_scroll_functions.config(command=self.functions.xview)
        v_scroll_functions.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll_functions.pack(side=tk.BOTTOM, fill=tk.X)
        self.functions.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Button(right, text="Remove Funcion", command=self.remove_func).pack(fill="x")
        tk.Button(right, text="New Funcion", command=self.create_func).pack(fill="x")



        def dbclick_widget_tree(event):
            # Open Code Edit Window with selected function
            # Opened via this listbox means it's a widget.
            # All automatic widget functions are prefix with 'f_' when opened.
            # open_edit_window(result, self, extra)  
            # extra [0 = as-is, 1 = prefix with 'f_']
            extra = 1
            selection_indices = self.tree.curselection()
            if selection_indices:
                index = selection_indices[0]
                selected_item = self.tree.get(index)
                result = selected_item.split(' ')[0]
                open_edit_window(result, self, extra) 
        
        self.tree.bind('<Double-Button-1>', dbclick_widget_tree)



        def dbclick_functions_tree(event):
            # Open Code Edit Window with selected function
            # Opened via this listbox means it's a function.
            # All automatic widget functions are prefix with 'f_' when opened.
            # open_edit_window(result, self, extra)  
            # extra [0 = as-is, 1 = prefix with 'f_']
            extra = 0
            selection_indices = self.functions.curselection()
            if selection_indices:
                index = selection_indices[0]
                selected_item = self.functions.get(index)
                result = selected_item.split(' ')[0]
                open_edit_window(result, self, extra)  
        
        self.functions.bind('<Double-Button-1>', dbclick_functions_tree)

    #-------------------------------------------------------------------------------------------

    # Project Comfiguration - Save GUI Configuration Settings as Default
    def save_mainapp_config(self):
        global config_filename
        save_app_config(os.path.join(".", config_filename))
        messagebox.showinfo("Saved GUI Default Configuration as: ", config_filename)
        
    #-------------------------------------------------------------------------------------------

    # Test App Debug View Function
    def debug_view(self):
        extra = 2
        open_edit_window("debug_test.py", self, extra)

    #-------------------------------------------------------------------------------------------
        
    # Test App Launch Function 
    def test_app(self):
        global exe_environment
        
        self.export_py(1)
        script_path = os.path.join(".", "debug_test.py")

        if exe_environment:
            python_exe = "RPyTkGUICreator.exe"
            command = [
                python_exe,
                '--run-script', 
                script_path
            ]
        else:
            python_exe = sys.executable
            command = [
                python_exe,
                "RPyTkGUICreator.py",
                '--run-script', 
                script_path
            ]


        # Disable the launch button when it's clicked
        if hasattr(self, 'launch_button') and self.launch_button is not None:
            self.launch_button.config(state=tk.DISABLED)
        
        # Hide the parent window
        self.root.withdraw()  
        
        # Create a new top-level window for the subprocess
        child_window = tk.Toplevel(self.root)
        child_window.title("Launch Test App Window")
        child_window.geometry("400x300")
        center_window(child_window)
        # Load the favicon dynamically
        child_window.iconbitmap(get_asset_path("favicon.ico")) 

        child_window.deiconify()
        
        # Create a Label widget to display results
        label = tk.Label(child_window, wraplength=400, justify="left", text="Running Test App...")
        label.pack(pady=20)
        output = tk.Label(child_window, wraplength=400, justify="left", text="")
        output.pack(pady=20)

        # Define what happens when the child window closes
        def on_close():
            self.root.deiconify()  # Bring parent window back
            child_window.destroy() # Permanently close child window

        # Intercept the 'X' close button click
        child_window.protocol("WM_DELETE_WINDOW", on_close)
        
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            label.config(text="Launch Test App completed successfully.")
            output.config(text=result.stdout)
            # Re-enable the launch button after subprocess completion
            if hasattr(self, 'launch_button') and self.launch_button is not None:
                self.launch_button.config(state=tk.NORMAL)
            on_close()

        except subprocess.CalledProcessError as e:
            label.config(text=f"Launch Test App 'debug_test.py' Failed with Error:")
            textError = e.stderr.replace(' \n', '\n\n')
            textOutput = ""
            flagError = False
            for line in textError.splitlines():
                if 'debug_test.py' in line or flagError == True:
                    textOutput += line + "\n"
                    flagError = True    # found 'debug_script' line, also output the rest as well.
            output.config(text=textOutput)

        finally:
            # Re-enable the launch button after subprocess completion
            if hasattr(self, 'launch_button') and self.launch_button is not None:
                self.launch_button.config(state=tk.NORMAL)



    #-------------------------------------------------------------------------------------------

    # Remove Function
    def remove_func(self):
        global CODE_BASE
        # Check if there is a selection
        selection_indices = self.functions.curselection()
        if selection_indices:
            index = selection_indices[0]
            selected_item = self.functions.get(index)
            result = selected_item.split(' ')[0]
            if result in CODE_BASE:     # in case user double-clicked to make function, but not save
                # Remove the item using del statement
                del CODE_BASE[result]
            else:
                messagebox.showinfo("Functions", f"Function '{result}' not found.")
                
            self.functions.delete(0, tk.END)    # re-build based on, if in the CODE_BASE
            for key, value in CODE_BASE.items():
                self.functions.insert(tk.END, key)
            
        else:
            messagebox.showinfo("Functions", "No function selected to remove.")


    # Create New Function
    def create_func(self):
        global CODE_BASE
        # Opens the pop-up modal on top of the main window
        new_func_name = simpledialog.askstring("Create New Function", "Enter name for new function: ", parent=self.root)
        
        if new_func_name:
            CODE_BASE[new_func_name] = ""
            self.functions.delete(0, tk.END)
            for key, value in CODE_BASE.items():
                self.functions.insert(tk.END, key)
     
    
    # UTILS
    def snap(self, v):
        return int(v / RPYTKGUIC_I_GRID_SIZE) * RPYTKGUIC_I_GRID_SIZE

    # CREATE
    def add_widget(self, t):

        if t=="Label": 
            w=tk.Label(self.canvas, text="Label")
        elif t=="Text":  
            w=tk.Text(self.canvas, width=22, height=5)
        elif t=="Button":  
            w=tk.Button(self.canvas, text="Button")
        elif t=="Checkbutton": 
            w=tk.Checkbutton(self.canvas, text="Checkbutton")
        elif t=="Listbox":
            w=tk.Listbox(self.canvas, width=15, height=5)
            for i in ["A","B","C"]:  
                w.insert("end",i)
        elif t=="Entry":  
            w=tk.Entry(self.canvas)
        elif t=="Spinbox":  
            w=tk.Spinbox(self.canvas, from_=0, to=10)
        elif t=="Scale":  
            w=tk.Scale(self.canvas, from_=0, to=100, orient="horizontal")
        elif t=="Canvas":  
            w=tk.Canvas(self.canvas, width=50, height=50, bg="lightgray")

        w.place(x=50,y=50)

        w.bind("<Button-1>", lambda e:self.select(w))
        w.bind("<B1-Motion>", lambda e:self.drag(w,e))
        w.bind("<Shift-B1-Motion>", lambda e:self.resize(w,e))

        w._name = f"w{len(self.widgets)}"

        self.widgets.append(w)
        self.update_tree()

    # SELECT
    def select(self, w):
        self.selected = w
        self.load_props(w)
        self.update_selection_box()

    def tree_select(self, e):
        i=self.tree.curselection()
        if i:
            self.select(self.widgets[i[0]])

    # MOVE
    def drag(self, w, e):
        x=self.snap(e.x_root - self.canvas.winfo_rootx())
        y=self.snap(e.y_root - self.canvas.winfo_rooty())
        w.place(x=x,y=y)
        self.update_selection_box()
        self.load_props(w)

    # RESIZE
    def resize(self, w, e):
        try: w.config(width=int(e.x/8))
        except: pass
        try: w.config(height=int(e.y/20))
        except: pass
        self.update_selection_box()

    # SELECTION BOX
    def update_selection_box(self):
        if not self.selected:
            self.selection_box.place_forget()
            return

        x=self.selected.winfo_x()
        y=self.selected.winfo_y()
        w=self.selected.winfo_width()
        h=self.selected.winfo_height()

        self.selection_box.place(x=x-2,y=y-2,width=w+4,height=h+4)

    # PROPERTIES
    def load_props(self, w):
        self.props["name"].set(w._name)
        self.props["x"].set(w.winfo_x())
        self.props["y"].set(w.winfo_y())

        for p in ["text","bg","fg","width","height"]:
            try: self.props[p].set(w[p])
            except: self.props[p].set("")

    def apply(self):
        if not self.selected: return
        w=self.selected

        w._name=self.props["name"].get()

        try: w.place(x=int(self.props["x"].get()), y=int(self.props["y"].get()))
        except: pass

        for p in ["text","bg","fg","width","height"]:
            val=self.props[p].get()
            if val:
                try: w[p]=val
                except: pass

        self.update_tree()
        self.update_selection_box()

    # COLOR PICKER
    def pick_color(self, prop):
        color = colorchooser.askcolor()[1]
        if color and self.selected:
            try:
                self.selected[prop] = color
                self.props[prop].set(color)
            except:
                pass

    # TREE
    def update_tree(self):
        self.tree.delete(0,"end")
        for w in self.widgets:
            self.tree.insert("end",f"{w._name} ({type(w).__name__})")

    # COPY/PASTE
    def serialize(self, w):
        d={"type":type(w).__name__,"x":w.winfo_x(),"y":w.winfo_y(),"name":w._name}
        for p in ["text","bg","fg","width","height"]:
            try: d[p]=w[p]
            except: d[p]=""
        return d

    def deserialize(self, d):
        self.add_widget(d["type"])
        w=self.widgets[-1]
        w.place(x=d["x"],y=d["y"])
        w._name=d["name"]
        for p in ["text","bg","fg","width","height"]:
            try: w[p]=d[p]
            except: pass

    def copy(self):
        if self.selected:
            self.clip=self.serialize(self.selected)

    def paste(self):
        if self.clip:
            self.deserialize(self.clip)

    def delete(self):
        if self.selected:
            self.selected.destroy()
            self.widgets.remove(self.selected)
            self.selected=None
            self.update_tree()
            self.update_selection_box()

    # SAVE/LOAD
    def save(self):
        data=[self.serialize(w) for w in self.widgets]
        f = filedialog.asksaveasfilename(defaultextension=".gui", filetypes=[("GUI files", "*.gui"), ("All files", "*.*")])

        if f: json.dump({"widgets":data,"menus":self.menus},open(f,"w"), indent=4)

        # seperate CODE file
        global CODE_BASE
        base_f = os.path.splitext(f)[0]
        new_f = base_f + ".code"
        if new_f: json.dump(CODE_BASE,open(new_f,"w"), indent=4)

        new_c = base_f + ".cfg"
        save_app_config(new_c)

        
    def load(self):
        f = filedialog.askopenfilename()
        if not f: return
        
        data=json.load(open(f))
        if not data: return
        
        for w in self.widgets: w.destroy()
        self.widgets=[]

        for d in data["widgets"]:
            self.deserialize(d)

        self.menus=data.get("menus",[])
        self.build_menu()
        
        self.update_tree()
        
        # seperate CODE file
        global CODE_BASE
        base_f = os.path.splitext(f)[0]
        new_f = base_f + ".code"
        CODE_BASE = json.load(open(new_f))
        self.functions.delete(0, tk.END)
        for key, value in CODE_BASE.items():
            self.functions.insert(tk.END, key)

        new_c = base_f + ".cfg"
        load_app_config(new_c)


    def new(self):
        result = messagebox.askyesno("Clear all and start New GUI", "Do you want to continue?")
        if result is True:
            for w in self.widgets: w.destroy()
            self.widgets = []
            self.selected = None
            self.update_tree()
            self.update_selection_box()
            self.clip = None
            self.menus = []
            self.build_menu()
            global CODE_BASE, config_filename
            CODE_BASE = {}
            # add init, library, main, pregui, postgui to functions List by adding the items to CODE_BASE
            CODE_BASE["init"] = "# ---- INIT ----\n\n"
            CODE_BASE["library"] = "# ---- LIBRARY ----\n\n" + str(EXT_LIBRARY) + "\n"
            CODE_BASE["main"] = "# ---- MAIN ----\n\n"
            CODE_BASE["pregui"] = "# ---- PRE-GUI ----\n\n"
            CODE_BASE["postgui"] = "# ---- POST-GUI ----\n\n"
            self.functions.delete(0, tk.END)
            for key, value in CODE_BASE.items():
                self.functions.insert(tk.END, key)
            
            # resets all global variables for toplevel title, size_x/y, top_x/y, ect...
            # to the 'current' Main app default.
            load_app_config(os.path.join(".", config_filename))

 



    # ADD MENU
    def add_menu(self):
        dialog_m = focused_dialog("Add Menu Heading", "Menu Heading:")
        while True:
            dialog_input = focused_dialog("Add Menu Item", "Menu Item label:")
            if dialog_input and dialog_input.strip():  # Check if input is not empty
                self.menus.append((dialog_m,dialog_input))
            else:
                break
        
        self.build_menu()


    # BUILD MENU
    def build_menu(self):
        menubar=tk.Menu(self.root)
        menus={}
        
        # build static main app menus - rebuild everytime !
        # --- File MENU---
        RSPYTIGUICFile=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='File',menu=RSPYTIGUICFile)
        RSPYTIGUICFile.add_command(label='New GUI', command=self.new)
        RSPYTIGUICFile.add_command(label='Load GUI Project File', command=self.load)
        RSPYTIGUICFile.add_command(label='Save GUI Project File', command=self.save)
        RSPYTIGUICFile.add_command(label='Export GUI as Python File', command=self.export_py)
        RSPYTIGUICFile.add_command(label='Exit')

        # --- Project MENU---
        RSPYTIGUICProject=tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label='Project Configuration',menu=RSPYTIGUICProject)
        RSPYTIGUICProject.add_command(label='Open Configuration Settings', command=open_configuration_window)
        RSPYTIGUICProject.add_command(label='Save Current Configuration as Default', command=self.save_mainapp_config)


        # build dynamic user menu
        for m,i in self.menus:
            if m not in menus:
                menus[m]=tk.Menu(menubar,tearoff=0)
                menubar.add_cascade(label=m,menu=menus[m])
            menus[m].add_command(label=i)   # File-->Save, m=File, i=Save

        self.root.config(menu=menubar)


#------------------------------------------------------------------------------------------


    # EXPORT
    def export_py(self, output_mode=0):
        # output_mode: 
        # 0 = SaveAs File Dialog
        # 1 = Auto save as 'debug_test.py' in App folder to Launch
        # 2 = Just 'return' the 'code' as 'text'... future?...
    
        global RPYTKGUIC_S_TITLE, RPYTKGUIC_I_X_SIZE, RPYTKGUIC_I_Y_SIZE, RPYTKGUIC_I_AUTOCENTER, RPYTKGUIC_I_TOPX, RPYTKGUIC_I_TOPY, RPYTKGUIC_I_RESIZE
        global RPYTKGUIC_I_SCROLLEDBOXES, RPYTKGUIC_I_AUTOFUNCTIONS

        now = datetime.now()
        
        code=[
            "#",
            "# This Python/Tkinter GUI was built with:",
            "#",
            "# Rocks Python-Tkinter GUI Creator 1v1",
            "#",
            f"# Built on:",
            f'# {now.strftime("%Y-%m-%d %H:%M:%S")}',
            "#",
            ""
        ]

        code.append(f"import tkinter as tk")
        code.append(f"from tkinter import filedialog, simpledialog, colorchooser, messagebox")
        code.append(f"")
        code.append(f"root = tk.Tk()")
        code.append(f"")


        # ---INIT CODE BLOCK---
        if "init" in CODE_BASE:
            content = CODE_BASE.get("init", "")
            if len(content) > 0:
                code.append(f"# ---INIT CODE BLOCK---")
                code.append(content)
                code.append("")
                code.append("")
            else:
                code.append(f"# ---EMPTY INIT CODE BLOCK---")
                code.append("")
                code.append("")
        else:
            code.append(f"# ---NO INIT CODE BLOCK---")
            code.append("")
            code.append("")



        if RPYTKGUIC_I_AUTOCENTER == 1:
        # ---AUTOCENTER WINDOW CODE BLOCK---
            code.append(f"# ---AUTOCENTER WINDOW CODE BLOCK---")
            code.append("")
            code.append(f'def center_window(w):')
            code.append(f'    w.withdraw()')
            code.append(f'    w.update_idletasks()')
            code.append(f'    x = (w.winfo_screenwidth() - w.winfo_width()) // 2')
            code.append(f'    y = (w.winfo_screenheight() - w.winfo_height()) // 2')
            code.append(f'    y = y - 15	# centers it better???? make up for titlebar??? in tkinter, not from tcl/tk')
            code.append("    w.geometry(f'+{x}+{y}')")
            code.append(f'    w.deiconify()')
            code.append("")
            code.append("")




        # ---LIBRARY CODE BLOCK---
        if "library" in CODE_BASE:
            content = CODE_BASE.get("library", "")
            if len(content) > 0:
                code.append(f"# ---LIBRARY CODE BLOCK---")
                code.append(content)
                code.append("")
                code.append("")
        else:
            code.append(f"# ---NO LIBRARY CODE BLOCK---")
            code.append("")
            code.append("")
    


        # ---CUSTOM USER FUNCTIONS CODE BLOCK---    
        code.append(f"# ---CUSTOM USER FUNCTIONS CODE BLOCK---")
        code.append("")
        code.append("")
        # Skipping Hard Coded Built-In Functions
        keys_to_skip = ["init", "library", "main", "pregui", "postgui"]
        # Loop through the Custom User Functions
        for key, value in CODE_BASE.items():
            # Check if the current key is in the list of keys to skip
            if key not in keys_to_skip:
                # Check if the current key is NOT a function for a widget ot menu item
                if not key.startswith('f_') and not key.startswith('m_'):
                    # Print the key and its value
                    # print(f"Key: {key}, Value: {value}")
                    # Export Custom Code Block
                    content = CODE_BASE.get(key, "")
                    if len(content) > 0:
                        code.append(f"# ---{key} CODE BLOCK---")
                        code.append(content)
                        code.append("")
                        code.append("")




        # ---MENU TKVAR() & PYTHON FUNCTION CODE---
        if self.menus:
            # Initialize the previous text variable
            previous_text = ""
            code.append("# --- MENU TKVAR() & PYTHON FUNCTION CODE ---")
            code.append("")
            # Iterate through each sublist in the array
            for sublist in self.menus:
                # Create Menu Item Name
                menuitemname = f"m_{sublist[0]}_{sublist[1]}"
                if menuitemname in CODE_BASE:
                    # Export Custom User Code Block
                    content = CODE_BASE.get(menuitemname, "")
                    if len(content) > 0:
                        code.append("# --- MENU ITEM CUSTOM USER CODE ---")
                        code.append(f"# ---{menuitemname} CODE BLOCK---")
                        code.append(content)
                        code.append("")
                        code.append("")
                    else:
                        # Custom User Code NOT FOUND - Export Auto-Function Code Block
                        if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                            code.append(f"# --- {sublist[0]}_{sublist[1]} MENU COMMAND AUTO-FUNCTION---")
                            code.append(f"def m_{sublist[0]}_{sublist[1]}():")
                            code.append(f'    messagebox.showinfo("Menu Item", "Function: m_{sublist[0]}_{sublist[1]}")')
                            code.append("")
                            code.append("")
                    
                else:        
                    # Export Auto-Function Code Block
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f"# --- {sublist[0]}_{sublist[1]} MENU COMMAND AUTO-FUNCTION---")
                        code.append(f"def m_{sublist[0]}_{sublist[1]}():")
                        code.append(f'    messagebox.showinfo("Menu Item", "Function: m_{sublist[0]}_{sublist[1]}")')
                        code.append("")
                        code.append("")
                
            code.append("")
            code.append("")


        # --- MENU GUI SECTION ---
        if self.menus:
            # ---NEW CODE---
            # Initialize the previous text variable
            previous_text = ""
            code.append("# --- MENU GUI SECTION ---")
            code.append("")
            code.append("menubar=tk.Menu(root)")
            code.append("")
            # Iterate through each sublist in the array
            for sublist in self.menus:
                # Check if the current first element is different from the previous text
                if sublist[0] != previous_text:
                    # Update the previous_text variable to the current first element
                    previous_text = sublist[0]
                    # Execute one line of code (placeholder: print a message)
                    code.append(f"# --- {sublist[0]} MENU---")
                    code.append(f"{sublist[0]}=tk.Menu(menubar,tearoff=0)")
                    code.append(f"menubar.add_cascade(label='{sublist[0]}',menu={sublist[0]})")
                
                menuname_text = f"m_{sublist[0]}_{sublist[1]}"
                if RPYTKGUIC_I_AUTOFUNCTIONS > 0 or len(CODE_BASE.get(menuname_text, "")) > 0: 
                    code.append(f"{sublist[0]}.add_command(label='{sublist[1]}', command=m_{sublist[0]}_{sublist[1]})")
                else:
                    code.append(f"{sublist[0]}.add_command(label='{sublist[1]}')")
                
            code.append("")
            code.append("root.config(menu=menubar)")
            code.append("")
            
            
            
        #WIDGETS TKVAR() & PYTHON FUNCTION CODE---------  
        code.append("")
        code.append("# --- WIDGETS TKVAR() & PYTHON FUNCTION CODE ---")
        code.append("")
        
        # Loops through widgets
        for w in self.widgets:
            n=w._name
            t=type(w).__name__ 
            x,y=w.winfo_x(),w.winfo_y()
            f = f"f_{n}"
            if t=="Label": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Label Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f"# Function f_{n}() for Label Widget: {n} - (bind)")
                        code.append(f"def f_{n}(event):")
                        code.append(f'    messagebox.showinfo("Label Widget: {n}", "Function: f_{n}")')
                        code.append(f"    # event.widget gives the specific label that was clicked")
                        code.append(f"    text_value = event.widget.cget('text')")
                        code.append(f'    messagebox.showinfo("Label Widget: w0", f"Label Text: " + text_value)')
                        code.append(f"    return")
                        code.append("")
                        code.append("")
                
                
            elif t=="Text": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Text Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f'# Function f_{n}() for Text Widget: {n} - (bind)')
                        code.append(f'# EXAMPLE FUNCTION simply clears Text Widget and set the contents')
                        code.append(f'def f_{n}(w):')
                        code.append(f'    {n}.delete(1.0, tk.END)    # Clear the Text widget')
                        code.append(f'    {n}.insert(tk.END, "Hello World !")    # Insert new text')
                        code.append(f'    messagebox.showinfo("Text Widget: {n}", "Function: f_{n}")    # Alert User of Click')
                        code.append(f"    return")
                        code.append("")
                
            elif t=="Button": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Button Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f"# Function f_{n}() for Button Widget: {n} - (command)")
                        code.append(f"def f_{n}():")
                        code.append(f'    messagebox.showinfo("Button Widget: {n}", "Function: f_{n}")')
                        code.append(f"    return")
                        code.append("")
 
                
            elif t=="Checkbutton": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Checkbutton Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f"# Function f_{n}() for Checkbutton Widget: {n} - (command)")
                        code.append(f"def f_{n}():")
                        code.append(f"    if {n}_var.get() == 1:")
                        code.append(f'        messagebox.showinfo("Checkbutton Widget: {n}", "Checkbutton is checked.")')
                        code.append(f"    else:")
                        code.append(f'        messagebox.showinfo("Checkbutton Widget: {n}", "Checkbutton is unchecked.")')
                        code.append(f"    return")
                        code.append("")
                
            elif t=="Listbox": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Listbox Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f'# Function f_{n}() for Listbox Widget: {n} - (bind)')
                        code.append(f'def f_{n}(event):')
                        code.append(f'    # Get the selected Listbox item value')
                        code.append(f'    selection = event.widget.curselection()')
                        code.append(f'    selected_item = event.widget.get(selection) if selection else ""')
                        code.append(f'    if selected_item:')
                        code.append(f'        messagebox.showinfo("Listbox Widget: {n}", "Function: f_{n} Selected list item: " + selected_item)')
                        code.append(f"    else:")
                        code.append(f'        messagebox.showinfo("Listbox Widget: {n}", "Function: f_{n} No Item Selected.")')
                        code.append(f'')
                        code.append(f'    return')
                        code.append('')
                
            elif t=="Entry": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Entry Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f"# Function f_{n}() for Entry Widget: {n} - (bind)")
                        code.append(f"def f_{n}(event):")
                        code.append(f"    entry_text = {n}.get()")
                        code.append(f'    messagebox.showinfo("Entry Widget: {n}", f"Function: f_{n} Entry Text: " + entry_text)')
                        code.append(f"    return")
                        code.append("")
                
            elif t=="Spinbox": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Spinbox Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f"# Function f_{n}() for Spinbox Widget: {n} - (command)")
                        code.append(f"def f_{n}():")
                        code.append(f"    {n}_var = {n}.get()")
                        code.append(f'    messagebox.showinfo("Spinbox Widget: {n}", "Function: f_{n} Value: " + {n}_var)')
                        code.append(f"    return")
                        code.append("")
                
            elif t=="Scale": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Scale Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f"# Function f_{n}() for Scale Widget: {n} - (bind)")
                        code.append(f"def f_{n}(val):")
                        code.append(f"    tmpval = {n}.get()")
                        code.append(f'    messagebox.showinfo("Scale Widget: {n}", "Function: f_{n} Value: \" + str(tmpval))')
                        code.append(f"    return")
                        code.append("")

            elif t=="Canvas": 
                content = CODE_BASE.get(f, "")
                if len(content) > 0:
                    code.append(f"# Function f_{n}() for Canvas Widget: {n}")
                    code.append(content)
                    code.append("")
                else:
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0:
                        code.append(f"# Function f_{n}() for Canvas Widget: {n} - (bind)")
                        code.append(f"def f_{n}(event):")
                        code.append(f'    messagebox.showinfo("Canvas Widget: {n}", "Function: f_{n}")')
                        code.append(f"    # event.x and event.y give you the exact pixel coordinates of the click")
                        code.append(f"    x_pos = event.x")
                        code.append(f"    y_pos = event.y")
                        code.append(f'    messagebox.showinfo("Canvas Widget: {n}", "Canvas clicked at pixel: X=" + str(x_pos) + ", Y=" + str(y_pos))')
                        code.append(f"    return")
                        code.append("")


        
        # ---MAIN CODE BLOCK---
        if "main" in CODE_BASE:
            content = CODE_BASE.get("main", "")
            if len(content) > 0:
                code.append(f"# ---MAIN CODE BLOCK---")
                code.append(content)
                code.append("")
                code.append("")
        else:
            code.append(f"# ---NO MAIN CODE BLOCK---")
            code.append("")
            code.append("")



        # ---PREGUI CODE BLOCK---
        if "pregui" in CODE_BASE:
            content = CODE_BASE.get("pregui", "")
            if len(content) > 0:
                code.append(f"# ---PREGUI CODE BLOCK---")
                code.append(content)
                code.append("")
                code.append("")
        else:
            code.append(f"# ---NO PREGUI CODE BLOCK---")
            code.append("")
            code.append("")
            

            
       #---------WIDGETS GUI CODE---------           
        code.append("")
        code.append("# --- WIDGETS GUI CODE ---")
        code.append("")

        # Loops through widgets
        for w in self.widgets:
            n=w._name
            t=type(w).__name__
            x,y=w.winfo_x(),w.winfo_y()
            try: mybg=w["bg"]
            except: pass
            try: myfg=w["fg"]
            except: pass
            # Force an update to calculate actual dimensions
            self.root.update() 
            # Get the actual pixel width and height of the widget
            mywidth = w.winfo_width()
            myheight = w.winfo_height()
            try: width=w["width"]
            except: pass
            try: height=w["height"]
            except: pass
            
                
            if t=="Label": 
                code.append(f"{n}=tk.Label(root,text='{w['text']}', fg='{myfg}',bg='{mybg}')")

                code.append(f"{n}.place(x={x},y={y},width={mywidth},height={myheight})")
                if RPYTKGUIC_I_AUTOFUNCTIONS > 0: code.append(f'{n}.bind("<Button-1>", f_{n})')	# has no command, so we bind
                code.append("")
                
                
                
            elif t=="Text": 
                if RPYTKGUIC_I_SCROLLEDBOXES > 0:
                    code.append(f'frame_{n} = tk.Frame(root)')
                    code.append(f'frame_{n}.place(x={x},y={y},width={mywidth},height={myheight})')
                    code.append(f'')
                    code.append(f'v_scroll_{n} = tk.Scrollbar(frame_{n}, orient=tk.VERTICAL)')
                    code.append(f'h_scroll_{n} = tk.Scrollbar(frame_{n}, orient=tk.HORIZONTAL)')
                    code.append(f'')
                    code.append(f'{n}=tk.Text(frame_{n}, wrap="none", xscrollcommand=h_scroll_{n}.set, yscrollcommand=v_scroll_{n}.set, fg="{myfg}",bg="{mybg}")')
                    code.append(f'')
                    code.append(f'v_scroll_{n}.config(command={n}.yview)')
                    code.append(f'h_scroll_{n}.config(command={n}.xview)')
                    code.append(f'')
                    code.append(f'v_scroll_{n}.pack(side=tk.RIGHT, fill=tk.Y)')
                    code.append(f'h_scroll_{n}.pack(side=tk.BOTTOM, fill=tk.X)')
                    code.append(f'')
                    code.append(f'{n}.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)')
                    code.append(f'')
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0: code.append(f'{n}.bind("<Button-1>", f_{n})')
                    code.append(f'')
                    code.append(f'')
                else:
                    code.append(f"{n}=tk.Text(root, fg='{myfg}',bg='{mybg}')")

                    code.append(f'{n}.place(x={x},y={y},width={mywidth},height={myheight})')
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0: code.append(f'{n}.bind("<Button-1>", f_{n})')
                    code.append('')

                
            elif t=="Button": 
                if RPYTKGUIC_I_AUTOFUNCTIONS > 0 or len(CODE_BASE.get(f"f_{n}", "")) > 0: 
                    code.append(f"{n}=tk.Button(root,text='{w['text']}', command=f_{n}, fg='{myfg}',bg='{mybg}')")
                else:
                    code.append(f"{n}=tk.Button(root,text='{w['text']}', fg='{myfg}',bg='{mybg}')")
                
                code.append(f'{n}.place(x={x},y={y},width={mywidth},height={myheight})')
                code.append("")

            
                
            elif t=="Checkbutton": 
                code.append(f"{n}_var = tk.IntVar()")
                if RPYTKGUIC_I_AUTOFUNCTIONS > 0 or len(CODE_BASE.get(f"f_{n}", "")) > 0: 
                    code.append(f"{n}=tk.Checkbutton(root,text='{w['text']}', variable={n}_var, command=f_{n}, fg='{myfg}',bg='{mybg}')")
                else:
                    code.append(f"{n}=tk.Checkbutton(root,text='{w['text']}', variable={n}_var, fg='{myfg}',bg='{mybg}')")
                
                code.append(f"{n}.place(x={x},y={y},width={mywidth},height={myheight})")
                code.append("")

                
            elif t=="Listbox": 
                if RPYTKGUIC_I_SCROLLEDBOXES > 0:
                    code.append(f'frame_{n} = tk.Frame(root)')
                    code.append(f'frame_{n}.place(x={x},y={y},width={mywidth},height={myheight})')
                    code.append(f'')
                    code.append(f'v_scroll_{n} = tk.Scrollbar(frame_{n}, orient=tk.VERTICAL)')
                    code.append(f'h_scroll_{n} = tk.Scrollbar(frame_{n}, orient=tk.HORIZONTAL)')
                    code.append(f'')
                    code.append(f'{n}=tk.Listbox(frame_{n}, xscrollcommand=h_scroll_{n}.set, yscrollcommand=v_scroll_{n}.set, fg="{myfg}",bg="{mybg}")')
                    code.append(f'')
                    code.append(f'v_scroll_{n}.config(command={n}.yview)')
                    code.append(f'h_scroll_{n}.config(command={n}.xview)')
                    code.append(f'')
                    code.append(f'v_scroll_{n}.pack(side=tk.RIGHT, fill=tk.Y)')
                    code.append(f'h_scroll_{n}.pack(side=tk.BOTTOM, fill=tk.X)')
                    code.append(f'')
                    code.append(f'{n}.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)')
                    code.append(f'')
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0: code.append(f'{n}.bind("<<ListboxSelect>>", f_{n})')
                    code.append(f'')
                    code.append(f'')
                else: 
                    code.append(f"{n}=tk.Listbox(root, fg='{myfg}',bg='{mybg}',width={width},height={height})")
                    
                    code.append(f"{n}.place(x={x},y={y})")
                    if RPYTKGUIC_I_AUTOFUNCTIONS > 0: code.append(f"{n}.bind('<<ListboxSelect>>', f_{n})")
                    code.append("")	# has no command

                
            elif t=="Entry": 
                code.append(f"{n}=tk.Entry(root, fg='{myfg}',bg='{mybg}')")
                
                code.append(f"{n}.place(x={x},y={y},width={mywidth},height={myheight})")
                if RPYTKGUIC_I_AUTOFUNCTIONS > 0: code.append(f'{n}.bind("<Button-1>", f_{n})')
                code.append("")	# has no command
                
            elif t=="Spinbox": 
                if RPYTKGUIC_I_AUTOFUNCTIONS > 0 or len(CODE_BASE.get(f"f_{n}", "")) > 0: 
                    code.append(f"{n}=tk.Spinbox(root, fg='{myfg}',bg='{mybg}',from_=0,to=10, command=f_{n})")
                else:
                    code.append(f"{n}=tk.Spinbox(root, fg='{myfg}',bg='{mybg}',from_=0,to=10)")
                
                code.append(f"{n}.place(x={x},y={y})")
                # code.append(f'# {n}.bind("<ButtonRelease-1>", f_{n})    # bind or command')
                code.append("")
          
            elif t=="Scale": 
                code.append(f"{n}=tk.Scale(root, from_=0, to=100, fg='{myfg}',bg='{mybg}', orient='horizontal')")
                
                code.append(f"{n}.place(x={x},y={y},width={mywidth},height={myheight})")
                if RPYTKGUIC_I_AUTOFUNCTIONS > 0: code.append(f'{n}.bind("<ButtonRelease-1>", f_{n})')
                code.append("")	# has command, but we need to bind it for ONE action per click-release

            elif t=="Canvas": 
                code.append(f"{n}=tk.Canvas(root,bg='{mybg}')")  # no fg (foreground)
                
                code.append(f"{n}.place(x={x},y={y},width={mywidth},height={myheight})")
                if RPYTKGUIC_I_AUTOFUNCTIONS > 0: code.append(f'{n}.bind("<ButtonRelease-1>", f_{n})')
                code.append("")


        # ---POSTGUI CODE BLOCK---
        if "postgui" in CODE_BASE:
            content = CODE_BASE.get("postgui", "")
            if len(content) > 0:
                code.append(f"# ---POSTGUI CODE BLOCK---")
                code.append(content)
                code.append("")
                code.append("")
        else:
            code.append(f"# ---NO POSTGUI CODE BLOCK---")
            code.append("")
            code.append("")



        #-----------------------------------

        if RPYTKGUIC_S_TITLE:
            code.append(f'root.title("{RPYTKGUIC_S_TITLE}")')
        else: 
            code.append(f'root.title("debug_test.py")')
        code.append("")
        
        if RPYTKGUIC_I_AUTOCENTER == 1:
            code.append(f'root.geometry("{RPYTKGUIC_I_X_SIZE}x{RPYTKGUIC_I_Y_SIZE}")')
            code.append(f'center_window(root)')
        else: 
            if RPYTKGUIC_I_TOPX > -1 and RPYTKGUIC_I_TOPY > -1:
                code.append(f'root.geometry("{RPYTKGUIC_I_X_SIZE}x{RPYTKGUIC_I_Y_SIZE}+{RPYTKGUIC_I_TOPX}+{RPYTKGUIC_I_TOPY}")')
            else:    
                code.append(f'root.geometry("{RPYTKGUIC_I_X_SIZE}x{RPYTKGUIC_I_Y_SIZE}")')
        code.append("")
        
        
        if RPYTKGUIC_I_RESIZE == 1:
            code.append(f'root.resizable(True, True)')
        else: 
            code.append(f'root.resizable(False, False)')
        code.append("")


        code.append("root.mainloop()")
        code.append("")


        #-----------end export_py() code generation--------------------
    
    
        # SaveAs File Dialog
        if output_mode == 0:
            f = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("All files", "*.*")])
            if f: open(f,"w").write("\n".join(code))
            
            
        # Auto save as 'debug_test.py' in App folder to Launch    
        if output_mode == 1:
            f = os.path.join(".", "debug_test.py")
            if f: open(f,"w").write("\n".join(code))
            
            
        # Just 'return' the code as 'text'
        if output_mode == 2:
            return ("\n".join(code))


            
 

# -----------------------------------------------------
# GUI end of class 'GuiCreator' for RPyTkGUICreator
# -----------------------------------------------------




#-----------------------------------------------------------------
# GUI start of 'CUSTOM' PyInstaller Section for 'GuiCreator'
#-----------------------------------------------------------------


#-----------------------------------------------------------------
# PyInstaller environment helpers
#-----------------------------------------------------------------

def is_frozen() -> bool:
    return bool(getattr(sys, "frozen", False))


def application_directory() -> Path:
    return Path(sys.executable).resolve().parent


def bundle_directory() -> Path:
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        return Path(meipass).resolve()

    return Path(__file__).resolve().parent


def launcher_executable() -> str:
    if is_frozen():
        return sys.executable

    return sys.executable


#-----------------------------------------------------------------
# Environment preparation
#-----------------------------------------------------------------

def build_child_environment(extra_environment: Optional[dict[str, str]] = None) -> dict[str, str]:
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    if extra_environment:
        env.update(extra_environment)

    return env


#-----------------------------------------------------------------
# Script execution inside current process
#-----------------------------------------------------------------

def execute_script(script_path: str | os.PathLike[str], script_args: Optional[Iterable[str]] = None) -> int:
    script = Path(script_path).expanduser().resolve()

    if not script.exists():
        print(
            f"Launcher error: script does not exist:\n  {script}",
            file=sys.stderr,
        )
        return 2

    if not script.is_file():
        print(
            f"Launcher error: script is not a file:\n  {script}",
            file=sys.stderr,
        )
        return 2

    if script.suffix.lower() != ".py":
        print(
            f"Launcher error: expected a .py file:\n  {script}",
            file=sys.stderr,
        )
        return 2

    args = list(script_args or [])

    old_argv = sys.argv[:]

    try:
        sys.argv = [str(script), *args]
        script_dir = str(script.parent)
        old_sys_path = sys.path[:]

        if script_dir in sys.path:
            sys.path.remove(script_dir)

        sys.path.insert(0, script_dir)

        try:
            runpy.run_path(
                str(script),
                run_name="__main__",
            )

        finally:
            sys.path[:] = old_sys_path

    except SystemExit as exc:
        code = exc.code

        if code is None:
            return 0

        if isinstance(code, bool):
            return int(code)

        if isinstance(code, int):
            return code

        print(str(code), file=sys.stderr)
        return 1

    except KeyboardInterrupt:
        print(
            "\nExternal script interrupted.",
            file=sys.stderr,
        )
        return 130

    except Exception:
        traceback.print_exc(file=sys.stderr)
        return 1

    finally:
        sys.argv[:] = old_argv


#-----------------------------------------------------------------
# Separate-process execution
#-----------------------------------------------------------------

def run_script_subprocess(script_path: str | os.PathLike[str], script_args: Optional[Iterable[str]] = None, *, cwd: str | os.PathLike[str] | None = None, environment: Optional[dict[str, str]] = None, forward_output: bool = True) -> int:
    script = Path(script_path).expanduser().resolve()

    if not script.exists():
        print(
            f"Launcher error: script does not exist:\n  {script}",
            file=sys.stderr,
        )
        return 2

    if not script.is_file():
        print(
            f"Launcher error: script is not a file:\n  {script}",
            file=sys.stderr,
        )
        return 2

    args = list(script_args or [])

    executable = launcher_executable()

    command = [
        executable,
        CHILD_FLAG,
        RUN_SCRIPT_FLAG,
        str(script),
        *args,
    ]

    env = build_child_environment(environment)

    if cwd is None:
        child_cwd = None
    else:
        child_cwd = str(Path(cwd).expanduser().resolve())

    print(
        "Starting external script:",
        file=sys.stderr,
    )
    print(
        "  " + " ".join(_quote_argument(x) for x in command),
        file=sys.stderr,
    )

    try:
        if forward_output:
            return _run_with_forwarded_output(
                command,
                env=env,
                cwd=child_cwd,
            )

        process = subprocess.Popen(
            command,
            cwd=child_cwd,
            env=env,
        )

        return _wait_for_process(process)

    except FileNotFoundError:
        print(
            f"Launcher error: executable could not be started:\n"
            f"  {executable}",
            file=sys.stderr,
        )
        return 2

    except OSError as exc:
        print(
            f"Launcher error starting external script:\n"
            f"  {exc}",
            file=sys.stderr,
        )
        return 2


#-----------------------------------------------------------------
# Output forwarding
#-----------------------------------------------------------------

def _run_with_forwarded_output(command: list[str], *, env: dict[str, str], cwd: Optional[str]) -> int:
    process = subprocess.Popen(
        command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=None,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )

    import threading

    def forward_stream(stream, destination):
        try:
            for line in iter(stream.readline, ""):
                destination.write(line)
                destination.flush()
        finally:
            stream.close()

    stdout_thread = threading.Thread(
        target=forward_stream,
        args=(process.stdout, sys.stdout),
        daemon=True,
    )

    stderr_thread = threading.Thread(
        target=forward_stream,
        args=(process.stderr, sys.stderr),
        daemon=True,
    )

    stdout_thread.start()
    stderr_thread.start()

    return_code = _wait_for_process(process)

    stdout_thread.join()
    stderr_thread.join()

    return return_code


#-----------------------------------------------------------------
# Process waiting / signal handling
#-----------------------------------------------------------------

def _wait_for_process(process: subprocess.Popen) -> int:
    try:
        return process.wait()

    except KeyboardInterrupt:
        print(
            "\nStopping external script...",
            file=sys.stderr,
        )

        try:
            process.terminate()
        except OSError:
            pass

        try:
            return_code = process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print(
                "External script did not terminate; killing it.",
                file=sys.stderr,
            )

            try:
                process.kill()
            except OSError:
                pass

            return_code = process.wait()

        # Ctrl+C.
        if return_code == 0:
            return 130

        return return_code


#-----------------------------------------------------------------
# Command-line quoting
#-----------------------------------------------------------------

def _quote_argument(value: str) -> str:
    value = str(value)

    if not value:
        return '""'

    if any(c in value for c in ' \t"'):
        return '"' + value.replace('"', '\\"') + '"'

    return value


#-----------------------------------------------------------------
# Launcher command-line handling
#-----------------------------------------------------------------

def parse_run_script_command(argv: list[str]):
    try:
        index = argv.index(RUN_SCRIPT_FLAG)
    except ValueError:
        return None

    if index + 1 >= len(argv):
        print(
            "Launcher error: --run-script requires a Python script.",
            file=sys.stderr,
        )
        return ("", [])

    script = argv[index + 1]
    script_args = argv[index + 2:]

    return script, script_args





#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

def main() -> int:
    argv = sys.argv[1:]

    if RUN_SCRIPT_FLAG in argv:

        parsed = parse_run_script_command(argv)

        if parsed is None:
            return 0

        script, script_args = parsed

        if not script:
            return 2

        return execute_script(
            script,
            script_args,
        )

    #-----------------------------------------------------
    # Normal application mode.
    #
    # Replace this section with your actual application startup.
    #-----------------------------------------------------

    print(
        "Normal application arguments:",
        argv,
    )
    


    #--------------------------------------------------------------
    # The real application you see, RPyTkGUICreator, starts here.
    #--------------------------------------------------------------
    
    
    #-----------------------------------------------------
    # GUI start of MainApp 'RPyTkGUICreator'
    #-----------------------------------------------------

    # create toplevel
    root = tk.Tk()

    # create GuiCreator class for RPyTkGUICreator
    guicreator = GuiCreator(root)

    # resize toplevel
    root.geometry("700x650")

    # Center the toplevel
    center_window(root)

    # Create the 'static' menu for Rocks Python/Tkinter GUI Creator
    guicreator.build_menu()

    # add init, main, pregui, postgui to functions List
    # by adding the items to CODE_BASE
    # same is done in: self.new()
    global CODE_BASE, EXT_LIBRARY
    CODE_BASE = {}
    CODE_BASE["init"] = "# ---- INIT ----\n\n"
    CODE_BASE["library"] = "# ---- LIBRARY ----\n\n" + str(EXT_LIBRARY) + "\n"
    CODE_BASE["main"] = "# ---- MAIN ----\n\n"
    CODE_BASE["pregui"] = "# ---- PRE-GUI ----\n\n"
    CODE_BASE["postgui"] = "# ---- POST-GUI ----\n\n"
    guicreator.functions.delete(0, tk.END)
    for key, value in CODE_BASE.items():
        guicreator.functions.insert(tk.END, key)



    # Load the favicon dynamically
    root.iconbitmap(get_asset_path("favicon.ico")) 


    # run forever - capture events
    root.mainloop()
    
    

    #-----------------------------------------------------
    # GUI end of MainApp 'RPyTkGUICreator'
    #-----------------------------------------------------

    

    return 0


#-----------------------------------------------------------------
# Entry point
#-----------------------------------------------------------------

if __name__ == "__main__":
    sys.exit(main())
    


#-----------------------------------------------------------------
# GUI end of 'CUSTOM' PyInstaller Section for 'GuiCreator'
#-----------------------------------------------------------------
    
#-----------------------------------------------------------------
# EOF
#-----------------------------------------------------------------



    