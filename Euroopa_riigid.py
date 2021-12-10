from module1 import *
from random import *
#from gtts import gTTS
#import os
sonastik={}     #Создал словарь с помощью литерала
riigid=linnad=[]
file=open("File.txt", "r")      #Открываем и читаем файл
for line in file:
    k, v=line.strip().split(" - ")
    sonastik[k.strip()] = v.strip()
    riigid.append(k.strip())
    linnad.append(v)
file.close()        #Закрываем файл
#print(sonastik)
#print(riigid)
#print(linnad)
riik=input("Введите название страны: ")
print(sonastik[riik])
linn=input("Введите название столицы: ")
print(riik)

#s=gTTS(text=linnad[8], lang="et", slow=False).save("heli,")
#os.system("heli.mp3")

a=input("Столица")
file=open("File.txt", "a")      #Открываем файл и дозаписываем в файл
print(sonastik)
o=input("Что исправить?")
z=input("На что исправить?")
sonastik.update({[o]: [z]})
file.close()   