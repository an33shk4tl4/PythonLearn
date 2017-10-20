import os
from datetime import datetime as dt
import time
# TODO
# blog this on dev.to

def checkfile(filename):
    try:
        st = os.stat(filename)
        fmtime = st.st_mtime
    except Exception as e:
        print e.message
        return
    print "*********init modification timestamp" , dt.fromtimestamp(fmtime).ctime()
    while True:
        print 'entered while loop'
        st = os.stat(filename)
        print 'collected file stats'
        yield dt.fromtimestamp(fmtime).ctime()
        print 'yield executed'
        if dt.fromtimestamp(st.st_mtime).ctime() <> dt.fromtimestamp(fmtime).ctime():
            print "File modification changed - new file modification timestamp", dt.fromtimestamp(fmtime).ctime()
            fmtime = st.st_mtime
            print 'set new mod time inside if condition'
        else:
            print 'Mod timestamps equal'
        time.sleep(2)

chk = checkfile(r'C:\filetowatch.txt')

for i in chk:
    print chk.next()
    print '---for loop next iteration after gen call'
