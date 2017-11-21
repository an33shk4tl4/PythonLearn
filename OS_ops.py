from __future__ import print_function
import os
import shutil
fout = open(r'c:/Users/bluefish/Desktop/hello.txt', 'a+')
print('hello this is a sample text .. ',file=fout)
fout.close()

PathExists = os.path.exists(r'c:/Users/bluefish/Desktop/hello.txt')
print('Does this path exist? {}'.format(PathExists))

PathExists = os.path.exists(r'c:/Users/bluefish/Desktop')
print('Does this path exist? {}'.format(PathExists))

print('Does this {0} path exist? {0}'.format(os.path.exists('.')))

# shutil.copy(r'c:/Users/bluefish/Desktop/hello.txt', r'c:/Users/bluefish/Desktop/hello1.txt')
shutil.copytree(r'c:/Users/bluefish/Desktop/f1/', r'c:/Users/bluefish/Desktop/f2/')

