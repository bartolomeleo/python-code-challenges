import os
import shutil

cwd=os.getcwd()
os.chdir('/projects/personal/python_projects/pythonLibrary')
os.system('mkdir today')

dir(os)
help(os)

shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

print(cwd)