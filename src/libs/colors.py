import sys

if sys.platform.startswith('win'):
    PLAT = 'win'
elif sys.platform.startswith('linux'):
    PLAT = 'nix'
elif sys.platform.startswith('darwin'):
    PLAT = 'mac'
else:
    print('This platform is not supported.')
    sys.exit(1)

if PLAT == 'nix':
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREY = '\033[38;5;245m'
    BOLD = '\033[1m'
    UNDERL = '\033[4m'
    ENDC = '\033[0m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
else:
    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    UNDERL = ''
    ENDC = ''
    BG_BLACK = ''
    BG_RED = ''
    BG_GREEN = ''
    BG_YELLOW = ''
    BG_BLUE = ''
    BG_MAGENTA = ''
    BG_CYAN = ''
    BG_WHITE = ''
