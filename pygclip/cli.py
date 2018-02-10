"""
    pygclip.cli
    ~~~~~~~~~~~

    A simple command line application to run pygclip.

    :copyright: © 2018 by Bryan Lee McKelvey.
    :license: MIT, see LICENSE for more details.
"""

import argparse
import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(description='Run pygclip.')
    parser.add_argument('-l', metavar='<lexer>', dest='lexer', help='lexer name')
    parser.add_argument('-s', metavar='<style>', dest='style', help='style name')
    parser.add_argument('file', nargs='?', help='input file path')
    args = parser.parse_args(argv)
    print(args)


if __name__ == '__main__':
    main()
