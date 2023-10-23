import os

fp = "temp.txt"

file = open(fp, "w")

if os.path.exists(fp):
    print("ok")
    file = open("temp.txt", "a")
else :
    print("error")
    file = open("temp.txt", "w")
#file.close()



# exception file read
import os

fp = "temp.txt"

if os.path.exists(fp):
    f = open(fp, "r")
    for line in f :
        print(line)

else :
    f = open(fp, "w")
    for i in range(100):
        f.write(str(i) + "\n")
        #print("error")
f.close()

#파일 삭제
import os

fp = "new.txt"

f = open(fp, "w")
f.close()
"""
os.remove(fp)
print("complete")"""