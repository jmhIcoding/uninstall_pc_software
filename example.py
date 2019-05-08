__author__ = 'jmh081701'
from util import *
if __name__ == '__main__':
    #first, get names of all the installed software .
    softwares=get_software()
    print(softwares)
    #second, select the software you want to uninstalled.
    software=softwares[0]
    uninstall_software(software)