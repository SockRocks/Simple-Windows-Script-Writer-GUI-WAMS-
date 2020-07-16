import os
import os.path
import sys
import tkinter
from tkinter import messagebox
from tkinter import *


def error_dist(error, file_name):
    if error == FileNotFoundError:
        tkinter.messagebox.showerror('File Not Found',
                                     'WAMS could not find {1}. To fix this ensure that {1} is in the C:\\Users\\{0}\\WAMS directory.'.format(
                                         os.environ['USERNAME'], file_name))
    elif error == 'icon_erorr':
        tkinter.messagebox.showwarning('Icon Not Found', 'The icon could not be found for the WAMS menu file. ')

def mainbatch():
    try:
        os.system('cd C:\\Users\\{0}\\WAMS & start file_maker.exe'.format(os.environ['USERNAME']))
    except FileNotFoundError:
        error_dist(FileNotFoundError, 'file_maker_runner.vbs')
    sys.exit()

def helpbutton():
    try:
        os.startfile('C:\\Users\\{0}\\WAMS\\help\\index.html'.format(os.environ['USERNAME']))
    except FileNotFoundError:
        error_dist(FileNotFoundError, 'index.html')


main = Tk()
main.title('WAMS')

try:
    main.iconbitmap = ('C:\\Users\\{0}\\WAMS\\icon\\proico_n.ico'.format(os.environ['USERNAME']))
except:
    error_dist('icon_error', None)

main.maxsize(100,124)
main.configure(background='darkgreen')
title = Label(main, text='WAMS\n 5.1.1.2', font='Arial 20 bold', fg='lightgreen', bg='darkgreen')
title.pack(side=TOP)
batch = Button(main, text='File Maker', fg='darkgreen', command=mainbatch)
batch.pack(fill=X)
hel = Button(main, text='Help', command=helpbutton, fg='darkgreen')
hel.pack(fill=X)
main.mainloop()
