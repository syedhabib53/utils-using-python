
import os
import shutil
import optparse


__author__ = 'Syed Habib M'


def rm_recursive(path, rm_dir=None, rm_file=None):
    """
    This is small util to remove given directory/file in given path recursively.
    """
    path = os.path.abspath(path)
    if rm_dir:
        print "Given Directory Name %s" % rm_dir
    if rm_file:
        print "Given File Name %s" % rm_file
    for dirname, dirnames, filenames in os.walk(path):
        print "Checking %s" % (os.path.join(path, dirname))
        if rm_dir in dirnames:
            print "Removing Directory %s" % (os.path.join(dirname, rm_dir))
            shutil.rmtree(os.path.join(dirname, rm_dir))
        if rm_file in filenames:
            print "Removing File %s" % (os.path.join(dirname, rm_file))
            os.remove(os.path.join(dirname, rm_file))


def main():
    usage = "%prog -p <dirpath> -d <dirname> (or) -f <filename>"
    parser = optparse.OptionParser(usage)
    parser.add_option("-p", "--path", dest="fullpath",
                      help="FULLPATH to recursive will made")
    parser.add_option("-d", "--dir", dest="dirname",
                      help="to remove DIRNAME")
    parser.add_option("-f", "--file", dest="filename",
                      help="to remove from FILENAME")
    (options, args) = parser.parse_args()

    path = os.path.abspath(options.fullpath)
    if os.path.exists(path):
        rm_dir = options.dirname
        rm_file = options.filename
        if rm_dir or rm_file:
            rm_recursive(path, rm_dir, rm_file)
        else:
            print "DirName or FileName is required"
    else:
        print "%s doesn't exists." % path
        print parser.get_usage()


if __name__ == '__main__':
    main()