# !/usr/bin/env python3
# shebang to make this file executable with python3

import shutil
import psutil


def check_disk_usage(disk):
    diskUsage = shutil.disk_usage(disk)
    freeDisk = (diskUsage.free/diskUsage.total)*100
    return 100-freeDisk


def check_cpu_usage():
    return psutil.cpu_percent(1)


def check_ram_usage():
    return psutil.virtual_memory().percent


def main():
    print(f"Disk usage: {check_disk_usage('/')}%")
    print(f"CPU usage: {check_cpu_usage()}%")
    print(f"RAM usage: {check_ram_usage()}%")


main()
