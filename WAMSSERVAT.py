import os
from tkinter import *
import tkinter.messagebox
import platform
import sys

class Setup:
    def __init__(self):
        self.errors = []
        self.folder_req = {'files': False, 'file_managers': False, 'runners': False, 'help_folder': False}
        self.files_req = {'files\\': False, 'help_folder\\index.html': False, 'help_folder\\stylesheet.css': False,
                     'file_managers\\file_maker|exe.WAMSbin': False, 'wams_file_maker_logo_icon.ico': False,
                          'runners\\file_maker_runner|vbs.WAMSbin':False}

        self.files_samps = {'batchmain|exe.WAMSbin': False, 'batchmain_icon.ico': False, 'command_insert.py': False,
                            'gobrand': False, 'globuser': False, 'batchmain_runner|vbs.WAMSbin':False}

    def check_matrix(self):
        self.folder_check()
        self.file_check()
        self.platform_check()

    def folder_check(self):

        for x in os.listdir(os.getcwd()):
            for y in self.folder_req:
                if y == x:
                    self.folder_req[y] = True

        for x in self.folder_req:
            if not self.folder_req[x]:
                self.errors.append(x)

        if len(self.errors) != 0:
            self.error_handler(folder_error=True)

    def file_check(self):
        for x in self.files_req:
            if x == 'files':
                for y in self.files_samps:
                    for z in os.listdir('files'):
                        if z == y:
                            self.files_samps[y] = True

                    if not self.files_samps[y]:
                        self.errors.append(y)

            elif os.path.exists(x):
                self.files_req[x] = True
            else:
                self.file_errors.append(x)

        if len(self.file_errors) != 0:
            self.error_handler(folder_error=False)

    def platform_check(self):
        if platform.system() != 'Windows':
            tkinter.messagebox.showerror('Platform Error',
                                         'You are running a system that does not support batch scripts. WAMS will be unable to run due to this purpose.')
            delete_all = tkinter.messagebox.askyesno('Delete WAMS?', 'Do you want to remove WAMS from your computer?')
            if delete_all == 'yes':

                folder_remove = {'files':['\\batchmain|exe.WAMSbin', '\\batchmain_icon.ico', '\\command_insert.py', '\\gobrand', '\\globuser',
                                          '\\batchmain_runner|vbs.WAMSbin'],
                                 'file_managers':['\\wams_file_maker_logo_icon.ico', '\\file_maker|exe.WAMSbin'],
                                 'runners':['\\file_maker_runner|vbs.WAMSbin'], 'help_folder':['\\index.html', '\\stylesheet.css']}
                for x in folder_remove:
                    for y in folder_remove[x]:
                        os.system('del /Q \"' + x + y + '\"')

                    os.system('RD /Q /S \"' + x + '\"')

                tkinter.messagebox.showinfo('WAMS has been Removed', 'WAMS has finished being uninstalled.')
                os.system('del {0}\\WAMSSERVAT.exe'.format(os.getcwd()))


            sys.exit()

    def error_handler(self, folder_error):

        if folder_error:
            tkinter.messagebox.showerror('Folders not Found','WAMSSERVAT.exe could not find these folders. Move these folders into the same directory as WAMSSERRVAT.exe')
            for x in self.errors:
                tkinter.messagebox.showerror('Folder not Found', 'Move this folder to the same directory as WAMSSERVAT.exe: ' + x)

        else:
            tkinter.messagebox.showerror('File Not Found','WAMS could not find these files. To fix this move these files into their required directories as displayed by the WAMS manual.')
            for x in self.file_errors:
                tkinter.messagebox.showerror('File Not Found', 'The file: {0} could not be found'.format(x))
        sys.exit()


class Assist(Setup):
    def __init__(self):
        self.int_path = 'C:\\Users\\{0}\\WAMS\\'.format(os.environ['USERNAME'])
        self.new_win = Tk()
        self.new_win.configure(background="orange")
        self.new_win.maxsize(400,500)
        self.new_win.minsize(400,500)
        self.new_win.title('WAMS Startup')
        self.file_log = Listbox(height=30, width=50)
        self.file_log.pack(pady=10)

        tkinter.messagebox.showinfo('Loading', 'Wait while WAMS checks and loads all the necessary files')

        if os.path.exists(self.int_path[:-1]):
            check = {'samples':False, 'help':False, 'projects':False, 'file_maker.exe':False, 'icon':False, 'file_maker_runner.vbs':False}

            for x in os.listdir(self.int_path[:-1]):
                if x == 'samples':
                    self.file_log.insert(END, 'samples has been found')
                    check['samples'] = True
                elif x == 'help':
                    self.file_log.insert(END, 'help has been found')
                    check['help'] = True
                elif x == 'projects':
                    self.file_log.insert(END, 'projects has been found')
                    check['projects'] = True
                elif x == 'file_maker.exe':
                    self.file_log.insert(END, 'file_maker.exe has been found')
                    check['file_maker.exe'] = True
                elif x == 'icon':
                    check['icon'] = True
                elif x == 'file_maker_runner.vbs':
                    check['file_maker_runner.vbs'] = True

            if not check['samples']:
                self.sample_config()

            if not check['help']:
                self.help_config()

            if not check['projects']:
                self.projects_config()

            if not check['file_maker.exe']:
                self.file_maker_config()

            if not check['icon']:
                self.icon_config()

            if not check['file_maker_runner.vbs']:
                self.file_maker_runner_config()

        else:
            os.mkdir(self.int_path[:-1])
            self.file_log.insert(END, 'The WAMS folder has been successfully created')
            self.sample_config()
            self.help_config()
            self.projects_config()
            self.file_maker_config()
            self.icon_config()
            self.file_maker_runner_config()

        if os.path.exists('WAMS & exe.WAMSbin'):
            self.WAMS_maker_exe()

        self.WAMSSERVAT_cleanup()
        self.file_log.insert(END, 'Complete!')
        tkinter.messagebox.showinfo('Complete', 'WAMS has finished setup.')



        os.startfile('WAMS.exe')
        os.system('del \"{0}\\WAMSSERVAT.exe\"'.format(os.getcwd()))
        sys.exit()

    def WAMS_maker_exe(self):
        with open('WAMS & exe.WAMSbin', 'rb')as WAMS:
            cbin = WAMS.readlines()
            WAMS.close()

        with open('WAMS.exe', 'wb')as WAMS:
            WAMS.writelines(cbin)
            WAMS.close()

    def WAMSSERVAT_cleanup(self):
        os.mkdir(self.int_path + 'WAMS_diagnose')

        file_cleanup = {'files':['\\batchmain & exe.WAMSbin', '\\batchmain_icon.ico', '\\command_insert.py', '\\globrand', '\\globuser',
                                          '\\batchmain_runner & vbs.WAMSbin'],
                                 'file_managers':['\\wams_file_maker_logo_icon.ico', '\\file_maker & exe.WAMSbin'],
                                 'runners':['\\file_maker_runner & vbs.WAMSbin'], 'help_folder':['\\index.html', '\\stylesheetWAMS.css'],
                        'WAMSSERVAT.exe':[], 'proico_n.ico':[], 'WAMS & exe.WAMSbin':[]}
        for x in file_cleanup:

            if len(file_cleanup[x]) != 0:
                os.mkdir(self.int_path + 'WAMS_diagnose\\' + x)
                for y in file_cleanup[x]:
                    with open(x + y, 'rb')as file_m:
                        cbin = file_m.readlines()
                        file_m.close()
                    with open(self.int_path + 'WAMS_diagnose\\' + x + y, 'wb')as file_m:
                        file_m.writelines(cbin)
                        file_m.close()
                    os.system('del /Q \"' + x + y + '\"')
            else:
                os.system('copy \"' + x + '\" \"{0}WAMS_diagnose\\{1}\"'.format(self.int_path, x))
                if x != 'WAMSSERVAT.exe':
                    os.system('del \"' + x + '\"')

            os.system('RD /S /Q \"' + x + '\"')

        if os.path.exists('WAMS & exe.WAMSbin'):
            os.remove('WAMS & exe.WAMSbin')

    def sample_config(self):
        os.mkdir(self.int_path + 'samples')
        for x in os.listdir('files'):
            file_extension = None
            icon = False
            with open('files\\' + x, 'rb')as cbin:
                _chin = cbin.readlines()
                cbin.close()
                # Files that will be included in samples: batchmain command_insert batchmain_icon.ico globuser globrand batchmain_runner.vbs
                if '.ico' in x or x.startswith('glob') or x.endswith('.py'):
                    file_name = x
                    icon = True

                if not icon:
                    metadata = x.split('&', 2)

                    file_name = metadata[0][:-1] + '.' + metadata[1][1:-8]

                with open('C:\\Users\\{0}\\WAMS\\samples\\'.format(os.environ['USERNAME']) + file_name, 'wb')as cop:
                    cop.writelines(_chin)
                    cop.close()

                self.file_log.insert(END, 'WAMS has copied  {0} to the samples folder'.format(x))

    def help_config(self):
        os.mkdir(self.int_path + 'help')
        err = False

        with open('help_folder\\index.html', 'rb')as helpcop:
            cbin = helpcop.readlines()
            helpcop.close()

        with open('help_folder\\stylesheetWAMS.css', 'rb')as helpcop:
            _cbin = helpcop.readlines()
            helpcop.close()

        try:
            with open(self.int_path + 'help\\index.html', 'wb')as fincop:
                fincop.writelines(cbin)
                fincop.close()

            with open(self.int_path + 'help\\stylesheetWAMS.css', 'wb')as fincop:
                fincop.writelines(_cbin)
                fincop.close()
        except PermissionError:
            self.file_log.insert(END, 'ERROR: The copying of the help files could not be completed due to a permission error! To fix this try running WAMS again in administrator mode')
            self.new_win.configure(background='red')
            tkinter.messagebox.showerror('Permission Error', 'The help files could not be copied due to a permission error! Try restarting WAMS in admin mode.')
            err = True

        if not err:
            self.file_log.insert(END, 'The help folder has been successfully created')

    def projects_config(self):
        err = False
        os.mkdir(self.int_path + 'projects')
        self.file_log.insert(END, 'The projects folder has been successfully created')

    def file_maker_config(self):
        err = False
        with open('file_managers\\file_maker & exe.WAMSbin', 'rb')as file_m:
            cbin = file_m.readlines()
            file_m.close()

        with open('file_managers\\wams_file_maker_logo_icon.ico', 'rb')as icc:
            ib = icc.readlines()
            icc.close()

        try:
            with open(self.int_path + 'file_maker.exe', 'wb')as file_m:
                file_m.writelines(cbin)
                file_m.close()

            with open(self.int_path + 'wams_file_maker_logo_icon.ico', 'wb')as iw:
                iw.writelines(ib)
                iw.close()
        except PermissionError:
            self.file_log.insert(END, 'ERROR: file_maker.exe, or its icon could not be copied due to a permission error! To fix this try running WAMS again in administrator mode')
            self.new_win.configure(background='red')
            err = True

        if not err:
            self.file_log.insert(END, 'file_maker.exe has been successfully copied')

    def icon_config(self):
        os.mkdir(self.int_path + 'icon')
        with open('proico_n.ico', 'rb')as logo:
            icb = logo.readlines()
            logo.close()

        with open(self.int_path + 'icon\\proico_n.ico', 'wb')as logcop:
            logcop.writelines(icb)
            logcop.close()
        self.file_log.insert(END, 'Icon copied')

    def file_maker_runner_config(self):
        with open('runners\\' + 'file_maker_runner & vbs.WAMSbin', 'rb')as runner:
            run = runner.readlines()
            runner.close()
        with open(self.int_path + 'file_maker_runner.vbs', 'wb')as runner:
            runner.writelines(run)
            runner.close()
        self.file_log.insert(END, 'Successfully copied file_maker_runner.vbs')


setup_config = Setup()
testing = Assist()
