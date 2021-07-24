string = 'AAAAAAAAAAAAAAAB823039C4030EB4E6D77A6F1208004500002513EA000027117C061B3CA0BC1D07051345BEF658001199E950524F5A4553534F52000000000000000000CEB8362F'
splited = ""
while string != "":
    splited += string[:2] + " "
    string = string[2:]
splited= splited.split()
new = []

for x in splited:
    new.insert(-1,int(x,16))
new.insert(0,new.pop(-1))

final = zip(splited,new)
for x in final:
    print(x)
