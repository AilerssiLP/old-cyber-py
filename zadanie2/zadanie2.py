import sys
import json

def hashFunction(hash):

    hash2 = []
    j = 0
    for i in range(len(hash)):

        char = hash[i]
        hash2.append(chr(ord(char)-3))
        j = j+1

    return hash2

def cesarCypher(hash):

    hash2 = []
    j = 0
    for i in range(len(hash)):

        char = hash[i]
        hash2.append(chr(ord(char)+3))
        j = j+1

    return hash2

#print(cesarCypher("Eniii"))

menoInput1 = input("meno: ")
hesloInput1 = input("heslo: ")
identifKey1 = input("overovaci kluc: ")

menoInput1=menoInput1.split()
hesloInput1=hesloInput1.split()
identifKey1=identifKey1.split()
menoInput=""
hesloInput=""
identifKey=""

for x in range(len(menoInput1)):
    menoInput=menoInput+menoInput1[x]
for y in range(len(hesloInput1)):
    hesloInput=hesloInput+hesloInput1[y]
for z in range(len(identifKey1)):
    identifKey=identifKey+identifKey1[z]

filenotaccessible = 0
subor = "hesla.csv"
try: 
    file = open(subor, 'r', encoding = 'utf8')
except IOError:
    print("chyba")
    filenotaccessible = 1
    
if(filenotaccessible != 1):
    bodka = 0
    poziciaDvojbotky = 0
    subor = file.readlines()#.split()
    heslo2=0
    jo = 0
    meno=0
    breaker1=0
    heslo=-1
    enter=0
    for i in range(10):
        reee= ""
        meno1=0
        reee = subor[i]
        hashovaneHeslo = []
        hashovaneMeno = []
        #reee.split()
        
        #print(len(reee))
        endThisShit = 0
        f = 0
        ##### citame meno ######
        while(endThisShit != 1):

            if(reee[f] == ':'):
                #print(" ",f)
                endThisShit = 1
                poziciaDvojbotky = f

            f = f+1

        for j in range(f-1):
            hashovaneMeno.append(reee[j])
        #### citame meno END #####

        endThisShit = 0
        c = 0
        
        #### citame hash heslo a menime na heslo######
        while(endThisShit != 1):

            if(reee[f+1] == ':'):
                #print(" ",f)
                endThisShit = 1

            f = f+1
            c = c+1 

        #print(c)
        for j in range(c):
            hashovaneHeslo.append(reee[j+poziciaDvojbotky+1])
        #### citame hash heslo a menime na heslo ENDD######

        hashovaneHeslo = hashFunction(hashovaneHeslo)

        ##################################
        menoa=0
        if(len(menoInput)==len(hashovaneMeno)):
            for menoa in range(len(hashovaneMeno)):
                if(menoInput[menoa]==hashovaneMeno[menoa]):
                    meno=i
                    meno1+=1
                    #print("yos",i)
            ##print(meno)
        
        hesloa=0
        #print(meno1,len(menoInput),len(hesloInput),len(hashovaneHeslo))
        
        if(meno1==len(menoInput) and len(hesloInput)==len(hashovaneHeslo)):
            for hesloa in range(len(hesloInput)):
                #print(hesloInput[hesloa],hashovaneHeslo[hesloa])
                if(hesloInput[hesloa]==hashovaneHeslo[hesloa]):
                    heslo=i
                    heslo2+=1
                    #print(hesloInput[hesloa])
                    if(hesloa+1==len(hashovaneHeslo)):
                        breaker1=1
        #print(breaker1)
        if(breaker1==1):
            break
            ##print(heslo)


        ##print(hashovaneHeslo)
        ##print(hashovaneMeno)

file.close()
#print("reee",meno,heslo)
##############klicek##########
prepis=0
if(meno1==len(menoInput) and heslo2==len(hashovaneHeslo)):
    key=[]
    smt=subor[meno]
    breaker = 1
    ree=0
    c=[]
    finalkey=""
    klicc=len(identifKey)
    for size in range(len(subor[meno])):
        key.append(smt[size])
    ####### kluc riadok  ###
    while(key[size]!=":"):
        size-=1
    size+=1
    for ree in range(len(key)-size):
        c.append(key[size+ree])
    #### c je riadok s klucmi####
    #print(c)
    for b in range(len(c)):
        if(c[b]!="," and c[b]!="\r" and c[b]!="\n" and c[b]!=""):
            finalkey=finalkey+c[b]
        elif(c[b]=="," and len(finalkey)==len(identifKey) and finalkey==identifKey):
            breaker=0
            break
        elif(c[b]=="\n" and len(finalkey)==len(identifKey) and finalkey==identifKey):
            breaker=0
            enter=1
            break
        elif(c[b]=="\r" and len(finalkey)==len(identifKey) and finalkey==identifKey):
            breaker=0
            enter=1
            break
        else:
            finalkey=""
    if(finalkey==identifKey and len(finalkey)==len(identifKey)and len(finalkey)>0):
        breaker=0
    if(breaker ==0 and len(finalkey)==len(identifKey)):
        print("ok")
        prepis =1
    else:
        print("chyba")
else:
    print("chyba")


if(prepis==1):
    riadok= subor[meno]
    hesloje=b#od 2. dvojbodky
    #print(c[b])
    #print(riadok[size+b])##dvojbodka + heslo(pozicia kde skoncilo)
    pole=[]
    for test in range(len(riadok)):
        pole.append(riadok[test])
    policko=[pole]
    #print("test",pole,"test2",b,"test3",size)
    if(enter!=1):
        for test2 in range(len(identifKey)+1):
        #pole[size+test2+b]=""
            d=test2-len(identifKey)
        #print(d)
            pole[size+b+d]=""
    else:
        for test2 in range(len(identifKey)):
            d=test2-len(identifKey)
            pole[size+b+d]=""
    #print(pole)
    #print(pole)
    ##hashFunction('d')
    #print(pole)
# with open('ehm.txt', 'w') as filehandle:
#     json.dump(pole(), filehandle)
    string=""
    for boi in range(len(pole)):
        string=string+pole[boi]
    ###############################
    riadok=[string]
    #print(riadok)

    subor[meno]=[riadok[0]]
    #print(subor[meno])
    file1=open("hesla.csv","w", encoding = 'utf8')
    for jejky in range(len(subor)):
        file1.writelines(subor[jejky])
    file1.close()