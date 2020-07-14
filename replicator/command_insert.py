import os

def boolinline():
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
