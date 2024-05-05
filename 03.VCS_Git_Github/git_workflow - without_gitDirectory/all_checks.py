#!/usr/bin/env python3
import os
import sys
import shutil


def check_disk_usage(disk, min_gb, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return False
    return True


def check_reboot():
    '''Return if there's pending Reboot or not'''
    return os.path.exists('/run/reboot-required')


def check_root_full():
    return check_disk_usage(path="/", min_gb=2, min_percent=10)


def main():
    CHECKS = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full")
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
