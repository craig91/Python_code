import os
import socket
import platform
import psutil
from byte_converter import bytes_to_gb

print("Architecture:", platform.architecture()[0])
usage = psutil.disk_usage('/')
print("Total disk size:", bytes_to_gb(usage.total))
print("Total disk space used:", bytes_to_gb(usage.used))
print("Total disk space available: ", bytes_to_gb(usage.free))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80))
print(s.getsockname()[0])
s.close()



# disk_partitions = psutil.disk_partitions()
# for parition in disk_partitions:


    # print("PARTITION DEVICE:" , parition.device)
    # print("FILE SYSTEM TYPE:" , parition.fstype)
    # print("MOUNT POINT", parition.mountpoint)

    # disk_usage = psutil.disk_usage(parition.mountpoint)
    # print("Total Disk Size", bytes_to_gb(disk_usage.total))
    # print("Free Disk Space", bytes_to_gb(disk_usage.free))
    # print("Used Disk Space", bytes_to_gb(disk_usage.used))

