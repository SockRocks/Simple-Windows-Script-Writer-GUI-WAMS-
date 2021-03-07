import os #Used for file checking and system calls
from sys import exit
### Tkinter Modules ###
import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk



'''Class used for the menu options'''
class menu_options:

    def mainbatch(self):
        '''the cd command must be used because, otherwise, the vbs script will start from the location of this file which will stop the relative
        paths from working'''

        try:
            os.system('cd C:\\Users\\{0}\\WAMS & start file_maker.exe'.format(os.environ['USERNAME']))
        except FileNotFoundError:
            error_dist(FileNotFoundError, 'file_maker_runner.vbs')

    def helpbutton(self):

        try:
            os.startfile('C:\\Users\\{0}\\WAMS\\help\\index.html'.format(os.environ['USERNAME']))
        except FileNotFoundError:
            error_dist(FileNotFoundError, 'index.html')

    def end(self):
        sys.exit()


'''Object used to perform effects on the button'''
#This object is organized using the first e as the <Enter> effect and using e2 as the <Leave> effect
class button_effects:
    def mainb_e(self, a):
        batch.configure(fg='lightgreen')

    def mainb_e2(self, a):
        batch.configure(fg='darkgreen')

    def title_e(self, a):
        title.configure(fg='darkgreen', bg='lightgreen')

    def title_e2(self, a):
        title.configure(fg='lightgreen', bg='darkgreen')

    def help_e(self, a):
        hel.configure(fg='lightgreen')

    def help_e2(self, a):
        hel.configure(fg='darkgreen')

    def quit_e(self, a):
        quik.configure(fg='lightgreen')

    def quit_e2(self, a):
        quik.configure(fg='darkgreen')

'''Error Distribution'''
#This function is used to distribute generic errors to the user
def error_dist(error, file_name):
    if error == FileNotFoundError:
        tkinter.messagebox.showerror('File Not Found', 'WAMS could not find {1}. To fix this ensure that {1} is in the C:\\Users\\{0}\\WAMS directory.'.format(os.environ['USERNAME'], file_name))
    elif error == 'icon_erorr':
        tkinter.messagebox.showwarning('Icon Not Found', 'The icon could not be found for the WAMS menu file. ')


'''Tkinter Window Setup'''
#Initial
main = tk.ThemedTk()
main.get_themes()
main.set_theme('plastik')
main.title('WAMS')
effect = button_effects()
menu_opt = menu_options()
main.configure(background='darkgreen')
main.maxsize(300,300)
main.minsize(300,300)
try:
    main.iconbitmap = ('C:\\Users\\{0}\\WAMS\\icon\\proico_n.ico'.format(os.environ['USERNAME']))
except:
    error_dist('icon_error', None)


title = Label(main, text='WAMS\n 5.3.7.3', font='Arial 20 bold', fg='lightgreen', bg='darkgreen')
title.bind('<Enter>', effect.title_e)
title.bind('<Leave>', effect.title_e2)
title.pack(side=TOP)

batch = Button(main, text='File Maker', fg='lightgreen', command=menu_opt.mainbatch)
batch.bind('<Enter>', effect.mainb_e)
batch.bind('<Leave>', effect.mainb_e2)
batch.pack(fill=X)

hel = Button(main, text='Help', command=menu_opt.helpbutton, fg='lightgreen')
hel.bind('<Enter>', effect.help_e)
hel.bind('<Leave>', effect.help_e2)
hel.pack(fill=X)

quik = Button(main, text='Quit', fg='lightgreen', command=menu_opt.end)
quik.bind('<Enter>', effect.quit_e)
quik.bind('<Leave>', effect.quit_e2)
quik.pack(fill=X)


main.mainloop()
