services = {"ftp": 21, "ssh":22, "smtp":25, "http":80}
services2 = {"ftp":21, "ssh":22, "smtp":25, "ldap":389}

services.update(services2)
print(services)

services["http"] = 8080

keys = services.keys()
items = services.items()
print(keys)
print(items)

#items.sort()
for key,value in services.items():
    print(key,value)


print(items)
