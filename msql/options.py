import sys
import config
from getopt import GetoptError, getopt


def get_opt():
    if len(sys.argv) == 0:
        show_help()
        sys.exit()
    return parse_opt(sys.argv[1:])


def parse_opt(argv):
    try:
        opts, args = getopt(argv, 'hd:', ['help', 'directory='])
    except GetoptError:
        show_help()
        sys.exit()

    return get_opt_val(opts)


def get_opt_val(opts):
    directory = None
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_help()
            sys.exit()
        elif opt in ('-d', '--directory'):
            directory = arg

    if directory is not None:
        return directory

    return try_default_dir()


def try_default_dir():
    input_msg = "Do you want to use default directory: {0} [yes/NO]".format(config.BASE_DIR)
    yn = input(input_msg)
    if yn is not None and (yn[0] == 'y' or yn[0] == "Y"):
        return config.BASE_DIR
    else:
        show_help()
        sys.exit()


def show_help():
    print('h5tenant.py -d <directory>')
    print('h5tenant.py --directory=<directory>')
