# https://github.com/Aetopia/Onefile-Python-Interpreter

import os; os.system('')
from sys import argv, path
from os.path import join
from runpy import run_path


def main():

    args = {}
    for index, arg in enumerate(argv[2:]): args[index] = arg
    run_path(join(path[0], 'main.py'), init_globals=args, run_name='__main__')


if __name__ == '__main__':
    main()
