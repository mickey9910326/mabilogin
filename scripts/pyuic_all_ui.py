import conf
import os
import glob
import platform

def do_pyuic():
    uifiles = glob.glob('ui/*.ui')

    # use unix-like path style
    # it will effect line 3 in ui_xxx.py
    if platform.system() =="Windows":
        uifiles = [file.replace('\\','/') for file in uifiles]

    for uifile in uifiles:
        name = os.path.split(uifile)[1]
        pyfile = 'mabilogin_gui/ui/ui_' + os.path.splitext(name)[0] + '.py'
        cmd    = 'PySide6-uic ' + uifile +' -o ' + pyfile
        print(cmd)
        os.system(cmd)

        fin = open(pyfile, "rt", encoding="utf-8")
        data = fin.read()
        data = data.replace('import resources_rc', 'import mabilogin_gui.ui.resources_rc')
        fin.close()
        fin = open(pyfile, "wt", encoding="utf-8")
        fin.write(data)
        fin.close()

def do_pyrcc():
    cmd = "PySide6-rcc ui/resources.qrc -o mabilogin_gui/ui/resources_rc.py"
    print(cmd)
    os.system(cmd)



def run():
    do_pyuic()
    do_pyrcc()



if __name__ == '__main__':
    run()
