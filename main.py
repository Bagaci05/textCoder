#open a text file and read it
from operator import le


textfile = open("texttochange.txt", "r")
text = textfile.read()
textfile.close()

def split(word):
    return [char for char in word]

#split to words and print
words = text.split()
changed = []

for i in words:
    changing =split(i)
    if len(changing) > 3:
        temp1 = changing[1]
        changing[1] = changing[2]
        changing[2] = temp1
        if len(changing) > 5:
            temp2 = changing[3]
            changing[3] = changing[4]
            changing[4] = temp2
        changed.append("".join(changing))
    else:
        changed.append(i)
#write to a file and close it
textfile = open("changed.txt", "w")
textfile.write(" ".join(changed))
textfile.close()