#MATH Formula = GB = Bytes / 1,073,824 bytes

GIGABYTES_IN_BYTES = 1073741824

def bytes_to_gb(byte_count):
    gb = round(int(byte_count) / GIGABYTES_IN_BYTES, 2)
    return f"{gb:.2f} GB"