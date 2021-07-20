string = 'AAAAAAAAAAAAAAAB48057F9F8C53DD64FA4D4180080045000020975000002D1190DA5C0BF4BB95AACFB905346F96000C4B664348495000000000000000000000000000008C03CC85'
splited = ""
while string != "":
    splited += string[:2] + " "
    string = string[2:]
print(splited)
splited= splited.split()

final = ""
for x in splited:
    final += str(int(x,16)) + " "
print(final)
