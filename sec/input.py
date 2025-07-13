#MATH formula = GigaBytes(GB) = Bytes(B) / 1,073741,824

GIGABYTE_IN_BYTES = 1073741824

def bytes_to_gb(byte_count):
   gb = round(int(byte_count) / GIGABYTE_IN_BYTES, 2)
   return f"{gb:.2f} GB"


result = bytes_to_gb(5000000000)
print(result)