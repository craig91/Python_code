import os
import socket
import platform
import psutil


print("Architecture:", platform.architecture()[0])
# usage = psutil.disk_usage('/')
# print(type(usage))
# print(usage)

disk_partitions = psutil.disk_partitions()
for parition in disk_partitions:
    print("PARTITION DEVICE:" , parition.device)
    print("FILE SYSTEM TYPE:" , parition.fstype)
    print("MOUNT POINT", parition.mountpoint)

    disk_usage = psutil.disk_usage(parition.mountpoint)
