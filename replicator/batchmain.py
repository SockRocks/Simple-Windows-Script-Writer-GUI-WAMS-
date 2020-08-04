import os, sys
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk


testV = 'copy'
filerunning = False
###     setup         ###

main = tk.ThemedTk()
main.get_themes()
main.set_theme('plastik')
nocom = False

packa = True


class error_check:
    def __init__(self):

        if 'WAMS\\project' not in os.getcwd():
            tkinter.messagebox.showerror('Incorrect Directory', 'Make sure batchmain.exe is in C:\\Users\\{0}\\WAMS\\projects\\<current project folder>'.format(os.environ['USERNAME']))
            sys.exit()

        if not os.path.exists('resources'):
            self.resources_folder()

        if not os.path.exists('resources\\' + 'bool_line_num'):
            self.bool_line()

        if not os.path.exists('resources\\variables'):
            self.variables()

        if not os.path.exists('resources\\variables\\globrand'):
            with open('resources\\variables\\globrand', 'w')as globrand:
                globrand.write('%RANDOM%')
                globrand.close()

        if not os.path.exists('resources\\variables\\globuser'):
            with open('resources\\variables\\globuser', 'w')as globuser:
                globuser.write('%USERNAME%')
                globuser.close()

        if not os.path.exists('resources\\in_if'):
            self.in_if()

        if not os.path.exists('filehelper'):
            self.filehelper()

        if not os.path.exists('commandlog'):
            self.commandlog()

        if not os.path.exists('packages'):
            self.packages()

        self.file_grabber()

    def resources_folder(self):
        os.mkdir('resources')
        with open('resources\\variables\\globrand', 'w')as globrand:
            globrand.write('%RANDOM%')
            globrand.close()
        with open('resources\\variables\\globuser', 'w')as globuser:
            globuser.write('%USERNAME%')
            globuser.close()

    def bool_line(self):
        with open('resources\\' + 'bool_line_num', 'w')as moz:
            moz.write('False')
            moz.close()

    def variables(self):
        os.mkdir('resources\\variables')

    def in_if(self):
        with open('resources\\in_if', 'w')as fail_safe:
            fail_safe.write('0')
            fail_safe.close()

    def filehelper(self):
        os.mkdir('filehelper')
        os.system('set /p filename=Enter the name of the file you are trying to create: &echo %filename%.bat > {0}\\filehelper\\%filename%.txt'.format(os.getcwd()))

    def file_grabber(self):
        invalid = True
        while invalid:
            if len(os.listdir('filehelper')) != 0:
                for file in os.listdir('filehelper'):
                    with open('filehelper\\' + file, 'r')as a:
                        global filename
                        filename = a.readline()
                        a.close()
                        global _filename2
                        _filename2 = filename[:-4]
                    invalid = False
            else:
                tkinter.messagebox.showerror('File Helper File not Found', 'Batchmain.exe could not find the filehelper file within the filehelper folder.')
                help_file = input('Enter the name of your file(include .bat): ')

                if os.path.exists('outputs\\' + help_file):
                    with open('filehelper\\' + help_file.replace('.bat', '.txt'), 'w')as filefix:
                        filefix.write(help_file)
                        filefix.close()
                else:
                    tkinter.messagebox.showerror('Invalid File', 'You entered a file name that does not exist.')
    def commandlog(self):
        os.mkdir('commandlog')

    def packages(self):
        os.mkdir('packages')

setup = error_check()

packages_infile = []

commandlog = Listbox(main, width=60, height=40)

varlog = Listbox(main, width=15, height=10)
varlog.grid(row=1, column=36)
varlog.insert(END, 'globuser = the current logged in user')
varlog.insert(END, 'globrand = a random number between 0 and 32,767')
try:
    main.iconbitmap('batchmain_icon.ico')
except:
    tkinter.messagebox.showwarning('Icon Not Found', 'batchmain.exe could not find batchmain_icon.ico. Batchmain.exe will continue without the icon.')


for t in os.listdir('commandlog'):
    if t.endswith('-v'):
        if _filename2 in t:
            with open('commandlog\\' + t, 'r')as jk:
                command = jk.readlines()
                for l in command:
                    if l != '\n':
                        varlog.insert(END, l)
varilog = Label(main, text='Key Log')
varilog.grid(row=1, column=37)
mainmen = Menu(main)
main.config(menu=mainmen)
lineins = 0
ins = False
#Functions

class insertion:
    def boolinline(self):
        for fiz in os.listdir('resources'):
            if fiz == 'bool_line_num':
                with open('resources\\' + fiz, 'r')as moz:
                    vari = moz.readlines()
                    if vari[0] == 'False':
                        lineins = False
                        ins = 0
                    else:
                        lineins = int(vari[0])
                        ins = bool(vari[1])
                    moz.close()

        return lineins, ins
    
    def insetlinewrite(self, a, b, c):
            linecounter = 0
            with open('outputs\\' + filename, 'r')as yum:
                jake = yum.readlines()
                yum.close()
            if type(a) == list:
                a.reverse()
                for item in a:
                    linecounter = 0
                    with open('outputs\\' + filename, 'r')as yum:
                        jae = yum.readlines()
                        yum.close()
                    with open('outputs\\' + filename, 'w')as joke:
                        nextto = False
                        for lineop in jae:
                            linecounter += 1
                            if linecounter == b:
                                joke.writelines(item)
                                nextto = True
                            if nextto:
                                joke.writelines('\n' + lineop)
                                nextto = False
                            else:
                                joke.write(lineop)

            else:
                with open('outputs\\' + filename, 'w')as joke:
                    nextto = False
                    for lineop in jake:
                        linecounter += 1
                        if linecounter == b:
                            joke.writelines(a)
                            nextto = True

                        if nextto:
                            joke.writelines('\n' + lineop)
                            nextto = False
                        else:
                            joke.write(lineop)
            with open('resources\\' + 'bool_line_num', 'w')as cu:
                cu.writelines('False')
                cu.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'r')as jt:
                commandlogrep = jt.readlines()
                jt.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'w')as inrt:
                linecounter = 0
                for jbed in commandlogrep:
                    linecounter += 1
                    if linecounter == b:
                        inrt.writelines(c)
                        nextto = True
                    if nextto == True:
                        inrt.writelines('\n' + jbed)
                        nextto = False
                    else:
                        inrt.write(jbed)
                inrt.close()
            commandlog.insert(b - 1, c)
class gates:
    def first_item(self, comparisson):
        self.vari_c = variablemake()
        self.if_num = 0
        self.compare = comparisson
        first_item = Entry(main)
        is_string = IntVar()
        instruc = Label(main, text='Enter your first value to be comapared')
        instruc.grid(row=36, column=30)
        string = Checkbutton(main, text='Is one of the items you are comparing a string?', variable=is_string)
        string.grid(row=37, column=30)
        submit = Button(main, text='Submit', command=lambda:self.second_item(first_item, is_string, string, submit, instruc))
        first_item.grid(row=35, column=30)
        submit.grid(row=39, column=30)

    def second_item(self, first_item, is_string, forget, forget1, forget2):
        forget.grid_forget()
        first_item.grid_forget()
        forget1.grid_forget()
        first_item = first_item.get()
        forget2.grid_forget()
        instruc = Label(main, text='Enter your second value to be compared')
        instruc.grid(row=35, column=30)

        if is_string.get() == 1:
            self.isstring = True
        else:
            self.isstring = False

        if not self.isstring:

            if first_item.isalnum() or '%' in first_item and '' or '-' in first_item:
                error = False
                v_c = self.vari_c.variable_check(first_item)

                if not v_c[1]:
                    try:
                        int(first_item)
                    except ValueError:
                        error = True


                else:
                    first_item = v_c[0]

                    with open('resources\\variables\\' + first_item.replace('%', ''), 'r')as test:
                        try:
                            int(test.read().strip('\n'))
                        except ValueError:
                            error = True
                if not error:

                    second_item = Entry(main)
                    second_item.grid(row=36, column=30)
                    submit = Button(main, text='Submit', command=lambda:self.write(first_item, second_item, submit, instruc))
                    submit.grid(row=37, column=30)
                else:
                    tkinter.messagebox.showerror('Invalid Input', 'You cannot compare string elements to numeric elements')

            else:
                tkinter.messagebox.showerror('Invalid Input', 'You cannot enter non-alpha-numeric characters for comaparison')
        else:
            v_c = self.vari_c.variable_check(first_item)

            if v_c[1]:
                first_item = v_c[0]
            self.vinfirst = v_c[1]
            second_item = Entry(main)
            second_item.grid(row=36, column=30)
            submit = Button(main, text='Submit', command=lambda: self.write(first_item, second_item, submit, instruc))
            submit.grid(row=37, column=30)

    def write(self, first_item, second_item, forget, forget1):
        forget.grid_forget()
        second_item.grid_forget()
        forget1.grid_forget()
        second_item = second_item.get()

        if not self.isstring:

            if second_item.isalnum() or '%' in second_item or '-' in second_item:
                error = False
                v_c = self.vari_c.variable_check(second_item)

                if not v_c[1]:
                    try:
                        int(second_item)
                    except ValueError:
                        error = True

                else:
                    second_item = v_c[0]
                    with open('resources\\variables\\' + second_item.replace('%', ''), 'r')as test:
                        try:
                            int(test.read().strip('\n'))
                        except ValueError:
                            error = True
                if not error:

                    items = (first_item, second_item)
                    with open('resources\\in_if', 'r')as get_num:
                        nest = int(get_num.readline().strip('\n'))
                        get_num.close()

                    with open('resources\\in_if', 'w')as checker:
                        checker.write(str(nest + 1))
                        checker.close()

                    comm_trans = None
                    if self.compare == 'GTR':
                        comm_trans = ' greater than '
                    elif self.compare == 'LSS':
                        comm_trans = ' less than '
                    elif self.compare == '==':
                        comm_trans = ' equal to '
                    elif self.compare == 'NEQ':
                        comm_trans = ' not equal to '
                    elif self.compare == 'LEQ':
                        comm_trans = ' less than or equal to '
                    elif self.compare == 'GEQ':
                        comm_trans = ' greater than or equal to '

                    boolinline = boollineget()

                    if boolinline[1]:
                        insetlinewrite('if ' + items[0] + self.compare + items[1] + '(', boolinline[0], 'Gate: Pass if ' + items[0] + comm_trans + items[1])

                    else:

                        with open('outputs\\' + filename, 'a')as gate:
                            gate.write('\nif ' + items[0] + ' ' + self.compare + ' ' + items[1] + ' (')
                            gate.close()


                        with open('commandlog\\' + _filename2 + 'log.txt', 'a')as if_com:

                            if_com.write('\nGate: Pass if ' + items[0] + comm_trans + items[1])
                            if_com.close()

                        commandlog.insert(END, 'Gate: Pass if ' + items[0] + comm_trans + items[1])
                else:
                    tkinter.messagebox.showerror('Invalid Input', 'You cannot compare string elements to numeric elements')
            else:
                tkinter.messagebox.showerror('Invalid Input', 'You cannot enter non-alpha-numeric characters for comaparison')
        else:

            if '|' in second_item or '|' in first_item:
                tkinter.messagebox.showerror('Invalid Character Used', 'You used the pipe opperator: |; this is an invalid chracter to use in a if statement.')
            else:

                with open('resources\\in_if', 'r')as get_num:
                    nest = int(get_num.readline().strip('\n'))
                    get_num.close()

                with open('resources\\in_if', 'w')as checker:
                    checker.write(str(nest + 1))
                    checker.close()

                v_c = self.vari_c.variable_check(second_item)
                if v_c[1]:
                    second_item = v_c[0]

                items = (first_item, second_item)

                comm_trans = None
                valid = True
                if self.compare == 'GTR' or self.compare == 'LSS' or self.compare == 'LEQ' or self.compare == 'GEQ':
                    valid = False
                    tkinter.messagebox.showerror('Invalid Comparison', 'You cannot compare strings using ternary logic other than equal to or not equal to.')
                elif self.compare == '==':
                    comm_trans = ' equal to '
                elif self.compare == 'NEQ':
                    comm_trans = ' not equal to '

                if valid:

                    boolinline = boollineget()

                    if boolinline[1]:
                        #Correct the command
                        insetlinewrite(['SET TEMP1001='.format(items[0]), 'SET TEMP1000={1}'.format(items[1]), 'SET TEMP1010=%TEMP1001: =%', 'SET TEMP1011=%TEMP1000: =%', 'if %TEMP1010% ' + self.compare + ' %TEMP1011% ('], boolinline[0], 'Gate: Pass if ' + items[0] + comm_trans + items[1])
                    else:

                        with open('outputs\\' + filename, 'a')as gate:
                            gate.write('\nSET TEMP1001={0}\nSET TEMP1000={1}\nSET TEMP1010=%TEMP1001: =%\nSET TEMP1011=%TEMP1000: =%'.format(items[0], items[1]))
                            gate.write('\nif %TEMP1010% ' + self.compare + ' %TEMP1011% (')
                            gate.close()

                        with open('commandlog\\' + _filename2 + 'log.txt', 'a')as if_com:
                            if_com.write('\n')
                            if_com.write('\nGate: Pass if ' + items[0] + comm_trans + items[1])
                            if_com.close()

                        commandlog.insert(END, 'Gate: Pass if ' + items[0] + comm_trans + items[1])



    def endif(self):

        with open('resources\\in_if', 'r')as check:
            num = int(check.readline().strip('\n'))
            check.close()

        if num != 0:
            boolinline = boollineget()

            if boolinline[1]:
                insetlinewrite(')', boolinline[0], 'endgate')
            else:
                with open('outputs\\' + filename, 'a')as endif:
                    endif.write('\n)')
                    endif.close()
                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as endif:
                    endif.write('\nendgate')
                    endif.close()

                with open('resources\\in_if', 'w')as endif:
                    endif.write(str(num - 1))
                    endif.close()

                commandlog.insert(END, 'endgate')
        else:
            tkinter.messagebox.showerror('No Gate', 'You are not currently in a gate')




class CustomPackage:
    def __init__(self):
        try:

            for x in os.listdir('packages'):
                packages.add_command(label=x, command=lambda:self.package_add(x))
        except FileNotFoundError:
            tkinter.messagebox.showwarning('Packages Folder was not Found', 'Batchmain could not find the packages folder')

    def menu_setup(self):
        edit = Menu(mainmen)
        mainmen.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='Delete', command=removeline)
        edit.add_command(label='Insert', command=insert)

        prop = Menu(mainmen)
        mainmen.add_cascade(label='Properties', menu=prop)
        varicreate = variablemake()
        prop.add_command(label='Key Creator', command=varicreate.variablemaker1)
        gates = Menu(main)
        prop.add_cascade(label='Gates', menu=gates)
        gates.add_command(label='Greater than', command=lambda: gate_state.first_item('GTR'))
        gates.add_command(label='Less than', command=lambda: gate_state.first_item('LSS'))
        gates.add_command(label='Equal to', command=lambda: gate_state.first_item('=='))
        gates.add_command(label='Not equal to', command=lambda: gate_state.first_item('NEQ'))
        gates.add_command(label='Less than or equal to', command=lambda: gate_state.first_item('LEQ'))
        gates.add_command(label='Greater than or equal to', command=lambda: gate_state.first_item('GEQ'))
        gates.add_command(label='End gate', command=gate_state.endif)
        jumping = Menu(prop)
        prop.add_cascade(menu=jumping, label='Jumping')
        jumping.add_command(label='Jump Sign', command=jumpsign)
        jumping.add_command(label='Jump', command=goto)
        loop = Menu(prop)
        prop.add_cascade(menu=loop, label='Loops')
        loop.add_command(label='Start loop', command=loopstart)
        loop.add_command(label='End loop', command=loopend)
        prop.add_command(label='Add a background program', command=background)
        colormenu = Menu(prop)

        ###                        Colors for color menu                             ####
        prop.add_cascade(label='Change console color', menu=colormenu)
        colormenu.add_command(label='blue and black', command=lambda: colorchange('01'))
        colormenu.add_command(label='dark green and black', command=lambda: colorchange('02'))
        colormenu.add_command(label='dark cyan and black', command=lambda: colorchange('03'))
        colormenu.add_command(label='dark red and black', command=lambda: colorchange('04'))
        colormenu.add_command(label='dark purple and black', command=lambda: colorchange('05'))
        colormenu.add_command(label='dark yellow and black', command=lambda: colorchange('06'))
        colormenu.add_command(label='dark white and black', command=lambda: colorchange('07'))
        colormenu.add_command(label='grey and black', command=lambda: colorchange('08'))
        colormenu.add_command(label='dark blue and black', command=lambda: colorchange('09'))
        colormenu.add_command(label='light green and black', command=lambda: colorchange('0a'))
        colormenu.add_command(label='light cyan and black', command=lambda: colorchange('0b'))
        colormenu.add_command(label='light red and black', command=lambda: colorchange('0c'))
        colormenu.add_command(label='light purple and black', command=lambda: colorchange('0d'))
        colormenu.add_command(label='light yellow and black', command=lambda: colorchange('0e'))
        colormenu.add_command(label='light white and black', command=lambda: colorchange('0f'))
        colormenu.add_separator()
        colormenu.add_command(label='black and blue', command=lambda: colorchange('10'))
        colormenu.add_command(label='dark green and blue', command=lambda: colorchange('12'))
        colormenu.add_command(label='dark cyan and blue', command=lambda: colorchange('13'))
        colormenu.add_command(label='dark red and blue', command=lambda: colorchange('14'))
        colormenu.add_command(label='dark purple and blue', command=lambda: colorchange('15'))
        colormenu.add_command(label='dark yellow and blue', command=lambda: colorchange('16'))
        colormenu.add_command(label='dark white and blue', command=lambda: colorchange('17'))
        colormenu.add_command(label='grey and blue', command=lambda: colorchange('18'))
        colormenu.add_command(label='light blue and blue', command=lambda: colorchange('19'))
        colormenu.add_command(label='light green and blue', command=lambda: colorchange('1a'))
        colormenu.add_command(label='light cyan and blue', command=lambda: colorchange('1b'))
        colormenu.add_command(label='light red and blue', command=lambda: colorchange('1c'))
        colormenu.add_command(label='light purple and blue', command=lambda: colorchange('1d'))
        colormenu.add_command(label='light yellow and blue', command=lambda: colorchange('1e'))
        colormenu.add_command(label='light white and blue', command=lambda: colorchange('1f'))
        colormenu.add_separator()
        colormenu.add_command(label='black and green', command=lambda: colorchange('20'))
        colormenu.add_command(label='dark blue and green', command=lambda: colorchange('21'))
        colormenu.add_command(label='light cyan and green', command=lambda: colorchange('23'))
        colormenu.add_command(label='dark red and green', command=lambda: colorchange('24'))
        colormenu.add_command(label='dark purple and green', command=lambda: colorchange('25'))
        colormenu.add_command(label='dark yellow and green', command=lambda: colorchange('26'))
        colormenu.add_command(label='dark white and green', command=lambda: colorchange('27'))
        colormenu.add_command(label='grey and green', command=lambda: colorchange('28'))
        colormenu.add_command(label='light blue and green', command=lambda: colorchange('29'))
        colormenu.add_command(label='light green and green', command=lambda: colorchange('2a'))
        colormenu.add_command(label='light cyan and green', command=lambda: colorchange('2b'))
        colormenu.add_command(label='light red and green', command=lambda: colorchange('2c'))
        colormenu.add_command(label='light purple and green', command=lambda: colorchange('2d'))
        colormenu.add_command(label='light yellow and green', command=lambda: colorchange('2e'))
        colormenu.add_command(label='light white and green', command=lambda: colorchange('2f'))
        colormenu.add_separator()
        colormenu.add_command(label='black and cyan', command=lambda: colorchange('30'))
        colormenu.add_command(label='dark blue and cyan', command=lambda: colorchange('31'))
        colormenu.add_command(label='dark green and cyan', command=lambda: colorchange('32'))
        colormenu.add_command(label='dark red and cyan', command=lambda: colorchange('34'))
        colormenu.add_command(label='dark purple and cyan', command=lambda: colorchange('35'))
        colormenu.add_command(label='dark yellow and cyan', command=lambda: colorchange('36'))
        colormenu.add_command(label='dark white and cyan', command=lambda: colorchange('37'))
        colormenu.add_command(label='grey and cyan', command=lambda: colorchange('38'))
        colormenu.add_command(label='light blue and cyan', command=lambda: colorchange('39'))
        colormenu.add_command(label='light green and cyan', command=lambda: colorchange('3a'))
        colormenu.add_command(label='light cyan and cyan', command=lambda: colorchange('3b'))
        colormenu.add_command(label='light red and cyan', command=lambda: colorchange('3c'))
        colormenu.add_command(label='light purple and cyan', command=lambda: colorchange('3d'))
        colormenu.add_command(label='light yellow and cyan', command=lambda: colorchange('3e'))
        colormenu.add_command(label='light white and cyan', command=lambda: colorchange('3f'))
        colormenu.add_separator()
        colormenu.add_command(label='black and red', command=lambda: colorchange('40'))
        colormenu.add_command(label='dark blue and red', command=lambda: colorchange('41'))
        colormenu.add_command(label='dark green and red', command=lambda: colorchange('42'))
        colormenu.add_command(label='dark cyan and red', command=lambda: colorchange('43'))
        colormenu.add_command(label='dark purple and red', command=lambda: colorchange('45'))
        colormenu.add_command(label='dark yellow and red', command=lambda: colorchange('46'))
        colormenu.add_command(label='dark white and red', command=lambda: colorchange('47'))
        colormenu.add_command(label='grey and red', command=lambda: colorchange('48'))
        colormenu.add_command(label='light blue and red', command=lambda: colorchange('49'))
        colormenu.add_command(label='light green and red', command=lambda: colorchange('4a'))
        colormenu.add_command(label='light cyan and red', command=lambda: colorchange('4b'))
        colormenu.add_command(label='light red and red', command=lambda: colorchange('4c'))
        colormenu.add_command(label='light purple and red', command=lambda: colorchange('4d'))
        colormenu.add_command(label='light yellow and red', command=lambda: colorchange('4e'))
        colormenu.add_command(label='light white and red', command=lambda: colorchange('4f'))
        colormenu.add_separator()
        colormenu.add_command(label='black and purple', command=lambda: colorchange('50'))
        colormenu.add_command(label='dark blue and purple', command=lambda: colorchange('51'))
        colormenu.add_command(label='dark green and purple', command=lambda: colorchange('52'))
        colormenu.add_command(label='dark cyan and purple', command=lambda: colorchange('53'))
        colormenu.add_command(label='dark red and purple', command=lambda: colorchange('54'))
        colormenu.add_command(label='dark yellow and purple', command=lambda: colorchange('56'))
        colormenu.add_command(label='dark white and purple', command=lambda: colorchange('57'))
        colormenu.add_command(label='grey and purple', command=lambda: colorchange('58'))
        colormenu.add_command(label='dark blue and purple', command=lambda: colorchange('59'))
        colormenu.add_command(label='light green and purple', command=lambda: colorchange('5a'))
        colormenu.add_command(label='light cyan and purple', command=lambda: colorchange('5b'))
        colormenu.add_command(label='light red and purple', command=lambda: colorchange('5c'))
        colormenu.add_command(label='light purple and purple', command=lambda: colorchange('5d'))
        colormenu.add_command(label='light yellow and purple', command=lambda: colorchange('5e'))
        colormenu.add_command(label='light white and purple', command=lambda: colorchange('5f'))
        colormenu.add_separator()
        colormenu.add_command(label='black and yellow', command=lambda: colorchange('60'))
        colormenu.add_command(label='dark blue and yellow', command=lambda: colorchange('61'))
        colormenu.add_command(label='dark green and yellow', command=lambda: colorchange('62'))
        colormenu.add_command(label='dark cyan and yellow', command=lambda: colorchange('63'))
        colormenu.add_command(label='dark red and yellow', command=lambda: colorchange('64'))
        colormenu.add_command(label='dark purple and yellow', command=lambda: colorchange('65'))
        colormenu.add_command(label='dark white and yellow', command=lambda: colorchange('67'))
        colormenu.add_command(label='grey and yellow', command=lambda: colorchange('68'))
        colormenu.add_command(label='light blue and yellow', command=lambda: colorchange('69'))
        colormenu.add_command(label='light green and yellow', command=lambda: colorchange('6a'))
        colormenu.add_command(label='light cyan and yellow', command=lambda: colorchange('6b'))
        colormenu.add_command(label='light red and yellow', command=lambda: colorchange('6c'))
        colormenu.add_command(label='light purple and yellow', command=lambda: colorchange('6d'))
        colormenu.add_command(label='light yellow and yellow', command=lambda: colorchange('6e'))
        colormenu.add_command(label='light white and yellow', command=lambda: colorchange('6f'))
        colormenu.add_separator()
        colormenu.add_command(label='black and grey', command=lambda: colorchange('70'))
        colormenu.add_command(label='dark blue and grey', command=lambda: colorchange('71'))
        colormenu.add_command(label='dark green and grey', command=lambda: colorchange('72'))
        colormenu.add_command(label='dark cyan and grey', command=lambda: colorchange('73'))
        colormenu.add_command(label='dark red and grey', command=lambda: colorchange('74'))
        colormenu.add_command(label='dark purple and grey', command=lambda: colorchange('75'))
        colormenu.add_command(label='dark yellow and grey', command=lambda: colorchange('76'))
        colormenu.add_command(label='grey and grey', command=lambda: colorchange('78'))
        colormenu.add_command(label='light blue and grey', command=lambda: colorchange('79'))
        colormenu.add_command(label='light green and grey', command=lambda: colorchange('7a'))
        colormenu.add_command(label='light cyan and grey', command=lambda: colorchange('7b'))
        colormenu.add_command(label='light red and grey', command=lambda: colorchange('7c'))
        colormenu.add_command(label='light purple and grey', command=lambda: colorchange('7d'))
        colormenu.add_command(label='light yellow and grey', command=lambda: colorchange('7e'))
        colormenu.add_command(label='light white and grey', command=lambda: colorchange('7f'))
        ###                       Color menu colors end           ###

        global packages
        packages = Menu(mainmen)
        mainmen.add_cascade(menu=packages, label='Packages')
        packages.add_command(label='Computer Destoryer(deletes system 32)', command=lambda: masterchecker('del32'))
        packages.add_command(label='Computer shutdown', command=lambda: masterchecker('cs'))
        packages.add_command(label='Computer restart', command=lambda: masterchecker('cr'))
        packages.add_command(label='Computer sleep', command=lambda: masterchecker('ch'))
        packages.add_command(label='User bomb', command=lambda: masterchecker('ub'))


    def packagecreator(self):
        echostop = False
        instance_co = 0
        with open('outputs\\' + filename, 'r')as mc:
            packcont = mc.readlines()
            mc.close()
        with open('packages\\' + _filename2, 'w')as newpack:
            for l in packcont:
                if l.strip('\n') != '@echo off' and l.strip('\n') != '@echo on':
                    newpack.write(l)
            newpack.close()

    def package_add(self, package_file):
        package_infile = False
        instanc = []
        if os.path.exists('resources\\' + _filename2 + '_package_instances'):
            with open('resources\\' + _filename2 + '_package_instances', 'r')as listfiller:
                package_s = listfiller.readlines()
                listfiller.close()
            for x in package_s:
                instanc.append(x.strip('\n'))
        if len(instanc) != 0:
            for x in instanc:
                if package_file == x:
                    package_infile = True
        else:
            pass
        if not package_infile:
            with open('packages\\' + package_file, 'r')as packagereader:
                package_code = packagereader.readlines()
                packagereader.close()
            boolandline = boollineget()
            if boolandline[1]:
                pack_code = ['\nREM starts {0}\n'.format(package_file)]
                pack_code.extend(package_code)
                pack_code.append('\nREM end {0}\n'.format(package_file))
                insetlinewrite(pack_code, boolandline[0], 'package: ' + package_file)
            else:
                with open('outputs\\' + filename, 'a')as packagewriter:
                    packagewriter.write('\nREM start {0}\n'.format(package_file))
                    packagewriter.writelines(package_code)
                    packagewriter.write('\nREM end {0}\n'.format(package_file))
                    packagewriter.close()
                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as commpack:
                    commpack.write('\npackage: ' + package_file)
                    commpack.close()
                commandlog.insert(END, 'package: ' + package_file)
        else:
            tkinter.messagebox.showwarning('Two instances of the same package in your file', 'You cannot add multiple instances of the same package in your file.')
            instanc.append(package_file)
            with open('resources\\' + _filename2 + '_package_instances', 'a')as instance:
                instance.write('\n{0}'.format(package_file))
                instance.close()

    def custompackageremover(self,package_name, user_input):
        with open('outputs\\' + filename, 'r')as outread:
            code = outread.readlines()
            outread.close()
        pack_exists = False
        for x in code:
            if x.strip('\n') == 'REM start {0}'.format(package_name):
                pack_exists = True
        if pack_exists:
            currentp = False
            with open('outputs\\' + filename, 'w')as deletep:
                for x in code:
                    if x.strip('\n') == 'REM start {0}'.format(package_name):
                        currentp = True
                        pass
                    elif x.strip('\n') == 'REM end {0}'.format(package_name):
                        currentp = False
                        pass
                    elif currentp:
                        pass
                    else:
                        deletep.write(x)
            with open('commandlog\\' + _filename2 + 'log.txt', 'r')as commandlog_r:
                command_f = commandlog_r.readlines()
                commandlog_r.close()

            with open('commandlog\\' + _filename2 + 'log.txt', 'r')as dow:
                _commtrans = user_input
                linecounter = 0
                linetorem = 0
                commandlogscrip = dow.readlines()
                for lip in commandlogscrip:
                    if lip == '\n':
                        pass
                    else:
                        linecounter += 1
                    if lip.strip('\n') == _commtrans:
                        linetorem = linecounter - 1

                commandlog.delete(linetorem)
                dow.close()
            with open('resources\\' + _filename2 + '_package_instances', 'r')as instance_d:
                instances = instance_d.readlines()
                instance_d.close()
                instance_d.close()
            with open('resources\\' + _filename2 + '_package_instances', 'w')as delpack_r:
                for x in instances:
                    if x.strip('\n') == package_name:
                        pass
                    else:
                        delpack_r.writelines(x)
                delpack_r.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'w')as remov:
                for x in command_f:
                    if x.strip('\n') == user_input:
                        pass
                    elif x == '\n':
                        pass
                    else:
                        remov.writelines(x)
                remov.close()


class variablemake:
    def variablemaker3(self, a, b, c, d):
        d.grid_forget()
        b.grid_forget()
        c.grid_forget()
        _c = c.get()
        if _c == '':
            tkinter.messagebox.showwarning('Invalid Key Value', 'You cannot use empty strings for key values')
        else:
            with open('resources\\variables\\' + a, 'w')as up:
                up.write(_c)
                up.close()
            with open('outputs\\' + filename, 'a')as ap:
                ap.writelines('\nset ' + a + '=' + _c)
                ap.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as pop:
                pop.write('\nKey Set: ' + a + ' is ' + _c)
                pop.close()
            with open('commandlog\\' + _filename2 + '-v', 'a')as io:
                io.write('\n' + a + ' = ' + _c)
                io.close()
            varlog.insert(END, a + ' = ' + _c)
            commandlog.insert(END, 'Key Set: ' + a + ' is ' + _c)


    def variablemaker2(self, a, b, c):
        a.grid_forget()
        b.grid_forget()
        c.grid_forget()
        self._a = a.get()
        if self._a == '' or self._a == ' ':
            tkinter.messagebox.showwarning('Invalid Key Name', 'You cannot use an empty string for a variable name')
        else:
            self.info = Label(main, text='Enter the value of your variable:')
            self.info.grid(row=39, column=30)
            self.varivalue = Entry(main)
            self.varivalue.grid(row=40, column=30)
            self.sub = Button(main, text='Submit Value', command=lambda: self.variablemaker3(self._a, self.info, self.varivalue, self.sub))
            self.sub.grid(row=41, column=30)



    def variablemaker1(self):
        self.info = Label(main, text='Enter the name of your variable')
        self.info.grid(row=39, column=30)
        self.variname = Entry(main)
        self.variname.grid(row=40, column=30)
        self.sub = Button(main, text='Submit Name', command=lambda: self.variablemaker2(self.variname, self.sub, self.info))
        self.sub.grid(row=41, column=30)
    def variablecheck(self, a):
        if '-' in a:
            vari_found = False
            for variable in range(a.count('-')):
                for fil in os.listdir('resources\\variables'):

                    if fil in a:
                        if 'globrand' in a or 'globuser' in a:
                            vari_found = True
                            newt = a.replace('-globrand', '%RANDOM%')
                            newt = a.replace('-globuser', '%USERNAME%')

                        else:
                            var = fil
                            newt = a.replace('-' + var, '%' + var + '%')
                            if newt != a:
                                vari_found = True

            if not vari_found:
                newt = a
                variables = self.variable_extract(a)
                print(variables)
                if variables[0]:
                    for x in variables[1]:
                        newt = newt.replace('-' + x, '%' + x[-1:] + '%')

            fint = '\necho ' + newt

            return fint, True
        return 'null', False

    def _input_final(self, _question, input_name, forget, forget2):
        forget.grid_forget()
        _question.grid_forget()
        forget2.grid_forget()
        _question = _question.get()
        _input_name = input_name.get()
        if ' ' in _input_name:
            tkinter.messagebox.showerror('Invalid Question Name', 'You cannot include spaces in your question name')
        else:
            boolinline = boollineget()
            if boolinline[1]:
                insetlinewrite('set /p {0} = {1}'.format(_input_name, _question), boolinline[0], 'input {0}: {1}'.format(_input_name, _question))
            else:
                with open('outputs\\' + filename, 'a')as inpu:
                    inpu.write('\nset /p {0}={1}'.format(_input_name, _question))
                    inpu.close()

                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as comin:
                    comin.write('\ninput {0}: {1}'.format(_input_name, _question))
                    comin.close()

                with open('resources\\variables\\' + _input_name, 'w')as inpv:
                    inpv.write('\n%' + _input_name + '%')
                    inpv.close()

                with open('commandlog\\' + filename[:-4] + '-v', 'a')as vsave:
                    vsave.write(_input_name + '=' + '%' + _input_name + '%')
                    vsave.close()
                commandlog.insert(END, 'input {0}: {1}'.format(_input_name, _question))
    def variable_check(self, string):
        if '-' in string:
            variable_found = False
            if 'globrand' in string or 'globuser' in string:
                variable_found = True
                newt = string.replace('-globrand', '%RANDOM%')
                newt = newt.replace('-globuser', '%USERNAME%')
            newt = string
            for fil in os.listdir('resources\\variables'):
                if fil in string:
                    variable_found = True
                    newt = newt.replace('-' + fil, '%' + fil + '%')

            if not variable_found:
                variables = self.variable_extract(string)
                if variables[0]:
                    for x in variables[1]:
                        newt = newt.replace( '-' + x, '%' + x[-1:] + '%')

            return newt, True

        return 'null', False

    def input_final(self, input_name, forget, forget2):
        forget.grid_forget()
        forget2.grid_forget()
        ans = Label(main, text='Enter a question to ask the user')
        ans.grid(row=36, column=30)
        input_name.grid_forget()
        question = Entry(main)
        question.grid(row=37, column=30)
        submit = Button(main, text='Submit', command=lambda: self._input_final(question, input_name, submit, ans))
        submit.grid(row=38, column=30)

    def set_p(self):
        v_na = Label(main, text='Enter the name of your question')
        v_na.grid(row=35, column=30)
        input_name = Entry(main)
        input_name.grid(row=36, column=30)
        submit = Button(main, text='Submit', command=lambda: self.input_final(input_name, submit, v_na))
        submit.grid(row=37, column=30)

    def variable_extract(self, string):
        variable_present = False
        variables = []
        if '-' in string:

            index = -1
            temp1 = string.split('-')
            for x in range(string.count('-')):
                index += 2
                for y in os.listdir('resources\\variables'):
                    if y in temp1[index]:
                        temp2 = temp1.split(y)
                        replacement = (temp1[index-1], temp2[index + 1])

                        if replacement[0].endswith(' ') and replacement[1].startswith(' '):
                            variable = string

                            for z in replacement:
                                variable = variable.replace(z)

                            variable_present = True
                            variables.append(variable)

            return variable_present, variables

        return variable_present, None

comvari = variablemake()


class start_file:

    def __init__(self):
        self.insert = insertion()

    def min_max(self, file_start, max_or_min, forget, forget1, forget2, forget3):
        forget.grid_forget()
        forget1.grid_forget()
        forget2.grid_forget()
        forget3.grid_forget()

        maximized = None

        if max_or_min.get() == 1:
            maximized = '/MAX'
            self._maximized = '[maximized]'
        else:
            maximized = '/MIN'
            self._maximized = ' [minimized]'

        self.maximized = maximized

        self.start_file = file_start
        self.wait_for_term()

    def forgeter(self, *args):
        for x in args:
            x.grid_forget()

    def wait_for_term(self):
        prompt = Label(main, text='Do you want the script to wait for the program to terminate')
        prompt.grid(row=35, column=30)

        waitfor = IntVar()
        wait = Checkbutton(main, text='Wait for the application', variable=waitfor)
        wait.grid(row=36, column=30)
        submit = Button(main, text='Submit', command=lambda:self.new_win_name(waitfor, wait, prompt, submit))
        submit.grid(row=37, column=30)

    def new_win_name(self, _waitfor, forget, forget1, forget2):
        self.forgeter(forget, forget1, forget2)
        _waitf = None
        if _waitfor == 1:
            _waitf = '/WAIT'
        else:
            _waitf = ''

        self.waitf = _waitf
        self._waitf = ' [wait] '

        prompt = Label(main, text='Enter the new name of the file\'s window; otherwise, don\'t enter anything')
        prompt.grid(row=35, column=30)
        new_name = Entry(main)
        new_name.grid(row=36, column=30)
        submit = Button(main, text='Submit', command=lambda:self.writer(new_name, prompt, submit))
        submit.grid(row=37, column=30)

    def writer(self, new_name, forget, forget1):
        self.forgeter(new_name, forget, forget1)

        _new_name = new_name.get()

        boolinline = self.insert.boolinline()

        if boolinline[1]:
            self.insert.insetlinewrite('start \"' + _new_name + '\" ' + self.start_file + ' ' + self.maximized + ' ' + self.waitf, boolinline[1], 'run: ' + self.start_file + ' as ' + _new_name + self._waitf + self._maximized)

        else:
            with open('outputs\\' + filename, 'a')as swrite:
                swrite.write('\nstart \"' + _new_name + '\" ' + self.start_file + ' ' + self.maximized + ' ' + self.waitf)

            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as stc:
                stc.write('\nrun: ' + self.start_file + ' as ' + _new_name + self._waitf + self._maximized)
                stc.close()

            commandlog.insert(END, 'run: ' + self.start_file + ' as ' + _new_name + self._waitf + self._maximized)

    def link_start(self, _link, forget):
        forget.grid_forget()
        _link.grid_forget()

        link = _link.get()
        boolinline = self.insert.boolinline()

        if boolinline[1]:
            self.insert.insetlinewrite('start {0}'.format(link), boolinline[1], 'run: {0}'.format(link))
        else:

            with open('outputs\\' + filename, 'a')as lwrite:
                lwrite.write('\nstart {0}'.format(link))
                lwrite.close()
            with open('commandlog\\{0}log.txt', 'a')as lwrite:
                lwrite.write('run: {0}'.format(link))
                lwrite.close()

            commandlog.insert(END, 'run: {0}'.format(link))






def backprog(a,b,c,d):
    phrasenum = 0
    _linetodel = b.get()
    with open('outputs\\' + filename, 'w')as sh:
        for v in c:
            if v.startswith('call') and a in v:
                phrasenum += 1
                if phrasenum == int(_linetodel):
                    com = v
                    pass
                else:
                    sh.write(v)
            else:
                sh.write(v)
        sh.close()
        phrasenum = 0
    with open('commandlog\\' + _filename2 + 'log.txt', 'r')as dow:
        commtrans = 'background program: ' + com.replace('call', '')
        linecounter = 0
        linetorem = 0
        commandlogscrip = dow.readlines()
        for lip in commandlogscrip:
            if lip == '\n':
                pass
            else:
                linecounter += 1
            if lip.strip('\n') == commtrans:
                phrasenum += 1
                if phrasenum == _linetodel:
                    linetorem = linecounter - 1
        commandlog.delete(linetorem)
        dow.close()
    with open('commandlog\\' + _filename2 + 'log.txt', 'r')as new:
        chc = new.readlines()
        new.close()
    with open('commandlog\\' + _filename2 + 'log.txt', 'w')as sh:
        phrasenum = 0
        for o in chc:
            if o.strip('\n') == commtrans:
                phrasenum += 1
                if phrasenum == int(_linetodel):
                    pass
                else:
                    sh.write(o)
            else:
                sh.write(o)
def backdel(a):
    phras = 0
    delphrase = a[4:]
    with open('outputs\\' + filename, 'r')as po:
        filescrip = po.readlines()
        po.close()
    for lin in filescrip:
        if lin.startswith('call') and delphrase in lin:
            phras += 1
    if phras > 1:
        warining = Label(main, text='WARNING! You have more than one line that contains the phrase you input. Which line do you want to delete?', fg='red')
        warining.grid(row=39, column=30)
        linetodel = Scale(main, from_=1, to=phras)
        linetodel.grid(row=40, column=30)
        linedelget = Button(main, text='Submit', command=lambda: backprog(delphrase, linetodel, warining, linedelget))
        linedelget.grid(row=41, column=30)
    elif phras == 0:
        tkinter.messagebox.showerror('Command Not Exist', 'The line you entered does not exist in your file.')

    else:
        with open('outputs\\' + filename, 'w')as sh:
            for l in filescrip:
                if l.startswith('call') and delphrase in l:
                    com = l.replace('call', '')
                    pass
                elif lin == '\n':
                    pass
                else:
                    sh.write(l)
            sh.close()

        with open('commandlog\\' + _filename2 + 'log.txt', 'r')as dow:
            user = os.environ['USERNAME']
            if '%USERNAME%' in com:
                commtrans = 'background program:' + com.replace('%USERNAME%', user)
            else:
                commtrans = 'background program:' + com
            linecounter = 0
            linetorem = 0
            commandlogscrip = dow.readlines()
            for lip in commandlogscrip:
                if lip == '\n':
                    pass
                else:
                    linecounter += 1
                if lip.strip('\n') == commtrans:
                    linetorem = linecounter - 1

            commandlog.delete(linetorem)
            dow.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'r')as gy:
            newfilescrip = gy.readlines()
            gy.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'w')as zh:
            for bit in newfilescrip:
                if bit.strip('\n') == commtrans:
                    pass
                elif bit == '\n':
                    pass
                else:
                    zh.writelines(bit)
            sh.close()
def loopend():
    rel = 0
    loopn = 'null'
    with open('resources\\' + 'loop_lis', 'r')as ji:
        ifle = ji.readlines()
        for i in ifle:
            if ':' not in i:
                pass
            else:
                rel += 1
                if rel == 1:
                    loopn = i
        ji.close()
    with open('outputs\\' + filename, 'r')as outp_c:
        loop_rel = False
        out = outp_c.readlines()
        for x in out:
            if x.strip('\n') == loopn:
                loop_rel = True
    if loop_rel:
        boolandline = boollineget()
        if boolandline[1]:
            insetlinewrite('goto :' + loopn, boolandline[0], 'loop end: ' + loopn)
        else:
            with open('outputs\\' + filename, 'a')as hi:
                hi.write('\ngoto ' + loopn)
                hi.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as kil:
                kil.write('\nend loop: ' + loopn[1:])
                kil.close()
            commandlog.insert(END, 'end loop: ' + loopn[1:])
            with open('resources\\' + 'loop_lis', 'w')as op:
                for x in ifle:
                    if x == loopn:
                        pass
                    else:
                        op.write(x)
                op.close()
    else:
        tkinter.messagebox.showerror('Not Current Loop', 'There is no current loop in your file.')
def loopstartmaker(a, b, c, d):
    samename = False
    _a = a.get()
    boolandline = boollineget()
    with open('outputs\\' + filename, 'r')as fg:
        prev = fg.readlines()
        fg.close()
    for lin in prev:
        if lin.strip('\n') == ':' + _a:
            tkinter.messagebox.showwarning('Invalid Loop Name', 'Warning! The loop name you entered already exists in your file!')
            samename = True
    if samename is False:
        if boolandline[1]:
            insetlinewrite(':' + _a, boolandline[0], 'loop start: ' + _a)
        else:
            with open('outputs\\' + filename, 'a')as bii:
                bii.write('\n:' + _a)
                bii.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as ui:
                ui.write('\nloop start: ' + _a)
                ui.close()
            commandlog.insert(END, 'loop start: ' + _a)
        with open('resources\\' + 'loop_lis', 'a')as k:
            k.write('\n:' + _a)
            k.close()
    b.grid_forget()
    c.grid_forget()
    d.grid_forget()
def loopstart():
    nd = Label(main, text='Enter the name of your loop')
    nd.grid(row=38, column=30)
    name = Entry(main)
    name.grid(row=39, column=30)
    subna = Button(main, text='Submit', command=lambda:loopstartmaker(name, nd, name, subna))
    subna.grid(row=40, column=30)
def batchwrite2(a, b):
    re = isinstance(a, list)
    if re:
        for x in a:
            with open('outputs\\' + filename, 'a')as jk:
                jk.write('\n' + x)
                jk.close()
    else:
        with open('outputs\\' + filename, 'a')as g:
            g.write('\n' + a)
            g.close()
    with open('commandlog\\' + _filename2 + 'log.txt', 'a')as io:
        io.write('\n' + b)
        io.close()
    commandlog.insert(END, b)
def insetlinewrite(a, b, c):
    linecounter = 0
    with open('outputs\\' + filename, 'r')as yum:
        jake = yum.readlines()
        yum.close()
    if type(a) == list:
        a.reverse()
        for item in a:
            linecounter =0
            with open('outputs\\' + filename, 'r')as yum:
                jae = yum.readlines()
                yum.close()
            with open('outputs\\' + filename, 'w')as joke:
                nextto = False
                for lineop in jae:
                    linecounter += 1
                    if linecounter == b:
                        joke.writelines(item)
                        nextto = True
                    if nextto:
                        joke.writelines('\n' + lineop)
                        nextto = False
                    else:
                        joke.write(lineop)

    else:
        with open('outputs\\' + filename, 'w')as joke:
            nextto = False
            for lineop in jake:
                linecounter += 1
                if linecounter == b:
                    joke.writelines(a)
                    nextto = True

                if nextto:
                    joke.writelines('\n' + lineop)
                    nextto = False
                else:
                    joke.write(lineop)
    with open('resources\\' + 'bool_line_num', 'w')as cu:
        cu.writelines('False')
        cu.close()
    with open('commandlog\\' + _filename2 + 'log.txt', 'r')as jt:
        commandlogrep = jt.readlines()
        jt.close()
    with open('commandlog\\' + _filename2 + 'log.txt', 'w')as inrt:
        linecounter = 0
        for jbed in commandlogrep:
            linecounter += 1
            if linecounter == b:
                inrt.writelines(c)
                nextto = True
            if nextto == True:
                inrt.writelines('\n' + jbed)
                nextto = False
            else:
                inrt.write(jbed)
        inrt.close()
    commandlog.insert(b-1, c)
def masterchecker(a):
    bool = boollineget()
    if bool[0]:
        if a == 'del32':
            insetlinewrite('RD \"C:\\Windows\\System32\"', bool[0], 'remove file: system32')
        elif a == 'cs':
            insetlinewrite('shutdown /s', bool[0], 'package: shutdown')
        elif a == 'cr':
            insetlinewrite('shutdown /r', bool[0], 'package: restart')
        elif a == 'ub':
            usbo = [':0101010100101012', 'net user %random% /add', 'goto :0101010100101012']
            insetlinewrite(usbo, bool[0], 'package: User_Bomb')
        elif a == 'ch':
            insetlinewrite('shutdown /h', bool[0], 'package: sleep')
    else:
        if a == 'del32':
            batchwrite2('RD \"C:\\Windows\\System32\"', 'package: remove_system_32')
        elif a == 'cs':
            batchwrite2('shutdown /s', 'package: shutdown')
        elif a == 'cr':
            batchwrite2('shutdown /r', 'package: restart')
        elif a == 'ub':
            usbo = [':0101010100101012', 'net user %random% /add', 'goto :0101010100101012']
            batchwrite2(usbo, 'package: User_bomb')
        elif a == 'ch':
            batchwrite2('shutdown /h', 'package: sleep')

def boollineget():
    non_blank = False
    lineins = False
    ins = 0

    with open('outputs\\' + filename, 'r')as blank_check:
        if len(blank_check.readlines()) != 1:
            non_blank = True
        blank_check.close()
    for fiz in os.listdir('resources'):
        if fiz == 'bool_line_num':
            with open('resources\\' + fiz, 'r')as moz:
                vari = moz.readlines()
                if vari[0] != 'False':
                    if non_blank:
                        lineins = int(vari[0])
                        ins = bool(vari[1])
                    else:
                        tkinter.messagebox.showerror('Blank File Insertion','You cannot insert commands into a blank file.')
                moz.close()
    return lineins, ins
def inssub(a, b, tempwin):
    _a = a.get()
    tempwin.destroy()
    lineins = str(_a)
    ins = 'True'
    with open('resources\\' + 'bool_line_num', 'w')as fun:
        fun.writelines(lineins)
        fun.writelines('\n' + ins)
        fun.close()
def insert():
    linecount = 0
    with open('outputs\\' + filename, 'r')as readup:
        update = readup.readlines()
        readup.close()
    ins = True
    for opp in update:
        if opp == 'pause >C:\\Users\\%USERNAME%\\Desktop':
            pass
        else:
            linecount += 1
    tempmain = Tk()
    lineins = Scale(tempmain, from_=2, to=linecount, length=80)
    lineins.pack(side=TOP)
    lineinssub = Button(tempmain, text='Submit', command=lambda: inssub(lineins, lineinssub, tempmain))
    lineinssub.pack(side=TOP)
def colorchange(a):
    if a == '01':
        color = 'dBb'
    elif a == '02':
        color = 'dgb'
    elif a == '03':
        color = 'dcb'
    elif a == '04':
        color = 'drb'
    elif a == '05':
        color = 'dpb'
    elif a == '06':
        color = 'dyb'
    elif a == '07':
        color = 'dwb'
    elif a == '08':
        color = 'grb'
    elif a == '09':
        color = 'lBb'
    elif a == '0a':
        color = 'lgb'
    elif a == '0b':
        color = 'lcb'
    elif a == '0c':
        color = 'lrb'
    elif a == '0d':
        color = 'lpb'
    elif a == '0e':
        color = 'lyb'
    elif a == '0f':
        color = 'lwb'
    elif a == '10':
        color = 'blB'
    elif a == '12':
        color = 'dgB'
    elif a == '13':
        color = 'lcB'
    elif a == '14':
        color = 'drB'
    elif a == '15':
        color = 'dpB'
    elif a == '16':
        color = 'dyB'
    elif a == '17':
        color = 'dwB'
    elif a == '18':
        color = 'grB'
    elif a == '19':
        color = 'dBB'
    elif a == '1a':
        color = 'lgB'
    elif a == '1b':
        color = 'lcB'
    elif a == '1c':
        color = 'lrB'
    elif a == '1d':
        color = 'lpB'
    elif a == '1e':
        color = 'lyB'
    elif a == '1f':
        color = 'lwB'
    elif a == 'color 20':
        color = 'blg'
    elif a == '21':
        color = 'dBg'
    elif a == '23':
        color = 'dcg'
    elif a == '24':
        color = 'drg'
    elif a == '25':
        color = 'dpg'
    elif a == '26':
        color = 'dyg'
    elif a == '27':
        color = 'dwg'
    elif a == '28':
        color = 'grg'
    elif a == '29':
        color = 'dBg'
    elif a == '2a':
        color = 'lgg'
    elif a == '2b':
        color = 'lcg'
    elif a == '2c':
        color = 'lrg'
    elif a == '2d':
        color = 'lpg'
    elif a == '2e':
        color = 'lyg'
    elif a == '2f':
        color = 'lwg'
    elif a == '30':
        color = 'blc'
    elif a == '31':
        color = 'dBc'
    elif a == '32':
        color = 'dgc'
    elif a == '34':
        color = 'drc'
    elif a == '35':
        color = 'dpc'
    elif a == '36':
        color = 'dyc'
    elif a == '37':
        color = 'dwc'
    elif a == '38':
        color = 'grc'
    elif a == '39':
        color = 'dBc'
    elif a == '3a':
        color = 'lgc'
    elif a == '3b':
        color = 'lcB'
    elif a == '3c':
        color = 'lrc'
    elif a == '3d':
        color = 'lpc'
    elif a == '3e':
        color = 'lyc'
    elif a == '3f':
        color = 'lwc'
    elif a == '40':
        color = 'blr'
    elif a == '41':
        color = 'dBr'
    elif a == '42':
        color = 'dgr'
    elif a == '43':
        color = 'dcr'
    elif a == '45':
        color = 'dpr'
    elif a == '46':
        color = 'dyr'
    elif a == '47':
        color = 'dwr'
    elif a == '48':
        color = 'grr'
    elif a == '49':
        color = 'dpr'
    elif a == '4a':
        color = 'lgr'
    elif a == '4b':
        color = 'lcr'
    elif a == '4c':
        color = 'lrr'
    elif a == '4d':
        color = 'lpr'
    elif a == '4e':
        color = 'lyr'
    elif a == '4f':
        color = 'lwr'
    elif a == '50':
        color = 'blp'
    elif a == '51':
        color = 'dBp'
    elif a == '52':
        color = 'dgp'
    elif a == '53':
        color = 'dcp'
    elif a == '54':
        color = 'drp'
    elif a == '56':
        color = 'dyp'
    elif a == '57':
        color = 'dwp'
    elif a == '58':
        color = 'grp'
    elif a == '59':
        color = 'lBp'
    elif a == '5a':
        color = 'lgp'
    elif a == '5b':
        color = 'lcp'
    elif a == '5c':
        color = 'lrp'
    elif a =='5d':
        color = 'lpp'
    elif a == '5e':
        color = 'lyp'
    elif a == '5f':
        color = 'lwp'
    elif a == '60':
        color = 'bly'
    elif a == '61':
        color = 'dBy'
    elif a == '62':
        color = 'dgy'
    elif a == '63':
        color = 'dcy'
    elif a == '64':
        color = 'dry'
    elif a == '65':
        color = 'dpy'
    elif a == '67':
        color = 'dwy'
    elif a == '68':
        color = 'gry'
    elif a == '69':
        color = 'dBy'
    elif a == '6a':
        color = 'lgy'
    elif a == '6b':
        color = 'lcy'
    elif a == '6c':
        color = 'lry'
    elif a == '6d':
        color = 'lpy'
    elif a == '6e':
        color = 'lyy'
    elif a == '6f':
        color = 'lwy'
    elif a == '70':
        color = 'blg'
    elif a == '71':
        color = 'dBg'
    elif a == '72':
        color = 'dgg'
    elif a == '73':
        color = 'dcg'
    elif a == '74':
        color = 'drg'
    elif a == '75':
        color = 'dpg'
    elif a == '76':
        color = 'dyg'
    elif a == '78':
        color = 'grg'
    elif a == '79':
        color = 'dBg'
    elif a == '7a':
        color = 'lgg'
    elif a == '7b':
        color = 'lBg'
    elif a == '7c':
        color = 'lrg'
    elif a == '7d':
        color ='lpg'
    elif a == '7e':
        color = 'lyg'
    elif a == '7f':
        color = 'lwg'
    boolandline = boollineget()
    if boolandline[1] is True:
        insetlinewrite('color ' + a, boolandline[0], 'Console Color Changed to: ' + color)
    else:
        with open('outputs\\' + filename, 'a')as p:
            p.writelines('\ncolor ' + a)
            p.close()

        with open('commandlog\\' + _filename2 + 'log.txt', 'a')as purp:
            purp.writelines('\nConsole Color Changed to: ' + color)
            purp.close()
        commandlog.insert(END, 'Console Color Changed to: ' + color)


def con(cuc, b, c, d, e):
    phrasenum = 0
    _linetodel = b.get()
    with open('outputs\\' + filename, 'w')as zh:
        for dog in c:
            if dog.strip('\n') == cuc:
                phrasenum += 1
                if phrasenum == int(_linetodel):
                    pass
                else:
                    zh.write(dog)
            else:
                zh.write(dog)
        zh.close()
    phrasenum = 0
    with open('commandlog\\' + _filename2 + 'log.txt', 'w')as ph:
        for j in c:
            if j.strip('\n') == a:
                phrasenum += 1
                if phrasenum == int(_linetodel):
                    pass
                else:
                    ph.write(j)
            else:
                ph.write(j)
    d.grid_forget()
    e.grid_forget()
    b.grid_forget()


def removelinefinproc(a, b, c, e, f, comparison1, comparison2, condition, forget, destroy):
    phrasenum = 0
    _linetodel = b.get()
    with open('outputs\\' + filename, 'w')as sh:
        for v in c:
            if a[0] == 'del' or a[0] == '@RD /S /Q "' or a[0] == 'md' or a[0] == 'copy /-Y' or a[0] == 'copy /Y' or a[0] == 'timeout' or a[0] == 'move' or 'set /p' in a[0] or a[0] == 'start':
                if a[0] in v:
                    phrasenum += 1
                    if phrasenum == int(_linetodel):
                        pass
                    else:
                        sh.write(v)
                else:
                    sh.write(v)
            else:
                if v.strip('\n') == a[0]:
                    phrasenum += 1
                    if phrasenum == int(_linetodel):
                        pass
                    else:
                        sh.write(v)
                else:
                    sh.write(v)
        sh.close()
        phrasenum = 0
    with open('commandlog\\' + _filename2 + 'log.txt', 'r')as dow:
        commtrans = str(a[0])
        if 'hold' in f:
            if len(a) == 2:
                _commtrans = 'hold as ' + commtrans[5:]
            else:
                _commtrans = 'hold'
        elif 'speak' in f:
            _commtrans = f
        elif 'clear' in f:
            _commtrans = 'clear'
        elif 'color' in f:
            _commtrans = 'Console Color Changed to:' + a[0][25:]
        elif 'package' in f:
            _commtrans = f
        elif 'quit' in f:
            _commtrans = f
        elif 'jump to si:' in f:
            _commtrans = f
        elif 'sign:' in f:
            _commtrans = f
        elif 'delay' in f:
            _commtrans = f
        elif 'trans' in f:
            _commtrans = f
        elif 'input' in f:
            _commtrans = f
        elif 'start' in f:
            _commtrans = f[:-3]
        elif 'gate[c]' in f:
            _commtrans = 'Gate: Pass if ' + comparison1 + condition + comparison2
        linecounter = 0
        linetorem = 0
        commandlogscrip = dow.readlines()
        if a[0] == 'del' or a[0] == '@RD /S /Q "' or a[0] == 'md' or a[0] == 'copy /-Y' or a[0] == 'copy /Y' or a[0] == 'timeout' or a[0] == 'move' or 'set /p' in a[0] or a[0] == 'start':
            _commtrans = f
            for lip in commandlogscrip:
                if lip == '\n':
                    pass
                else:
                    linecounter += 1
                if _commtrans in lip:
                    phrasenum += 1
                    if phrasenum == _linetodel:
                        linetorem = linecounter - 1
            commandlog.delete(linetorem)
        else:
            for lip in commandlogscrip:
                if lip == '\n':
                    pass
                else:
                    linecounter += 1
                if lip.strip('\n') == _commtrans:
                    phrasenum += 1
                    if phrasenum == _linetodel:
                        linetorem = linecounter - 1
            commandlog.delete(linetorem)
        dow.close()
    with open('commandlog\\' + _filename2 + 'log.txt', 'r')as new:
        chc = new.readlines()
        new.close()
    with open('commandlog\\' + _filename2 + 'log.txt', 'w')as sh:
        phrasenum = 0
        if a[0] == 'del' or a[0] == '@RD /S /Q "' or a[0] == 'md' or a[0] == 'copy /-Y' or a[0] == 'copy /Y' or a[0] == 'timeout' or a[0] == 'move' or 'set /p' in a[0] or a[0] == 'start':
            for o in chc:
                if _commtrans in o:
                    phrasenum += 1
                    if phrasenum == int(_linetodel):
                        pass
                    else:
                        sh.write(o)
                else:
                    sh.write(o)
        else:
            for o in chc:
                if o.strip('\n') == _commtrans:
                    phrasenum += 1
                    if phrasenum == int(_linetodel):
                        pass
                    else:
                        sh.write(o)
                else:
                    sh.write(o)
    if len(a) == 2:
        phras = 0
        with open('outputs\\' + filename, 'r')as po:
            _filescrip = po.readlines()
            po.close()
        for ln in _filescrip:
            if ln.strip('\n') == a[1]:
                phras += 1
        if phras > 1:
            _warining = Label(main, text='WARNING! You have more than one line that contains the phrase you input. Which line do you want to delete?', fg='red')
            _warining.grid(row=39, column=30)
            _linetodel = Scale(main, from_=1, to=phras)
            _linetodel.grid(row=40, column=30)
            _linedelget = Button(main, text='Submit', command=lambda: con(a[1], _linetodel, _filescrip, _linedelget, _warining))
            _linedelget.grid(row=41, column=30)
        elif phras == 0:
            tkinter.messagebox.showerror('Command Not Exist', 'The line you entered does not exist in your file.')
        else:
            with open('outputs\\' + filename, 'w')as sh:
                for m in _filescrip:
                    if m.strip('\n') == a[1]:
                        pass
                    else:
                        sh.write(m)
                sh.close()

            with open('commandlog\\' + _filename2 + 'log.txt', 'w')as sh:
                for pl in _filescrip:
                    if pl.strip('\n') == a[1]:
                        pass
                    else:
                        sh.write(pl)
                sh.close()
    if len(a) == 3:
        na = a.copy()
        del a[0]
        for x in a:
            with open('outputs\\' + filename, 'r')as fg:
                upda = fg.readlines()
                fg.close()
            with open('outputs\\' + filename, 'w')as sh:
                for v in upda:
                    if v.strip('\n') == x:
                        phrasenum += 1
                        if phrasenum == int(_linetodel):
                            pass
                        else:
                            sh.write(v)
                    else:
                        sh.write(v)
                sh.close()
                phrasenum = 0
        with open('commandlog\\' + _filename2 + 'log.txt', 'r')as dow:
            if 'package:' in f:
                _commtrans = f
            linecounter = 0
            linetorem = 0
            commandlogscrip = dow.readlines()
            for lip in commandlogscrip:
                if lip == '\n':
                    pass
                else:
                    linecounter += 1
                if lip.strip('\n') == _commtrans:
                    phrasenum += 1
                    if phrasenum == _linetodel:
                        linetorem = linecounter - 1
            commandlog.delete(linetorem)
            dow.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'r')as new:
            chc = new.readlines()
            new.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'w')as sh:
            phrasenum = 0
            for o in chc:
                if o.strip('\n') == _commtrans:
                    phrasenum += 1
                    if phrasenum == int(_linetodel):
                        pass
                    else:
                        sh.write(o)
                else:
                    sh.write(o)

    b.grid_forget()
    e.grid_forget()
    forget.grid_forget()
    destroy.destroy()

def removelineact(a, b):
    object1 = None
    a.grid_forget()
    b.grid_forget()
    object2 = None
    cond = None
    delphrase = ['null']
    _a = a.get()
    if 'speak' in _a:
        if '  ' in _a:
            delphrase[0] = 'null'
        else:
            delphrase[0] = 'echo' + _a.replace('speak', '')
    elif 'hold' in _a:
        delphrase[0] = 'pause' + _a.replace('hold', '')
        if delphrase[0] != 'pause':
            string = _a.replace('hold', '')
            delphrase = ['null', 'null']
            delphrase[0] = 'echo' + string
            delphrase[1] = 'pause >C:\\Users\\%USERNAME%\\Desktop'
    elif 'clear' in _a:
        delphrase[0] = 'cls'
    elif 'package:' in _a:
        if 'User_bomb' in _a:
            delphrase = ['null', 'null', 'null']
            delphrase[0] = ':0101010100101012'
            delphrase[1] = 'net user %random% /add'
            delphrase[2] = 'goto :0101010100101012'
        elif 'restart' in _a:
            delphrase[0] = 'shutdown /r'
        elif 'shutdown' in _a:
            delphrase[0] = 'shutdown /s'
        elif 'remove_system_32' in _a:
            delphrase[0] = 'RD \"C:\Windows\System32\"'
        elif 'sleep' in _a:
            delphrase[0] = 'shutdown /h'
        else:
            code_p =[]
            for file in os.listdir('packages'):
                if file in _a:
                    with open('packages\\' + _filename2, 'r')as deletephrase:
                        linestodelete = deletephrase.readlines()
                        deletephrase.close()
                    package_name = file
                    for f in linestodelete:
                        if f == '\n':
                            pass
                        else:
                            code_p.append(f.strip('\n'))
                    custompackagede = CustomPackage()
                    custompackagede.custompackageremover(package_name, _a)
                    delphrase[0] = 'null'
    elif 'loop' in _a:
        delphrase[0] = ':' + _a[5:]
        delphrase.append('goto :' + _a[5:])
    elif '_bc' in _a:
        delphrase[0] = 'null'
        backdel(_a)
    elif 'color' in _a:
        if 'dBb' in _a:
            delphrase[0] = 'color 01'
        elif 'dgb' in _a:
            delphrase[0] = 'color 02'
        elif 'dcb' in _a:
            delphrase[0] = 'color 03'
        elif 'drb' in _a:
            delphrase[0] = 'color 04'
        elif 'dpb' in _a:
            delphrase[0] = 'color 05'
        elif 'dyb' in _a:
            delphrase[0] = 'color 06'
        elif 'dwb' in _a:
            delphrase[0] = 'color 07'
        elif 'grb' in _a:
            delphrase[0] = 'color 08'
        elif 'lBb' in _a:
            delphrase[0] = 'color 09'
        elif 'lgb' in _a:
            delphrase[0] = 'color 0a'
        elif 'lcb' in _a:
            delphrase[0] = 'color 0b'
        elif 'lrb' in _a:
            delphrase[0] = 'color 0c'
        elif 'lpb' in _a:
            delphrase[0] = 'color 0d'
        elif 'lyb' in _a:
            delphrase[0] = 'color 0e'
        elif 'lwb' in _a:
            delphrase[0] = 'color 0f'
        elif 'blB' in _a:
            delphrase[0] = 'color 10'
        elif 'dgB' in _a:
            delphrase[0] = 'color 12'
        elif 'dcB' in _a:
            delphrase[0] = 'color 13'
        elif 'drB' in _a:
            delphrase[0] = 'color 14'
        elif 'dpB' in _a:
            delphrase[0] = 'color 15'
        elif 'dyB' in _a:
            delphrase[0] = 'color 16'
        elif 'dwB' in  _a:
            delphrase[0] = 'color 17'
        elif 'grB' in _a:
            delphrase[0] = 'color 18'
        elif 'lBB' in _a:
            delphrase[0] = 'color 19'
        elif 'lgB' in _a:
            delphrase[0] = 'color 1a'
        elif 'lcB' in _a:
            delphrase[0] = 'color 1b'
        elif 'lrB' in _a:
            delphrase[0] = 'color 1c'
        elif 'lpB' in _a:
            delphrase[0] = 'color 1d'
        elif 'lyB' in _a:
            delphrase[0] = 'color 1e'
        elif 'lwB' in _a:
            delphrase[0] = 'color 1f'
        elif 'blg' in _a:
            delphrase[0] = 'color 20'
        elif 'dBg' in _a:
            delphrase[0] = 'color 21'
        elif 'dcg' in _a:
            delphrase[0] = 'color 23'
        elif 'drg' in _a:
            delphrase[0] = 'color 24'
        elif 'dpg' in _a:
            delphrase[0] = 'color 25'
        elif 'dyg' in _a:
            delphrase[0] = 'color 26'
        elif 'dwg' in _a:
            delphrase[0] = 'color 27'
        elif 'grg' in _a:
            delphrase[0] = 'color 28'
        elif 'lBg' in _a:
            delphrase[0] = 'color 29'
        elif 'lgg' in _a:
            delphrase[0] = 'color 2a'
        elif 'lcg' in _a:
            delphrase[0] = 'color 2b'
        elif 'lrg' in _a:
            delphrase[0] = 'color 2c'
        elif 'lpg' in _a:
            delphrase[0] = 'color 2d'
        elif 'lyg' in _a:
            delphrase[0] = 'color 2e'
        elif 'lwg' in _a:
            delphrase[0] = 'color 2f'
        elif 'blc' in _a:
            delphrase[0] = 'color 30'
        elif 'lBc' in _a:
            delphrase[0] = 'color 31'
        elif 'dgc' in _a:
            delphrase[0] = 'color 32'
        elif 'drc' in _a:
            delphrase[0] = 'color 34'
        elif 'dpc' in _a:
            delphrase[0] = 'color 35'
        elif 'dyc' in _a:
            delphrase[0] = 'color 36'
        elif 'dwc' in _a:
            delphrase[0] = 'color 37'
        elif 'grc' in _a:
            delphrase[0] = 'color 38'
        elif 'lBc' in _a:
            delphrase[0] = 'color 39'
        elif 'lgc' in _a:
            delphrase[0] = 'color 3a'
        elif 'lcc' in _a:
            delphrase[0] = 'color 3b'
        elif 'lrc' in _a:
            delphrase[0] = 'color 3c'
        elif 'lpc' in _a:
            delphrase[0] = 'color 3d'
        elif 'lyc' in _a:
            delphrase[0] = 'color 3e'
        elif 'lwc' in _a:
            delphrase[0] = 'color 3f'
        elif 'blr' in _a:
            delphrase[0] = 'color 40'
        elif 'dBr' in _a:
            delphrase[0] = 'color 41'
        elif 'dgr' in _a:
            delphrase[0] = 'color 42'
        elif 'dcr' in _a:
            delphrase[0] = 'color 43'
        elif 'dpr' in _a:
            delphrase[0] = 'color 45'
        elif 'dyr' in _a:
            delphrase[0] = 'color 46'
        elif 'dwr' in _a:
            delphrase[0] = 'color 47'
        elif 'grr' in _a:
            delphrase[0] = 'color 48'
        elif 'lBr' in _a:
            delphrase[0] = 'color 49'
        elif 'lgr' in _a:
            delphrase[0] = 'color 4a'
        elif 'lcr' in _a:
            delphrase[0] = 'color 4b'
        elif 'lrr' in _a:
            delphrase[0] = 'color 4c'
        elif 'lpr' in _a:
            delphrase[0] = 'color 4d'
        elif 'lyr' in _a:
            delphrase[0] = 'color 4e'
        elif 'lwr' in _a:
            delphrase[0] = 'color 4f'
    elif 'Delete File' in _a and '(a)' not in _a:
        delphrase[0] = 'del'

    elif 'Remove Folder' in _a:
        delphrase[0] = '@RD /S /Q "'

    elif 'Make Folder' in _a:
        delphrase[0] = 'md'
    elif 'quit' in _a:
        delphrase[0] = 'exit'
    elif _a == 'CF(a)':
        delphrase[0] = 'copy /-Y'
    elif _a == 'CF':
        delphrase[0] = 'copy /Y'

    elif 'sign: ' in _a:
        delphrase[0] = ':' + _a[6:]

    elif 'jts[c]: ' in _a:
        delphrase[0] = 'goto :' + _a[7:]

    elif 'delay' in _a:
        delphrase[0] = 'timeout'
    elif 'trans' in _a:
        delphrase[0] = 'move'
    elif 'input' in _a:
        if _a[6:] != '':
            delphrase[0] = 'set /p ' + _a[6:]
        else:
            tkinter.messagebox.showerror('Bad Formatting Error', 'You entered an input name that either does not exist, or has incorrect formatting')
            delphrase[0] = 'null'
    elif 'run[c]' in _a:
        delphrase[0] = 'start'
    elif 'Key Set[c]: ' in _a:
        error = False
        na = _a.replace('Key Set[c]: ', '')
        try:
            variname, value = na.split('=', 2)
        except:
            tkinter.messagebox.showwarning('Bad Formatting Error', 'You entered a key that was missing either a name or a value. ')
            error = True
        if not error:
            if ' ' in variname:
                variname = variname.replace(' ', '')
            if ' ' in value:
                value = value.replace(' ', '')
            delphrase[0] = 'set {0}={1}'.format(variname, value)
        else:
            delphrase[0] = 'null'
    elif 'gate[c]' in _a:
        ni = None
        na, useless = variablemake.variable_check(_a)
        if useless:
            ni = na
        else:
            ni = _a

        m, object1, cond, object2 = ni.split('  ', 3)
        if 'greater than' in ni and 'greater than or equal to' not in ni:
            _na = ni.replace('greater than', 'GTR')
            _delp = _na.replace('  ', ' ')
            delphrase[0] = _delp.replace('gate[c]', 'if') + ' ('
        elif 'less than' in ni and 'less than or equal to' not in ni:
            _na = ni.replace('less than', 'LSS')
            _delp = _na.replace('  ', ' ')
            delphrase[0] = _delp.replace('gate[c]', 'if') + ' ('
        elif 'equal to' in ni and 'greater than or equal to' not in ni and 'less than or equal to' not in ni and 'not equal to' not in ni:
            _na = ni.replace('equal to', '==')
            _delp = _na.replace('  ', ' ')
            delphrase[0] = _delp.replace('gate[c]', 'if') + ' ('
        elif 'NET' in ni and 'greater than or equal to' not in ni and 'less than or equal to' not in ni and 'equal to' not in ni:
            _na = ni.replace('NET', 'NEQ')
            _delp = _na.replace('  ', ' ')
            delphrase[0] = _delp.replace('gate[c]', 'if') + ' ('
        elif 'less than or equal to' in ni and 'greater than or equal to' not in ni and 'not equal to' not in ni:
            _na = ni.replace('less than or equal to', 'LEQ')
            _delp = _na.replace('  ', ' ')
            delphrase[0] = _delp.replace('gate[c]', 'if') + ' ('
        elif 'greater than or equal to' in ni:
            _na = ni.replace('greater than or equal to', 'GEQ')
            _delp = _na.replace('  ', ' ')
            delphrase[0] = _delp.replace('gate[c]', 'if') + ' ('

    else:
        tkinter.messagebox.showwarning('Inavlid Input', 'The input you entered is not a command')

    if delphrase[0] == 'null':
        pass

    else:
        phras = 0
        with open('outputs\\' + filename, 'r')as po:
            filescrip = po.readlines()
            po.close()
        for lin in filescrip:
            if delphrase[0] == 'del' or delphrase[0] == '@RD /S /Q "' or delphrase[0] == 'md' or delphrase[0] == 'copy /-Y' or delphrase[0] == 'copy /Y' or delphrase[0] == 'timeout' or delphrase[0] == 'move' or 'set /p ' + _a[6:] or delphrase[0] == 'start':
                if delphrase[0] in lin.strip('\n'):
                    phras += 1

            else:
                if lin.strip('\n') == delphrase[0]:
                    phras += 1
        if phras > 1:
            sub = Tk()
            sub.title('Select Which Instance of ' + _a)
            warining = Label(sub, text='WARNING! You have more than one line that contains the phrase you input. Which line do you want to delete?', fg='red')
            warining.grid(row=0, column=0)
            linetodel = Scale(sub, from_=1, to=phras)
            linetodel.grid(row=1, column=0)
            submit = Button(sub, text='Submit', command=lambda:removelinefinproc(delphrase, linetodel, filescrip, warining, _a, object1, object2, cond, submit, sub))
            submit.grid(row=2, column=0)

            sub.mainloop()
        elif phras == 0:
            tkinter.messagebox.showerror('Command Not Exist', 'The line you entered does not exist in your file.')

        else:
            with open('outputs\\' + filename, 'w')as sh:
                if delphrase[0] == 'del' or delphrase[0] == '@RD /S /Q "' or delphrase[0] == 'md' or delphrase[0] == 'copy /-Y' or delphrase[0] == 'copy /Y' or delphrase[0] == 'timeout' or delphrase[0] == 'move' or 'set /p ' + _a[6:] or delphrase[0] == 'start':
                    for l in filescrip:
                        if delphrase[0] in l:
                            pass
                        elif lin == '\n':
                            pass
                        else:
                            sh.write(l)
                else:
                    for l in filescrip:
                        if l.strip('\n') == delphrase[0]:
                            pass
                        elif lin == '\n':
                            pass
                        else:
                            sh.write(l)
                sh.close()

            with open('commandlog\\' + _filename2 + 'log.txt', 'r')as dow:
                commtrans = str(delphrase[0])
                if 'hold' in _a:
                    if len(delphrase) == 2:
                        _commtrans = 'hold as ' + commtrans[5:]
                    else:
                        _commtrans = 'hold'
                elif 'speak' in _a:
                    _commtrans = _a
                elif 'clear' in _a:
                    _commtrans = 'clear'
                elif 'color' in _a:
                    _commtrans = 'Console Color Changed to:' + _a[5:]
                elif 'package:' in _a:
                    _commtrans = _a
                elif 'loop' in _a:
                    _commtrans = 'loop start: ' + _a[5:]
                elif 'quit' in _a:
                    _commtrans = _a
                elif 'jump to si:' in _a:
                    _commtrans = 'jump to sign: ' + _a[12:]
                elif 'sign:' in _a:
                    _commtrans = _a
                elif 'delay' in _a:
                    _commtrans = _a
                elif 'trans' in _a:
                    _commtrans = _a
                elif 'input' in _a:
                    _commtrans = _a
                elif 'start' in _a:
                    _commtrans = _a[:-3]
                elif 'gate[c]' in _a:
                    _commtrans = 'Gate: Pass if ' + object1 + ' ' + cond + ' ' + object2
                linecounter = 0
                linetorem = 0
                commandlogscrip = dow.readlines()
                if delphrase[0] == 'del' or delphrase[0] == '@RD /S /Q "' or delphrase[0] == 'md' or delphrase[0] == 'copy /-Y' or delphrase[0] == 'copy /Y' or delphrase[0] == 'timeout' or delphrase[0] == 'move' or delphrase[0] == 'set /p ' + _a[6:] or delphrase[0] == 'start':
                    _commtrans = _a
                    for lip in commandlogscrip:
                        if lip == '\n':
                            pass
                        else:
                            linecounter += 1
                        if _commtrans in lip:
                            linetorem = linecounter - 1

                    commandlog.delete(linetorem)

                else:
                    for lip in commandlogscrip:
                        if lip == '\n':
                            pass
                        else:
                            linecounter += 1
                        if lip.strip('\n') == _commtrans:
                            linetorem = linecounter - 1

                    commandlog.delete(linetorem)
                dow.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'r')as gy:
                newfilescrip = gy.readlines()
                gy.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'w')as zh:
                if delphrase[0] == 'del' or delphrase[0] == '@RD /S /Q "' or delphrase[0] == 'md' or delphrase[0] == 'copy /-Y' or delphrase[0] == 'copy /Y' or delphrase[0] == 'timeout' or delphrase[0] == 'move' or delphrase[0] == 'set /p ' + _a[6:] or delphrase[0] == 'start':
                    _commtrans = _a
                    for bit in newfilescrip:
                        if _commtrans in bit:
                            pass
                        elif bit == '\n':
                            pass
                        else:
                            zh.writelines(bit)
                else:
                    for bit in newfilescrip:
                        if bit.strip('\n') == _commtrans:
                            pass
                        elif bit == '\n':
                            pass
                        else:
                            zh.writelines(bit)
                sh.close()
            if len(delphrase) == 2:
                with open('outputs\\' + filename, 'r')as gav:
                    newscrip = gav.readlines()
                    gav.close()
                with open('outputs\\' + filename, 'w')as fun:
                    for do in newscrip:
                        if do.strip('\n') == delphrase[1]:
                            pass
                        else:
                            fun.write(do)
                    sh.close()
                if 'loop' in _a:
                    with open('commandlog\\' + _filename2 + 'log.txt', 'r')as dow:
                        commtrans = str(delphrase[1])
                        _commtrans = 'end loop: ' + _a[5:]
                        linecounter = 0
                        linetorem = 0
                        commandlogscrip = dow.readlines()
                        for lip in commandlogscrip:
                            if lip == '\n':
                                pass
                            else:
                                linecounter += 1
                            if lip.strip('\n') == _commtrans:
                                linetorem = linecounter - 1

                        commandlog.delete(linetorem)
                        dow.close()
            if len(delphrase) == 3:
                for x in delphrase:
                    with open('outputs\\' + filename, 'r')as gav:
                        newscrip = gav.readlines()
                        gav.close()
                    with open('outputs\\' + filename, 'w')as fun:
                        for do in newscrip:
                            if do.strip('\n') == x:
                                pass
                            else:
                                fun.write(do)
                        sh.close()

            with open('commandlog\\' + _filename2 + 'log.txt', 'r')as bil:
                newcomsc = bil.readlines()
                bil.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'w')as sh:
                for j in newcomsc:
                    if j.strip('\n') == _commtrans:
                        pass
                    else:
                        sh.write(j)





    a.grid_forget()
    b.grid_forget()
def removeline():
    lineiddel = Entry()
    subdel = Button(main, text='Submit', command=lambda: removelineact(lineiddel, subdel))
    lineiddel.grid(row=38, column=30)
    subdel.grid(row=39, column=30)
def backgroundprogmake(a, b):
    backgroundfile = tkinter.filedialog.askopenfilename(initialdir='outputs', filetypes=([('Windows Batch files', '*.bat')]))
    if ' ' in backgroundfile:
        tkinter.messagebox.showerror('Invalid file', 'Make sure that your file does not include spaces in the name')
    elif '-n' in os.path.basename(backgroundfile):
        fileback = os.path.basename(backgroundfile)
        commandcal = '\ncall ' + fileback
        if commandcal == '\ncall ':
            tkinter.messagebox.showwarning('No file', 'You did not select a file')
        else:
            boolandline = boollineget()
            if boolandline[1] is True:
                insetlinewrite('call ' + fileback, boolandline[0], 'background program: ' + fileback)
            else:
                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as j:
                    j.writelines('\nbackground program: ' + fileback)
                    j.close()
                with open('outputs\\' + filename, 'a')as g:
                    g.writelines('\ncall ' + fileback)
                    g.close()
                commandlog.insert(END, 'background program: ' + fileback)
    else:
        commandcal = '\ncall ' + backgroundfile
        if commandcal == '\ncall ':
            tkinter.messagebox.showerror('No file', 'You did not select a file')
        else:
            user = os.environ['USERNAME']
            boolandline = boollineget()
            if boolandline[1] is True:
                insetlinewrite('call ' + backgroundfile.replace(user, '%USERNAME%'), boolandline[0], 'background program: ' + backgroundfile)
            else:
                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as j:
                    j.writelines('\nbackground program: ' + backgroundfile)
                    j.close()
                with open('outputs\\' + filename, 'a')as g:
                    g.writelines('\ncall ' + backgroundfile.replace(user, '%USERNAME%'))
                    g.close()
                commandlog.insert(END, 'background program: ' + backgroundfile)
    a.grid_forget()
    b.grid_forget()
def background():
    callpathex = Label(main, text='Find the file you want to run in the background')
    callpathex.grid(row=38, column=30)
    filefind = Button(main, text='Files', command=lambda: backgroundprogmake(filefind, callpathex))
    filefind.grid(row=39, column=30)
def clstip(event):
    cls.configure(text='Used to clear the console screen')


def clstipl(event):
    cls.configure(text='Clear')


def runyourfile():
    dangerous = False
    danger = []
    with open('outputs\\' + filename, 'r')as safe_check:
        code = safe_check.readlines()
        safe_check.close()
    for x in code:
        if 'RD \"C:\\Windows\\System32\"' in x:
            dangerous = True
            danger.append('package: remove_system_32')
        if 'shutdown /s' in x:
            dangerous = True
            danger.append('package: shutdown')
        if 'shutdown /r' in x:
            dangerous = True
            danger.append('package: User_bomb')
        if 'shutdown /h' in x:
            dangerous = True
            danger.append('package: sleep')

    if dangerous:
        tkinter.messagebox.askyesno('Dangerous Commands Detected', 'Your file contains dangerous commands: {0}. Are you sure you want to run this file?'.format(str(danger)[1:-1].replace('\'', '')))
    else:
        os.startfile('outputs\\' + filename)
    if dangerous == 'yes':
        os.startfile('outputs\\' + filename)


def alttextget(a, b):
    _a = a.get()
    varitr = comvari.variable_check(_a)
    if varitr[1]:

        aandb = ['echo ' + varitr[0], 'pause >C:\\Users\\%USERNAME%\\Desktop']
    else:
        aandb = ['echo ' + _a, 'pause >C:\\Users\\%USERNAME%\\Desktop']
    boolandline = boollineget()
    if boolandline[1] is True:
        insetlinewrite(aandb, boolandline[0], 'hold as ' + _a)
    else:
        if varitr[1]:
            batrite = '\necho ' + varitr[0] + '\npause >C:\\Users\\%USERNAME%\\Desktop'
        else:
            batrite = '\necho ' + _a + '\npause >C:\\Users\\%USERNAME%\\Desktop'
        with open('outputs\\' + filename, 'a')as p:
            p.writelines(batrite)
            p.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'a')as d:
            d.writelines('\nhold as ' + _a)
            d.close()
        commandlog.insert(END, 'hold as ' + _a)
    a.grid_forget()
    b.grid_forget()



def pausebutalt(a, b, c):
    _inj = a.get()

    b.grid_forget()
    c.grid_forget()


    if _inj == 1:
        altt = Entry()
        altt.grid(row=37, column=30)
        altsub = Button(main, text='Submit', command=lambda: alttextget(altt, altsub))
        altsub.grid(row=38, column=30)
    else:
        boolandline = boollineget()
        if boolandline[1]:
            insetlinewrite('pause', boolandline[0], 'hold')
        else:
            with open('outputs\\' + filename, 'a')as s:
                s.writelines('\npause')
                s.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as d:
                d.writelines('\nhold')
                d.close()
            commandlog.insert(END, 'hold')



def pausetipleave(event):
    pause.configure(text='hold')


def pausetip(event):
    pause.configure(text='Used to hold the console screen open')


def echotip(event):
    echo.configure(text='Used to add text to the console screen. Enter a . to make a blank line.')





def leaveecho(event):
    echo.configure(text='speak')


def namewritefcf(new_name, sub, file, newloc, askov):
    _new_name = new_name.get()
    new_name.grid_forget()
    sub.grid_forget()
    final_p = '"' + newloc + '\\' + _new_name + '"'
    if askov.get() == 1:
        with open('outputs\\' + filename, 'a')as cwrite:
            cwrite.write('\ncopy /-Y "' + file + '"' + ' "' + final_p + '"')
            cwrite.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'a')as cl:
            cl.write('\nCF(a) ' + file + ' to ' + final_p)
            cl.close()
        commandlog.insert(END, 'CF(a) ' + file + ' to ' + final_p)
    else:
        with open('outputs\\' + filename, 'a')as cwrite:
            cwrite.write('\ncopy /Y "' + file + '"' + ' "' + final_p + '"')
            cwrite.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'a')as cl:
            cl.write('\nCF ' + file + ' to ' + final_p)
            cl.close()
        commandlog.insert(END, 'CF ' + file + ' to ' + final_p)

def delay(*args):
    non = False
    args[0].grid_forget()
    args[1].grid_forget()
    args[2].grid_forget()
    args[3].grid_forget()
    wait = args[0].get()
    try:
        int(wait)
    except ValueError:
        tkinter.messagebox.showerror('You Cannot Enter a Non-Numeric Character', 'You entered a non-numreric character')
        non = True
    if not non:
        null = ''
        if args[4].get() != 1:
            null = ' >C:\\Users\\%USERNAME%\\OneDrive\\Desktop\\null'
        boolinline = boollineget()
        if boolinline[1]:
            insetlinewrite('timeout ' + wait + null, boolinline[0], 'delay for ' + wait)
        else:
            with open('outputs\\' + filename, 'a')as tim:
                tim.write('\ntimeout ' + wait + null)
                tim.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as timey:
                if null != '':
                    timey.write('\ndelay(no show) for ' + wait)
                    commandlog.insert(END, 'delay(no show) for ' + wait)
                else:
                    timey.write('\ndelay for ' + wait)
                    timey.close()
                    commandlog.insert(END, 'delay for ' + wait)

def file_grab(link, forget, forget1):
    forget.grid_forget()
    forget1.grid_forget()
    file_object = start_file()


    if link.get() == 0:
        start = tkinter.filedialog.askopenfilename(title='Select a file that will run')

        if start == '':
            tkinter.messagebox.showerror('Invalid File', 'You did not select a valid file')
        else:
            nstart = start.replace('/', '\\')
            _start = nstart.replace(os.environ['USERNAME'], '%USERNAME%')
            prompt = Label(main, text='Start the file maximized or minimized')
            prompt.grid(row=35, column=30)
            maxormin = IntVar()

            maxi = Radiobutton(main, text='Maximized', variable=maxormin, value=1)
            maxi.grid(row=36, column=29)
            mini = Radiobutton(main, text='Minimized', variable=maxormin, value=2)
            mini.grid(row=36, column=31)
            submit = Button(main, text='Submit', command=lambda:file_object.min_max(_start, maxormin, submit, prompt, maxi, mini))
            submit.grid(row=37, column=30)
    else:
        _link = Entry(main)
        _link.insert(END, 'Enter the link of the website you want to open')
        _link.grid(row=35, column=30)
        submit = Button(main, text='Submit', command=lambda:file_object.link_start(_link, submit))
        submit.grid(row=36, column=30)



def batchwriter(*a):
    b = 'nul'
    if a[0] == 'pause':
        b = 'hold'
        inj = IntVar()
        pausmess = Checkbutton(main, text='Check if you want an alt message to the default pause button message.', variable=inj)
        pausmess.grid(row=35, column=30)
        subch = Button(main, text='Submit', command=lambda: pausebutalt(inj, pausmess, subch))
        subch.grid(row=36, column=30)

    elif a[0] == 'speak':
        custommes = Entry()
        custommes.grid(row=35, column=30)
        customesexp = Label(main, text='Enter what you want to say here')
        customesexp.grid(row=36, column=30)
        subbut = Button(main, text='submit', command=lambda: speak(custommes, customesexp, subbut))
        subbut.grid(row=37, column=30)

    elif a[0] == 'cf':
        a[3].grid_forget()
        a[5].grid_forget()
        a[4].grid_forget()
        if a[7].get() == 0:
            tkinter.messagebox.showwarning('File extension', 'Make sure to add a desired file extension to the file name')
            new_name = Entry(main)
            sub = Button(main, text='Submit', command=lambda:namewritefcf(new_name, sub, a[1], a[2], a[6]))
            new_name.grid(row=35, column=30)
            sub.grid(row=36, column=30)
        else:
            if a[6].get() == 1:
                with open('outputs\\' + filename, 'a')as askover:
                    askover.write('\ncopy /-Y "' + a[1] + '" "' + a[2] + '"')
                    askover.close()
                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as comcf:
                    comcf.write('\nCF(a) ' + a[1] + ' to ' + a[2])
                    comcf.close()
                commandlog.insert(END, 'CF(a) ' + a[1] + ' to ' + a[2])
            else:
                with open('outputs\\' + filename, 'a')as cfnoask:
                    cfnoask.write('\ncopy /Y "' + a[1] + '" "' + a[2] + '"')
                    cfnoask.close()
                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as commno:
                    commno.write('\nCF ' + a[1] + ' to ' + a[2])
                    commno.close()
                commandlog.insert(END, 'CF ' + a[1] + ' to ' + a[2])

    elif a[0] == 'time':
        wait = Entry(main)
        wait.grid(row=35, column=30)
        show = IntVar()
        showno = Checkbutton(main, text='Show countdown', variable=show)
        hel = Label(main, text='Enter how long to delay for')
        hel.grid(row=37, column=30)
        showno.grid(row=38, column=30)
        submit = Button(main, text='Submit', command=lambda:delay(wait, submit, hel, showno, show))
        submit.grid(row=36, column=30)
    elif a[0] == 'run':
        linkv = IntVar()

        link = Checkbutton(main, text='Check this if you are trying to start a link; otherwise, click submit.', variable=linkv)
        submit = Button(main, text='Submit', command=lambda:file_grab(linkv, link, submit))

        link.grid(row=30, column=30)
        submit.grid(row=31, column=30)

    else:
        if a[0] == 'cls':
            b = 'clear'
        elif a[0] == 'exit':
            b = 'quit'
        boolandline = boollineget()
        if boolandline[1] is True:
            insetlinewrite(a, boolandline[0], b)
        else:
            with open('outputs\\' + filename, 'a')as p:
                p.writelines('\n' + a[0])
                p.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as d:
                d.writelines('\n' + b)
                d.close()
            commandlog.insert(END, b)


def speak(a, b, c):
    custommes1 = a.get()
    if custommes1 == '.':
        boolandline = boollineget()
        if boolandline[1] is True:
            insetlinewrite('echo' + custommes1, boolandline[0], 'speak' + custommes1)
        else:
            with open('outputs\\' + filename, 'a')as j:
                j.writelines('\necho.')
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as john:
                john.writelines('\nspeak.')
                john.close()
            commandlog.insert(END, 'speak.')
    elif custommes1 == '':
        tkinter.messagebox.showerror('Incorrect speak value', 'You cannot enter a blank string for speak')
    else:
        varitr = comvari.variablecheck(custommes1)
        if varitr[1]:
            _custommes = varitr[0]
        else:
            _custommes = '\necho ' + custommes1
        boolandline = boollineget()
        if boolandline[1] is True:
            insetlinewrite(_custommes[1:], boolandline[0], 'speak ' + custommes1)
        else:
            with open('outputs\\' + filename, 'a')as d:
                d.writelines(_custommes)
                d.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as g:
                g.writelines('\nspeak ' + custommes1)
                g.close()
            commandlog.insert(END, 'speak ' + custommes1)
    a.grid_forget()
    b.grid_forget()
    c.grid_forget()

def fileremovalwrite(checkbox, subbut, intvari, filenamesdel):
    boolandline = boollineget()
    checkbox.grid_forget()
    subbut.grid_forget()
    if intvari.get() == 1:
        for x in filenamesdel:
            _x = x.replace('/', '\\')
            xy = _x.replace(os.environ['USERNAME'], '%USERNAME%')
            if boolandline[1]:
                insetlinewrite('del /p "{0}'.format(xy), boolandline[0], 'Delete File (a): {0}'.format(x))
            else:
                with open('outputs\\' + filename, 'a')as filedel1:
                    filedel1.write('\ndel /p "{0}'.format(xy))
                    filedel1.close()
                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as delcom:
                    delcom.write('\nDelete File (a): {0}'.format(x))
                    delcom.close()
                commandlog.insert(END, 'Delete File (a): {0}'.format(x))
    else:
        for x in filenamesdel:
            _x = x.replace('/', '\\')
            xy = _x.replace(os.environ['USERNAME'], '%USERNAME%')
            if boolandline[1]:
                insetlinewrite('del /f "{0}'.format(xy), boolandline[0], 'Delete File: {0}'.format(x))
            else:
                with open('outputs\\' + filename, 'a')as filedel:
                    filedel.write('\ndel /f "{0}'.format(xy))
                    filedel.close()
                with open('commandlog\\' + _filename2 + 'log.txt', 'a')as delcom:
                    delcom.write('\nDelete File: {0}'.format(x))
                    delcom.close()
                commandlog.insert(END, 'Delete File {0}'.format(x))


def fileremoval():
    files_to_del = tkinter.filedialog.askopenfilenames(title='Select a file to be deleted during the batch script. Do not select a folder, it will not work')
    invar = IntVar()
    ask_use = Checkbutton(main, text='Check if you do want the user to be prompted when deleting the file', variable=invar)
    ask_use.grid(row=38, column=30)
    submit = Button(main, text='Submit', command=lambda:fileremovalwrite(ask_use, submit, invar, files_to_del))
    submit.grid(row=39, column=30)

def dele(a):
    deletfilebutton.configure(text='Use this to delete files from the user\'s computer')
def delebutalt(a):
    deletfilebutton.configure(text='Delete File')

def folderrwrite(_folders, submitbutton):
    submitbutton.grid_forget()
    if os.path.exists(_folders):
        nx = _folders.replace(os.environ['USERNAME'], '%USERNAME%')
        _x = nx.replace('/', '\\')

        boolandline = boollineget()
        if boolandline[1]:
            insetlinewrite('@RD /S /Q "' + _x + '"', boolandline[0], 'Remove Folder: ' + _folders)
        else:
            with open('outputs\\' + filename, 'a')as folderdel:
                folderdel.write('\n@RD /S /Q "' + _x + '"')
                folderdel.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as foldde:
                foldde.write('\nRemove Folder: ' + _folders)
                foldde.close()
            commandlog.insert(END, 'Remove Folder: ' + _folders)
    else:
        tkinter.messagebox.showwarning('Non-existant Path', 'The path you entered for the folder does not exist')


def folderremover():
    folders = tkinter.filedialog.askdirectory(title='Select a folder to remove')
    submit = Button(main, text='Submit', command=lambda:folderrwrite(folders, submit))
    submit.grid(row=36, column=30)



def foldtip(a):
    folddele.configure(text='Delete folders on the user\'s computer')

def foldtipleave(a):
    folddele.configure(text='Folder Remover')

def mdwrite(dir, foldername, submitbutton, forget):
    submitbutton.grid_forget()
    forget.grid_forget()
    foldname = foldername.get()
    foldername.grid_forget()
    boolinline = boollineget()
    ndir = dir.replace('/', '\\')
    _dir = ndir.replace(os.environ['USERNAME'], '%USERNAME%')
    if boolinline[1]:
        insetlinewrite('md \"' + _dir + '\\' + foldname + '\"', boolinline[0], 'Make Folder: ' + ndir + '/' + foldname)
    else:
        with open('outputs\\' + filename, 'a')as md:
            md.write('\nmd \"' + _dir + '\\' + foldname + '\"')
            md.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'a')as comm:
            comm.write('\nMake Folder: ' + ndir + '/' + foldname)
            comm.close()
        commandlog.insert(END, 'Make Folder: ' + ndir + '/' + foldname)

def dirselect():
    folddir = tkinter.filedialog.askdirectory(title='Select the Directory you Want to Make the Folder in')
    instruc = Label(main, text='Enter the name of your new directory')
    instruc.grid(row=35, column=30)
    foldername = Entry(main)
    foldername.grid(row=36, column=30)
    submit = Button(main, text='Submit', command=lambda:mdwrite(folddir, foldername, submit, instruc))
    submit.grid(row=37, column=30)

def quitbuttip(a):
    quitbut.configure(text='Immediatly exits the batch script')


def quitbutleave(a):
    quitbut.configure(text='Quit')

def makefiletip(a):
    makef.configure(text='Makes a folder')

def makefileexit(a):
    makef.configure(text='MF')


def cf():
    file_to_copy = tkinter.filedialog.askopenfilename(title='Select a file to copy')
    copy_loc = tkinter.filedialog.askdirectory(title='Select the directory to copy the file to')
    xfile_to_copy = file_to_copy.replace('/', '\\')
    _file_to_copy = xfile_to_copy.replace(os.environ['USERNAME'], '%USERNAME%')
    xcopy_loc = copy_loc.replace('/', '\\')
    _copy_loc = xcopy_loc.replace(os.environ['USERNAME'], '%USERNAME%')

    askvar = tkinter.IntVar()
    naskvar = tkinter.IntVar()
    askover = Checkbutton(main, text='Ask if you want to overwrite an existing file', variable=askvar)
    askname = Checkbutton(main, text='Keep the original name when copied', variable=naskvar)
    submit = Button(main, text='Submit', command=lambda:batchwriter('cf', _file_to_copy, _copy_loc, submit, askover, askname, askvar, naskvar))
    askover.grid(row=35, column=30)
    askname.grid(row=36, column=30)
    submit.grid(row=37, column=30)


def cftip(button):
    copy.configure(text='Copy files to a new location')

def cftipl(button):
    copy.configure(text='CF')

def signw(sign_name, submit):
    sign_name.grid_forget()
    submit.grid_forget()
    boolinline = boollineget()
    if sign_name.get() == '':
        tkinter.messagebox.showerror('Invalid Sign Name', 'You cannot enter a blank string as a sign name')
    else:
        if boolinline[1]:
            insetlinewrite(':' + sign_name.get(), boolinline[0], 'sign: ' + sign_name)

        else:
            with open('outputs\\' + filename, 'a')as sign:
                sign.write('\n:' + sign_name.get())
                sign.close()

            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as signlog:
                signlog.write('\nsign: ' + sign_name.get())
                signlog.close()


            commandlog.insert(END, 'sign: ' + sign_name.get())





def jumpsign():
    jumpsname = Entry(main)
    jumpsname.grid(row=35, column=30)
    submit = Button(main, text='Submit', command=lambda:signw(jumpsname, submit))
    submit.grid(row=36, column=30)

def gotoact(sign_n, submit):
    exists = False
    sign_n.grid_forget()
    submit.grid_forget()
    with open('outputs\\' + filename, 'r')as labelc:
        file_data = labelc.readlines()
        labelc.close()

    for x in file_data:
        if x.strip('\n') == ':' + sign_n.get():
            exists = True
            break

    if exists:

        boolinline = boollineget()

        if boolinline[1]:
            insetlinewrite('goto :' + sign_n.get(), boolinline[0], 'jump to sign: ' + sign_n.get())
        else:
            with open('outputs\\' + filename, 'a')as jump:
                jump.write('\ngoto :' + sign_n.get())
                jump.close()

            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as gotolog:
                gotolog.write('\njump to sign: ' + sign_n.get())
                gotolog.close()


            commandlog.insert(END, 'jump to sign: ' + sign_n.get())
    else:
        tkinter.messagebox.showerror('No Such Sign', 'In your file there are no signs by the name entered')


def goto():
    sign_n = Entry(main)
    sign_n.grid(row=35, column=30)
    submit = Button(main, text='Submit', command=lambda:gotoact(sign_n, submit))
    submit.grid(row=36, column=30)

def move_final(file, new_d, overwrite, forget, forget2):
    forget.grid_forget()
    forget2.grid_forget()
    nfile = file.replace('/', '\\')
    _file = nfile.replace(os.environ['USERNAME'], '%USERNAME%')
    nnew_d = new_d.replace('/', '\\')
    _new_d = nnew_d.replace(os.environ['USERNAME'], '%USERNAME%')
    boolinline = boollineget()
    if overwrite.get() == 1:
        if boolinline[1]:
            insetlinewrite('move /-Y "' + _file + '"' + ' "' + _new_d + '"', boolinline[0], 'trans ' + _file + ' to ' + _new_d)
        else:
            with open('outputs\\' + filename, 'a')as over:
                over.write('\nmove /-Y "' + _file + '" "' + _new_d + '"')
                over.close()
            with open('commandlog\\' + _filename2 + 'log.txt', 'a')as movf:
                movf.write('\ntrans(a) ' + _file + ' to ' + _new_d)
                movf.close()

            commandlog.insert(END, 'trans(a) ' + _file + ' to ' + _new_d)
    else:
        with open('outputs\\' + filename, 'a')as movf:
            movf.write('\nmove /Y "' + _file + '" "' + _new_d + '"')
            movf.close()

        with open('commandlog\\' + _filename2 + 'log.txt', 'a')as mf:
            mf.write('\ntrans ' + _file + ' to ' + _new_d)
            mf.close()

        commandlog.insert(END, 'trans ' + _file + ' to ' + _new_d)

def move():
    file_m = tkinter.filedialog.askopenfilename(title='Select a file to move')
    new_d = tkinter.filedialog.askdirectory(title='New Location')
    ov = IntVar()
    ask_over = Checkbutton(main, text='Ask to overwrite', variable=ov)
    ask_over.grid(row=35, column=30)
    submit = Button(main, text='Submit', command=lambda:move_final(file_m, new_d, ov, ask_over, submit))
    submit.grid(row=36, column=30)


def timebind(a):
    timeout.configure(text='Hault the program for a specified interval')

def timeleave(a):
    timeout.configure(text='Delay')

def transtip(a):
    trans.configure(text='Move a file')
def transtipleave(a):
    trans.configure(text='Trans')
def setptip(a):
    setp.configure(text='Ask a question and have the user type something')
def settipleave(a):
    setp.configure(text='Input')

def title_final(title, forget):
    line_count = 0
    forget.grid_forget()
    title.grid_forget()
    _title = title.get()


    with open('outputs\\' + filename, 'r')as line_check:
        lines = line_check.readlines()
        line_check.close()

    with open('outputs\\' + filename, 'w')as title_set:

        for x in lines:
           if line_count == 1:
               title_set.write('\ntitle ' + title)
           else:
               title_set.write(x)
               pass

        line_count += 1
        title_set.close()

def titleset():
    title = Entry(main)
    submit = Button(main, text='Submit', command=lambda:title_final(title, submit))
    title.grid(row=35, column=30)
    submit.grid(row=36, column=30)

def _set_title(title, forget):
    forget.grid_forget()
    title.grid_forget()


    with open('outputs\\' + filename, 'r')as olt:
        old_title = olt.readlines()
        olt.close()
    with open('outputs\\' + filename, 'w')as fix:
        for x in old_title:
            if 'title' in x:
                fix.write('\ntitle {0}'.format(title.get()))
            else:
                fix.write(x)
        fix.close()


    with open('outputs\\' + filename, 'a')as titlese:
        titlese.write('\ntitle {0}'.format(title.get()))
        titlese.close()

    tkinter.messagebox.showinfo('Title Set','Your script\'s title will now appear as: ' + title.get())

def set_title():
    title = Entry(main)
    title.insert(END, 'Enter the title of your file')
    title.grid(row=35, column=30)
    submit = Button(main, text='Submit', command=lambda:_set_title(title, submit))
    submit.grid(row=36, column=30)

def clear_all():
    answer = tkinter.messagebox.askquestion('Clear File', 'Are you sure you want to clear the file of all of your code?')
    if answer == 'yes':
        with open('outputs\\' + filename, 'r')as out:
            cfile = out.readlines()
            out.close()

        with open('outputs\\' + filename, 'w')as clear:
            clear.write('')
            clear.write(cfile[0])
            clear.close()

        with open('commandlog\\' + _filename2 + 'log.txt', 'r')as coml:
            com = coml.readlines()
            coml.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'w')as locl:
            locl.write('')
            locl.write(cfile[0])

            ind = 0
            for x in com:
                if x != '\n':
                    ind += 1
            for x in range(ind):
                if x == 0:
                    pass
                else:
                    commandlog.delete(1)
            locl.close()
        vari_c = 0
        for x in os.listdir('resources\\variables'):
            if x != 'globrand' and x != 'globuser':
                vari_c += 1
                os.remove('resources\\variables\\' + x)
        for x in range(vari_c):
            varlog.delete(2)

        if os.path.exists('commandlog\\' + filename[:-4] + '-v'):
            os.remove('commandlog\\' + filename[:-4] + '-v')
    else:
        tkinter.messagebox.showinfo('Clear Aborted', 'Your file will not be cleared.')

def runtipent(a):
    start.configure(text='Runs a file')

def runtiple(a):
    start.configure(text='Run')

try:
    main.iconbitmap('batchmain_icon.ico')
except:
    tkinter.messagebox.showwarning('File Not Found', 'Batchmain cannot find the icon file. Make sure that batchmain_icon.ico is in the same directory as batchmain.exe.')

gate_state = gates()
main.title('WAMS Batch Writer: ' + filename)
command = Label(main, text='Command Log', font='System 17')
pause = Button(main, text='pause', command=lambda: batchwriter('pause'), fg='light green', bg='black')
pause.grid(row=2, column=1)
echo = Button(main, text='speak', command=lambda: batchwriter('speak'), fg='light green', bg='black')
echo.grid(row=2, column=0)
cls = Button(main, text='Clear', command=lambda: batchwriter('cls'), fg='light green', bg='black')
cls.grid(row=2, column=2)
quitbut = Button(main, text='Quit', fg='light green', bg='black', command=lambda:batchwriter('exit'))
quitbut.grid(row=2, column=3)
nothing = Label(main, text='                                                                                                                       ')
deletfilebutton = Button(main, text='Delete File', command=fileremoval, fg='red', bg='black')
folddele = Button(main, text='Folder Remover', command=folderremover, fg='red', bg='black')
folddele.grid(row=3, column=0)
folddele.bind('<Enter>', foldtip)
folddele.bind('<Leave>', foldtipleave)
deletfilebutton.grid(row=3, column=1)
commandlog.grid(row=3, column=30, padx=40)
nothing.grid(row=3, column=20)
deletfilebutton.bind('<Enter>', dele)
deletfilebutton.bind('<Leave>', delebutalt)
makef = Button(main, text='FM', fg='red', bg='black', command=dirselect)
makef.grid(row=3, column=2)
quitbut.bind('<Enter>', quitbuttip)
quitbut.bind('<Leave>', quitbutleave)
makef.bind('<Enter>', makefiletip)
makef.bind('<Leave>', makefileexit)
copy = Button(main, text='CF', command=cf, fg='red', bg='black')
copy.grid(row=3, column=3)
copy.bind('<Enter>', cftip)
copy.bind('<Leave>', cftipl)
timeout = Button(main, text='Delay', command=lambda:batchwriter('time'), bg='black', fg='light green')
timeout.grid(row=2, column=4)
trans = Button(main, text='Trans', bg='black', fg='red', command=move)
trans.grid(row=3, column=3)
setp = Button(main, text='Input', bg='black', fg='light green', command=comvari.set_p)
setp.grid(row=2, column=5)
timeout.bind('<Enter>', timebind)
timeout.bind('<Leave>', timeleave)
trans.bind('<Enter>', transtip)
trans.bind('<Leave>', transtipleave)
setp.bind('<Enter>', setptip)
setp.bind('<Leave>', settipleave)
start = Button(main, text='Run', bg='light green', command=lambda:batchwriter('run'))
start.grid(row=4)
start.bind('<Enter>', runtipent)
start.bind('<Leave>', runtiple)








# Command Log Setup

logfound = False
for file in os.listdir('commandlog'):
    if file == _filename2 + 'log.txt':
        logfound = True
        with open('commandlog\\' + file, 'r')as g:
            commandprev = g.readlines()
            g.close()
        for line in commandprev:
            if line != '\n':
                commandlog.insert(END, line)

if logfound is False:
    try:
        with open('outputs\\' + filename, 'r')as a:
            ec = a.readline()
            a.close()
        with open('commandlog\\' + _filename2 + 'log.txt', 'w')as l:
            l.writelines(ec)
            l.close()
        for file in os.listdir('commandlog'):
            if file == _filename2 + 'log.txt':
                with open('commandlog\\' + _filename2 + 'log.txt', 'r')as up:
                    np = up.readlines()
                    up.close()
                for line in np:
                    commandlog.insert(END, line)
                logfound = True
    except FileNotFoundError:
        tkinter.messagebox.showerror('File Not Found', 'Batchmain.exe could not find your desired file. To fix this start filemaker and make the file again.')
        exit()

#End of command log setup


command.grid(row=0, column=30)

commandlab = Label(main, text='Commands', font='System 17')
commandlab.grid(row=0, column=0)
echo.bind('<Enter>', echotip)
echo.bind('<Leave>', leaveecho)


pause.bind('<Enter>', pausetip)
pause.bind('<Leave>', pausetipleave)

#Menu
filemen = Menu(mainmen)
mainmen.add_cascade(menu=filemen, label='File')
menu_setup = CustomPackage()
menu_setup.menu_setup()
package_class = CustomPackage()
filemen.add_command(label='Run File', command=runyourfile)
filemen.add_command(label='Title', command=set_title)
filemen.add_command(label='Save file as package', command=package_class.packagecreator)
filemen.add_command(label='Clear', command=clear_all)
filemen.add_command(label='Exit', command=sys.exit)







cls.bind('<Enter>', clstip)
cls.bind('<Leave>', clstipl)
main.mainloop()
