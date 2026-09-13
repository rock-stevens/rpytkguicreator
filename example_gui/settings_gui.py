#
# This Python/Tkinter GUI was built with:
#
# Rocks Python-Tkinter GUI Creator 1v1
#
# Built on:
# 2026-09-10 09:33:37
#

import tkinter as tk
from tkinter import filedialog, simpledialog, colorchooser, messagebox

root = tk.Tk()

# ---INIT CODE BLOCK---
# ---- INIT ----




# ---AUTOCENTER WINDOW CODE BLOCK---

def center_window(w):
    w.withdraw()
    w.update_idletasks()
    x = (w.winfo_screenwidth() - w.winfo_width()) // 2
    y = (w.winfo_screenheight() - w.winfo_height()) // 2
    y = y - 15	# centers it better???? make up for titlebar??? in tkinter, not from tcl/tk
    w.geometry(f'+{x}+{y}')
    w.deiconify()


# ---NO LIBRARY CODE BLOCK---


# ---CUSTOM USER FUNCTIONS CODE BLOCK---



# --- WIDGETS TKVAR() & PYTHON FUNCTION CODE ---



    # Function f_entTitle() for Entry Widget: entTitle - (bind)
    def f_entTitle(event):
        entry_text = entTitle.get()
        messagebox.showinfo("Entry Widget: entTitle", f"Function: f_entTitle Entry Text: " + entry_text)
        return


    # Function f_entWinXSize() for Entry Widget: entWinXSize - (bind)
    def f_entWinXSize(event):
        entry_text = entWinXSize.get()
        messagebox.showinfo("Entry Widget: entWinXSize", f"Function: f_entWinXSize Entry Text: " + entry_text)
        return



    # Function f_entWinYSize() for Entry Widget: entWinYSize - (bind)
    def f_entWinYSize(event):
        entry_text = entWinYSize.get()
        messagebox.showinfo("Entry Widget: entWinYSize", f"Function: f_entWinYSize Entry Text: " + entry_text)
        return

    # Function f_chkAutoCenterWin() for Checkbutton Widget: chkAutoCenterWin - (command)
    def f_chkAutoCenterWin():
        if chkAutoCenterWin_var.get() == 1:
            messagebox.showinfo("Checkbutton Widget: chkAutoCenterWin", "Checkbutton is checked.")
        else:
            messagebox.showinfo("Checkbutton Widget: chkAutoCenterWin", "Checkbutton is unchecked.")
        return




    # Function f_entTopXPos() for Entry Widget: entTopXPos - (bind)
    def f_entTopXPos(event):
        entry_text = entTopXPos.get()
        messagebox.showinfo("Entry Widget: entTopXPos", f"Function: f_entTopXPos Entry Text: " + entry_text)
        return

    # Function f_entTopYPos() for Entry Widget: entTopYPos - (bind)
    def f_entTopYPos(event):
        entry_text = entTopYPos.get()
        messagebox.showinfo("Entry Widget: entTopYPos", f"Function: f_entTopYPos Entry Text: " + entry_text)
        return

    # Function f_chkWindowResizable() for Checkbutton Widget: chkWindowResizable - (command)
    def f_chkWindowResizable():
        if chkWindowResizable_var.get() == 1:
            messagebox.showinfo("Checkbutton Widget: chkWindowResizable", "Checkbutton is checked.")
        else:
            messagebox.showinfo("Checkbutton Widget: chkWindowResizable", "Checkbutton is unchecked.")
        return

    # Function f_chkAutoAddScrollBars() for Checkbutton Widget: chkAutoAddScrollBars - (command)
    def f_chkAutoAddScrollBars():
        if chkAutoAddScrollBars_var.get() == 1:
            messagebox.showinfo("Checkbutton Widget: chkAutoAddScrollBars", "Checkbutton is checked.")
        else:
            messagebox.showinfo("Checkbutton Widget: chkAutoAddScrollBars", "Checkbutton is unchecked.")
        return

    # Function f_chkAddAutoFunctions() for Checkbutton Widget: chkAddAutoFunctions - (command)
    def f_chkAddAutoFunctions():
        if chkAddAutoFunctions_var.get() == 1:
            messagebox.showinfo("Checkbutton Widget: chkAddAutoFunctions", "Checkbutton is checked.")
        else:
            messagebox.showinfo("Checkbutton Widget: chkAddAutoFunctions", "Checkbutton is unchecked.")
        return



    # Function f_entGridSize() for Entry Widget: entGridSize - (bind)
    def f_entGridSize(event):
        entry_text = entGridSize.get()
        messagebox.showinfo("Entry Widget: entGridSize", f"Function: f_entGridSize Entry Text: " + entry_text)
        return



    # Function f_entFontSizeButtons() for Entry Widget: entFontSizeButtons - (bind)
    def f_entFontSizeButtons(event):
        entry_text = entFontSizeButtons.get()
        messagebox.showinfo("Entry Widget: entFontSizeButtons", f"Function: f_entFontSizeButtons Entry Text: " + entry_text)
        return



    # Function f_entFontNameEditor() for Entry Widget: entFontNameEditor - (bind)
    def f_entFontNameEditor(event):
        entry_text = entFontNameEditor.get()
        messagebox.showinfo("Entry Widget: entFontNameEditor", f"Function: f_entFontNameEditor Entry Text: " + entry_text)
        return


    # Function f_entFontSizeEditor() for Entry Widget: entFontSizeEditor - (bind)
    def f_entFontSizeEditor(event):
        entry_text = entFontSizeEditor.get()
        messagebox.showinfo("Entry Widget: entFontSizeEditor", f"Function: f_entFontSizeEditor Entry Text: " + entry_text)
        return

    # Function f_btnOk() for Button Widget: btnOk - (command)
    def f_btnOk():
        messagebox.showinfo("Button Widget: btnOk", "Function: f_btnOk")
        return

    # Function f_btnSave() for Button Widget: btnSave - (command)
    def f_btnSave():
        messagebox.showinfo("Button Widget: btnSave", "Function: f_btnSave")
        return

    # Function f_btnCancel() for Button Widget: btnCancel - (command)
    def f_btnCancel():
        messagebox.showinfo("Button Widget: btnCancel", "Function: f_btnCancel")
        return

    # ---MAIN CODE BLOCK---
    # ---- MAIN ----




    # ---PREGUI CODE BLOCK---
    # ---- PRE-GUI ----





    # --- WIDGETS GUI CODE ---

    lblTitle=tk.Label(root,text='Project Window Title', fg='SystemButtonText',bg='SystemButtonFace')
    lblTitle.place(x=11,y=11,width=116,height=21)

    entTitle=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entTitle.place(x=141,y=11,width=304,height=19)
    entTitle.bind("<Button-1>", f_entTitle)

    lblWinXSize=tk.Label(root,text='Project Window X Size', fg='SystemButtonText',bg='SystemButtonFace')
    lblWinXSize.place(x=11,y=41,width=123,height=21)

    entWinXSize=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entWinXSize.place(x=142,y=42,width=64,height=19)
    entWinXSize.bind("<Button-1>", f_entWinXSize)

    lblWinYSize=tk.Label(root,text='Project Window Y Size', fg='SystemButtonText',bg='SystemButtonFace')
    lblWinYSize.place(x=11,y=71,width=123,height=21)

    entWinYSize=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entWinYSize.place(x=142,y=72,width=64,height=19)
    entWinYSize.bind("<Button-1>", f_entWinYSize)

    chkAutoCenterWin_var = tk.IntVar()
    chkAutoCenterWin=tk.Checkbutton(root,text='Auto Center Project Window', variable=chkAutoCenterWin_var, command=f_chkAutoCenterWin, fg='SystemWindowText',bg='SystemButtonFace')
    chkAutoCenterWin.place(x=231,y=41,width=179,height=25)

    lblTopXPos=tk.Label(root,text='Project Top X Position', fg='SystemButtonText',bg='SystemButtonFace')
    lblTopXPos.place(x=11,y=111,width=123,height=21)

    lblTopYPos=tk.Label(root,text='Project Top Y Position', fg='SystemButtonText',bg='SystemButtonFace')
    lblTopYPos.place(x=12,y=142,width=123,height=21)

    entTopXPos=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entTopXPos.place(x=142,y=112,width=64,height=19)
    entTopXPos.bind("<Button-1>", f_entTopXPos)

    entTopYPos=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entTopYPos.place(x=141,y=141,width=64,height=19)
    entTopYPos.bind("<Button-1>", f_entTopYPos)

    chkWindowResizable_var = tk.IntVar()
    chkWindowResizable=tk.Checkbutton(root,text='Project Window Resizable', variable=chkWindowResizable_var, command=f_chkWindowResizable, fg='SystemWindowText',bg='SystemButtonFace')
    chkWindowResizable.place(x=231,y=71,width=163,height=25)

    chkAutoAddScrollBars_var = tk.IntVar()
    chkAutoAddScrollBars=tk.Checkbutton(root,text='Auto Add Scrollbars to Text and Listbox Widgets', variable=chkAutoAddScrollBars_var, command=f_chkAutoAddScrollBars, fg='SystemWindowText',bg='SystemButtonFace')
    chkAutoAddScrollBars.place(x=231,y=111,width=281,height=25)

    chkAddAutoFunctions_var = tk.IntVar()
    chkAddAutoFunctions=tk.Checkbutton(root,text='Automatically Add Placeholder Functions for Widgets', variable=chkAddAutoFunctions_var, command=f_chkAddAutoFunctions, fg='SystemWindowText',bg='SystemButtonFace')
    chkAddAutoFunctions.place(x=231,y=141,width=311,height=25)

    lblSnapToGrid=tk.Label(root,text='Snap To Grid Size', fg='SystemButtonText',bg='SystemButtonFace')
    lblSnapToGrid.place(x=11,y=181,width=97,height=21)

    entGridSize=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entGridSize.place(x=151,y=181,width=64,height=19)
    entGridSize.bind("<Button-1>", f_entGridSize)

    lblFontSizeButtons=tk.Label(root,text='Font and Size Buttons', fg='SystemButtonText',bg='SystemButtonFace')
    lblFontSizeButtons.place(x=12,y=212,width=120,height=21)

    entFontSizeButtons=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entFontSizeButtons.place(x=151,y=211,width=64,height=19)
    entFontSizeButtons.bind("<Button-1>", f_entFontSizeButtons)

    lblFontNameEditor=tk.Label(root,text='Font Name for Editor', fg='SystemButtonText',bg='SystemButtonFace')
    lblFontNameEditor.place(x=11,y=241,width=117,height=21)

    entFontNameEditor=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entFontNameEditor.place(x=151,y=241,width=64,height=19)
    entFontNameEditor.bind("<Button-1>", f_entFontNameEditor)

    lblFontSizeEditor=tk.Label(root,text='Font Size for Editor', fg='SystemButtonText',bg='SystemButtonFace')
    lblFontSizeEditor.place(x=11,y=271,width=105,height=21)

    entFontSizeEditor=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')
    entFontSizeEditor.place(x=151,y=271,width=64,height=19)
    entFontSizeEditor.bind("<Button-1>", f_entFontSizeEditor)

    btnOk=tk.Button(root,text='Ok', command=f_btnOk, fg='SystemButtonText',bg='SystemButtonFace')
    btnOk.place(x=381,y=321,width=66,height=26)

    btnSave=tk.Button(root,text='Save', command=f_btnSave, fg='SystemButtonText',bg='SystemButtonFace')
    btnSave.place(x=241,y=321,width=66,height=26)

    btnCancel=tk.Button(root,text='Cencal', command=f_btnCancel, fg='SystemButtonText',bg='SystemButtonFace')
    btnCancel.place(x=121,y=321,width=66,height=26)

    # ---POSTGUI CODE BLOCK---
    # ---- POST-GUI ----




root.title("Project Configuration - Rocks Python-Tkinter GUI Creator")

root.geometry("550x380")
center_window(root)

root.resizable(True, True)

root.mainloop()
