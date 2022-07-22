from cProfile import run
from turtle import title, width
from file_sorter import sorter
from tkinter import (
    E,
    Tk,
    Label,
    messagebox,
    Button,
    Listbox,
    Entry,
    Frame,
)
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askdirectory


root = Tk()
root.title("File Sorter")
root.configure(bg="light blue")
# change the root size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 550
height = 100
align_window = f"{width}x{height}+{(screen_width-width)//2}+{(screen_height-height)//2}"
root.geometry(align_window)

folder_path = ""


def clear_entry():
    input_area.delete(0, "end")


def set_path(path):
    clear_entry()
    input_area.insert(0, path)


def choose_folder():
    global folder_path
    folder_path = askdirectory()
    set_path(folder_path)


def run_sorter():
    path = input_area.get()
    try:
        sorter(path)
    except PermissionError as e:
        showerror(title="Error", message=str(e))
    except OSError:
        showerror(title="Error", message="Folder not selected")
    else:
        showinfo(title="Files Moved", message="Files Moved Successfully")


input_area = Entry(root, width=60)
input_button = Button(
    root, text="Select Folder", relief="raised", command=choose_folder
)
run_button = Button(
    root, text="Sort Folder", relief="raised", width=40, command=run_sorter
)

input_area.pack(side="left", padx=2)
input_button.pack(side="left", padx=5)
run_button.pack(side="right", padx=5)

root.resizable(False, False)
root.mainloop()
