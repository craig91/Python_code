from sys import platform

if platform == 'linux' or platform == 'linux2':
    ip = sb.run(["ifconfig", "getifaddr", "en0"]), capture_output = True)
    