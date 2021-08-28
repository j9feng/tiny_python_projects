#!/usr/bin/env python3
"""
Author : jf440947 <jf440947@localhost>
Date   : 2021-08-27
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crows Nest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A positional argument')

    parser.add_argument('-s',
                        '--side',
                        help='specify which side of the boat',
                        metavar='str',
                        type=str,
                        default='larboard')

#    parser.add_argument('-i',
#                        '--int',
#                        help='A named integer argument',
#                        metavar='int',
#                        type=int,
#                        default=0)
#
#    parser.add_argument('-f',
#                        '--file',
#                        help='A readable file',
#                        metavar='FILE',
#                        type=argparse.FileType('rt'),
#                        default=None)
#
    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.side
#    int_arg = args.int
#    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.word

    print(f'str_arg = "{str_arg}"')
#    print(f'int_arg = "{int_arg}"')
#    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    if pos_arg[0] in "AEIOU":
        article='An'
    elif pos_arg[0] in "aeiou":
        article='an' 
    elif pos_arg[0].islower():
        article='a'
    else:
        article='A'
    side = str_arg 
    print(f'Ahoy, Captain, {article} {pos_arg} off the {side} bow!')
#    print(dir(args))
#

# --------------------------------------------------
if __name__ == '__main__':
    main()
