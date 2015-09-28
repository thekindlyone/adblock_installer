# coding: utf-8
import os
from os.path import join,exists
import sys
import tkFileDialog
import zipfile

sysdrive=os.environ['SYSTEMDRIVE']
install_locs=[join(sysdrive+'/',path) for path in ['Program Files/Mozilla Firefox' ,'Program Files (x86)/Mozilla Firefox']]

def makedir(loc):
    print 'makedir',loc
    ext_directory='browser/extensions/{d10d0bf8-f5b5-c8b4-a8b2-2b9879e08c5d}'
    pref_directory='browser/default/preferences'
    
    if exists(loc):
        ext_path=join(loc,ext_directory)
        pref_path=join(loc,pref_directory)
        print 'DEBUG loc {}, ext_dir {}, ext_path {}'.format(loc,ext_directory,join(loc,ext_directory))
            
        try:
            if not exists(ext_path):
                os.makedirs(ext_path)
            if not exists(pref_path):
                os.makedirs(pref_path)
            with open(join(pref_path,'autoconfig.js'),'w') as f:
                f.write('pref("extensions.autoDisableScopes", 0);')
            return ext_path            
        except Exception as e:
            print 'ERROR {}'.format(e)
        

def extract(loc):
    print 'extracting at ',loc
    with zipfile.ZipFile('adblock.zip', "r") as z:
        z.extractall(loc)               
            
def install(loc):
    print 'installing',loc
    ext_path=makedir(loc)
    if ext_path:
        extract(ext_path)    


def main():    
    for loc in install_locs:
        print loc
        if exists(loc):
            install(loc)
            break
    else:
        loc=tkFileDialog.askdirectory()
        if loc:
            install(loc)
        else:
            sys.exit(0)    
                
if __name__ == '__main__':
    main()        