sentence = input()

ret = ''

for s in sentence:
    if ord('a') <= ord(s) <= ord('z'):
        rot = ord(s) + 13
        if rot > ord('z'):
            ret += chr(rot - 26)
        else:
            ret += chr(rot)
    elif ord('A') <= ord(s) <= ord('Z'):
        rot = ord(s) + 13
        if rot > ord('Z'):
            ret += chr(rot - 26)
        else:
            ret += chr(rot)
    else:
        ret += s

print(ret)