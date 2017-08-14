__author__ = 'akatla'
# program to walk a directory

import os , fnmatch

rootdir='c:/testroot'
#use / in windows or else use \\ as path separator

for dirName,subdirList,fileList in os.walk(rootdir):
    print 'Found directory ' , os.path.normpath(dirName)
    flist = fnmatch.filter(os.listdir(os.path.normpath(dirName)),'J*')
    print flist
    for fname in fileList:
        # print fname , os.path.normpath(dirName) + fname
        print os.path.join(os.path.normpath(dirName),fname)
