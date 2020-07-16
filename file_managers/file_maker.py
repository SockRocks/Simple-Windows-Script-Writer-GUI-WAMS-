from tkinter import *
import tkinter.messagebox
import os
import os.path
import tkinter.filedialog

main = Tk()

lis = Listbox(main, height= 10, fg='blue', bg='orange', relief=SUNKEN, highlightthickness=7)
lis.pack(side=TOP, fill=X)
def error_dist(error, other_data):
    if error == 'Invalid Project Name':
        tkinter.messagebox.showerror('Invalid Project Name', 'You cannot name your project a blank name.')
    elif error == 'project_already_exists':
        tkinter.messagebox.showerror('Project already exists', 'Another project shares that name.')
    elif error == 'invalid_path':
        tkinter.messagebox.showerror('Invalid Path', 'You cannot select folders outside of the {0} folder'.format(other_data))
    elif error == 'invalid_filename':
        error_info = 'No data provided'
        if other_data == 1:
            error_info = 'You cannot enter a blank file name.'
        elif other_data == 2:
            error_info = 'A file already exists by that name inside of that project.'
        tkinter.messagebox.showerror('Invalid File Name', error_info)
    elif error == 'file_not_found':
        tkinter.messagebox.showerror('File Not Found', 'file_maker.exe could not find ' + other_data)


class projecr_creation:

    def __init__(self, project_name):
        self.projn = project_name.get()
        if self.projn == '' or self.projn == ' ':
            error_dist('Invalid Project Name', 1)
        exists = False
        for x in os.listdir('projects'):
            if x == self.projn:
                exists = True
        if not exists:
            self.project_maker()
        else:
            error_dist('project_already_exists', None)

    def project_maker(self):
        os.mkdir('projects\\' + self.projn)
        fold = ('commandlog', 'outputs', 'resources', 'resources\\variables', 'packages', 'filehelper')
        for x in fold:
            os.mkdir('projects\\' + self.projn + '\\' + x)
        for x in os.listdir('samples'):
            with open('samples\\' + x, 'rb')as samp_c:
                sbin = samp_c.readlines()
                samp_c.close()
            if x == 'globuser' or x == 'globrand':

                with open('projects\\' + self.projn + '\\resources\\variables\\' + x, 'wb')as variset:
                    variset.writelines(sbin)
                    variset.close()
            else:
                with open('projects\\' + self.projn + '\\' + x, 'wb')as nc:
                    nc.writelines(sbin)
                    nc.close()
        lis.insert(END, self.projn)



class file_maker:
    def __init__(self, filename):
        echo = tkinter.messagebox.askquestion('Echo', 'Show commands on?(This will show all the commands you put in the script in the console. Recomended to be off)')
        self.file_n = filename.get()
        file_n = True
        if self.file_n == '' or self.file_n == ' ':
            error_dist('invalid_filename', 1)
            self.project = 'null'

        else:
            tkinter.messagebox.showinfo('Select a Project', 'Select the project you want to make a new file in.')
            _project = tkinter.filedialog.askdirectory(initialdir='projects'.format(os.environ['USERNAME']), title='Select a project')
            self.project = _project.replace('/', '\\')

        if 'WAMS\\projects' not in self.project or self.file_n == ' ':
            if 'WAMS\\projects' not in self.project and self.project != 'null':
                error_dist('invalid_path', 'projects')
        else:
            exists = False
            for x in os.listdir(self.project + '\\' + 'outputs'):
                if x[:-4] == self.file_n:
                    exists = True
                    error_dist('invalid_filename', 2)

            if not exists:
                for x in os.listdir(self.project + '\\filehelper'):
                    os.remove(self.project + '\\filehelper\\' + x)

                with open(self.project + '\\' + 'outputs\\' + self.file_n + '.bat', 'w')as new_f:
                    if echo == 'yes':
                        new_f.write('@echo on')
                    else:
                        new_f.write('@echo off')
                    new_f.close()
                with open(self.project + '\\' + 'filehelper\\' + self.file_n + '.txt', 'w')as newh:
                    newh.write(self.file_n + '.bat')
                    newh.close()

                os.system('cd {0} & start batchmain_runner.vbs'.format(self.project))






def openfil():
    file = tkinter.filedialog.askopenfilename(title='Open a File', initialdir='projects', filetypes=([('Batch File', '*.bat')]))
    nfile = file.replace('/', '\\')
    file_name = os.path.basename(nfile)
    project_name = nfile.split('\\')
    generic = 'projects\\' + project_name[5]


    if 'outputs' in nfile:
        for x in os.listdir(generic + '\\filehelper'):
            os.remove(generic + '\\filehelper\\' + x)

        with open( generic + '\\filehelper\\' + file_name[:-4] + '.txt', 'w')as op:
            op.write(file_name)
            op.close()

        os.system('cd {0} & start batchmain_runner.vbs'.format(generic))
            
    else:
        tkinter.messagebox.showerror('Invalid Path', 'You cannot select a file outside of the projects folder.')


def filedelete():
    k = tkinter.filedialog.askopenfilenames(initialdir='outputs', filetypes=([('Batch files', '*.bat')]))
    for x in k:
        if 'outputs' not in x:
            error_dist('invalid_path', 'outputs')
        else:
            os.remove(x)

projects = projecr_creation
files = file_maker
try:
    main.iconbitmap('wams_file_maker_logo_icon.ico')
except:
    tkinter.messagebox.showwarning('Icon Not Found', 'The icon for file_maker.exe could not be found. File_maker.exe will continue without it.')
main.title('File Maker')
main.configure(background='orange')
main.maxsize(400,500)
main.minsize(400,500)


file_l = Label(main, text='Projects', font='Times 13', bg='orange', fg='blue')
file_l.pack(side=TOP)



name = Label(main, text='File Creation', font='times 14', bg='orange', fg='blue')
name.pack()
newf = Label(main, text='Enter a name for your new file:', bg='orange', fg='blue')
newf.pack()
filename = Entry(main)
filename.pack()

sub = Button(main, text='Submit', command=lambda:files(filename))
sub.pack()
openfiletitle = Label(main, text='Open a File', font='times 14', bg='orange', fg='blue')
openfiletitle.pack()


openfile = Button(main, text='Files', command=openfil)
openfig = Label(main, text='Click the button below to see the legible files to open', bg='orange', fg='blue')
openfig.pack()
openfile.pack()


project = Label(main, text='Create a new project', font='times 14', bg='orange', fg='blue')
project.pack()


instruct = Label(main, text='For multiple files that rely on eachother. Enter a name for this project', bg='orange',fg='blue')
instruct.pack()
projname = Entry()
projname.pack()
projnamesub = Button(main, text='Submit', command=lambda:projects(projname))
projnamesub.pack()

filedelete = Button(main, text='Delete file', command=filedelete)
filedelete.pack()
#setup
for file in os.listdir('projects'):
    lis.insert(END, file)
lis.pack()
main.mainloop()
