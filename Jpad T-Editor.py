from tkinter import *
from tkinter import ttk,filedialog,Tk,font,colorchooser,messagebox
from PIL import ImageTk,Image
import os,sys
import win32print
import win32api



root = Tk()
root.title("JPad Text Editior")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))

root.iconbitmap("icon.ico")

# Global variable set
global open_status_name
open_status_name = False

global selected
selected = 0

global print_file

print_file = "no"

# New file creation
def new_file():
    # Delete Previous text
    my_text.delete(1.0,END)
    # Update Title and Status bas
    root.title("New File - JPad Text Editior")
    status_bar.config(text="New File        ")

    global open_status_name
    open_status_name = False

# Open file function
def open_file():
    # Delete Previous text

    # Grab filname
    text_file = filedialog.askopenfilename(title="Open File",filetypes=(("Text Files","*.txt"),("HTML File","*.html"),("Python Files","*.py"),("All Files","*-*")))
    # Check to see if there is a file name
    if text_file:
        # Make filname global so we can access it in the program
        global open_status_name
        open_status_name = text_file
    if text_file == "":
        pass
    else:
        my_text.delete(1.0, END)
        name = text_file
        status_bar.config(text=f"{name}        ")
        root.title(f"{name} - JPad Text Editior")

        #Open File
        with open(text_file,'r') as fp:
            # Read the file
            stuff = fp.read()
            # Insert the data
            my_text.insert(END,stuff)


def save_as_file():
    global print_file
    text_file = filedialog.asksaveasfilename(title="Save File",defaultextension=".*",filetypes=(("Text Files","*.txt"),("HTML File","*.html"),("Python Files","*.py"),("All Files","*-*")))

    if text_file:
        name= text_file
        print_file = name
        status_bar.config(text=f"{name}        ")
        root.title(f"{name}- JPad Text Editior")
        with open(name,"w") as fp:
            fp.write(my_text.get(1.0,END))


# Save file
def save_file():
    global open_status_name
    if open_status_name:
        global print_file
        print_file = open_status_name
        with open(open_status_name,"w") as fp:
            fp.write(my_text.get(1.0,END))
            status_bar.config(text=f"{open_status_name}        ")
            root.title(f"{open_status_name}- JPad Text Editior")
    else:
        save_as_file()


# Cut text
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Grap selected text from textbox
            selected = my_text.selection_get()
            #Delete selection
            my_text.delete("sel.first","sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

# Copy
def copy_text(e):
    global selected
    # Chech to see if we used keybord shortcuts
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        # Grab selected
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
# Past
def past_text(e):
    global selected
    # Check to see if keybord shotcut used
    if e:
        selected = root.clipboard_get()
    else:
        position = my_text.index(INSERT)
        my_text.insert(position,selected)

# Bold text
def bolder():
    bold_font = font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight="bold")

    # configure a tag
    my_text.tag_configure("bold",font=bold_font)
    current_tags = my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold","sel.first","sel.last")

    else:
        my_text.tag_add("bold","sel.first","sel.last")

# Italics text
def italics():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    # configure a tag
    my_text.tag_configure("italic", font=italics_font)
    current_tags = my_text.tag_names("sel.first")
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")

    else:
        my_text.tag_add("italic", "sel.first", "sel.last")



# Color text
def text_color():
    # Pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        status_bar.config(text=my_color)

        color_font = font.Font(my_text, my_text.cget("font"))


        # configure a tag
        my_text.tag_configure("colored", font=color_font,foreground=my_color)
        current_tags = my_text.tag_names("sel.first")
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")

        else:
            my_text.tag_add("colored", "sel.first", "sel.last")


# Background color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

# Change all text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)

def print_function():
    global print_file
    if print_file == "no":
        messagebox.showinfo("Wait", "First save the file before print")

    else:
        file_to_print = print_file
        if file_to_print:
            win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)
# Select all text
def select_all(e):
    my_text.tag_add('sel',1.0,'end')

# Clear Text
def clear_all(e):
    my_text.delete(1.0,END)

# # Font size
# def font_size():
#     def size_select():
#         size = window_spine.get()
#         # start_index = my_text.index(SEL_FIRST)
#         # end_index = my_text.index(SEL_LAST)
#         #
#         # my_text.tag_configure("selected",font=("helvetica",size))
#         # my_text.tag_add("selected",start_index,end_index)
#
#         selected_size = window_spine.get()
#         my_text.tag_add("sel","sel.first","sel.last")
#         text_font = font.Font(size=selected_size)
#         my_text.tag_config("sel",font=text_font)
#         window.destroy()
#     window = Toplevel()
#     window.title("Text Size")
#     window.geometry("230x80")
#     window.resizable(False,False)
#     window.iconbitmap("icon.ico")
#     window_label = Label(window,text="Font Size :")
#     window_label.grid(row=0,column=0,pady=10)
#     window_spine = Spinbox(window, from_=1, to=100)
#     window_spine.grid(row=0,column=1,pady=10)
#     window_button = Button(window, text="Select",command=size_select)
#     window_button.grid(row=1,column=1,columnspan=2)

# About funtion
def about_function():
    win = Toplevel()
    win.title("About")
    win.geometry("230x120")
    win.resizable(False,False)
    win.iconbitmap("icon.ico")
    win_label = Label(win,text="J-Tech Software Development \nCompany\nFounder : Shaikh Akram\nContact : 9890873444",font=("Helvetica",10))
    win_label.grid(row=0,column=1,pady=5)
    win_button = Button(win, text="Ok",command=win.destroy,width=8)
    win_button.grid(row=1,column=1,columnspan=2)

# Closing the window
def on_closing():
    answer = messagebox.askyesnocancel("Save","Do you want save file before exiting?")
    if answer is None:
        return
    elif answer:
        save_file()
    root.destroy()
# Create tool bar
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Status bar to bottom
status_bar = Label(root, text="Ready          ",anchor=E,)
status_bar.pack(fill=X,side=BOTTOM,ipady=3)

# Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scroll bar for text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

# Scroll bar Horizontal
hor_scroll = Scrollbar(my_frame,orient=HORIZONTAL)
hor_scroll.pack(side=BOTTOM,fill=X)

# Create text box
my_text = Text(my_frame,width=121,height=30,font=("Helvetica",13),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)

my_text.pack()

# configer our scorllbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)


# Menu bar
my_menu = Menu(root)
root.config(menu=my_menu)

# Add file menu

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New          ",command=new_file)
file_menu.add_command(label="Open         ",command=open_file)
file_menu.add_command(label="Save         ",command=save_file)
file_menu.add_command(label="Save As      ",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Edit menu
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut     ",command=lambda : cut_text(False),accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy    ",command=lambda : copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label="Past    ",command=lambda : past_text(False),accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo    ",command=my_text.edit_undo,accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo    ",command=my_text.edit_redo,accelerator="(Ctrl+x)")
edit_menu.add_command(label="Select All    ",command=lambda: select_all(True),accelerator="(Ctrl+a)")
edit_menu.add_command(label="Clear    ",command=lambda: clear_all(True),accelerator="(Ctrl+y)")


# Print menu
print_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Print",menu=print_menu)
print_menu.add_command(label="Print          ",command=print_function)


# Format menu
format_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Format",menu=format_menu)
format_menu.add_command(label="Bold           ",command=bolder)
format_menu.add_command(label="Italics        ",command=italics)
format_menu.add_separator()
# format_menu.add_command(label="Font-Size        ",command=font_size)



# Color menu
color_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Colors",menu=color_menu)
color_menu.add_command(label="Change Selected Text ",command=text_color)
color_menu.add_separator()
color_menu.add_command(label="All Text             ",command=all_text_color)
color_menu.add_command(label="Background color     ",command=bg_color)

# Edit menu
about_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="About",menu=about_menu)
about_menu.add_command(label="Info    ",command=about_function)

# Edit bindings
root.bind("<Control-Key-x>",cut_text)
root.bind("<Control-Key-c>",copy_text)
root.bind("<Control-Key-v>",past_text)

# Binding the function
root.bind("<Control-A>",select_all)
root.bind("<Control-Y>",clear_all)


# Bold Button
bold_image = ImageTk.PhotoImage(Image.open("bold.png"))
bold_button = Button(toolbar_frame, image=bold_image,compound=CENTER,command=bolder)
bold_button.grid(row=0,column=0,sticky=W,padx=5)

# Italics button
italics_image = ImageTk.PhotoImage(Image.open("italics.png"))
italics_button = Button(toolbar_frame, image=italics_image,compound=CENTER,command=italics)
italics_button.grid(row=0,column=1,padx=5)

# Undo button
undo_image = ImageTk.PhotoImage(Image.open("undo.png"))
undo_button = Button(toolbar_frame, image=undo_image,compound=CENTER,command=my_text.edit_undo)
undo_button.grid(row=0,column=2,padx=5)


# redo button
redo_image = ImageTk.PhotoImage(Image.open("redo.png"))
redo_button = Button(toolbar_frame,image=redo_image,compound=CENTER,command=my_text.edit_redo)
redo_button.grid(row=0,column=3,padx=5)

# Color button
color_image = ImageTk.PhotoImage(Image.open("color.png"))
color_button = Button(toolbar_frame,image=color_image,compound=CENTER,command=text_color)
color_button.grid(row=0,column=4,padx=5)

# Print button
print_image = ImageTk.PhotoImage(Image.open("print.png"))
print_button = Button(toolbar_frame, image=print_image,compound=CENTER,command=print_function)
print_button.grid(row=0,column=5,padx=5)

# Font Size
# size_image = ImageTk.PhotoImage(Image.open("fontsize.png"))
# size_button = Button(toolbar_frame, image=size_image,compound=CENTER,command=font_size)
# size_button.grid(row=0,column=6,padx=5)

root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()