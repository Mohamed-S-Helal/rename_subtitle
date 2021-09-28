import os
from difflib import get_close_matches
ls = os.listdir()
l1 = [i for i in ls if '.mp4' in i]
l2 = [i for i in ls if '.vtt' in i]
l3 = [get_close_matches(i, l2)[0] for i in l1]


for i in l2:
    if i not in l3:
        print(i)
        print(os.system('rem '+'"'+i+'"'))

# print('ren "'+l3[0]+'" '+'"'+l1[0][:-3]+'vtt"')

for i,j in zip(l1,l3):
    print(os.system('ren "'+j+'" '+'"'+i[:-3]+'vtt"'))





