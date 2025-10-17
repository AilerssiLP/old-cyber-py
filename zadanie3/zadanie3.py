import getpass
import sys
import json 

user = getpass.getuser()

# import sys
# import getpass

# user= getpass.getuser()
# vklad=""
# c="ziaden subor"
# ls_pole=[]
# prava = "rwx"

#     temp=""
#     d=0
#     while(cd!=0):
#         temp=temp+pole[d]
#         d+=1
#         cd-=1

#     if(temp=="ls"):
#         if(ls_pole==[]):
#             print(c)
#         for i in range(len(ls_pole)):
#             print(ls_pole[i])
#     if(temp=="touch"):
#         output=vkladik+" "+user+" "+prava
#         ls_pole.append(output)
#     if(temp=="chmod"):
#         gucci=0
#         filler=ls_pole[0]
#         if(ord(vkladik[0])<55 and ord(vkladik[0])>47):
#             vkladik2=""
#             for i in range(len(vkladik)-2):
#                 vkladik2=vkladik2+vkladik[i+2]
#             gucci=1
#         else:
#             print("chyba")
#         vkladik=vkladik2

#         ################
# """         for i in range(len(ls_pole)):
#             pokuser=ls_pole[i]
#             pokuser2=""
#             for j in range(len(vkladik)):
#                 pokuser2=pokuser2+pokuser[j]
#                 if(pokuser2==vkladik):
                    
#             if(pokuser) """
#         ################

#         if(gucci==1):
#             for i in range(len(output)):
#                 if(output[i]=="-" or output[i]=="r" and output[i+1]=="-" or output[i+1]=="w" and output[i+2]=="-" or output[i+2]=="x"):
#                     prava="r--"
#                     output=vkladik+" "+user+" "+prava
#                     ls_pole[0]=output
#                     break
                
#     if(temp=="quit"):
#         break




def pokusicek2(text):
    vadim=""
    a=0
    d=a
    suka="pokusik"
    vadim=vadim+suka
    #print("je to list text"+vadim)
    text1 = (text + "/").split("/")
    c=0
    #print("ree")
    if (len(text1) > 2):
        c=1
        if(c==3):
            print("ree")
        return "home/" + text
    debuger=""
    a=3
    d=a
    suka="stop him"
    vadim=vadim+suka
    #print("je to list text"+vadim)
    return f"{pouzivatelia.folder}/{''.join(text1[:-1:])}"



##list    
##--------------------------------------------------------------##


def ls(dict):
    for i in dict:

        demon=""

        text = ''

        meno = user

        faker="faker"
        


        for c in (pouzivatelia.ludia.values()):

            if i in (c[faker]):

                meno = c['meno']

        ###nist
        if (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 0):
            text = ""

            ##### citanie
        if (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 4):
            text += "r"

        elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 5):
            text += "r"

        elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 6):
            text += "r"

        else:
            text += "-"

            #### pisanie
        if (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] ==2):
            text += "w"

        elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 3):
            text += "w"

        elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 6):
            text += "w"    
            
        else:
            text += "-"

            ###########spust
        if (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] ==1):
            text += "x"

        elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 3):
            text += "x"

        elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 5):
            text += "x"
            
        else:
            text += "-"
            
        if (pouzivatelia.ludia[pouzivatelia.meno]['file'][i] == 7):
            text = "rwx"
        ######--------------------------------------##

        print(f"{i.split('/')[-1]} {meno} {text}")





##--------------------------------------------------------------##

##pouzivatelia
class pouzivatelia(object):
    faker="faker"
    ##--------------------------------------------------------------
    ludia = {user: {faker: [], "file": {}, 'meno': user},

             }
    ##--------------------------------------------------------------

    folder = 'home'

    ##--------------------------------------------------------------

    meno = user



prikazky = ["mkdir", "cd", "chown", "zapis", "ls", "quit", "touch", "rm", "chmod", "vypis", "spusti"]



pole = ''

b1=""

# while(vklad!="quit"):
#     vklad = input("# ")
#     pole=[]
#     cd=0
#     medzera=0
#     vkladik=""
#     for i in range(len(vklad)):
#         if(vklad[i]==" " and medzera==0):
#             medzera=i
#             continue
#         if(medzera==0):
#             pole.append(vklad[i])
#             cd+=1
#         else:
#             vkladik=vkladik+vklad[i]

#     #print(cd)
c1=""
d1=""

homik = {'home': []}
if(c1=="homik"):
    print("im home")

if(d1=="debuger"):
    print("system error")

while pole != 'quit':
    pole = input("# ") + ' '
    pole = pole.split(" ")
    faker="faker"
    makac=0
    stoper=1
    if (pole[0] in prikazky):
        stoper=0

        file_meno = pokusicek2(pole[1])

        if (pole[0] == "mkdir"):
            if(stoper==100):
                print("reeee")
                print(pole[0])
                stoper=0
                makac=makac+stoper
            if (pole[1] == ''):
                print("chyba")
                if(stoper==100):
                    print("reeee")
                    print(pole[0])
                    stoper=0
                    makac=makac+stoper
            else:
                if(stoper==100):
                    print("reeee")
                    print(pole[0])
                    stoper=0
                    makac=makac+stoper
                ####----
                #### ostatne subory

                if (file_meno not in homik.keys()):
                    if(stoper==90):
                        print("oh not again")
                        print(pole[0])
                        stoper=0
                        makac=makac+stoper
                    homik[file_meno] = [] ######
                    if(makac==1000):
                        print("pokusik")
                        print(pole[0])
                        stoper=0
                        makac=makac+stoper
                    homik["/".join(file_meno.split("/")[:-1:])].append(file_meno)
                    makac=0
                    pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] = 7
                    if(makac==100):
                        print("pokusik")
                        print(pole[0])
                        stoper=0
                        makac=makac+stoper
                    pouzivatelia.ludia[pouzivatelia.meno][faker].append(file_meno)
                else:
                    print("chyba")
                    # print(pouzivatelia.ludia)
                    # print(pouzivatelia.ludia)

        elif (pole[0] == "cd"):
            stoper=0
            makac=0
            debugerik=2
            try:
                # print(pouzivatelia.ludia)
                if(makac==100):
                    print(pouzivatelia.folder)
                    debugerik=100
                
                if (pole[1] == '..'):

                    if(makac==50):
                        print(pouzivatelia.folder)
                        debugerik=1
                    ####
                    #----
                    pouzivatelia.folder = "/".join(pouzivatelia.folder.split("/")[:-1:])


                    if(makac==27):
                        print(pouzivatelia.folder)
                        debugerik=27
                    
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==3):
                    pouzivatelia.folder += "/" + pole[1]
                    #print("ok")
                    #print("ok")
                    #print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==5):
                    pouzivatelia.folder += "/" + pole[1]
                    #print("ok")
                    #print("ok")
                    #print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==7):
                    pouzivatelia.folder += "/" + pole[1]
                    #print("ok")
                    #print("ok")
                    #print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==1):
                    pouzivatelia.folder += "/" + pole[1]
                    #print("ok")
                    #print("ok")
                    #print("ok")
                else:
                    print("chyba")
                    #print("folder")
                    #print(makac)
                    #print("ok")
            except:
                print("chyba")
                    #print("folder")
                    #print(makac)
                    #print("ok")

        elif (pole[0] == 'touch'):
            stoper=0
            fixer=2

            if (pole[1] == ''):
                fixer=0
                print("chyba")

            else:

                if(fixer==5):
                    print(pouzivatelia.folder)
                    stoper=23
                if (file_meno not in homik[pouzivatelia.folder]):
                    if(fixer==5):
                        print(pouzivatelia.folder)
                        stoper=23
                    if (pouzivatelia.folder not in homik.keys()):
                        if(fixer==5):
                            print(pouzivatelia.folder)
                            stoper=23
                        homik[pouzivatelia.folder] = []
                    if(stoper==2345):
                        fixer=23
                        print(pouzivatelia.folder)
                    
                    homik["/".join(file_meno.split("/")[:-1:])].append(file_meno)
                    pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] = 7
                    pouzivatelia.ludia[pouzivatelia.meno]["faker"].append(file_meno)
                else:
                    fixer=29970
                    print("chyba")
                    ################

        elif (pole[0] == "vypis"):
            stoper=0
            fixer=3333
            try:
                if (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==4):
                    print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==5):
                    print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==6):
                    print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==7):
                    print("ok")
                else:
                    print("chyba")
            except:
                print("chyba")
                #print(fixer)
                #print("ok")
        elif (pole[0] == "spusti"):
            stoper=0
            try:
                if (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==1):
                    print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==3):
                    print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==5):
                    print("ok")
                elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==7):
                    print("ok")
                else:
                    print("chyba")
            except:
                print("chyba")
                maker=0
                if(maker==23):
                    print(maker)
                    print(pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno])
        elif (pole[0] == 'zapis'):
            stoper=0
            maker=0
            if (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==2):
                print("ok")
            elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==3):
                print("ok")
            elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==6):
                print("ok")
            elif (pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno] ==7):
                print("ok")
            else:
                print("chyba")
                maker=0
                if(maker==23):
                    print(maker)
                    print(pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno])

        elif (pole[0] == "ls"):
            stoper=0
            fixer=0
            if(fixer==23):
                print(stoper)
                print(pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno])    
            if (pole[1] not in ["", " "]):
                maker=0
                ls([file_meno])
                
                if(fixer==200):
                    print(maker)
                    print(pole[1])
            else:
                maker=0
                fixer=fixer+maker

                p = homik[pouzivatelia.folder]
                ls(p)
                
                if(maker==23):
                    print(maker)
                    print(pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno])

        elif (pole[0] == "rm"):
            stoper=0
            debuf=32
            prepinas=0
            prepinas=prepinas+debuf
            if(prepinas==20):
                prepinas+debuf
            del pouzivatelia.ludia[pouzivatelia.meno]['file'][file_meno]
            try:
                del homik[file_meno]
            except:
                pass
            stoper=9
            debuf=2
            prepinas=0
            prepinas=prepinas+debuf
            if(prepinas==20):
                prepinas+debuf
            meno_folder = "/".join(file_meno.split("/")[:-1:])
            if(prepinas==20):
                prepinas+debuf
            homik[meno_folder].remove(file_meno)
            for i in pouzivatelia.ludia.keys():
                try:
                    pouzivatelia.ludia[pouzivatelia.meno]['faker'].remove(file_meno)
                    if(prepinas==20):
                        prepinas+debuf
                except:
                    pass
        # elif pole[0] == "info":
        #     print(homik)
        #     print(pouzivatelia.ludia)
        # root
        elif (pole[0] == "chmod"):
            stoper=0
            if(stoper==900):
                break
            fixer3=9
            meno = pokusicek2(pole[2])
            if(fixer3==20):
                print(meno)
            try:
                if(fixer3==20):
                    print(meno)
                pouzivatelia.ludia[pouzivatelia.meno]['file'][meno] = int(pole[1])
            #########################
            #----------
            #aosfo
            except:
                print("chyba")
                if(fixer3==35):
                    print(meno)
                    ######
        ##############
        ###### predatie uzivatela

        elif (pole[0] == "chown"):
            stoper=0
            text="chown"
            if (pole[1] not in pouzivatelia.ludia.keys() and stoper==0):
                if(stoper==3):
                    print(meno)
                pouzivatelia.ludia[pole[1]] = {"faker": [], "file": {}, 'meno': pole[1]}
                if(text=="ree"):
                    print("fck me")
            if(text=="ree"):
                print("fck me")
            if(text=="ahoj"):
                print(meno)
            meno = pokusicek2(pole[2])

            try:

                if(meno=="karolgotthe king"):
                    print("pepohappy")
                i=0
                for k in (pouzivatelia.ludia.values()):
                    for jo in range(5):
                        i+=1
                    if (meno in k['faker']):
                        pouzivatelia.ludia[k['meno']]['faker'].remove(meno)
                        break
                    for jo in range(6):
                        i+=1
                pouzivatelia.ludia[pole[1]]['faker'].append(meno)
                for jo in range(8):
                    i+=1
                pouzivatelia.ludia[pole[1]]['file'][file_meno] = 7
                if(i==-1):
                    print(i)
            except:
                print("chyba")

        elif (pole[0] == "quit"):
            stoper=0
            break

    else:
        stoper=2
        print("chyba")
