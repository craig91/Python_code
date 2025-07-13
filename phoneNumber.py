def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            print(text[i])
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# print('Is 455-555-4242 a phone number? ', is_phone_number('415-555-4242'))
# print(is_phone_number('415-555-4242'))
# print('Is moshi moshi a phone number', is_phone_number('Moshi Moshi'))
# print(is_phone_number('moshi moshi'))

print(is_phone_number('1234567891012'))