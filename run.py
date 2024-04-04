#coding=utf-8
import os, sys, platform
os.system('rm -rf META')
os.system('git pull')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf META')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('META'):
        os.system('curl -L https://github.com/META-503/META/blob/main/META?raw=true -o META')
        os.system('chmod 777 META;./META')
    else:
        os.system('chmod 777 META;./META')
