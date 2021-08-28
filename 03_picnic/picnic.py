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
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='items',
                        nargs='+',
                        help='Items to bring')
    parser.add_argument('-s',
                        '--sorted',
                        help='sort the list first',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here """

    args = get_args()
    should_sort = args.sorted
    items = args.items
    if should_sort:
        items=sorted(items)
    cnt = len(items)
    items_str=''
    if cnt ==1:
        items_str=items[0]
    elif cnt==2:
        items_str=f"{items[0]} and {items[1]}"
    elif cnt > 2:
        for i in range(cnt-1):
            items_str += f"{items[i]}, "
        items_str=f"{items_str}and {items[cnt-1]}"

    print(f"You are bringing {items_str}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
