import os
import requests
import json
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
print("Your IP Address:" , s.getsockname()[0])
s.close()

print("Your Public IP:" ,json.loads(requests.get("https://api.seeip.org/jsonip?").text)["ip"])
country = json.loads(requests.get("https://api.seeip.org/geoip").text) ["country"]
city = json.loads(requests.get("https://api.seeip.org/geoip").text) ["city"]

print("Location: " + city + "," + country)
# print(json.loads(requests.get("https://api.seeip.org/geoip").text)["country"])


# disk_partitions = psutil.disk_partitions()
# for parition in disk_partitions:


    # print("PARTITION DEVICE:" , parition.device)
    # print("FILE SYSTEM TYPE:" , parition.fstype)
    # print("MOUNT POINT", parition.mountpoint)

    # disk_usage = psutil.disk_usage(parition.mountpoint)
    # print("Total Disk Size", bytes_to_gb(disk_usage.total))
    # print("Free Disk Space", bytes_to_gb(disk_usage.free))
    # print("Used Disk Space", bytes_to_gb(disk_usage.used))

