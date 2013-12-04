__author__ = 'Syed Habib'


import os


def rm_recursive(path, rm_dir=None, rm_file=None):
    '''
    This is small util to remove given directory/file in given path recursively.
    '''
    if rm_dir:
        print "Given Directory Name %s" % rm_dir
    if rm_file:
        print "Given File Name %s" % rm_file
    for dirname, dirnames, filenames in os.walk(path):
        print "Checking %s" %(os.path.join(path, dirname))
        if rm_dir in dirnames:
            print "Removing Directory %s" %(os.path.join(dirname, rm_dir))
            os.rmdir(os.path.join(dirname, rm_dir))
        if rm_file in filenames:
            print "Removing File %s" %(os.path.join(dirname, rm_file))
            os.remove(os.path.join(dirname, rm_file))


if __name__ == '__main__':
    rm_recursive('.', '.svn', 'demo.txt')