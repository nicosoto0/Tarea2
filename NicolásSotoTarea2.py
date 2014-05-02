
# coding: utf-8

# In[1]:

#Dominios a los que se puede llegar desde apple.com (outdegrees)
import time
import gzip

t1 = time.time()

dominio = "apple.com" + chr(9)

#en la variabl index se tiene que indtroducir el path de donde se encuentra el documento
index = gzip.open("pld-index.gz","rb")
while 1>0:
    try:
        txt1 =  index.readline()
        if txt1 == "":
            break
        if txt1[0:len(dominio)] == dominio:
            indice = txt1.rfind(chr(9))
            num = txt1[indice + 1:-1]       
            print(num)
            break
    except:
        break
index.close()

t2 = time.time() - t1

buscar = num + chr(9)
t3 = time.time()

cont2 = 0
contador = 0
arc = gzip.open("pld-arc.gz","rb")

while 1 >0 :
    try:
        txt2 = arc.readline()      
        if txt2 == "":
            cont2 += 1
        else:
            cont2 = 0
        if cont2 == 5:
            break       
        if buscar == txt2[0:len(buscar)]:
            contador += 1
    except:
        break

arc.close()

t4 = time.time() -t3

print(str(t2//60) + "min. y " + str(t2%60) + "seg.")

print(str(t4//60) + "min. y " + str(t4%60) + "seg.")

print(contador)

                


# In[2]:

#Dominios que van a wikipedia.com (indegrees)
import time
import gzip

t1 = time.time()

dominio = "wikipedia.com"

#en la variabl index se tiene que indtroducir el path de donde se encuentra el documento
index = gzip.open("pld-index.gz","rb")
while 1>0:
    try:
        txt1 =  index.readline()
        if txt1 == "":
            break
        if txt1[0:len(dominio)] == dominio:
            indice = txt1.rfind(chr(9))
            num = txt1[indice + 1:-1]       
            print(num)
            break
    except:
        break
index.close()

t2 = time.time() - t1
print(str(t2//60) + "min. y " + str(t2%60) + "seg.")



t3 = time.time()

#en la variabl index se tiene que indtroducir el path de donde se encuentra el documento
arc = gzip.open("pld-arc.gz","rb")


buscar = chr(9)+num
con3 = 0
contador2 = 0    
while 1>0:
    try:
        txt2 = arc.readline()
        if txt2 == "":
            cont2 += 1
        else:
            cont2 = 0
        if cont2 == 5:
            break       
        if (txt2.rfind(buscar)!= -1):
            contador2 += 1
    except:
        break
arc.close()
t4 = time.time() - t3
print(contador2)    
print(str(t4//60) + "min. y " + str(t4%60) + "seg.")


# In[3]:

#Subdominios de blogspot.com
import time
import gzip

t1 = time.time()

dominio = "blogspot.com" + chr(9)

#en la variabl index se tiene que indtroducir el path de donde se encuentra el documento
contador3 = 0
index = gzip.open("sd1-index.gz","rb")
while 1>0:
    try:
        txt1 =  index.readline()
        if txt1 == "":
            break
        if txt1.rfind(dominio) != -1:
            contador3 += 1
    except:
        break
index.close()

t2 = time.time() - t1

print(contador3)
print(str(t2//60) + "min. y " + str(t2%60) + "seg.")


# In[ ]:

#indegree y outdegree de dominios dados
import time
import gzip

t1 = time.time()

#dominio = "blogg.se" + chr(9)
#dominio = "petervidani.com" + chr(9)
dominio = "youtube.com" + chr(9)

#en la variabl index se tiene que indtroducir el path de donde se encuentra el documento
index = gzip.open("pld-index.gz","rb")
while 1>0:
    try:
        txt1 =  index.readline()
        if txt1 == "":
            break
        if txt1[0:len(dominio)] == dominio:
            indice = txt1.rfind(chr(9))
            num = txt1[indice + 1:-1]       
            print(num)
            break
    except:
        break
index.close()

t2 = time.time() - t1

t3 = time.time()

bus_indegree = num + chr(9)
bus_outdegree = chr(9) + num

cont2 = 0
indegree = 0
outdegree = 0
#en la variable arc se tiene que indtroducir el path de donde se encuentra el documento
arc = gzip.open("pld-arc.gz","rb")

while 1 >0 :
    try:
        txt2 = arc.readline()      
        if txt2 == "":
            cont2 += 1
        else:
            cont2 = 0
        if cont2 == 5:
            break       
        if bus_indegree == txt2[0:len(bus_indegree)]:
            indegree += 1
        if (txt2.rfind(bus_outdegree) != -1):
            outdegree += 1
    except:
        break

arc.close()

t4 = time.time() -t3

print("indigree: " + str(indegree))
print("outdegree: " + str(outdegree))
print(str(t2//60) + "min. y " + str(t2%60) + "seg.")

print(str(t4//60) + "min. y " + str(t4%60) + "seg.")

