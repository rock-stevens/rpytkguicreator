This folder contains an example GUI created with Rocks Python-Tkinter GUI Creator 1v1.

It is the GUI for the 'Project Configuration' dialog box for Rocks Python-Tkinter GUI Creator 1v1.

Very little was done to incorporate it into the app.

I didn't even export it !!


I created it, hit 'Launch' once. No errors. Open in 'Debug View', copied to another editor I had open.

Pushed all the code over to the right one indention and added the 'def open_configuration_window(): ' function name at the top.

(Note: The code editor in RPyTkGUICreator will do the same, indent and un-indent with the TAB and SHIFT+TAB keys)

Changed the first part of code where it creates the 'toplevel' and make sure it is 'modal' by:

1. I renamed the Toplevel being created from 'root' to 'config_win'

2. I added this code right afterwards to make the GUI/Dialog 'modal'

```python

# Force 'config_win' to the front and lock focus
config_win.lift()          # Pulls it to the top
config_win.grab_set()      # Freezes interaction with the root window

```

3. Did a search for 'root' and replaced it with 'config_win', which renames all the 'parent' windows when the widgets are created.


For example this line:

```python

entWinYSize=tk.Entry(root, fg='SystemWindowText',bg='SystemWindow')

```


Which would change to:

```python

entWinYSize=tk.Entry(config_win, fg='SystemWindowText',bg='SystemWindow')

```


4. Added my code to the functions I wanted to, and pretty much done.


5. And I call it from my main application like this:


It's attached to the 'command' on a menu item 'Open Configuration Settings', so the command looks like:

```python

command=open_configuration_window

```

6. Last I made sure any message boxes etc, has the 'parent' property set to the actual new parent, 'config_win'. 


Strange effect if you don't. 


When a message box pops up, and the 'parent' is not set at all, the Main App window comes to the top. Then goes away after you close the message box. 


So I forced the 'parent' window to be 'config_win' instead of defaulting to 'root'.

Like this:


```python

messagebox.showinfo("Title", "Message", parent=config_win)

```


Other than my specific code for the GUI dialog box. That's about it.



