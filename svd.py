from tkinter import Tk
from tkinter.filedialog import askopenfilename

def get_file():
    # Open file explorer and return found filename
    Tk().withdraw()
    return askopenfilename()
print(get_file())