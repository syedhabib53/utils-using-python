
import os
import optparse


__author__ = 'Syed Habib M'


def rename_recursive(path, from_name, to_name):
    for dirname, dirnames, filenames in os.walk(path, topdown=False):
        print "Checking %s" % os.path.abspath(dirname)
        _from_name = os.path.join(dirname, from_name)
        _to_name = os.path.join(dirname, to_name)
        if os.path.exists(_from_name):
            print "Renaming %s to %s" % (
                os.path.abspath(_from_name), os.path.abspath(_to_name))
            os.rename(_from_name, _to_name)


def main():
    usage = "%prog -p <path> --from <fromname> --to <toname>"
    parser = optparse.OptionParser(usage)
    parser.add_option('-p', '--path', dest='fullpath',
                      help='FULLPATH to recursive will made')
    parser.add_option('--from', dest='fromname',
                      help='NAME to be changed dir or file')
    parser.add_option('--to', dest='toname',
                      help='NAME for renaming dir or file')
    (options, args) = parser.parse_args()
    path = os.path.abspath(options.fullpath)
    if os.path.exists(path):
        from_name = options.fromname
        to_name = options.toname
        if from_name and to_name:
            rename_recursive(path, from_name, to_name)
        else:
            print parser.get_usage()
    else:
        print "%s doesn't exists." % path
        print parser.get_usage()


if __name__ == '__main__':
    main()