#!/usr/bin/env python3
import os
import sys
import shutil
import socket


def check_disk_usage(disk, min_gb, min_percent):
    """Returns True if free space is less than min_gb or min_percent, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False


def check_reboot():
    '''Returs True if there's pending Reboot, False otherwise.'''
    return os.path.exists('/run/reboot-required')


def check_root_full():
    '''Returns True if the root partition is full, False otherwise.'''
    return check_disk_usage(path="/", min_gb=2, min_percent=10)


def check_no_network():
    """Returns True if there is no working network, false otherwise."""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True


def main():
    CHECKS = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full"),
        (check_no_network, "No working network"),
    ]
    evertything_ok = True
    for check, msg in CHECKS:
        if check():
            print(msg)
            evertything_ok = False

    if not evertything_ok:
        print("Not all checks passed")
        sys.exit(1)

    print("Everything ok")
    sys.exit(0)
