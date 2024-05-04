#!/usr/bin/env python3
import os
import sys


def check_reboot():
    '''Return if there's pending Reboot or not'''
    # commit -a -m "escaping staging area"
    return os.path.exists('/run/reboot-required')


def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    else:
        print("No pending Reboot.")
        sys.exit(0)


main()
