__author__ = 'Syed Habib'


import os


def rm_recursive(path, rm_dir=None):
    '''
    This is small util to remove given directory in given path recursively.
    '''
    for dirname, dirnames, filenames in os.walk(path):
        print "Checking %s in %s" %(rm_dir, os.path.join(path, dirname))
        if rm_dir in dirnames:
            print "Removing %s" %(os.path.join(dirname, rm_dir))
            os.rmdir(os.path.join(dirname, rm_dir))


if __name__ == '__main__':
    rm_recursive('.', '.svn')